import numpy as np
import matplotlib.pyplot as plt

def plot_scatter(cartesian_sphere):
    fig, axs = plt.subplots(ncols=3, figsize=(15, 5))
    axs[0].scatter(cartesian_sphere[0], cartesian_sphere[1], color='r', label='Plot 1', marker=",",s=1)
    axs[0].set_title('XY')
    axs[0].set_xlabel('X')
    axs[0].set_ylabel('Y')
    axs[0].legend()

    axs[1].scatter(cartesian_sphere[0], cartesian_sphere[2], color='g', label='Plot 2', marker=",",s=1)
    axs[1].set_title('XZ')
    axs[1].set_xlabel('X')
    axs[1].set_ylabel('Z')
    axs[1].legend()

    axs[2].scatter(cartesian_sphere[1], cartesian_sphere[2], color='b', label='Plot 3', marker=",",s=1)
    axs[2].set_title('YZ')
    axs[2].set_xlabel('Y')
    axs[2].set_ylabel('Z')
    axs[2].legend()

    plt.tight_layout()
    plt.show()
    
def plot_histogram(cartesian_sphere):
    
    fig, axh = plt.subplots(ncols=3, figsize=(12, 3))
    axh[0].hist(cartesian_sphere[0], bins=100, color='r', alpha=0.7)
    axh[0].set_title('X')
    axh[0].set_xlabel('Position')
    axh[0].set_ylabel('Frequency')

    axh[1].hist(cartesian_sphere[1], bins=100, color='g', alpha=0.7)
    axh[1].set_title('Y')
    axh[1].set_xlabel('Position')
    axh[1].set_ylabel('Frequency')

    axh[2].hist(cartesian_sphere[2], bins=100, color='b', alpha=0.7)
    axh[2].set_title('Z')
    axh[2].set_xlabel('Position')
    axh[2].set_ylabel('Frequency')
    
    plt.tight_layout()
    plt.show()