function [Data_f, Param_f] = EM(Data, Param)
%{ 
This is the main EM algorithm. It has two steps Expectation and
Maximization. The whole process is done in a while loop until a desired
error has reached. 

Input: 
    Data: the dataset including the points and labels [x y label]
    Param: parameters of the Normal Distributions (mu, sigma, lambda)

Output: 
    Data_f: the dataset with updated labels
    Param_f: final parameters that the algorithm has converged to
%}

shift = 10000;  % a big number
iter = 0;       % counter
epsilon = 0.001; % percision
formatSpec = 'iteration: %d, error: %2.4f, mu1: [%2.4f %2.4f], mu2: [%2.4f %2.4f] \n';

while shift > epsilon
    iter = iter + 1;

    % E-step
    Data_ = expectation(Data, Param);
    
    % M-step
    Param_ = maximization(Data_, Param);
    
    % calculate the distance/error from the previous set of params
    shift = calc_distance(Param, Param_);
    
    fprintf(formatSpec, iter, shift, Param_.mu1, Param_.mu2);    

    Data = Data_;
    Param = Param_;
    
    clear Data_ Param_
end
Data_f = Data;
Param_f = Param;
end