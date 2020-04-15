# ECE318-toolkit

Toolkit helpful to the course ECE318 fundamental optics.

## Usage
ECE318 toolkit now support the following commands:
```
fr         Find fresnal coef and return refractive angle      Required Arguments: ['ni', 'nt', 'theta_i']
r2fin      Find finesse with reflectivity                     Required Arguments: ['R']
fin2r      Find reflectivity with finesse                     Required Arguments: ['Finesse']
prop       Convert between different light properties         Required Arguments: ['type', 'value'] 
q/quit     Quit the toolkit                                   Required Arguments: ['NONE']
help       Show this help message                             Required Arguments: ['NONE']
```

## Command Usage
### fr (Find fresnel coef)
fr supports both radius and degree input. It can also detect Total Internal Reflection automatically.\
added partial caculation for field and intensity penetration depth
```
ECE318_toolkit >> fr 1 1.5 30deg
theta_t:  0.3398 = 19.471 deg
r_te:  -0.2404 		t_te:  0.7596
r_tm:  -0.1589 		t_tm:  0.7726
ECE318_toolkit >> fr 1 1.5 0.5235987
theta_t:  0.3398 = 19.471 deg
r_te:  -0.2404 		t_te:  0.7596
r_tm:  -0.1589 		t_tm:  0.7726

ECE318_toolkit >> fr 1.5 1 60deg
Total Internal Reflection
phi_te:  -1.671 = -95.741 deg		phi_tm:  0.7645 = 43.803 deg
(for pen_dep calculation) beta:  0.8292 *(w/c)  =  5.2097 /freq
```
### fin2r/r2fin (Find finesse coef from reflectivity, and vice versa)
fin2r supports both percentage expression and float expression.
```
ECE318_toolkit >> fin2r 76.95
Reflectivity: 0.959998
ECE318_toolkit >> r2fin 0.96
Coef of Finesse: 2400.0 Finesse:  76.953
ECE318_toolkit >> r2fin 96%
Coef of Finesse: 2400.0 Finesse:  76.953
```
### prop (Convert between light's spacial and temporal properties)
index of refraction initially setup to be 1.\
prop support input under standard SI units (suggest using scientific notation for nm, THz, ps etc).
```
ECE318_toolkit >> prop k 4.19E6
index of refraction =  1
k =  4.19e+06 rad/m,  f =  6.669e+05 m-1,  lam =  1.5e-06 m; 
w =  1.256e+15 rad/s,  V =  1.999e+14 Hz,  T =  5.002e-15 s; 
ECE318_toolkit >> prop n 1.2
set up new index of refraction =  1.2
ECE318_toolkit >> prop lam 1500E-9
index of refraction =  1.2
k =  4.189e+06 rad/m,  f =  6.667e+05 m-1,  lam =  1.5e-06 m; 
w =  1.046e+15 rad/s,  V =  1.666e+14 Hz,  T =  6.004e-15 s; 
```

