import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused imports

def update_var(var, var_dot, dt=0.001):
    var = var +  var_dot*dt
    return var


def update_var_dot(var, weights):
    var = var.reshape(-1,1)
    var_dot = weights@var
    return var_dot

def plotter(var_list):
    color = np.array([i for i in range(len(var_list[:,1]))])
    color = color[::-1]
    tline = np.arange(var_lim[0], var_lim[1],dt)
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1, projection='3d')
    ax.scatter(var_list[:,0], var_list[:,1], np.array([0 for i in range(len(var_list[:,1]))]), c=color, s=1, cmap='jet')


def plot_nullcline(w):
    x1 = np.linspace(var_lim[0]-1, var_lim[1]+1,100)
    x2 = -w[0,0]/w[0,1] * x1
    plt.plot(x1,x2, 'k--')
    x2 = -w[1,0]/w[1,1] * x1
    plt.plot(x1,x2, 'k--')







    # ███    ███  █████  ██ ███    ██
    # ████  ████ ██   ██ ██ ████   ██
    # ██ ████ ██ ███████ ██ ██ ██  ██
    # ██  ██  ██ ██   ██ ██ ██  ██ ██
    # ██      ██ ██   ██ ██ ██   ████




## Edit the Weights matrix just below:
#w = np.array([[0.001,2],[-2,1]])
w = np.array([[0,5],[-5,-2]])

# set your initial values for the variables
var = np.array([[1,4]]).T

# specidy how ling you want to keep tracking the variables
t_total = 10

# Leave these parameters default
dt = 0.001
var_list = []

for i in range(int(t_total/dt)):
    var_dot = update_var_dot(var, w)
    var = update_var(var, var_dot, dt)
    var_list.append(var.T[0])

var_list = np.array(var_list)
var_lim = (np.min(var_list[:,0]), np.max(var_list[:,1]))
plotter(var_list)
plot_nullcline(w)
plt.show()
plt.axis('equal')
