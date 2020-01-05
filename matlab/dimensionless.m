addpath('Functions/Dimensionless/')
clear all

% Parameter declaration:
%----------------------------------------
    global n;
    global alpha;
    global zero;
    n=-20;
    alpha=4;
    lastel=8150; % High cutoff point for the plot.
    firstel=1;  % Low cutoff point for the plot.
    zero=0.01;      % High cutoff point for the bvp solver.
    infty=22;    % High cutoff point for the bvp solver.
%----------------------------------------

% BVP:
%----------------------------------------
    xmesh =linspace(zero,infty,1845);
    solinit = bvpinit(xmesh, @guess);
    opts=bvpset('Stats', 'on', 'NMax', 185000);
    sol = bvp4c(@bvpfunc, @bcfunction, solinit,opts);
    lastel = size(sol.x,2);
    residue=sol.stats.maxres;
%----------------------------------------

% Field definitions:
%----------------------------------------
    A0=sol.y(3,:);
    Ainbetween=sol.y(4,:)+n./sol.x; % This should alleviate numerical noise
    derivA=der(Ainbetween, sol.x);
    derivA0=der(A0, sol.x);
    fdoubleprime=der(sol.y(2,:), sol.x);
    Aterm = (Ainbetween./sol.x);
    Bfield= (derivA  + Aterm(1:end));
    flux = (sol.y(4,:).*sol.x+n);
    remainderenergy=((1-sol.y(1,:).^2).*(A0-1).*sol.y(1,:).^2./2 + (A0-1).^2.*sol.y(1,:).^2+(alpha-2).*(sol.y(1,:).^2 -1).*Bfield./2).*sol.x;
    BPSenergy=((sol.y(2,:)-(sol.y(4,:).*sol.y(1,:))).^2);
    modelFlux=Bfield.*(sol.x.^2)./2;
%----------------------------------------

% Energy Computation:
%----------------------------------------
    energy = energyd(sol.y, sol.x);
    coreEnergy=coreE(energy(firstel), zero);
%----------------------------------------

% Plots:
%----------------------------------------

% Plot 1 (everything):
%----------------------------------------

% This defines the colours of the plots using an rgb scheme from 0 to 1.
set(gca, 'ColorOrder', [1 0 0; 0.7 0.1 0.8; 0 1 0; 0.7 0.2 0.1;0.1 0.2 1;0.2 0.2 0.1],'NextPlot', 'replacechildren');   

% This defines which profiles are to be plotted.
    plot(sol.x(firstel:lastel),Bfield(firstel:lastel), sol.x(firstel:lastel), sol.y(1,firstel:lastel), sol.x(firstel:lastel), A0(firstel:lastel)-1, sol.x(firstel:lastel) , flux(firstel:lastel), '--', sol.x(firstel:lastel),derivA0(firstel:lastel),sol.x(firstel:lastel), energy(firstel:lastel), 'LineWidth', 2)
legend('B(r)','f(r)','A_0(r)','A_\theta(r)','E(r)',"ℰ(r)",'Location','northeast','FontSize',18);

% Title
mytitleText = ['n=',num2str(n),', \alpha=',num2str(alpha)];
title(mytitleText,'FontSize', 20);

%----------------------------------------



%----------------------------------------

% Characteristics:
%----------------------------------------
    dx=diff(sol.x);
    dx1=[dx, dx(end)];
    dx2=[dx(1),dx];
    dx = dx1./2 + dx2./2;
    coreFlux=coreE(Bfield(firstel), zero);
    totalflux=sum(sol.x.*Bfield.*dx(1:end))+coreFlux;
    totalenergy=sum(sol.x.*energy.*dx(1:end))+coreEnergy;
    radius=radest(energy, sol.x);
    radius_flux_based=radest(flux-modelFlux, sol.x);
    [maxenergy, indexof_maxenergy] = max(energy);
    [maxBfield, indexof_maxBfield] = max(Bfield);
    radius_energy_peak_based=max(sol.x(indexof_maxenergy));
    A0max=A0(firstel);
    A0fint=sum(sol.x.*A0.*dx(1:end));
    totalremainderenergy=sum(remainderenergy.*dx);
    totalremainderBPSeqn=sum(BPSenergy.*dx);
%----------------------------------------

% Write data:
%----------------------------------------
    data = [n,alpha,totalflux, totalenergy, radius, A0max,maxBfield, residue];


    % Writes data to file ../data/Dimensionless_Data.txt
    %----------------------------------------
    fileID = fopen('../data/Dimensionless_Data.txt','a');
    nbytes = fprintf(fileID,'%5f %5f %5f %5f %5f %5f %5f %5f\n',data);
    fclose(fileID);
    %----------------------------------------

    % Writes solutions to file ../data/solutions/dimensionless_solution_n<<value of n>>_alpha<<value of alpha>>.csv
    % The profiles are the Magnetic field, scalar field, A0, Atheta, the electric field and the energy.
    %----------------------------------------
    solution_to_write=[sol.x(firstel:lastel);Bfield(firstel:lastel); sol.y(1,firstel:lastel);  A0(firstel:lastel)-1; flux(firstel:lastel);derivA0(firstel:lastel); energy(firstel:lastel)];
    solutions_filename = ['../data/solutions/dimensionless_solution_n',num2str(n),'_alpha',num2str(alpha),'.csv'];
    flush_old_data = fopen(solutions_filename, 'w');
    overwrite = fprintf(flush_old_data, '');
    fclose(flush_old_data);
    solutions_file = fopen(solutions_filename, 'a');
    nbytes2 = fprintf(solutions_file, 'x,B,f,A0,Atheta,A0`, energy\n');
    nbytes3 = fprintf(solutions_file, '%5f,%5f,%5f,%5f,%5f,%5f,%5f\n', solution_to_write);
    fclose(solutions_file);
    %----------------------------------------


    % Writes the error in how well the BPS equation is satisfied to a file ../data/solutions/dimensionless_BPS_eqn_n<<value of n>>_alpha<<value of alpha>>.csv
    %----------------------------------------
    BPS_data_to_write=[sol.x(firstel:lastel); sol.y(2,firstel:lastel)- sol.y(4,firstel:lastel).*sol.y(1,firstel:lastel)];
    BPS_filename = ['../data/solutions/dimensionless_BPS_eqn_n',num2str(n),'_alpha',num2str(alpha),'.csv'];
    flush_old_data_BPS = fopen(BPS_filename, 'w');
    overwrite = fprintf(flush_old_data_BPS, '');
    fclose(flush_old_data_BPS);
    BPS_file = fopen(BPS_filename, 'a');
    nbytes4 = fprintf(BPS_file, 'x,bps\n');
    nbytes5 = fprintf(BPS_file, '%5f,%5f\n', BPS_data_to_write);
    fclose(BPS_file);
    %----------------------------------------

%----------------------------------------
