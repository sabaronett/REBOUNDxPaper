# REBOUNDxPaper
Supplemental resources to accompany our implementation paper for new features in REBOUNDx versions 3.0.5 and 3.1.0. Includes `mesa2txt` tutorial, with scripts to import, isolate, and export data from [MESA](http://mesa.sourceforge.net/) (Modules for Experiments in Stellar Astrophysics), for use with ["Parameter Interpolation"](https://reboundx.readthedocs.io/en/latest/effects.html#parameter-interpolation) in REBOUNDx.

## Prerequisites
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)
- [REBOUND](https://rebound.readthedocs.io/)
- [REBOUNDx](https://reboundx.readthedocs.io/)
- [py_mesa_reader](https://github.com/wmwolf/py_mesa_reader) (for `mesa2txt.ipynb`)

## Usage

### Figures from Baronett, et al. (2020)
This repository contains Jupyter Notebooks (e.g., [`fig1.ipynb`](https://github.com/sabaronett/REBOUNDxPaper/blob/master/fig1.ipynb)) with code to generate the figures seen in our implementation paper, [Baronett et al. (2020)](https://arxiv.org).

### MESA-REBOUNDx Parameter Interpolation
For those interested in incorporating stellar evolution data from MESA into REBOUND simulations, we recommend following the methodology laid out in [`mesa2txt.ipynb`](https://github.com/sabaronett/REBOUNDxPaper/blob/master/mesa2txt.ipynb), to easily extract desired stellar properties from MESA output logs, for use with REBOUNDx's ["Paramter Interpolation"](https://reboundx.readthedocs.io/en/latest/effects.html#parameter-interpolation).

### MESA Project Files
We've made available our MESA project files, including custom inlists, etc., under the `mesa` subfolder. See the subfolder's [README](https://github.com/sabaronett/REBOUNDxPaper/tree/master/mesa) for more details.

## Acknowledgement
If you find any code here useful in your research, in particular the [`mesa2txt`](https://github.com/sabaronett/REBOUNDxPaper/blob/master/mesa2txt.ipynb) methodology, we would greatly appreciate a citation of our immplementation paper, [Baronett et al. (2020)](https://arxiv.org), in your work.

## Issues
If you have any questions, suggestions, or encounter any problems with the code in this repository, please let us know by opening an [issue](https://github.com/sabaronett/REBOUNDxPaper/issues). We appreciate the feedback.
