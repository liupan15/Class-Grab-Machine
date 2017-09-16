close all; clear; clc;

%  ---------------------  no problem --------------------

direct = dir('*.jpg');

lens = size(direct, 1);

tmp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';

X = [];
y = zeros(lens, size(tmp, 2) * 5);

for i = 1 : lens
    filename = direct(i).name;
    string = strrep(filename, '.jpg', '');
    img = imread(filename);
    img = rgb2gray(img);
    %img = imresize(img, 0.5);
    img = reshape(img, 1, size(img, 1) * size(img, 2));
    X = [X; img];
    for j = 1 : size(string, 2)
        tmp1 = strfind(tmp, string(j));
        y(i, tmp1 + (j - 1) * 62) = 1;
    end
end

X = double(X);
X = X / 255;
save('X.mat', 'X');
save('y.mat', 'y');
