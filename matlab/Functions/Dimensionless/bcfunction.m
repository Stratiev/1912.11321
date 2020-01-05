% Boundary conditions function.
%----------------------------------------
function res = bcfunction(ya,yb) 
global n;
global alpha;
global zero;
res = [ ya(1)
        ya(4)+n/zero+zero/(alpha*2)
        yb(1)-1
        yb(3)-1];
end
%----------------------------------------
