import numpy as np
from helpers import make_data
from helpers import display_world
from utils import initialize_constraints, get_poses_landmarks, print_all
import matplotlib.pyplot as plt
from slam import slam


#Set the following parameters:
    # world parameters
num_landmarks      = 15       # number of landmarks
N                  = 20       # time steps
world_size         = 15.0    # size of world (square)

    # robot parameters
measurement_range  = 12.0     # range at which we can sense landmarks
motion_noise       = 2.0      # noise in robot motion
measurement_noise  = 2.0      # noise in the measurements
distance           = 3.0     # distance by which robot (intends to) move each iteratation 





# make_data instantiates a robot, AND generates random landmarks for a given world size and number of landmarks
print("The REAL values are:")
data = make_data(N, num_landmarks, world_size, measurement_range, motion_noise, measurement_noise, distance)
mu = slam(data, N, num_landmarks, world_size, motion_noise, measurement_noise)
print("___________________________________________________")
# print out the resulting landmarks and poses
if(mu is not None):
    poses, landmarks = get_poses_landmarks(mu, N, num_landmarks)
    print("\n\nThe PREDICTED values are:")
    print_all(poses, landmarks)



#Displaying
plt.rcParams["figure.figsize"] = (20,20)
if 'poses' in locals():
    print('Last pose: ', poses[-1])
    display_world(int(world_size), poses[-1], landmarks)