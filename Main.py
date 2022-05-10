# Main.py
import cv2
import numpy as np
import os
import DetectChars
import DetectPlates
import PossiblePlate

# module level variables ##########################################################################
SCALAR_BLACK = (0.0, 0.0, 0.0)
SCALAR_WHITE = (255.0, 255.0, 255.0)
SCALAR_YELLOW = (0.0, 255.0, 255.0)
SCALAR_GREEN = (0.0, 255.0, 0.0)
SCALAR_RED = (0.0, 0.0, 255.0)

###################################################################################################
def getLicensePlateNumber(file_name):
    blnKNNTrainingSuccessful = DetectChars.loadKNNDataAndTrainKNN()         # attempt KNN training
    if blnKNNTrainingSuccessful == False:                               # if KNN training was not successful
        print("\nerror: KNN traning was not successful\n")  # show error message
        return None                                                # and exit program
    # end if
    imgOriginalScene  = cv2.imread(file_name)               # open image
    if imgOriginalScene is None:
        return None                            
    listOfPossiblePlates = DetectPlates.detectPlatesInScene(imgOriginalScene)           # detect plates
    if(listOfPossiblePlates==None):
        return None
    plate = DetectChars.detectCharsInPlates(listOfPossiblePlates)        # detect chars in plates
    if(plate==None):
        return None
    else:
        return plate
    