function Data = expectation(Data, Param)
%{ 
This function calculates the first step of the EM algorithm, Expectation.
It calculates the probability of each specific data point belong to each
cluster or class

Input: 
    Data : nx3 (number of data points , [x, y, label])
    Param: (mu, sigma, lambda)

Output: 
    Data: the dataset with updated labels
%}

for ii = 1: size(Data,1)
    x = Data(ii, 1:2);
    p_cluster1 = prob(x, Param.mu1, Param.sigma1, Param.lambda(1,1));
    p_cluster2 = prob(x, Param.mu2, Param.sigma2, Param.lambda(1,2));
    
    if p_cluster1 > p_cluster2
        Data(ii, 3) = 1;
    else
        Data(ii, 3) = 2;
    end
end
end