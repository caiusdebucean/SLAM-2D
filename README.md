# SLAM-2D
A robust method for Landmark Tracking and self Localization in 2D space, using probability, motion models and linear algebra. This is the third and _final_ project of the [*Udacity's Computer Vision Nanodegree*](https://www.udacity.com/course/computer-vision-nanodegree--nd891).

### Project Overview

This is an implementation of **_SLAM_** _(Simultaneous Localization and Mapping)_ for a 2-D world. The premise is that your _agent (or robot)_ is trying to create a map of the environment from only sensor and motion data gathered over time. _SLAM_ gives us a way to track the location of the _robot_ in the world in real-time, and also identify the locations of _landmarks (such as trees, buildings or other world features)_.

_This is a representation of the 2D world. The landmarks are shown with a purple "X" and the robot's location is mapped with a red circle._

![Representation](https://i.imgur.com/eFYfWy8.png)


To better understand how this works, unzip the `notebooks.zip` archive found in the _Notebooks folder_ and go through all the 3 jupyter notebooks located there.

### Requirements
Create an environment with _python 3.6_, activate it and run the following command:

> pip install -r requirements.txt

### Configure and Run

**Configuration** is done by changing the parameters of the system. They are found in the `run.py` file, along with what they represent. *Modify to your will and test out different configurations.*
The landmark locations and robot movements will be *generated* by the program, based on the parameters given. 
To **Run** the system, go into the terminal:

> python run.py

### How it works

To implement *Graph SLAM*, a matrix and a vector (**omega** and **xi**, respectively) are introduced. The matrix is square and labeled with all the robot poses *(i,x,y)* and all the landmarks *(i, Lx, Ly)*. 
Every time you make an observation, for example, as you move between two poses by some distance *dx* and *dy* and can relate those two positions, you can represent this as a numerical relationship in these matrices.
Below you can see a matrix representation of **omega** and a vector representation of **xi**.

![Matrix multiplication](https://i.imgur.com/3QeDJav.png)

To **"solve"** for all these poses and landmark positions, I use linear algebra; all the positional values are in the vector ***mu*** which can be calculated as a product of the ***inverse* *of* *omega*** times ***xi***.

![Formula representation](https://i.imgur.com/6TD3RJ1.png)

_To better understand how the omega and xi matrices are updated while taking into account noise, study the notebooks provided._

### Experiment results

Below is an already _calculated_ state of the **omega**,**xi** and **mu** matrices, with a *world size* of *10*, *number of landmarks* of *3* and only *3 time steps*:

![Calculated results examples](https://i.imgur.com/hvPBIFb.png)

The first **6** _(or 3 x 2)_ values represent the **3** pairs of coordinates **(x,y)** for the **Estimated poses** at each one of the 3 time steps. The _last_ one of these 3 pairs represents the final pose of the robot. The remaining **6** values are the other **3** pairs of **(x,y)** coordinates for the **3 Estimated Landmarks**.

The _Real_ values are:

> Landmarks coordinates:  [ [1, 8], [2, 8], [0, 1] ]
Robot final pose: [ x=4.62431 y=8.99146 ]

Compared to the estimated final pose of _[x=4.7 y=9.1]_ we can conclude that due to the measurement noise and motion noise the results are expected to be _a bit_ uncertain. This means that increasing the number of measurements and decreasing noise is beneficial. 

Debucean Caius-Ioan @Udacity 
