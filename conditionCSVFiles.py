## CONDITION .CSV DATA FILES
# DESCRIPTION
#
# This function will condition *.csv files from choosen source folder.
# (Works only for ";" delimited files with "," as decimal divider)
#
#  Conditioned files will be placed in choosen destination folder.
# Syntax:
#     
# Inputs:
#     directoryNameSource    - Source folder as char array (may be omitted)
#     directoryNameDestination     - Destination folder as char array (may be omitted)
# Outputs:
#    csv_list - Files loaded in a list
#
# See also:

# Importing modules 
import os
import glob
import pandas as pd
from tkinter import *
from tkinter import Tk, filedialog
#creating a function 
def conditionCSVFiles():
# changing directory to where the csv are located 
    root = Tk() # pointing root to Tk() to use it as Tk() in program.
    root.withdraw() # Hides small tkinter window.
    root.attributes('-topmost', True) # Opened windows will be active. above all windows despite of selection.
    directoryNameSource = filedialog.askdirectory() # Returns opened path as str
    print(directoryNameSource+ "/") 
    
# changing directory to where the csv are located        
    os.chdir(directoryNameSource+ "/")
    print("Directory changed")
    
#Creating a folder in the desiginated path which in this case it's directoryNameSource    
    directory = "Conditioned"
    parent_dir = directoryNameSource
    directoryNameDestination = os.path.join(parent_dir, directory+"/") 
    os.mkdir(directoryNameDestination+"/")
    print("Directory '% s' created" % directory)
    
# create a list of all the csv files in the directory
    csv_list = glob.glob(os.path.join("*.csv"))
    print(csv_list)
    for a_file in csv_list:  # creating a loop and giving the list a variale
            with open( a_file,"r") as file:# open the file in read mode and read it
              text = file.read()
# join() method combines all contents of 
# csvfile.csv and formed as a string
              text = ''.join([i for i in text]) 
# search and replace the contents
              text = text.replace("§", "") 
              text = text.replace("£", "") 
              text = text.replace("¤#:","") 
              text = text.replace("_", "") 
              text = text.replace(",", ".") 
              text = text.replace("Â", "")
# open the files from the desiginated path in write mode 
# and replaces all the text.  
              with open(directoryNameDestination + a_file,"w") as file:
               file.write(text)
               file.close()
# Translate from swedish list to english  
               swedish=["Momenttest","Kopplingstest"]
               english=["Torque test","Clutch test"]
               df = pd.read_csv(a_file, header = None)
               df.replace(to_replace =swedish, 
                 value = english, 
                  inplace = True)
               df.to_csv(directoryNameDestination + a_file, header=['Conditioned'], index = False)
               
# Main
if __name__ == '__main__':
   conditionCSVFiles()
