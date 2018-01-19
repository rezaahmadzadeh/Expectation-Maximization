function D = generate_random_data(n)
%{ 
This function generates random data
The points are drawn from two Normal Distributions with parameters (mu, sigma)

Input: 
    n: number of points in each cluster

Output: 
    D: the generated dataset [x y label]
%}
mu1 = [0, 5];
mu2 = [5 , 0];
sigma1 = [2, 0; 0, 3];
sigma2 = [4, 0; 0, 1];

rng default  % For reproducibility
D1 = mvnrnd(mu1, sigma1, n);
D2 = mvnrnd(mu2, sigma2, n);
D = [D1(:,1) D1(:,2) 1*ones(size(D1,1),1);
D2(:,1) D2(:,2) 2*ones(size(D2,1),1)];
end

          