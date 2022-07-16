import logging
import os
import re
import subprocess
import sys

FILE_WITH_CONFLICTS = os.path.join(os.curdir, "merge.txt")
CONFLICT_START_PATTERN = "<<<<<<<"
CONFLICT_CENTER_PATTERN = "======="
CONFLICT_END_PATTERN = ">>>>>>>"


def read_file_with_conflicts():
    conflict_start = conflict_end = -1
    with open(FILE_WITH_CONFLICTS, "r") as conflict_file:
        for i, line in enumerate(conflict_file):
            # Check whether this line is the start of a conflict
            if re.match(CONFLICT_START_PATTERN, line):
                conflict_start = i + 1
            # Check whether this line is the center of a conflict
            if re.match(CONFLICT_CENTER_PATTERN, line):
                conflict_end = i
                conflict_start += 1
                if validate_line(conflict_start, conflict_end):
                    authors = git_blame(conflict_start, conflict_end)
                    if authors:
                        logging.info(
                            get_report_message(
                                "our", conflict_start, conflict_end, authors
                            )
                        )
                conflict_start = i + 1
                conflict_end = -1
            # Check whether this line is the end of a conflict
            if re.match(CONFLICT_END_PATTERN, line):
                conflict_end = i
                conflict_start += 1
                if validate_line(conflict_start, conflict_end):
                    authors = git_blame(conflict_start, conflict_end)
                    if authors:
                        logging.info(
                            get_report_message(
                                "their", conflict_start, conflict_end, authors
                            )
                        )
                conflict_start = conflict_end = -1


def get_report_message(side, start, end, authors):
    author_msg = f"the authors are" if len(authors) > 1 else "the author is"
    return (
        f"Conflicts on {side} side\n"
        f"from line {start} to line {end}\n"
        f"{author_msg} {','.join(authors)}" 
    )


def validate_line(start, end):
    return start >= 0 and start <= end


def git_blame(start, end):
    git_blame_pattern = (
        "[0-9a-f]{8}\s+\(([\w|\d|\s]+)\s+\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}"
    )
    authors = []
    try:
        output = (
            subprocess.check_output(
                ["git", "blame", "-L", f"{start},{end}", FILE_WITH_CONFLICTS],
                encoding="utf-8",
            )
            .strip()
            .splitlines()
        )
        for line in output:
            match = re.match(git_blame_pattern, line)
            if match:
                authors.append(match.group(1))
        return list(set(authors))
    except subprocess.CalledProcessError:
        logging.error("Failed to run git blame")
        return []


if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    read_file_with_conflicts()
