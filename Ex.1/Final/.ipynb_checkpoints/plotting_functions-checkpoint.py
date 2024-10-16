import numpy as np
import matplotlib.pyplot as plt

def plot_scatter(cartesian_sphere):
    fig, axs = plt.subplots(ncols=3, figsize=(15, 5))
    axs[0].scatter(cartesian_sphere[0], cartesian_sphere[1], color='r', label='along z-axis', marker=",",s=1)
    axs[0].set_title('XY')
    axs[0].set_xlabel('X')
    axs[0].set_ylabel('Y')
    axs[0].legend(loc='upper right')

    axs[1].scatter(cartesian_sphere[0], cartesian_sphere[2], color='g', label='along y-axis', marker=",",s=1)
    axs[1].set_title('XZ')
    axs[1].set_xlabel('X')
    axs[1].set_ylabel('Z')
    axs[1].legend(loc='upper right')

    axs[2].scatter(cartesian_sphere[1], cartesian_sphere[2], color='b', label='along x-axis', marker=",",s=1)
    axs[2].set_title('YZ')
    axs[2].set_xlabel('Y')
    axs[2].set_ylabel('Z')
    axs[2].legend(loc='upper right')

    plt.tight_layout()
    plt.show()
    
def plot_histogram(cartesian_sphere):
    
    fig, axh = plt.subplots(ncols=3, figsize=(15, 5))
    axh[0].hist(cartesian_sphere[0], bins=100, color='r', alpha=0.7)
    axh[0].set_title('1D histogram of X distribution')
    axh[0].set_xlabel('Position X')
    axh[0].set_ylabel('Frequency')

    axh[1].hist(cartesian_sphere[1], bins=100, color='g', alpha=0.7)
    axh[1].set_title('1D histogram of Y distribution')
    axh[1].set_xlabel('Position Y')
    axh[1].set_ylabel('Frequency')

    axh[2].hist(cartesian_sphere[2], bins=100, color='b', alpha=0.7)
    axh[2].set_title('1D histogram of Z distribution')
    axh[2].set_xlabel('Position Z')
    axh[2].set_ylabel('Frequency')
    
    plt.tight_layout()
    plt.show()