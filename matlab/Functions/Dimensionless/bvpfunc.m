% Statement of BVP:
function dydx = bvpfunc(x,y)
    global n;
    global alpha;

% Note on notation:
%   f = y(1)
%   f'=\gamma=y(2)
%   A0 = y(3)
%   a = y(4)

% The equations in physics notation are:
%       1. f' = \gamma
%       2. \gamma' = - \gamma/r +(a)^2* f -  A0^2* f+ \lambda f^3
%       3. A0'= (f^2 a )/\kappa
%       4. a' = -\mu^3/(\lambda) - a/r+ f^2 A0


dydx = zeros(4,1);
dydx = [y(2)
       (-y(2)/x +(y(4))^2*y(1))-(y(3)^2*y(1))+y(1)^3
       ((y(1)^2)*y(4)/alpha)
       (-1)./alpha - y(4)/x + y(1)^2*y(3)./alpha];

end
%----------------------------------------
