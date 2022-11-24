% Estimate pi by Monte Carlo methods. Use vector/matrix math so very fast,
% but must plot at the end.
% Owain Kenway
function [mcp2,err,et] = mcp2(N)
  s_t = tic;
  
  % initialise plot
  clf;
  x = 0:0.0001:1;
  y = sqrt(1 .- x.^2);
  plot(x,y,'k');
  colours = [0 0 1; 1 0 0 ];
  hold on;
  
  % Generate random x and y
  s_x = rand(1,N);
  s_y = rand(1,N);
  
  % is a "truth" array of if a point is in
  R = (s_x.^2 + s_y.^2) <= 1; 
  
  % map in or out to colours in colour map
  c = colours(R .+ 1, :);
  
  % plot
  scatter(s_x,s_y,1,c);
  hold off;
  
  % return estimate, error
  ratio = sum(R)/N;
  mcp2 = 4*ratio;
  err = abs(pi - mcp2);
  et = toc(s_t);
end
