# ***GENERAL INFO: here are physics tasks***

---

## ***DESCRIPTION FOR absolute_black_body.py***
+ This script demonstrates numerical modeling of Planck's radiation laws, verification of Wien's displacement law and the Stefan-Boltzmann law.

### ***The task consists of three parts:***
1. *Plots the spectral luminosity*
   + for given temperatures from 500 to 2500 K, the spectral luminosity of a blackbody as a function of frequency is calculated and visualized.
2. *Testing of Wien's displacement law*
   + the maximum frequency of emission for each temperature is calculated, and it is verified that the ratio of temperature to frequency remains approximately constant.
3. *Testing of the Stefan-Boltzmann law*
   + the total radiant energy (integral under the plot) for each temperature is calculated;
   + the dependence of the total energy of radiation on temperature to degree 4 is compared.
   
## ***REQUIREMENTS***
+ **numpy**
+ **matplotlib**

---

## ***DESCRIPTION FOR bownian.py***
+ This script demonstrates modeling the Brownian motion of a particle on a plane using random directions and step lengths.

### ***The task consists of four parts:***
1. *Initialization*
   + the particle starts moving from the starting point (0, 0).
2. *Parameters*
    + *num_steps* specifies the number of steps of Brownian motion (default 100).
3. *Motion Simulation*
    + at each step, a random angle and step length are generated;
    + the coordinates of the particle are updated based on these parameters.
4. *Visualization*
    + the motion trajectory is displayed on a plot.

## ***REQUIREMENTS***
+ **numpy**
+ **matplotlib**

---

## ***DESCRIPTION FOR damped_oscillations.py***
+ This script simulates damped oscillations of a mechanical system (spring-mass-damper) based on the numerical solution of the equations of motion using the Euler method.
+ Euler's method is used to numerically solve the system of differential equations.

## ***REQUIREMENTS***
+ **numpy**
+ **matplotlib**

---

## ***DESCRIPTION FOR fermat's_principle_of_reflection.py***
+ This script models a test of Fermat's principle using points in a two-dimensional plane and their reflection with respect to a line.
+ The user enters the coordinates of three points through the console (A, B, C):
   + **point A**: start point;
   + **point B**: end point;
   + **point C**: intermediate point (line for reflection).

### ***The task consists of four parts:***
1. *Calculating the distance between points*:
   + the formula fot the distance between two points in a plane is used.
2. *Calculating the total path*:
   + the distances before and after the intermediate point are summed up.
3. *Finding a reflected point*:
   + finds a reflected point for one of the points relative to the line given by the other point.
4. *Path Comparison*:
   + checks whether Fermat's principle is satisfied by comparing the lengths of two alternative paths.

---



