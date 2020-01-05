addpath('Functions/Sixth_order_Dimensionless/')
clear all

% Parameter declaration:
%----------------------------------------
    global n;
    global alpha;
    global zero;
    n=-1;
    alpha=5;
    lastel=7150; % High cutoff point for the plot.
    firstel=1;  % Low cutoff point for the plot.
    zero=0.1;      % High cutoff point for the bvp solver.
    infty=30;    % High cutoff point for the bvp solver.
%----------------------------------------

% BVP:
%----------------------------------------
    xmesh =linspace(zero,infty,2845);
    solinit = bvpinit(xmesh, @guess);
    opts=bvpset('Stats', 'on', 'NMax', 285000, 'RelTol', 1e-9);
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
    Aterm = (Ainbetween./sol.x);
    Bfield= (derivA  + Aterm(1:end));
    flux = (sol.y(4,:).*sol.x+n);
    remainderenergy=((1-sol.y(1,:).^2).*(A0-1).*sol.y(1,:).^2./2 + (A0-1).^2.*sol.y(1,:).^2+(alpha-2).*(sol.y(1,:).^2 -1).*Bfield./2).*sol.x;
    BPSenergy=((sol.y(2,:)-(sol.y(4,:).*sol.y(1,:))).^2).*sol.x;
    modelFlux=Bfield(firstel:lastel).*sol.x(firstel:lastel).^2./2;
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
set(gca, 'ColorOrder', [1 0 0; 0.7 0.1 0.8; 0 1 0; 0.7 0.2 0.1;0.1 0.2 1;0.2 0.2 0.1],'NextPlot', 'replacechildren');   
    plot(sol.x(firstel:lastel),Bfield(firstel:lastel), sol.x(firstel:lastel), sol.y(1,firstel:lastel), sol.x(firstel:lastel), A0(firstel:lastel)-1, sol.x(firstel:lastel) , flux(firstel:lastel), '--', sol.x(firstel:lastel),derivA0(firstel:lastel),sol.x(firstel:lastel), energy(firstel:lastel), 'LineWidth', 2)
legend('B(r)','f(r)','A_0(r)','A_\theta(r)','E(r)',"ℰ(r)",'Location','northeast','FontSize',18);
%xlim([0 8]); % set x axis limit
%ylim([-1.2 3]); % y axis limit
%set(gca,'YTick',[-1 -0.5 0 0.5 1]);  % set where the ticks should be 
%set(gca,'XTick',(0:2.5:10)); % or this way: start at 0, then every 2.5 until reach 10
mytitleText = ['n=',num2str(n),', \alpha=',num2str(alpha)];
title(mytitleText,'FontSize', 20); % add title %ylabel('','FontSize', 18); % add y label xlabel('r','FontSize', 18); % add xlabel
fig1=gcf;
name1=['../figures/dimensionless_6thorder_n',num2str(n),'alpha',erase(num2str(alpha),"."),'all.png'];
saveas(fig1,name1)
close all
%----------------------------------------

% Plot 2 (energy):
%----------------------------------------
set(gca, 'ColorOrder', [0.2 0.2 0.1],'NextPlot', 'replacechildren');   
    plot(sol.x(firstel:lastel), energy(firstel:lastel), 'LineWidth', 2)
legend("ℰ(r)",'Location','northeast','FontSize',18);
%xlim([0 8]); % set x axis limit
ylim([0 max(energy(firstel:lastel))+1]); % y axis limit
%set(gca,'YTick',[-1 -0.5 0 0.5 1]);  % set where the ticks should be 
%set(gca,'XTick',(0:2.5:10)); % or this way: start at 0, then every 2.5 until reach 10
mytitleText = ['n=',num2str(n),', \alpha=',num2str(alpha)];
title(mytitleText,'FontSize', 20); % add title
%ylabel('','FontSize', 18); % add y label
xlabel('r','FontSize', 18); % add xlabel
fig2=gcf;
name2=['../figures/dimensionless_6thorder_n',num2str(n),'alpha',erase(num2str(alpha),"."),'energy.png'];
saveas(fig2,name2)
%close all
%----------------------------------------

% Plot 3 (profiles):
%----------------------------------------
set(gca, 'ColorOrder', [1 0 0; 0.7 0.1 0.8; 0 1 0; 0.7 0.2 0.1;0.1 0.2 1;0.2 0.2 0.1;0 0.5 0.8; 0 0.2 0.9],'NextPlot', 'replacechildren');   
    plot(sol.x(firstel:lastel),Bfield(firstel:lastel), sol.x(firstel:lastel), sol.y(1,firstel:lastel), sol.x(firstel:lastel), A0(firstel:lastel)-1, sol.x(firstel:lastel) , flux(firstel:lastel)./abs(n), '--', sol.x(firstel:lastel),derivA0(firstel:lastel), 'LineWidth', 2)
