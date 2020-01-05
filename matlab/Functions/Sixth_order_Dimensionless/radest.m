% Radius estimation.
%----------------------------------------
function rad = radest(E,x)
    threshold = 0.01;
    global n;
    global alpha;
    ll=length(E);
    for it=1:ll
        if abs(E(it))<threshold
            rad =x(it);
            break
        end
    end
end
%----------------------------------------

