close all;

N = 10000;

CD = 0.06293;   
rho_air = 1.225;

masse_helico = normrnd(0.001406845, 0.0001, 1, N); 
masse_tromb = normrnd(0.00036, 0.0001, 1, N); 
Hauteur = normrnd(5, 0.0009, 1, N);
Rw = normrnd(0.045, 2.5e-7, 1, N);
Rr = normrnd(0.14, 2.5e-7, 1, N);
Tw = normrnd(0.02, 2.5e-7, 1, N);

t = Hauteur.*Rr.*sqrt((pi*rho_air*CD)./(2*(masse_helico + 2*masse_tromb)));

variance_temps = var(t)
moyenne_temps = mean(t)
histogram(t);


pf = normcdf(5.30, moyenne_temps, sqrt(variance_temps)) 