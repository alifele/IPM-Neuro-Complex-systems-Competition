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
    color = color[::1]
    tline = np.arange(var0_lim[0], var0_lim[1],dt)
    plt.scatter(var_list[:,0], var_list[:,1], c=color, s=1, cmap='jet')


def plot_nullcline(w):
    x1 = np.linspace(var0_lim[0]-1, var0_lim[1]+1,100)
    x2 = -w[0,0]/w[0,1] * x1
    plt.plot(x1,x2, 'k--')
    x2_2 = -w[1,0]/w[1,1] * x1
    plt.plot(x1,x2_2, 'k--')


def eigplot(w):
    W,V = np.linalg.eig(w)
    print(V)
    V = np.real(V)
    x1 = np.linspace(var0_lim[0], var0_lim[1],100)
    for i in range(len(W)):
        y = V[1,i]/V[0,i] * x1
        plt.plot(x1,y, 'r--', label='eigen')


def arrow_plotter():
    var_dot_list = []
    x_range = np.linspace(var0_lim[0], var0_lim[1], 50)
    y_range = np.linspace(var1_lim[0], var1_lim[1], 50)
    scale=200
    for x_ in x_range:
        for y_ in y_range:
            var = np.array([[x_, y_]]).T
            var_dot = update_var_dot(var, w)
            #var_dot_list.append(var_dot.T[0])

            plt.arrow(x_, y_, var_dot.T[0][0]/scale, var_dot.T[0][1]/scale, head_length=0.7,
            head_width=0.2, color='k',
            alpha = 0.5)






    # ███    ███  █████  ██ ███    ██
    # ████  ████ ██   ██ ██ ████   ██
    # ██ ████ ██ ███████ ██ ██ ██  ██
    # ██  ██  ██ ██   ██ ██ ██  ██ ██
    # ██      ██ ██   ██ ██ ██   ████




## Edit the Weights matrix just below:
#w = np.array([[0.001,2],[-2,1]])
w = np.array([[-1,2],[2,1]])

# set your initial values for the variables
var = np.array([[2,4]]).T

# specidy how ling you want to keep tracking the variables
t_total = 1

# Leave these parameters default
dt = 0.001
var_list = []

for i in range(int(t_total/dt)):
    var_dot = update_var_dot(var, w)
    var = update_var(var, var_dot, dt)
    var_list.append(var.T[0])


var_list = np.array(var_list)
shift = 10
#var0_lim = (np.min(var_list[:,0])-shift, np.max(var_list[:,0])+shift)
#var1_lim = (np.min(var_list[:,1])-shift, np.max(var_list[:,1])+shift)

lims0 = [-10,10]
lims1 = [-10,10]
var0_lim = (lims0[0]-shift, lims0[1]+shift)
var1_lim = (lims1[0]-shift, lims1[1]+shift)


#plotter(var_list)
plot_nullcline(w)
eigplot(w)
arrow_plotter()


from matplotlib.lines import Line2D


plt.legend( ['Nullcline1','Nullcline2', 'Eigenvector1','Eigenvector1'])

plt.xlim([var0_lim[0], var0_lim[1]])
plt.ylim([var1_lim[0], var1_lim[1]])
plt.show()
plt.axis('equal')
