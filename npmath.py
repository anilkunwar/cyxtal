#!/usr/bin/env python
# coding=utf-8

# Functions commonly used but somehow still missing in standard Numpy
# packages.


import numpy as np
from numpy.linalg import norm


def normalize(vec, axis=None):
    """
    return a normalized vector/matrix
    axis=None : normalize entire vector/matrix
    axis=0    : normalize by column
    axis=1    : normalize by row
    """
    vec = np.array(vec, dtype=np.float64)
    if axis is None:
        return vec/norm(vec)
    else:
        return np.divide(vec,
                         np.tile(norm(vec, axis=axis),
                                 vec.shape[axis],
                                 ).reshape(vec.shape,
                                           order='F' if axis == 1 else 'C',
                                           )
                         )


def random_three_vector():
    """
    Generates a random 3D unit vector (direction) with a uniform spherical
    distribution Algo from
    http://stackoverflow.com/questions/5408276/python-uniform-spherical-distribution
    """
    phi = np.random.uniform(0, np.pi*2)
    costheta = np.random.uniform(-1, 1)

    theta = np.arccos(costheta)
    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)
    return np.array([x, y, z])


if __name__ == "__main__":
    # demo for func normalize()
    vector = np.random.random(3)
    print(vector)
    print(normalize(vector))

    # demo for random_three_vector
    randv = random_three_vector()
