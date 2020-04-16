from utils import initialize_constraints
import numpy as np

def slam(data, N, num_landmarks, world_size, motion_noise, measurement_noise):
    
    omega, xi = initialize_constraints(N, num_landmarks, world_size)
    measurement = []
    motion = []
    omega_plus = np.zeros(omega.shape)
    xi_plus = np.zeros(xi.shape)
    
    
    
    for i in range(N-1):
        measurement.append(data[i][0])
        motion.append(data[i][1])
#     print(f"Measurement is {measurement}")
#     print(f"Motion is {motion}")

        for measure in measurement[i]: #measure step
            index = measure[0] #index
            x_land = measure[1] #x coord for landmark
            y_land = measure[2] #y coord for landmark
            
            #pairing x information with y information is usless as they are 0. treat it as one separate matrix
            
            #Omega
            #x pairings
            omega_plus[2*i, 2*i] += 1 / measurement_noise #x - x
            omega_plus[2*i, 2*N + 2*index] -= 1 / measurement_noise #x - x_land
            omega_plus[2*N + 2*index, 2*i] -= 1 / measurement_noise #x_land - x
            omega_plus[2*N + 2*index, 2*N + 2*index] += 1 / measurement_noise #x_land - x_land
            #x pairings have 1 on main diaglonal, -1 on secondary diagonal. treated it as one matrix for x
            
            #y pairings - shifted by +1 from x
            omega_plus[2*i + 1, 2*i + 1] += 1 / measurement_noise #y - y
            omega_plus[2*i + 1, 2*N + 2*index + 1] -= 1 / measurement_noise #y - y_land
            omega_plus[2*N + 2*index + 1, 2*i + 1] -= 1 / measurement_noise #y_land - y
            omega_plus[2*N + 2*index + 1, 2*N + 2*index + 1] += 1 / measurement_noise #y_land - y_land
            #y pairings have the same as x, 1 main diagonal; -1 secondary diagonal.
            
            #Xi
            xi_plus[2*i, 0] -= x_land / measurement_noise #x
            xi_plus[2*N + 2*index, 0] += x_land / measurement_noise #x_land
            xi_plus[2*i + 1, 0] -= y_land / measurement_noise #y
            xi_plus[2*N + 2*index + 1, 0] += y_land / measurement_noise
            
            omega = omega + omega_plus
            xi = xi + xi_plus
            
        
        #motion step
        omega_plus = np.copy(omega)
        xi_plus = np.copy(xi)
        dx = motion[i][0]
        dy = motion[i][1]
        
        #Omega
        #x pairings with x_new=(x+1)*2
        omega_plus[2*i, 2*i] += 1 / motion_noise #x - x
        omega_plus[2*i, 2*(i+1)] -= 1 / motion_noise #x - new_x
        omega_plus[2*(i+1), 2*i] -= 1 / motion_noise #new_x - x
        omega_plus[2*(i+1), 2*(i+1)] += 1 / motion_noise #new_x - new_x
        
        #y pairings with y_new=(y+1)*2
        omega_plus[2*i + 1, 2*i + 1] += 1 / motion_noise #y - y
        omega_plus[2*i + 1, 2*(i+1) + 1] -= 1 / motion_noise #y - new_y
        omega_plus[2*(i+1) + 1, 2*i + 1] -= 1 / motion_noise #new_y - y
        omega_plus[2*(i+1) + 1, 2*(i+1) + 1] += 1 / motion_noise #new_y - new_y
        
        #Xi
        xi_plus[2*i, 0] -= dx / motion_noise #x
        xi_plus[2*(i+1), 0] += dx / motion_noise #new_X
        xi_plus[2*i + 1, 0] -= dy / motion_noise #y
        xi_plus[2*(i+1) + 1, 0] += dy / motion_noise #new_y
        
        omega = omega + omega_plus
        xi = xi + xi_plus

    omega_inv = np.linalg.inv(np.matrix(omega))
    
    mu = omega_inv*xi
    
    return mu # return `mu`
