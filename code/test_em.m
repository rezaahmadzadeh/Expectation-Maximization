%% Expectation-Maximization (EM) Algorithm
%{
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
Code: Reza Ahmadzadeh - IRIM 2018
===================================================

%}
clc, clear, close all

% number of points in each cluster
num_points = 100; 

% generate random data using two 2D Normal distributions with 100 data points 
Data = generate_random_data(num_points);

% reshuffle the data labels
Data_r = [Data(:,1:2) randi(2,2*num_points,1)];

% make some initial guess
Param = make_initial_guess();

% run EM to find the parameters 
[Data_f, Param_f] = EM(Data_r, Param);

%% plot the results
figure; subplot(1,3,1);
scatter(Data(:,1), Data(:,2), 10, 'MarkerEdgeColor', [0 0.5 0.5], 'MarkerFaceColor',[0 0.7 0.7], 'LineWidth',1.5);
grid on; box on;
xlabel('x'); ylabel('y');title('raw data');

Data1 = Data(Data(:,3)==1, :);
Data2 = Data(Data(:,3)==2, :);
subplot(1,3,2);hold on
scatter(Data1(:,1), Data1(:,2), 10, 'MarkerEdgeColor', [0.5 0 0], 'MarkerFaceColor',[0.7 0 0], 'LineWidth',1.5);
scatter(Data2(:,1), Data2(:,2), 10, 'MarkerEdgeColor', [0 0.5 0], 'MarkerFaceColor',[0 0.7 0], 'LineWidth',1.5);
grid on; box on;
xlabel('x'); ylabel('y');title('true value');

Data_f1 = Data_f(Data_f(:,3)==1, :);
Data_f2 = Data_f(Data_f(:,3)==2, :);
subplot(1,3,3); hold on
scatter(Data_f1(:,1), Data_f1(:,2), 10, 'MarkerEdgeColor', [0.5 0 0], 'MarkerFaceColor',[0.7 0 0], 'LineWidth',1.5);
scatter(Data_f2(:,1), Data_f2(:,2), 10, 'MarkerEdgeColor', [0 0.5 0], 'MarkerFaceColor',[0 0.7 0], 'LineWidth',1.5);
grid on; box on;
xlabel('x'); ylabel('y');title('data clustered by EM');
