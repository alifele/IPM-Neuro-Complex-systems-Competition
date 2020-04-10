import numpy as np
import matplotlib.pyplot as plt



def update_var(var, var_dot, dt=0.001):
    var = var +  var_dot*dt
    return var


def update_var_dot(var):
    var = var.reshape(-1,1)
    var_dot[0,0] = (2+var[0,0])*(var[1,0] - var[0,0])
    var_dot[1,0] = (4-var[0,0])*(var[1,0] + var[0,0])
    return var_dot


def plotter(var_list):
    color = np.array([i for i in range(len(var_list[:,1]))])
    color = color[::1]
    tline = np.arange(var_lim[0], var_lim[1],dt)
    plt.scatter(var_list[:,0], var_list[:,1], c=color, s=1, cmap='jet')





#set your initial values for the variables
var = np.array([[1,4]]).T
var_dot = np.array([[0,0]]).T
# specidy how ling you want to keep tracking the variables
t_total = 3

# Leave these parameters default
dt = 0.001
var_list = []


for i in range(int(t_total/dt)):
    var_dot = update_var_dot(var)
    var = update_var(var, var_dot, dt)
    var_list.append(var[:,0])

var_list = np.array(var_list)
var_lim = (np.min(var_list[:,0]), np.max(var_list[:,1]))
plotter(var_list)
#plot_nullcline(w)
plt.show()
plt.axis('equal')
