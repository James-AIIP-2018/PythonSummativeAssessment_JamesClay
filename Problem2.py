'''
Created on 10 Feb 2018

@author: james
'''
import datetime

def storeDataset(sensorNetwork):
    '''Function to store sensor datastream to a file
    
    Datastream from sensors is an input to this function which stores this to a historical data file.
    NOTE: Historical Data file is generated in text format without headers. It is a file which should be read by an application. It contains a datetime with associated list or lists per line. The extension is "sds"'''
   
    # Current system date and time
    currentDateTime = datetime.datetime.now()
    
    # Open a text file with "sds" extension in append mode (historical file)
    with open("dataLog.sds", "a") as dataFile:
        
        # Write the dataset to the historical "sds" file
        dataFile.write(str(currentDateTime)+": "+str(sensorNetwork)+"\n")