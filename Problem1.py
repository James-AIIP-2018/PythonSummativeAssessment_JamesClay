'''
Created on 10 Feb 2018

@author: james
'''
import random

def sensorDataGenerate():
    '''Function to generate a sensor reading
    
    Returns a random float between 0 and 1'''
    
    # Generate a random float from 0 to 1
    return random.random()              

def sensorClusterGenerate():
    '''Function to generate a sensor cluster
    
    Returns a list of 16 random floats between 0 and 1'''
    
    # List representing a single sensor cluster
    sensorCluster = []
    
    # Loop through 16 sensors and generate random data
    for i in range(0,16):
        sensorCluster.append(sensorDataGenerate())
        
    # Return the single cluster with generated data
    return sensorCluster

def dataStreamGenerate():
    '''Function to generate a data stream or sensor clusters
    
    Returns a list of 32 sensor clusters'''
    
    # List representing sensor clusters
    sensorNetwork = []
    
    # Loop through 32 sensors clusters and generate random data
    for i in range(0,32):
        sensorNetwork.append(sensorClusterGenerate())
        
    # Return the dataset
    return sensorNetwork