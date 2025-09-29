#if_name_=="_main_" in python

import shubh
shubh.welcome()

#as we have already made a file name "shubh.py" and we have made another file in an order to import the things we have written in the "shubh file"
#but here is the problem when i write "shubh.welcome" then in output will print two times. 
#also if we remove "shubh.welcome()" then it will also continue and print the output only one time.

#it is mainly used to control the execution of code depending on whether the file is being run directly or imported as a module into another script.
#it also helps you separate executable code from importable code.