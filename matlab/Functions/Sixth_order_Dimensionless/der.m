% Derivative computation.
%----------------------------------------
function derivative = der(y,x)
    dy=gradient(y);
    dx=gradient(x);
    derivative=dy./dx;
    %derivative=[derivative, derivative(end)]; % Addition of an extra element is necessary to make array sizes match.
end
%----------------------------------------

