#importing modules
import pandas as pd
import csv
import matplotlib.pyplot as plt
import os
from tkinter import *
from tkinter import Tk, filedialog
import glob
from prettytable import PrettyTable
#creating a fuction called plot
def plot():
    root = Tk() # pointing root to Tk() to use it as Tk() in program.
    root.withdraw() # Hides small tkinter window.
    root.attributes('-topmost', True) # Opened windows will be active. above all windows despite of selection.
    directoryNameSource = filedialog.askdirectory() # Returns opened path as str
    print(directoryNameSource+ "/") 
    
# changing directory to where the csv are located        
    os.chdir(directoryNameSource+ "/")
    print("Directory changed")
    
# the size and the layout of the figure
    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True

# create a list of all the csv files in the directory
    csv_list = glob.glob(os.path.join("*.csv"))
    print(csv_list)
    for a_file in csv_list:
        fh = open(a_file)
        df_reader = pd.read_csv(a_file) #reads the whole file using pandas
        csv_reader = csv.reader(fh, delimiter =';')#reads the file and finds the header
        csv_header = next(csv_reader)#reads the  header
        if csv_header == ['Conditioned']: #Confirming if the conditioned is the header
            while ['Conditioned']:#if the header is true
            #checking the second row
                if df_reader.iloc[0].values.tolist() == ['Torque test']:#Confirming if its Torque test
                #If it is Torque test
                    index = 0
                    myTable = PrettyTable([a_file,"time","clutch","pMin","pMax"]) # creating headers for the table
                    for row in csv_reader:#reads all the row in the file
                        if len(row) == 3:#reads the row with data in 3 cells
                            row = [row[0],row[1] , row[2]]
                            # reads the cell and splits them and put them in a table
                            input = row[1]
                            A = input.split(" ")
                            clutch=A[0]
                            input = row[2]
                            B = input.split(" ")
                            time=B[0]
                        elif len(row) == 4:
                            row = [row[0],row[1] , row[2],row[3]]
                            input = row[2]
                            C = input.split(" ")
                            pMin=C[0]
                            input = row[3]
                            D = input.split(" ")
                            pMax=D[0]
                            myTable.add_row([index,time,clutch,pMin,pMax])
                            index= index + 1 
                            print(myTable) #prints the table                
                #It reads the header in the csv file
                #Then creats a plot
                    headers = ['Time', 'PressureP9', 'PressureP10','PressureP11','PressureP12','PressureP13','PressureP14','StallTorque','TorqueEngine','AdwinSpeedTurbine_HTL3xxB']
                    df = pd.read_csv(a_file,skiprows= 20, names=headers, delimiter =';')
                    df.PressureP9.plot(color='k')
                    df.PressureP10.plot(color='g')
                    df.PressureP11.plot(color='b')
                    df.PressureP12.plot(color='m')
                    df.PressureP13.plot(color='c')
                    df.PressureP14.plot(color='r')
                    df.StallTorque.plot(color='k')
                    df.TorqueEngine.plot(color='g')
                    df.AdwinSpeedTurbine_HTL3xxB.plot(color='b')
                    plt.title("Torque test" + " "+a_file)
                    plt.xlabel('Pressure')
                    plt.ylabel('Time')
                    plt.show()
                
            
                elif df_reader.iloc[0].values.tolist() == ['Clutch test']:#if not Torque test, it Confirms if its Clutch test
                #if it is Clutch test
                    index = 0
                    myTable = PrettyTable([a_file,"time","clutch","current","pMin","pMax"]) # creating headers for the table
                    for row in csv_reader:#reads all the row in the file
                        if len(row) == 3:#reads the row with data in 3 cells
                            row = [row[0],row[1] , row[2]]
                            # reads the cell and splits them and put them in a table
                            input = row[1]
                            A = input.split(" ")
                            clutch=A[0]
                            current=A[1]
                            input = row[2]
                            B = input.split(" ")
                            time=B[0]
                        elif len(row) == 4:
                            row = [row[0],row[1] , row[2],row[3]]
                            input = row[2]
                            C = input.split(" ")
                            pMin=C[0]
                            input = row[3]
                            D = input.split(" ")
                            pMax=D[0]
                            myTable.add_row([index,time,clutch,current,pMin,pMax])
                            index= index + 1 
                            print(myTable) #prints the table   
                     #It reads the header in the csv file
                     #Then creats a plot    
                    headers = ['Time', 'PressureP9', 'PressureP10','PressureP11','PressureP12','PressureP13','PressureP14']
                    df = pd.read_csv(a_file,skiprows= 43, names=headers, delimiter =';')
                    df.PressureP9.plot(color='k')
                    df.PressureP10.plot(color='g')
                    df.PressureP11.plot(color='b')
                    df.PressureP12.plot(color='m')
                    df.PressureP13.plot(color='c')
                    df.PressureP14.plot(color='r')
                    plt.title("Clutch test" + " "+a_file)
                    plt.xlabel('Pressure')
                    plt.ylabel('Time')
                    plt.show()
                elif df_reader.iloc[0].values.tolist() == ['Lockup test']:
                    print("found Lockup test")
                else:
                    print("Not working")
                break
plot()