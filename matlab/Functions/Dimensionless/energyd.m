% Energy density.
%----------------------------------------
function energy = energyd(y,x)
    global n;
    global alpha;

% Function redefinition:

    f = y(1,:);
    %fprime = der(y(1,:),x);
    fprime = y(2,:);
    A0 = y(3,:);
    A=y(4,:);
    Arescaled=y(4,:)+n./x; % This should alleviate numerical noise
    Aprime= der(Arescaled,x);
    minenergy=-1/2;
energy=  fprime.^2+ f.^2.*(Arescaled- n./x).^2 + f.^2.*(A0 -1).^2 -f.^2 + (1./2).*f.^4 -minenergy ;
end
%----------------------------------------

