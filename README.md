# Expectation-Maximization
Expectation-Maximization (EM) algorithm in Matlab

This code implements the Expectation-Maximization (EM) algorithm and tests it on a simple 2D dataset.

The Expectation–Maximization (EM) algorithm is an iterative method to find maximum likelihood or maximum a posteriori (MAP) estimates of parameters in statistical models, where the model depends on unobserved latent variables. The EM iteration alternates between performing an expectation (E) step, which creates a function for the expectation of the log-likelihood evaluated using the current estimate for the parameters, and a maximization (M) step, which computes parameters maximizing the expected log-likelihood found on the E step. These parameter-estimates are then used to determine the distribution of the latent variables in the next E step.

![testing EM algorithm](https://github.com/rezaahmadzadeh/Expectation-Maximization/blob/master/result/EM_result.png?raw=true "EM")


### Version ###
*  1.0

### How do I get set up? ###

#### MATLAB ####
* The algorithm is coded in MATLAB
* No extra Toolbox is required
* clone the repository, 
* In Matlab, set the `code` folder as the current path and run the `test_em.m` file.
