from ast import arg
from datetime import datetime
import sys

#Task 3a and b)
#Function to take a message and append it to a file
def log_entry(filename, message):

    file = open(filename, 'a')
    now = str(datetime.now())
    file.write("\n")
    file.write(now + ":")
    file.write("\n")
    file.write("\t" + message)
    file.write("\n")
    file.close()


log_entry("log_file.txt", "Insert entry here")



#Task 3c and 3d)
#Insert message in command line after python file.
def log_entry_2(filename):
    
    file = open(filename, 'a')
    
    #If there is no message, no value will be assigned to argv.
    if sys.argv[1:] != []:
        argv = str(sys.argv[1:])
        now = str(datetime.now())
        file.write(now)
        file.write("\n")

    #If there is no value assigned to argv, this will fail and an exception will be raised.
    try:
            file.write(argv)
            file.write("\n")

    except:
        print("An exception occured, no message provided.")
   
    file.close()


log_entry_2("log_file.txt") 

 