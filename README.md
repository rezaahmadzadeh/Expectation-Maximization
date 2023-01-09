# Expectation-Maximization
Expectation-Maximization (EM) algorithm in Matlab and Python

This code implements the Expectation-Maximization (EM) algorithm and tests it on a simple 2D dataset.

The Expectation–Maximization (EM) algorithm is an iterative method to find maximum likelihood or maximum a posteriori (MAP) estimates of parameters in statistical models, where the model depends on unobserved latent variables. The EM iteration alternates between performing an expectation (E) step, which creates a function for the expectation of the log-likelihood evaluated using the current estimate for the parameters, and a maximization (M) step, which computes parameters maximizing the expected log-likelihood found on the E step. These parameter-estimates are then used to determine the distribution of the latent variables in the next E step.

## Example - MATLAB ##

In this example, we first generate a dataset of points from two Normal distributions and label the dataset. This dataset with correct labels are our true values. Then we reshuffle the labels and run the EM algorithm for the new dataset. The EM algorithm clusters the dataset correctly and also estimates the parameters of two Normal distributions that could be used to draw the points. 

![testing EM algorithm](https://github.com/rezaahmadzadeh/Expectation-Maximization/blob/master/result/EM_result.png?raw=true "EM")

The result that I get on my machine is as follows:

```
iteration: 1, error: 1.7244, mu1: [1.2662 1.7053], mu2: [3.6623 3.0902] 
iteration: 2, error: 2.6173, mu1: [0.3989 2.7791], mu2: [4.3558 2.0659] 
iteration: 3, error: 3.2419, mu1: [0.0288 4.2253], mu2: [5.0751 0.4715] 
iteration: 4, error: 0.6577, mu1: [0.0377 4.5441], mu2: [5.0656 0.1329] 
iteration: 5, error: 0.3204, mu1: [0.1280 4.6579], mu2: [5.0202 -0.0363] 
iteration: 6, error: 0.1810, mu1: [0.1833 4.7249], mu2: [4.9603 -0.1089] 
iteration: 7, error: 0.0000, mu1: [0.1833 4.7249], mu2: [4.9603 -0.1089] 
```

## Example - Python ##
Here, we generated a new 2D dataset similar to the one above and tested the python version of the algorithm.

![testing EM algorithm](https://github.com/rezaahmadzadeh/Expectation-Maximization/blob/master/result/EM_result_python.png?raw=true "EM")

The result that I get on my machine is as follows:

```
iter: 1, error: 2.029586515126125, mu1: [1.17678819 1.95190418], mu2: [3.77180604 2.96341528]
iter: 2, error: 3.106544647452483, mu1: [0.41602816 3.22681386], mu2: [4.76689272 1.68264085]
iter: 3, error: 3.2266364206724742, mu1: [-0.02893002  4.63086576], mu2: [5.40751145 0.05006616]
iter: 4, error: 0.3650377672928439, mu1: [-0.04878351  4.83147512], mu2: [ 5.26045562 -0.02127781]
iter: 5, error: 0.28674238851510725, mu1: [-0.06527338  4.97445883], mu2: [ 5.11766831 -0.01867893]
iter: 6, error: 0.0, mu1: [-0.06527338  4.97445883], mu2: [ 5.11766831 -0.01867893]
```
### Version ###
*  2.0 - Python implementation added
*  1.0 - MATLAB implementation

### How do I get set up? ###

#### Python ####
* The algorithm is coded in Python 3.x
* it relies on `numpy` and `scipy` modules
* clone the repository
* run the `test_em.py` from the `python` folder.

#### MATLAB ####
* The algorithm is coded in MATLAB
* No extra Toolbox is required
* clone the repository, 
* In Matlab, set the `code` folder as the current path and run the `test_em.m` file.
