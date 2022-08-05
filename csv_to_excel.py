#Importing modules
import pandas as pd
import os
import glob
from tkinter import *
from tkinter import Tk, filedialog

root = Tk() # pointing root to Tk() to use it as Tk() in program.
root.withdraw() # Hides small tkinter window.
root.attributes('-topmost', True) # Opened windows will be active. above all windows despite of selection.
directoryNameSource = filedialog.askdirectory() # Returns opened path as str
print(directoryNameSource+ "/") 

# changing directory to where the csv are located        
os.chdir(directoryNameSource+ "/")
print("Directory changed")

#creating list for the file
csv_list = glob.glob(os.path.join("*.csv"))

#changing the list and deleting the word ".xlsx"
file_name_list = [s.replace(".csv","")for s in csv_list]

#creating a new file where the new file will be stored
directory = "Converted_to_xlsx"
parent_dir = directoryNameSource
directoryNameDestination = os.path.join(parent_dir, directory+"/") 
os.mkdir(directoryNameDestination+"/")
print("Directory '% s' created" % directory)

#converting the files
for a_file in file_name_list:
        read_file = pd.read_csv (a_file+'.csv')
        read_file.to_excel (directoryNameDestination+"/"+a_file+'.xlsx', index = None, header=True)
