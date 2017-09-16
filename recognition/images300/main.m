close all; clear; clc;

input_layer_size = 2500;
hidden_layer_size = 25;
num_labels = 62 * 5;

load('X.mat');
load('y.mat');

X = double(X);
% ------------- rand    this is no sense
tmp = [X, y];
sel = randperm(size(tmp, 1));
data = tmp(sel, :);
X = data(:, 1: end - 310);

y = data(:, end - 309 : end);

% -------------- initial
initial_Theta1 = randInitializeWeights(input_layer_size, hidden_layer_size);
initial_Theta2 = randInitializeWeights(hidden_layer_size, num_labels);

initial_nn_params = [initial_Theta1(:) ; initial_Theta2(:)];

fprintf('Training Neural Network... \n');
options = optimset('MaxIter', 15000);
lambda = 1;

costFunction = @(p) nnCostFunction(p, input_layer_size, hidden_layer_size, num_labels, X, y, lambda);

[nn_params, cost] = fmincg(costFunction, initial_nn_params, options);

Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
                 hidden_layer_size, (input_layer_size + 1));

Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                 num_labels, (hidden_layer_size + 1));
             
predict(Theta1, Theta2, X(1, :))
save('Theta1.mat', 'Theta1');
save('Theta2.mat', 'Theta2');