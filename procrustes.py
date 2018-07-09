#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import glob
import numpy as np
from matplotlib import pyplot as plt

input_file = 'dataset_raw.txt'
output_file = 'dataset_procrustes.txt'
reference_species = 'Cacan11'

output_list = []
data = []
fig = plt.figure()
with open(input_file, 'r') as fd_in:
    for i, line in enumerate(fd_in):
        if i > 0:
        
            # Parse the values
            values = line.split(',')
            species = values[0]
            points = list(map(float, map(str.strip, values[1:])))
            points = np.array(points).reshape((-1, 2))
            
            # Translation
            centroid = points.mean()
            points = points - centroid
            
            # Scaling
            scale = points.std()
            points = points / scale
            
            data.append((species, points))

# Select the reference species for the rotation
species_ref, points_ref = list(filter(lambda x: x[0] == reference_species, data))[0]
print('Reference species: {}'.format(species_ref))
for i, (species, points) in enumerate(data):

    print('Transforming {}...'.format(species))

    # Rotation
    theta = -np.arctan2(np.sum(points_ref[:,0]*points[:,1] - points_ref[:,1]*points[:,0]), np.sum(points_ref*points))
    M = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    new_points = M.dot(points.T).T
    points[:] = new_points

    # Round values
    new_points = new_points.round(3)

    # Plot the values
    plt.rcParams['svg.fonttype'] = 'none'
    plt.subplot(9, 18, i+1)
    plt.fill(new_points[:,0], new_points[:,1])
    #plt.plot(new_points[:,0], new_points[:,1], '.k')
    plt.axis('off')
    ax = plt.gca()
    ax.set_aspect('equal')
    ax.invert_yaxis()
    plt.title(species[:9], fontsize=8)
 

with open(output_file, 'w') as fd_out:
    fd_out.write('ID, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8\n')
    for i in range(len(data)):
        # Write the output
        species, points = data[i]
        output_line = species + ', ' + ', '.join(points.ravel().astype(str)) + '\n'
        fd_out.write(output_line)

plt.subplots_adjust(hspace=0.5)
plt.show()
