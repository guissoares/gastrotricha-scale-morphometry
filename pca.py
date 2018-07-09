#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import glob
import numpy as np
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt
from collections import OrderedDict

input_file, title, scale_of_the_scales = ('dataset_procrustes.txt', 'PCA - Positions', .06)
#input_file, title, scale_of_the_scales = ('distances.txt', 'PCA - Distances', .06)
#input_file, title, scale_of_the_scales = ('angles.txt', 'PCA - Angles', 3.)
#input_file, title, scale_of_the_scales = ('all_data.txt', 'PCA - Positions, Angles and Distances', 0.06)
plot_type = 'scales'    # '2d', '3d' or 'scales'
annotation = True
colors = ['#ffdb1d', '#629ea0', '#601047']
legend_labels = ['unilobate', 'trilobate', 'pentalobate']
points_file = 'dataset_procrustes.txt'
aspect_ratio = 5./8.

def parse_data_file(filename):
    X = []
    y = []
    S = []
    with open(filename, 'r') as fd_in:
        for i, line in enumerate(fd_in):
            if i > 0:
                # Parse the values
                values = line.split(',')
                species = values[0]
                values = values[1:]
                points = list(map(float, map(str.strip, values)))
                X.append(points)
                label = int(species[-1])
                S.append(species[:-1])
                y.append(label)
    return S, np.array(X), np.array(y)
S, X, y = parse_data_file(input_file)

print(X.shape)
labels, y = np.unique(y, return_inverse=True)

pca = PCA()
Xpca = pca.fit_transform(X)
print('=================================================')
print(' PC          Eigenvalues          % of total var ')
print('-------------------------------------------------')
for i, (eigv, r) in enumerate(zip(pca.explained_variance_, pca.explained_variance_ratio_)):
    print(' {: >2d}            {: >8.3f}                {: >5.2f}'.format(i+1, eigv, 100*r))
print('=================================================')

plt.rcParams['svg.fonttype'] = 'none'
if plot_type == '3d':
    from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for i in range(len(labels)):
        mask = (y == i)
        ax.scatter(Xpca[mask,0], Xpca[mask,1], Xpca[mask,2], color=colors[i])
    if annotation:
        for i, x in enumerate(Xpca):
            ax.annotate(S[i], x[:2], size='x-small', xytext=(6,2), textcoords='offset pixels')      
    ax.legend(legend_labels)
    plt.title(title)
    plt.show()
elif plot_type == '2d':
    for i in range(len(labels)):
        mask = (y == i)
        plt.scatter(Xpca[mask,0], Xpca[mask,1], color=colors[i])
    if annotation:
        for i, x in enumerate(Xpca):
            plt.annotate(S[i], x[:2], size='x-small', xytext=(6,2), textcoords='offset pixels')
    plt.legend(legend_labels)
    plt.title(title)
    plt.show()
elif plot_type == 'scales':
    _, points, _ = parse_data_file(points_file)
    for i in range(len(Xpca)):
        polygon = points[i].reshape(-1, 2)
        polygon[:,1] = -polygon[:,1]
        polygon[:,0] = aspect_ratio * polygon[:,0]
        polygon = polygon * scale_of_the_scales + Xpca[i,:2]
        plt.fill(polygon[:,0], polygon[:,1], color=colors[y[i]], label=legend_labels[y[i]])
    if annotation:
        for i, x in enumerate(Xpca):
            plt.annotate(S[i], x[:2], size='xx-small', xytext=(6,2), textcoords='offset pixels')
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = OrderedDict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys())
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.title(title)
    plt.gca().set_aspect(aspect_ratio)
    plt.show()
else:
    print('Error: "plot_type" must be either \'2d\', \'3d\' or \'scales\'')
