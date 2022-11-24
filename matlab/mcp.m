% Estimate pi by Monte Carlo methods, plot points as they are estimated.
% Owain Kenway
function [mcp,err, et] = mcp(N)
  s_t = tic;
  number_in = 0;
  
  % initialise plot
  clf;
  x = 0:0.0001:1;
  y = sqrt(1 .- x.^2);
  plot(x,y,'k');
  hold on;
  
  % looping sample
  for i=1:N
    s_x = rand;
    s_y = rand;

    % if sample is in plot in red else plot in blue
    if (s_x^2 + s_y^2 <= 1) 
      number_in = number_in + 1;
      scatter(s_x,s_y,1,'r');
    else
      scatter(s_x,s_y,1,'b');
    end
    
    % force update
    drawnow();
  end
  
  hold off;
  
  % return estimate, error
  ratio = number_in/N;
  mcp = 4*ratio;
  err = abs(pi - mcp);
  et = toc(s_t);
endfunction
