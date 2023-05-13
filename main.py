from plotter import plot_3d_function


# Define any two-variable function
def my_function(x, y):
    return x**2 + y**2


# Call plotter
plot_3d_function(
    function=my_function,
    center=(0, 0),
    radius=100,
    num_gridlines=30
)
