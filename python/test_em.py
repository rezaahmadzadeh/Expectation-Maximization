'''
Expectation-Maximization (EM) Algorithm

This is a test program for the Expectation-Maximization algorithm.
At the beginning, we generate two sets of points from two normal
distributions and label them as cluster 1 and 2. This will serve as our 
true value dataset.
The we reshuffle the labels to make the dataset ready for the algorithm.
Given the number of clusters, the algorithm is going to look at the data 
and estimate paramters for two normal distributions that the data is drawn 
from. These parameters include the means and standard variances of those 
Normal Distributions.   
In the next step, we make some initial guess and intentionally we use a bad
guess for the parameters.
Now we run the EM algorithm and the algorithm starts from the initial guess
and iteratively converges to the solution. 
===================================================
Code: Reza Ahmadzadeh - 2023
===================================================
'''
import numpy as np
import matplotlib.pyplot as plt
from EM import *


def generate_random_data(n):
    '''
    This function generates random data
    The points are drawn from two Normal Distributions with parameters (mu, sigma)
    Input: 
        n: number of points in each cluster
    Output: 
        D: the generated dataset, size: 2n x 3 [x y label]
    '''
    mu1 = np.array([0.0, 5.0])
    mu2 = np.array([5.0 , 0.0])
    sigma1 = np.array([[2.0, 0.0], [0.0, 3.0]])
    sigma2 = np.array([[4.0, 0.0], [0.0, 1.0]])

    # For reproducibility
    rng = np.random.default_rng(seed=42)
    D1 = rng.multivariate_normal(mu1, sigma1, n)
    D2 = rng.multivariate_normal(mu2, sigma2, n)
    p1 = np.hstack((D1, np.zeros((n, 1))))
    p2 = np.hstack((D2, np.ones((n, 1))))
    D = np.vstack((p1, p2))
    D_shuffled = rng.permutation(D.copy(), axis=0)
    return D, D_shuffled


# number of points in each cluster
num_points = 100

# generate random data using two 2D Normal distributions with 100 data points 
Data, Data_r = generate_random_data(num_points)

# make some initial guess
Param = make_initial_guess()

# run EM to find the parameters 
Data_f, Param_f = EM(Data_r, Param)

plt.scatter(Data_r[:, 0], Data_r[:, 1], 10, 'b')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Raw Data')
plt.show()


Data1 = Data[0:num_points, 0:2]
Data2 = Data[num_points:2*num_points, 0:2]
plt.scatter(Data1[:, 0], Data1[:, 1], 10, 'b')
plt.scatter(Data2[:, 0], Data2[:, 1], 10, 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('True Value')
plt.show()

Data_f1 = Data_f[Data_f[:,2]==0, :]
Data_f2 = Data_f[Data_f[:,2]==1, :]
plt.scatter(Data_f1[:, 0], Data_f1[:, 1], 10, 'b')
plt.scatter(Data_f2[:, 0], Data_f2[:, 1], 10, 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Data Clustered by EM')
plt.show()
