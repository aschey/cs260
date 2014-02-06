from sys import argv
import subprocess

def main():
    search = argv[1]
    time = argv[2]
    inSet = argv[3] # either in or out
    maxSize = argv[4]
    numTrials = argv[5]
    replicates = argv[6]
    if search == "binary":
        command = str.format("python3 makeintegers.py {0} 0 1 0", maxSize)
        
    elif search == "linear":
        command = str.format("python3 makeintegers.py {0} 0 1 {0}", maxSize)
    
    # get raw data from the subprocess
    data = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    # read the data and return it as a bytes object, decode it into a string, 
    # then convert it to a list
    ints = eval(data.communicate()[0].decode(encoding="UTF-8"))
    # close the data stream
    data.stdout.close()
    print(ints)
    
    
main()

