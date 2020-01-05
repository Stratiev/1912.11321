% Initial guess function.
%----------------------------------------
function g = guess(x) 
global n;
global alpha;
    if (x>1)   
       g= [ x
           x
           1
           1/x];
    else
       g= [ x
           x
           1
           0.00004*x];
    end
end 
%----------------------------------------
