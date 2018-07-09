#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import glob
import numpy as np
from scipy.spatial.distance import pdist

input_file = 'dataset_procrustes.txt'
output_file = 'distances.txt'

output_list = []
with open(input_file, 'r') as fd_in, open(output_file, 'w') as fd_out:
    for i, line in enumerate(fd_in):
        if i == 0:
            fd_out.write('ID, d12, d13, d14, d15, d16, d17, d18, d23, d24, d25, d26, d27, d28, d34, d35, d36, d37, d38, d45, d46, d47, d48, d56, d57, d58, d67, d68, d78\n')
        else:
        
            # Parse the values
            values = line.split(',')
            species = values[0]
            points = list(map(float, map(str.strip, values[1:])))
            points = np.array(points).reshape((-1, 2))
            
            # Calculate the distances
            D = pdist(points)
            print(D)
            
            # Write the output
            output_line = species + ', ' + ', '.join(D.astype(str)) + '\n'
            fd_out.write(output_line)
