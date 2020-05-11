#!/usr/bin/env python
# coding: utf-8

# Feature Description and Matching

# Imports
import argparse
import cv2 as cv
import features
import globals
import numpy as np
import outputs
import save_figures

# Initializing global variables
globals.initialize()

# Message from usage
message = '''main.py [-h]

             --detector     {SIFT, SURF, KAZE, ORB, BRISK,AKAZE}
             --descriptor   {SIFT, SURF, KAZE, BRIEF, ORB, BRISK, AKAZE, FREAK}
             --matcher      {BF, FLANN}'''

# Create the parser
parser = argparse.ArgumentParser(description = 'Feature Description and Matching.',
                                usage = message)

# Argument --detector
parser.add_argument('--detector',
                    action = 'store',
                    choices = ['SIFT', 'SURF', 'KAZE', 'ORB', 'BRISK', 'AKAZE'],
                    required = True,
                    metavar = '',
                    dest = 'detector',
                    help = 'select the detector to be used in this experiment')

# Argument --descriptor
parser.add_argument('--descriptor',
                    action = 'store',
                    choices = ['SIFT', 'SURF', 'KAZE', 'BRIEF', 'ORB', 'BRISK', 'AKAZE', 'FREAK'],
                    required = True,
                    metavar = '',
                    dest = 'descriptor',
                    help = 'select the descriptor to be used in this experiment')

# Argument --matcher
parser.add_argument('--matcher',
                    action = 'store',
                    choices = ['BF', 'FLANN'],
                    required = True,
                    metavar = '',
                    dest = 'matcher',
                    help = 'select the matcher to be used in this experiment')

# Execute the parse_args() method
arguments = parser.parse_args()

# Initiate Detector and Descriptor

# Initiate detector selected
if arguments.detector == 'SIFT':
    globals.detector = features.SIFT()

elif arguments.detector == 'SURF':
    globals.detector = features.SURF()

elif arguments.detector == 'KAZE':
    globals.detector = features.SIFT()

elif arguments.detector == 'ORB':
    globals.detector = features.ORB()

elif arguments.detector == 'BRISK':
    globals.detector = features.BRISK()

elif arguments.detector == 'AKAZE':
    globals.detector = features.AKAZE()

# Initiate descriptor selected
if arguments.descriptor == 'SIFT':
    globals.descriptor = features.SIFT()

elif arguments.descriptor == 'SURF':
    globals.descriptor = features.SURF()

elif arguments.descriptor == 'KAZE':
    globals.descriptor = features.SIFT()

elif arguments.descriptor == 'BRIEF':
    globals.descriptor = features.BRIEF()

elif arguments.descriptor == 'ORB':
    globals.descriptor = features.ORB()

elif arguments.descriptor == 'BRISK':
    globals.descriptor = features.BRISK()

elif arguments.descriptor == 'AKAZE':
    globals.descriptor = features.AKAZE()

elif arguments.descriptor == 'FREAK':
    globals.descriptor = features.FREAK()

# Open and Convert the input image from BGR to GRAYSCALE
image1 = cv.imread(filename = 'Figures/image1.jpg',
                   flags = cv.IMREAD_GRAYSCALE)

# Open and Convert the training-set image from BGR to GRAYSCALE
image2 = cv.imread(filename = 'Figures/image2.jpg',
                   flags = cv.IMREAD_GRAYSCALE)

# Could not open or find the images
if image1 is None or image2 is None:
    print('\nCould not open or find the images.')
    exit(0)

# Find the keypoints and compute
# the descriptors for input image
globals.keypoints1, globals.descriptors1 = features.features(image1)

# Print
print('\nInput image:\n')

# Print infos for input image 
features.prints(keypoints = globals.keypoints1,
                descriptor = globals.descriptors1)

# Find the keypoints and compute
# the descriptors for training-set image
globals.keypoints2, globals.descriptors2 = features.features(image2)

# Print
print('Training-set image:\n')

# Print infos for training-set image
features.prints(keypoints = globals.keypoints2,
                descriptor = globals.descriptors2)

# Matcher 
output = features.matcher(image1 = image1,
                          image2 = image2,
                          keypoints1 = globals.keypoints1,
                          keypoints2 = globals.keypoints2,
                          descriptors1 = globals.descriptors1,
                          descriptors2 = globals.descriptors2,
                          matcher = arguments.matcher,
                          descriptor = arguments.descriptor)

# Save Figure Matcher
save_figures.saveMatcher(output = output,
			             matcher = arguments.matcher,
                         descriptor = arguments.descriptor)

# Save keypoints and descriptors into a file
# from input image
outputs.saveKeypointsAndDescriptors(keypoints = globals.keypoints1,
								    descriptors = globals.descriptors1,
                                    matcher = arguments.matcher,
                                    descriptor = arguments.descriptor,
                                    flags = 1)

# Save keypoints and descriptors into a file
# from training-set image
outputs.saveKeypointsAndDescriptors(keypoints = globals.keypoints2,
								    descriptors = globals.descriptors2,
                                    matcher = arguments.matcher,
                                    descriptor = arguments.descriptor,
                                    flags = 2)

# Print
print('Done!\n')

# Print
print('Feature Description and Matching executed with success!')