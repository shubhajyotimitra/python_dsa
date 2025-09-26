#Virtual Environment:
#A virtual environment is a tool used to isolate specific python environment on a single machine
#it also allowing you to work on multiple projects with different dependencies and packages without conflicts.


#in this we got to know how to install virtual environment and inside the virtual environment i can install anything according to my choise.
#once the virtual environment is activated, any packages that you install using pip will be installed in the virtual environment
#how to activate virtual environment: source myenv/bin/activate


#suppose if i have to give someone my project including all of my packages used in it then ,
#The "requirement.txt"file is used.
#in this , while we are in my own virtual environment by this command "pip freeze" we can see how many files we have installed in it 
#also by this command "pip freeze > requirements.txt"
#after that if someone runs this command "pip install -r requirements.txt"

import pandas as pd
print(pd.__version__)

#from the above snippet we got to know which version is install in the python global version environment 

#on the other hand if i have to check which version is install in my own virtual environment.
#firstly what we have to do is : we have to create virtual environment.
#python3 -m venv myenv by this we can create virtual environment
#note: instead of "myenv" we can create whatever we want to name my virtual environment file .
#to activate what we have created virtual environment we have to write:
#source my env/bin/activate , by this the virtual environment that we have created will be activate
#after that we have to write:
# => python,import pandas as pd,pd.__version__
#thereafter we got to know which version of panda is install in my virtual environment


