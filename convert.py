#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import glob

input_dir = 'data'
files_list = glob.glob(os.path.join(input_dir, '*.txt'))
output_file = 'dataset_raw.txt'

output_list = []
for f in sorted(files_list):
    with open(f, 'r') as fd:
        filename = os.path.splitext(os.path.split(f)[-1])[0]
        filename = filename.replace('.', '')
        filename_parts = filename.split(' ')
        genus = filename_parts[0]
        species = filename_parts[1:-2]
        if species[0] == 'acanthocephalus':
            species[0] = 'acephalus'
        other_info = filename_parts[-2]
        number_of_lobes = filename_parts[-1]
        identifier = genus + ''.join(species)[:5-len(other_info)] + other_info + number_of_lobes
        output_line = [identifier]
        for i, line in enumerate(fd):
            if i > 0:
                p, x, y, s, c, ID = line.split()
                output_line += [x, y]
        output_list.append(output_line)
        print(output_line)

with open(output_file, 'w') as fd:
    fd.write('ID, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8\n')
    for line in output_list:
        fd.write(', '.join(line) + '\n')
