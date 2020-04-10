import numpy as np
import matplotlib.pyplot as plt



def update_var(var, var_dot, dt=0.001):
    var = var +  var_dot*dt
    return var


def update_var_dot(var):
    var = var.reshape(-1,1)
    x1 = var[0,0]
    x2 = var[1,0]
    var_dot[0,0] = 1 - x1*x2
    var_dot[1,0] = x1 - x2**3

    return var_dot


def plotter(var_list):
    color = np.array([i for i in range(len(var_list[:,1]))])
    color = color[::1]
    plt.scatter(var_list[:,0], var_list[:,1], c=color, s=1, cmap='jet')



def arrow_plotter():
    var_dot_list = []
    x_range = np.linspace(var0_lim[0], var0_lim[1], 50)
    y_range = np.linspace(var1_lim[0], var1_lim[1], 50)
    scale= 300
    for x_ in x_range:
        for y_ in y_range:
            var = np.array([[x_, y_]]).T
            var_dot = update_var_dot(var)
            #var_dot_list.append(var_dot.T[0])

            plt.arrow(x_, y_, var_dot.T[0][0]/scale, var_dot.T[0][1]/scale,head_length=0.1,  head_width=0.05, color='k',
            alpha = 0.5)






#set your initial values for the variables
var = np.array([[4,-2]]).T
var_dot = np.array([[0,0]], dtype=float).T
# specidy how ling you want to keep tracking the variables
t_total = 3
# Leave these parameters default
dt = 0.001
var_list = []


for i in range(int(t_total/dt)):
    var_dot = update_var_dot(var)
    var = update_var(var, var_dot, dt)
    var_list.append(var.T[0])


var_list = np.array(var_list)
var0_lim = (np.min(var_list[:,0])-4, np.max(var_list[:,0])+4)
var1_lim = (np.min(var_list[:,1])-4, np.max(var_list[:,1])+4)

plotter(var_list)
arrow_plotter()
plt.xlim([var0_lim[0], var0_lim[1]])
plt.ylim([var1_lim[0], var1_lim[1]])
plt.show()
#plt.axis('equal')
