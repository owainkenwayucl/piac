function [mcp2,err, et] = mcp2(N)
  s_t = tic;
  number_in = 0;
  
  % initialise plot
  clf;
  x = 0:0.0001:1;
  y = sqrt(1 .- x.^2);
  plot(x,y,'k');
  hold on;
  s_x = rand(1,N);
  s_y = rand(1,N);
  R = (s_x.^2 + s_y.^2) <= 1;
  number_in = sum(R);
  scatter(s_x,s_y);
  
  hold off;
  % return estimate, error
  ratio = number_in/N;
  mcp2 = 4*ratio;
  err = abs(pi - mcp2);
  et = toc(s_t);
endfunction
