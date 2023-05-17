import matplotlib.pyplot as plt
import numpy as np
import math


def plot_3d_function(function, center, radius, num_gridlines):
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    vectorized_fn = np.vectorize(function)

    x_center, y_center = center
    x_interval = np.linspace(x_center-radius, x_center+radius, num_gridlines)
    y_interval = np.linspace(y_center-radius, y_center+radius, num_gridlines)

    x_arr, y_arr = np.meshgrid(x_interval, y_interval)

    ax.plot_surface(x_arr, y_arr, vectorized_fn(x_arr, y_arr))

    plt.show()
