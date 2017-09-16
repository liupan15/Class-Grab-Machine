close all; clear; clc;

load('Theta1.mat');
load('Theta2.mat');

load('X.mat');
load('y.mat');
X = double(X);

direct = dir('*.jpg');

cnt = 0;
for i = 1:300
    %data = X(i, :);
%     filename = direct(i).name;
%     string1 = strrep(filename, '.jpg', '');
%     img = imread(filename);
%     imshow(img);
%     img = rgb2gray(img);
%     img = imresize(img, [25, 100],'bilinear', 'Antialiasing', false)
%     img = reshape(img, 1, size(img, 1) * size(img, 2));
%     img = double(img);
%     img = img / 255
    img = X(i, :);
    string2 = predict(Theta1, Theta2, img)
    if(strcmpi(string1, string2))
        cnt = cnt + 1;
    end
    pause;
end

% cnt / 300
% data = reshape(data, 50 * 0.6, 200 * 0.6);
% imshow(data);
% num = y(1, :);
% % size(num)
% 
% num = reshape(num, 62, 5);
% num = num';