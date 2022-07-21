from cgitb import text
import re
import subprocess

def git_blam(line_range, f):
    #Restrict the output within certain line range
    subprocess.run(["git","blame", "-L", line_range, f, ">>", "text.txt"])

def git_Ignore():
    #Ignore whitespace changes
    subprocess.run(["git","blame", "-w",  "/merge.txt"])

def git_log():
    #Track file content changes
    subprocess.run(["git", "log", "-S", "Bob", "--/merge.txt"])

if __name__ == "__main__":  
    f1 = "merge.txt"
    rang = ['6,8', '15,17', '24,29']
    fp = open("text.txt","r")
    a = fp.read()
    
    for i in range(3):
        git_blam(rang[i],f1)
        result = re.search( r'(?<=\().+?(?= 20)', a, re.M|re.I)
        result_line = re.search(r'(?<=00 ).+?(?=\))',a, re.M|re.I)
        print(result.group(),result_line.group())

    
    
    
    
   
    

    


    