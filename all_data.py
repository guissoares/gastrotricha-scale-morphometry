#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import glob
import numpy as np
from sklearn.decomposition import PCA

input_files = ['dataset_procrustes.txt', 'angles.txt', 'distances.txt']
output_file = 'all_data.txt'

# Read all the input files
all_data = []
for input_file in input_files:
    file_data = {
        'header': [],
        'species': [],
        'data': []
    }
    with open(input_file, 'r') as fd_in:
        for i, line in enumerate(fd_in):
            # Parse the values
            values = line.split(',')
            values = list(map(str.strip, values))
            if i == 0:
                file_data['header'] = values[1:]
            else:
                species = values[0]
                data = list(map(float, values[1:]))
                assert len(data) == len(file_data['header']), 'Error: all lines must have the same number of elements for each file'
                file_data['species'].append(species)
                file_data['data'].append(data)
    all_data.append(file_data)

# Check consistency between all the data
f0 = all_data[0]
for f in all_data[:1]:
    assert len(f['species']) == len(f0['species']), 'Error: all files must have the same number of species'
    for sp0, spx in zip(f0['species'], f['species']):
        assert sp0 == spx, 'Error: the names of the species in all files must match'

# Standardize the data for each input file
for f in all_data:
    f['data'] = np.array(f['data'])
    pca = PCA(n_components=1)
    pca.fit(f['data'])
    mean = pca.mean_
    std = pca.explained_variance_**0.5
    f['data'] = (f['data'] - mean) / std

# Combine all the data
headers = ['ID']
species = all_data[0]['species']
data = []
for f in all_data:
    headers += f['header']
    data.append(f['data'])
data = np.hstack(data)

# Write output file
with open(output_file, 'w') as fd_out:
    fd_out.write(', '.join(headers) + '\n')
    for i in range(len(data)):
        output_line = species[i] + ', ' + ', '.join(data[i].astype(str)) + '\n'
        fd_out.write(output_line)
