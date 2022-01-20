# Figure 4

## Prerequisites
- [NumPy](https://numpy.org/)
- [REBOUND](https://rebound.readthedocs.io/)
- [REBOUNDx](https://reboundx.readthedocs.io/)
- [psutil](https://pypi.org/project/psutil/) (optional, for tracking active memory usage)

## Sample Scripts
Contained here are two main subdirectories that correspond to the top ([`/engulfment/`](https://github.com/sabaronett/REBOUNDxPaper/blob/master/fig4/engulfment)) and bottom ([`/expansion/`](https://github.com/sabaronett/REBOUNDxPaper/blob/master/fig4/expansion)) subplots in Fig. 4 of [Baronett et al. (2022)](https://doi.org/10.1093/mnras/stac043).
Each one contains all the plotted runs, e.g., [`/1e3/`](https://github.com/sabaronett/REBOUNDxPaper/blob/master/fig4/engulfment/1e3), corresponding to the respective "parameter update interval" (in years) measured in that simulation (see Fig. 4 and §4.1 of our paper for more information).
Also included are required stellar evolution data from `MESA` needed to run the scripts as well as sample output results from runs on a compute cluster.

## Acknowledgement
If you find any code here useful in your research, we would greatly appreciate a citation of our immplementation paper, [Baronett et al. (2022)](https://doi.org/10.1093/mnras/stac043), in your work.

## Issues
If you have any questions, suggestions, or encounter any problems with the code in this repository, please let us know by opening an [issue](https://github.com/sabaronett/REBOUNDxPaper/issues).
We appreciate any feedback.
