function Param = maximization(Data, Param)
%{ 
This function calculates the second step of the EM algorithm, Maximization.
It updates the parameters of the Normal distributions according to the new 
labled dataset.

Input: 
    Data : nx3 (number of data points , [x, y, label])
    Param: (mu, sigma, lambda)

Output: 
    Param: updated parameters 
%}

points_in_cluster1 = Data(Data(:,3) == 1,:);
points_in_cluster2 = Data(Data(:,3) == 2,:);

percent_cluster1 = size(points_in_cluster1,1) / size(Data,1);
percent_cluster2 = 1 - percent_cluster1;

% calculate the weights
Param.lambda = [percent_cluster1, percent_cluster2];

% calculate the means
Param.mu1 = [mean(points_in_cluster1(:,1)), mean(points_in_cluster1(:,2))];
Param.mu2 = [mean(points_in_cluster2(:,1)), mean(points_in_cluster2(:,2))];

% calculate the variances
Param.sigma1 = [std(points_in_cluster1(:,1)) 0; 0 std(points_in_cluster1(:,2))];
Param.sigma2 = [std(points_in_cluster2(:,1)) 0; 0 std(points_in_cluster2(:,2))];

end