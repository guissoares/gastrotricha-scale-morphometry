#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import glob
import numpy as np

input_file = 'dataset_procrustes.txt'
output_file = 'angles.txt'

output_list = []
with open(input_file, 'r') as fd_in, open(output_file, 'w') as fd_out:
    for i, line in enumerate(fd_in):
        if i == 0:
            point_indices = np.array([
                [8, 1, 2],
                [1, 2, 3],
                [2, 3, 4],
                [3, 4, 5],
                [4, 5, 6],
                [6, 7, 8],
                [7, 8, 1],
                [6, 1, 4],
                [2, 5, 8],
                [7, 1, 3],
                [3, 5, 7],
                [2, 4, 7],
            ]) - 1
            angle_names = ['a{}{}{}'.format(k1+1, k2+1, k3+1) for k1, k2, k3 in point_indices]
            fd_out.write('ID, ' + ', '.join(angle_names) + '\n')
        else:
        
            # Parse the values
            values = line.split(',')
            species = values[0]
            points = list(map(float, map(str.strip, values[1:])))
            points = np.array(points).reshape((-1, 2))
            
            # Calculate the angles
            angles = []
            for k1, k2, k3 in point_indices:
                pA = points[k1]
                pB = points[k2]
                pC = points[k3]
                v1 = pA-pB
                v2 = pC-pB
                theta1 = np.arctan2(v1[0], v1[1])
                theta2 = np.arctan2(v2[0], v2[1])
                angle_radians = (theta2-theta1) % (2*np.pi)
                angle_degrees = 180 * angle_radians / np.pi
                angles.append(angle_degrees)
            angles = np.array(angles).round(3)
            print(angles)
            
            # Write the output
            output_line = species + ', ' + ', '.join(angles.astype(str)) + '\n'
            fd_out.write(output_line)
