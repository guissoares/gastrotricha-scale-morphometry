# Morphometry of Gastrotricha scales 

This repository contains the data and the Python scripts used in the morphometric analysis of scales of Gastrotricha. This work was part of a Master's project developed at by Kayla Wirthwein at the University of Campinas, Brazil, under the supervision of André Garraffoni.

## Getting Started

### Prerequisites

- Python 3
- NumPy
- SciPy
- scikit-learn
- Matplotlib

### Data description

In the analysis we used data from 8 landmarks in the scales of animals of the phylum [Gastrotricha](https://en.wikipedia.org/wiki/Gastrotrich). 67 species were studied, from which a total of 162 sample scales were analyzed.

The directory `data` contains *.txt* files, each with data from a different sample. The files were generated using [ImageJ](https://imagej.net), and are named as such:

    [genus] [species] [index] [number of lobes].txt

where

- `genus`: the genus of the specimen of the sample, according to its scientific name
- `species`: the species of the specimen of the sample, according to its scientific name
- `index`: a number that distinguishes samples from the same species
- `number of lobes`: the number of lobes of the sample, which can be either 1, 3 or 5

#### Examples:

- `C. aemilianus 1 3.txt` (Chaetonotus *aemilianus*, sample #1, trilobate scale)
- `C. aemilianus 2 3.txt` (Chaetonotus *aemilianus*, sample #2, trilobate scale)
- `C. brachyurus 1 1.txt` (Chaetonotus *brachyurus*, sample #1, unilobate scale)
- `C. brachyurus 2 5.txt` (Chaetonotus *brachyurus*, sample #2, pentalobate scale)
- `Ceph. kisielewskii 1 1.txt` (Cephalionotus *kisielewskii*, sample #1, unilobate scale)
- `Ceph. kisielewskii 2 1.txt` (Cephalionotus *kisielewskii*, sample #2, unilobate scale)


## Authors
- [**Kayla Wirthwein**](https://www.researchgate.net/profile/Kayla_Wirthwein) - *Researcher*
- [**Guilherme S. Soares**](https://www.researchgate.net/profile/Guilherme_Saraiva_Soares) - *Programmer*
- [**André R. S. Garraffoni**](https://www.researchgate.net/profile/Andre_Garraffoni) - *Research Supervisor*


## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
