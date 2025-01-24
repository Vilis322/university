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
+ **Python 3.7.x**
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
+ **Python 3.7.x**
+ **numpy**
+ **matplotlib**


---


## ***DESCRIPTION FOR damped_oscillations.py***
+ This script simulates damped oscillations of a mechanical system (spring-mass-damper) based on the numerical solution of the equations of motion using the Euler method.
+ Euler's method is used to numerically solve the system of differential equations.

## ***REQUIREMENTS***
+ **Python 3.7.x**
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


## ***DESCRIPTION FOR forced_oscillations_and_resonance.py***
+ This script models and builds the resonance curve of a system with a harmonic forcing force. The system is a damped oscillator (mass on a spring) with given parameters of mass, stiffness, drag coefficient and amplitude of the forcing force.

### ***The task consists of five parts:***
1. *System parameters*:
   + mass (*m*), spring stiffness (*k*), coefficient of resistance (*r*), amplitude of the forcing force (*Fm*);
   + initial conditions for the position (*x0*) and velocity (*v0*);
   + the time step (*dt*) and simulation duration (*t_max*).
2. *frequency analysis*:
   + varying the frequencies of the forcing force from 0.1 to 5.0 rad/s with 100 values;
   + for each frequency, the motion of the system is modeled using the Euler method.
3. *Numerical solution of the equation of motion*:
   + the equation takes into account the effects of forcing force, spring elasticity and damping;
   + velocity (*v*) and position (*x*) are updated at each time step.
4. *Amplitude*:
   + for each frequency, the maximum value of the displacement modulus (*|x|*) as the amplitude.
5. *Plotting the resonance curve*:
   + the dependence of amplitude on frequency (*A(ω)*) is visualized by means of a plot. 

## ***REQUIREMENTS***
+ **Python 3.7.x**
+ **numpy**
+ **matplotlib**


---


## ***DESCRIPTION FOR light_path_time.py***
+ This script calculates the optimal path of light through two environments using Fermat's principle, and finds the minimum travel time of the light path.

### ***The task consists of five parts:***
1. *The speed of light in the environment*:
   + the function *light_speed_in_the_environment* calculates the speed of light in an environment with a given refractive index *n*, where *c* is the speed of light in vacuum.
2. *Time function*:
   + the function *time_function* calculates the total path time of the light, where *x* is the point of the boundary of the environment through which light passes, *v1* and *v2* are speeds of light in the first and second environments, respectively.
3. *Finding the optimal x*:
   + the function *find_optimal_x* finds *x* that minimizes *T(x)*, using the minimize scalar method from the *scipy*;
   + the method is bounded by the interval from 0 to *l*.
4. *Parameters initialization*:
   + distances given *a*, *b* and *l*, the refractive coefficients for air and water;
   + the velocities of light *v1* and *v2* are calculated;
   + optimal point *x* is found through the *find_optimal_x* function;
   + the final minimum time is calculated via the time function.
5. *Result*:
   + the script outputs the optimal time for light to path through both environments, converted to seconds.

## ***REQUIREMENTS***
+ **scipy**


---


## ***DESCRIPTION FOR lissajous_figure.py***
+ This script plots a Lissajous figure - a graphical representation of two harmonic oscillations occurring along mutually perpendicular axes (*X* and *Y*).

### ***The task consists of three parts:***
1. *Time initialization*:
   + a time array is created as a sequence of uniformly distributed values for the interval from 0 to *t_max*.
2. *Calculation of X and Y coordinates*:
   + trigonometric functions (*cos* and *sin*) which depend on time, amplitudes (*A1*, *A2*) and frequency ratio (*n*) are used for calculations.
3. *Plotting*:
   + a plot is created where *X* and *Y* values are combined to plot the Lissajous figure;
   + grid, axis signatures and uniform scaling also added.

## ***REQUIREMENTS***
+ **Python 3.7.x**
+ **matplotlib**


---


## ***DESCRIPTION FOR planetary_trajectory.py***
+ This script simulates the motion of a planet around a star in the field of central gravitational force.
+ The calculations are performed by Euler method and the results are visualized in the form of the planet orbit on the plot.

### ***The task consists of three parts:***
1. *Initialization of initial parameters*:
   + known physical parameters are used: gravitational constant, mass of the star and planet, initial coordinates and velocities.
2. *Solving the equations of motion using the Euler's method*:
   + the distance to the center of mass is calculated for each step;
   + accelerations in the *X* and *Y* axes are determined based of the law of universal gravitation;
   + coordinates and velocities are updated with step time.
3. *Trajectory plotting*:
   + using the coordinates of the planet, the trajectory of the planet is plotted.
   + the center (star) is shown on the plot as a yellow dot.

## ***REQUIREMENTS***
+ **Python 3.7.x**
+ **matplotlib**
+ **numpy**


---


## ***DESCRIPTION FOR random_walk.py***
+ This script models a one-dimensional random walk of a particle and calculates the average square of its displacement *S²* as a function of the number of steps *N*.

### ***The task consists of three parts:***
1. *Random Step Generation*:
   + for each value of N from a given range, a random wandering of the particle is modeled;
   + the steps take the values -1 or +1 with equal probability.
2. *Calculating the squares of the offsets*:
   + for each wander, the final displacement is calculated *xN* and its square (*xN*)²;
   + average value *S²* over all tests for a given *N* is maintained.
3. *Plotting*:
   + the plot shows the dependence of the average square of displacement on the number of steps *N*.

## ***REQUIREMENTS***
+ **Python 3.7.x**
+ **matplotlib**
+ **numpy**


---