legend('B(r)','f(r)','A_0(r)','A_\theta(r)/n','E(r)','Location','northeastoutside','FontSize',18);
%xlim([0 8]); % set x axis limit
ylim([-1/alpha-0.1 max(sol.y(1,firstel:lastel))+0.1]); % y axis limit
%set(gca,'YTick',[-1 -0.5 0 0.5 1]);  % set where the ticks should be 
%set(gca,'XTick',(0:2.5:10)); % or this way: start at 0, then every 2.5 until reach 10
mytitleText = ['n=',num2str(n),', \alpha=',num2str(alpha)];
title(mytitleText,'FontSize', 20); % add title
%ylabel('','FontSize', 18); % add y label
xlabel('r','FontSize', 18); % add xlabel
fig3=gcf;
name3=['../figures/dimensionless_6thorder_n','alpha',erase(num2str(alpha),"."),'profiles.png'];
saveas(fig3,name3)
%close all
%----------------------------------------


%% Plot 4 (auxilliary):
%%----------------------------------------
%set(gca, 'ColorOrder', [1 0 0; 0.7 0.1 0.8; 0 1 0; 0.7 0.2 0.1;0.1 0.2 1;0.2 0.2 0.1;0 0.5 0.8; 0 0.2 0.9],'NextPlot', 'replacechildren');   
%    plot(sol.x(firstel:lastel),(sol.y(4,firstel:lastel)+n./(sol.x(firstel:lastel))),sol.x(firstel:lastel),Bfield(firstel:lastel).*sol.x(firstel:lastel).^2./2,sol.x(firstel:lastel) , flux(firstel:lastel), 'LineWidth', 2)
%legend('B(r)','f(r)','A_0(r)','A_\theta(r)/n','E(r)','Location','northeastoutside','FontSize',18);
%%xlim([0 8]); % set x axis limit
%ylim([n-2 max(sol.y(1,firstel:lastel))+0.1]); % y axis limit
%%set(gca,'YTick',[-1 -0.5 0 0.5 1]);  % set where the ticks should be 
%%set(gca,'XTick',(0:2.5:10)); % or this way: start at 0, then every 2.5 until reach 10
%mytitleText = ['n=',num2str(n),', \alpha=',num2str(alpha)];
%title(mytitleText,'FontSize', 20); % add title
%%ylabel('','FontSize', 18); % add y label
%xlabel('r','FontSize', 18); % add xlabel
%fig3=gcf;
%name3=['../figures/dimensionless_6thorder_n','alpha',erase(num2str(alpha),"."),'profiles.png'];
%saveas(fig3,name3)
%%close all
%%----------------------------------------

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
    radius_energy_peak_based=max(sol.x(indexof_maxenergy));
    A0max=A0(firstel);
    A0fint=sum(sol.x.*A0.*dx(1:end));
    totalremainderenergy=sum(remainderenergy.*dx)
    totalremainderBPSeqn=sum(BPSenergy.*dx)
    totalenergy
%----------------------------------------

% Write data:
%----------------------------------------
    data = [n,alpha,totalflux, totalenergy, radius, radius_flux_based, radius_energy_peak_based, A0max, residue];

    fileID = fopen('../data/Dimensionless_6thorder_Data.txt','a');
    nbytes = fprintf(fileID,'%5f %5f %5f %5f %5f %5f %5f %5f %5f\n',data);
    fclose(fileID);

    solution_to_write=[sol.x(firstel:lastel);Bfield(firstel:lastel); sol.y(1,firstel:lastel);  A0(firstel:lastel)-1; flux(firstel:lastel);derivA0(firstel:lastel); energy(firstel:lastel)];
    solutions_filename = ['../data/solutions/dimensionless_6thorder_solution_n',num2str(n),'_alpha',num2str(alpha),'.csv'];
    flush_old_data = fopen(solutions_filename, 'w');
    overwrite = fprintf(flush_old_data, '');
    fclose(flush_old_data);
    solutions_file = fopen(solutions_filename, 'a');
    nbytes2 = fprintf(solutions_file, 'x,B,f,A0,Atheta,A0`, energy\n');
    nbytes3 = fprintf(solutions_file, '%5f,%5f,%5f,%5f,%5f,%5f,%5f\n', solution_to_write);
    fclose(solutions_file);
%----------------------------------------
