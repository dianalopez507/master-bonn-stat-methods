import numpy as np

def sample_sphere(n):
    cos_theta = np.random.uniform(-1,1,n)
    theta = np.arccos(cos_theta)
    phi = np.random.uniform(0,2*np.pi,n)

    return theta, phi

def get_cartesian_coords(phi, theta, r = 1):
    x= r*np.sin(theta)*np.cos(phi)
    y= r*np.sin(theta)*np.sin(phi)
    z = r*np.cos(theta)
    return x, y, z
