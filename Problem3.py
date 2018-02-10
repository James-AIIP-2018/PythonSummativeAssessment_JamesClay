'''
Created on 10 Feb 2018

@author: james
'''
import random
import Problem1 as dataGenerate
import Problem2 as dataStore

# Setup logging 
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Logging filename: sensorErrors.log in write mode (will overwrite existing log file)
handler = logging.FileHandler('sensorErrors.log', 'w')

# Set logging format to include the date and time, logging level and the actual logging message
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

handler.setFormatter(formatter)
logger.addHandler(handler)

def isPositiveFloat(s):
    '''Function test if the passed poarameter is a positive float.
    
    Returns True if the input parameter is a positive float (or zero), else returns False.'''
    
    # Try and exception block
    try:
        # Attempt to cast the parameter to a float
        number = float(s)
        
        # Test if the number is 0 or greater
        if number >=0:
            return True
        else:
            return False
        
    # If the casting to a float fails, return False
    except ValueError:
        return False

def corruptDataSet(sensorNetwork):
    '''Function which will randomly corrupt a dataset.
    
    Returns a randomly corrupted dataset from a passes valid dataset.'''
    
    # Randomly decide how many sensors have failed
    numberOfFailures = random.randint(0, (32*16))
    
    # Initialise clusterID and sensorID
    clusterID = 1
    sensorID = 1
    
    # Loop through each sensor failure
    for i in range(0,numberOfFailures):
        # Find a sensor (randomly) which has not yet failed
        while True:
            # Randomly select a cluster and sensor
            clusterID = random.randint(1, 32)
            sensorID = random.randint(1, 16)
            
            # If the sensor has not already failed, then select the sensor
            if sensorNetwork[clusterID-1][sensorID-1] != 'err':
                break
        
        # Mark the sensor as failed
        sensorNetwork[clusterID-1][sensorID-1] = 'err'
        
        # Loop through other sensors in the cluster and set their readings to '' as they are on the same circuit (cluster) and so can not report data
        for i in range(0,16):
            if sensorNetwork[clusterID-1][i] != 'err':
                sensorNetwork[clusterID-1][i] = ''
    
    # Return the corrupted dataset
    return sensorNetwork

def containsError(sensorNetwork):
    '''Function check a dataset, log sensor errors and return a filtered dataset.
    
    Function accepts a dataset as a parameter.
    The dataset is examined for sensor errors.
    Identified errors are modified to -1, a non-valid float value.
    The Cluster and Sensor ID are logged to repair.
    The filtered dataset is returned.'''
    
    # Loop through entire dataset, sensor by sensor
    for i in range(0,32):
        for j in range(0,16):
            
            # If the sensor reports an error 
            if sensorNetwork[i][j] == 'err':
                # Filter the error to -1 (non-valid float)
                sensorNetwork[i][j] = -1
                # Log the failed sensor information to the log file for repair.
                logger.info("SENSOR ERROR: Cluster: "+str(i+1)+", Sensor: "+str(j+1))
    
    # Return the filtered dataset
    return sensorNetwork


# Main - no specific main, not required in assessment. This block is demonstrating the functions
sensorData = dataGenerate.dataStreamGenerate()
corruptSensorData = corruptDataSet(sensorData)
dataStore.storeDataset(corruptSensorData)

filteredSensorData = containsError(corruptSensorData)