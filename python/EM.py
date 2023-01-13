'''
===================================================
Expectation-Maximization (EM) Algorithm

Code: Reza Ahmadzadeh - 2023
===================================================
'''
import numpy as np
from scipy.stats import norm


def make_initial_guess():
    '''
    This function makes an inital guess for the EM algorithm to start from
    Here we make the initial parameters manually but they can be calculated 
    using methods such as k-means.
    Input: 
    Output: 
        Param: a dictionary containing the parameters of the two Normal 
            Distributions mu1 (1x2), mu2 (1x2), sigma1 (2x2), sigma2 (1x2), 
            lambda1 (1x1), lambda2 (1x1)
    '''
    Param = dict(
        mu1 = np.array([1.0, 1.0]),
        mu2 = np.array([4.0, 4.0]),
        sigma1 = np.array([[1.0, 0.0],[0.0, 1.0]]),
        sigma2 = np.array([[1.0, 0.0],[0.0, 1.0]]),
        lambd = np.array([0.4, 0.6])
    )
    return Param


def calc_distance(Param, Param_):
    '''
    This function calculates the distance between two sets of parameters. 
    Input: 
        Param : old parameters
        Param_: new parameters
    Output: 
        d: semi-Euclidean distance
    '''
    return np.linalg.norm(Param['mu1'] - Param_['mu1']) + np.linalg.norm(Param['mu2'] - Param_['mu2'])


def prob(point, mu, sigma, lambd):
    '''
    calculate probability / likelihood
    Probability that given a set of parameters \theta for the PDFs the data X can be
    observed.; this is equivalent of the likelihood of the parameters \theta
    given data points X
    point = [x y]
    mu : 1x2
    sigma : 2x2
    lambda : 1x2
    sigma has to be square (actually semi definite positive)
    TODO: check for semidefinite positiveness and fix if not
    Sigma = (Sigma + Sigma.T)  / 2
    '''
    p = lambd
    for ii in range(len(point)):
        p *= norm.pdf(point[ii], mu[ii], sigma[ii,ii])
    return p


def expectation(Data, Param):
    '''
    This function calculates the first step of the EM algorithm, Expectation.
    It calculates the probability of each specific data point belong to each
    cluster or class
    Input: 
        Data : nx3 (number of data points , [x, y, label])
        Param: (mu, sigma, lambda)
    Output: 
        Data: the dataset with updated labels
    '''
    for ii in range(np.shape(Data)[0]):
        x = Data[ii, 0:2]
        p_cluster1 = prob(x, Param['mu1'], Param['sigma1'], Param['lambd'][0])
        p_cluster2 = prob(x, Param['mu2'], Param['sigma2'], Param['lambd'][1])
        
        if p_cluster1 > p_cluster2:
            Data[ii, 2] = 0
        else:
            Data[ii, 2] = 1
    return Data


def maximization(Data, Param):
    '''
    This function calculates the second step of the EM algorithm, Maximization.
    It updates the parameters of the Normal distributions according to the new 
    labled dataset.
    Input: 
        Data : nx3 (number of data points , [x, y, label])
        Param: (mu, sigma, lambda)
    Output: 
        Param: updated parameters 
    '''
    Param_ = Param.copy()
    points_in_cluster1 = Data[Data[:,2] == 0, :]
    points_in_cluster2 = Data[Data[:,2] == 1, :]

    percent_cluster1 = np.size(points_in_cluster1,0) / np.size(Data,0)
    percent_cluster2 = 1 - percent_cluster1

    # calculate the weights
    Param_['lambd'] = np.array([percent_cluster1, percent_cluster2])

    # calculate the means
    Param_['mu1'] = np.array([np.mean(points_in_cluster1[:,0]), np.mean(points_in_cluster1[:,1])])
    Param_['mu2'] = np.array([np.mean(points_in_cluster2[:,0]), np.mean(points_in_cluster2[:,1])])

    # calculate the variances
    Param_['sigma1'] = np.array([[np.std(points_in_cluster1[:,0]), 0.0], [0.0, np.std(points_in_cluster1[:,1])]])
    Param_['sigma2'] = np.array([[np.std(points_in_cluster2[:,0]), 0.0], [0.0, np.std(points_in_cluster2[:,1])]])

    return Param_


def EM(Data, Param, shift=1e8, epsilon=1e-5):       
    '''
    This is the main EM algorithm. It has two steps Expectation (E) and
    Maximization (M). The whole process is done in a while loop until a desired
    error has reached. 
    Input: 
        Data: the dataset including the points and labels [x y label]
        Param: parameters of the Normal Distributions (mu, sigma, lambda)
    Output: 
        Data: the dataset with updated labels
        Param: final parameters that the algorithm has converged to
    '''
    iter = 0
    while shift > epsilon:

        iter += 1

        # E-step
        Data_ = expectation(Data, Param)

        # M-step
        Param_ = maximization(Data_, Param)

        shift = calc_distance(Param, Param_)

        print(f'iter: {iter}, error: {shift}, mu1: {Param_["mu1"]}, mu2: {Param_["mu2"]}')    

        Data = Data_
        Param = Param_
    return Data, Param