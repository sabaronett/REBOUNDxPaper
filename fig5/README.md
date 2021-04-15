# Figure 5

## Prerequisites
- [NumPy](https://numpy.org/)
- [REBOUND](https://rebound.readthedocs.io/)
- [REBOUNDx](https://reboundx.readthedocs.io/)
- [psutil](https://pypi.org/project/psutil/) (for tracking active memory usage)

## Sample Scripts
Contained here are two main subdirectories that correspond to the solid ([`/tides_off/`](https://github.com/sabaronett/REBOUNDxPaper/blob/master/fig5/tides_off)) and dashed ([`/tides_on/`](https://github.com/sabaronett/REBOUNDxPaper/blob/master/fig5/tides_on)) curves in Fig. 5 of [Baronett et al. (2021)](https://arxiv.org).  Each one contains a sample set of runs, e.g., [`/10Mearth/`](https://github.com/sabaronett/REBOUNDxPaper/blob/master/fig5/tides_off/10Mearth/), corresponding to the respective orbital mass sequentially initialized across a range of semi-major axes from 0.4 to 1.6 AU in 0.1 AU increments (see Fig. 5 and §4.2 of our paper for more information).  Also included are required stellar evolution data from `MESA` needed to run the scripts as well as sample output results from runs on a compute cluster.

## Acknowledgement
If you find any code here useful in your research, we would greatly appreciate a citation of our immplementation paper, [Baronett et al. (2021)](https://arxiv.org), in your work.

## Issues
If you have any questions, suggestions, or encounter any problems with the code in this repository, please let us know by opening an [issue](https://github.com/sabaronett/REBOUNDxPaper/issues). We appreciate the feedback.
