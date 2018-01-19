function Param = make_initial_guess()
%{ 
This function makes an inital guess for the EM algorithm to start from
Here we make the initial parameters manually but they can be calculated 
using methods such as k-means.

Input: 

Output: 
    Param: a structure containing the parameters of the two Normal 
        Distributions mu1 (1x2), mu2 (1x2), sigma1 (2x2), sigma2 (1x2), 
        lambda1 (1x1), lambda2 (1x1)
%}

Param = struct();
Param.mu1 = [1, 1];
Param.mu2 = [4, 4];
Param.sigma1 = [1 0; 0 1];
Param.sigma2 = [1 0; 0 1];
Param.lambda = [0.4, 0.6];
end