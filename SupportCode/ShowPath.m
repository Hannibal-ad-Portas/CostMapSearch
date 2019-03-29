function [] = ShowPath(fnamePath)
fp = fopen(fnamePath, 'r');
A = fscanf(fp, '%d %d', [2, Inf]);
fclose(fp);
x = A(1, :) + 1;
y = A(2, :) + 1;
plot(x, y, '-ro', 'linewidth', 3);
end

