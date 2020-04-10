import numpy as np
import matplotlib.pyplot as plt

def update_var(var, var_dot, dt=0.001):
    var = var +  var_dot*dt
    return var


def update_var_dot(var, weights):
    var = var.reshape(-1,1)
    var_dot = weights@var
    return var_dot

def plotter(var_list):
    tline = np.arange(0,t_total,dt)
    var_list = np.array(var_list)

    fig = plt.figure(figsize=(6,12))
    ax = fig.add_subplot(4,2,(1,4))
    ax.plot(var_list[:,0], var_list[:,1] )
    ax.set_xlabel("Var1")
    ax.set_ylabel("Var2")
    ax = fig.add_subplot(4,2,(5,6))
    ax.plot(tline, var_list[:,0])
    ax.set_ylabel("Var1")
    ax.set_xlabel("time")
    ax = fig.add_subplot(4,2,(7,8))
    ax.plot(tline, var_list[:,1])
    ax.set_ylabel('Var2')
    ax.set_xlabel('time')
    plt.show()



## Edit the Weights matrix just below:
w = np.array([[1,2],[3,-5]])

# set your initial values for the variables
var = np.array([[1,4]]).T

# specidy how ling you want to keep tracking the variables
t_total = 1

# Leave these parameters default
dt = 0.001
var_list = []

for i in range(int(t_total/dt)):
    var_dot = update_var_dot(var, w)
    var = update_var(var, var_dot, dt)
    var_list.append(var.T[0])

plotter(var_list)
