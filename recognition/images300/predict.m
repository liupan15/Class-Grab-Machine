function string = predict(Theta1, Theta2, X)
%PREDICT Predict the label of an input given a trained neural network
%   p = PREDICT(Theta1, Theta2, X) outputs the predicted label of X given the
%   trained weights of a neural network (Theta1, Theta2)

% 只支持一组数据
% Useful values
m = size(X, 1);
%num_labels = size(Theta2, 1);     %%%%%%

% You need to return the following variables correctly 
% p = zeros(size(X, 1), 1);
h1 = sigmoid([ones(m, 1) X] * Theta1')
h2 = sigmoid([ones(m, 1) h1] * Theta2');
h2 = reshape(h2, 62, 5);
h2 = h2';
string = '';
[dummy, p] = max(h2, [], 2);

tmp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';

for i = 1 : 4
    string = strcat(string, tmp(p(i)));
end
if(dummy(5) > 0.1)
    string = strcat(string, tmp(p(5)));
end
% =========================================================================
X = reshape(X, 50 * 0.5, 200 *0.5);
%X = uint8(X);
imshow(X);

