import numpy as np
from math import *

def initialize_constraints(N, num_landmarks, world_size):
    ''' This function takes in a number of time steps N, number of landmarks, and a world_size,
        and returns initialized constraint matrices, omega and xi.'''

    omega_size = 2*(N + num_landmarks)
    omega = np.zeros((omega_size,omega_size))
    omega[0][0] = 1
    omega[1][1] = 1
    
    xi = np.zeros((omega_size,1))
    xi[0][0] = world_size / 2
    xi[1][0] = world_size / 2
                  
    
    return omega, xi
    
def get_poses_landmarks(mu, N, num_landmarks):
    # create a list of poses
    poses = []
    for i in range(N):
        poses.append((mu[2*i].item(), mu[2*i+1].item()))

    # create a list of landmarks
    landmarks = []
    for i in range(num_landmarks):
        landmarks.append((mu[2*(N+i)].item(), mu[2*(N+i)+1].item()))

    # return completed lists
    return poses, landmarks

def print_all(poses, landmarks):
    print('\n')
    print('Estimated Poses:')
    for i in range(len(poses)):
        print('['+', '.join('%.3f'%p for p in poses[i])+']')
    print('\n')
    print('Estimated Landmarks:')
    for i in range(len(landmarks)):
        print('['+', '.join('%.3f'%l for l in landmarks[i])+']')
