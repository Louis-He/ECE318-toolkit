# ECE318-toolkit

Toolkit helpful to the course ECE318 fundamental optics.

## Usage
ECE318 toolkit now support the following commands:
```
fr         Find fresnal coef             Required Arguments: ['ni', 'nt', 'theta_i']
q/quit     Quit the toolkit              Required Arguments: ['NONE']
help       Show this help message        Required Arguments: ['NONE']
```

## Command Usage
### fr (Find fresnal coef)
fr supports both radius and degree input. It can also detect Total Internal Reflection automatically.
```
ECE318_toolkit >> fr 1 1.5 30deg
r_te:  -0.2404 		t_te:  0.7596
r_tm:  -0.1589 		t_tm:  0.7726

ECE318_toolkit >> fr 1 1.5 0.5235987
r_te:  -0.2404 		t_te:  0.7596
r_tm:  -0.1589 		t_tm:  0.7726

ECE318_toolkit >> fr 1.5 1 60deg
Total Internal Reflection
phi_te:  -1.671 = -95.741 deg		phi_tm:  0.7645 = 43.803 deg
```
