#!/usr/bin/env python
# coding: utf-8

# Imports
import numpy as np
import os

# Call function saveKeypointsAndDescriptors
def saveKeypointsAndDescriptors(keypoints,
								descriptors,
								matcher,
                                descriptor,
                                flags):
	# flags = 1: input image or queryDescriptors
	# flags = 2: training-set image trainDescriptors
	
	# File name
	filename1 = 'Outputs/%s-with-%s-keypoints%s.txt' % (matcher, descriptor, flags)
	filename2 = 'Outputs/%s-with-%s-descriptors%s.txt' % (matcher, descriptor, flags)

	# Delete a file if it exists
	if os.path.exists(filename1):
		os.remove(filename1)

	elif os.path.exists(filename2):
		os.remove(filename2)

	# Save keypoints into a file
	np.savetxt(fname = filename1,
				X = keypoints,
				fmt='%s')

	# Save descriptors into a file
	np.savetxt(fname = filename2,
			   X = descriptors,
			   fmt = "%d")