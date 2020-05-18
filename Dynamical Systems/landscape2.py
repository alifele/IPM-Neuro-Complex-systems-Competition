import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d



def var_dot_calculate(x_var, y_var):
    '''
    Note that the x_var and y_var must be in the shape of m*m which is created
    be the outer (it is also used for the surface plots)
    '''

    x_var_dot = x_var + y_var - x_var*(x_var**2 + y_var**2)
    y_var_dot = -(x_var-y_var) - y_var*(x_var**2 + y_var**2)

    return x_var_dot, y_var_dot



def var_creator(m,n, N):
    x_var = np.outer(np.linspace(-m, m, N), 1*np.ones(N))
    y_var = np.outer(np.linspace(-n, n, N), 1*np.ones(N)).T
    return x_var, y_var


def arrow_plotter(x_var, y_var, x_var_dot, y_var_dot):
    scale_x = np.max(x_var_dot) * 10
    scale_y = np.max(y_var_dot) * 10
    scaler = 1/(10*(x_var_dot**2 + y_var_dot**2)**0.5)
    for i, x_ in enumerate(x_var[:,0]):
        for j, y_ in enumerate(y_var[0,:]):
            plt.arrow(x_, y_, x_var_dot[i,j]*scaler[i,j], y_var_dot[i,j]*scaler[i,j], head_width=0.13, color='k',
            alpha = 0.5, head_length=0.15)



def arrow_norm_surface(x_var, y_var, x_var_dot, y_var_dor):
    z = (x_var_dot**2 + y_var_dot**2)**0.5
    ax = plt.axes(projection='3d')
    ax.plot_surface(x_var, y_var, z,cmap='viridis', edgecolor='none')
    ax.set_title('Surface plot')

def diff(x):
    L = len(x)
    D = np.zeros(L-1)
    for i in range(L-1):
        D[i] = (x[i+1] - x[i])*3
    return D

def integral(x,c):
    L = len(x)
    I = np.zeros(L)
    I[0] = c
    for i in range(L-1):
        I[i+1] = I[i] + x[i]

    return I




def potential_surface_plotter(x_var, y_var, x_var_dot, y_var_dot):
    h = 0
    shift = 0
    dx = 0.01
    dy = 0.01
    mat_var = h * x_var + shift
    Y_var = h * y_var + shift
    X_var = h * x_var + shift


    for i, elem in enumerate(x_var_dot):
        Y_var[i] = integral(elem,0)

    #for i in range(X_var.shape[0]-1):
    #    Y_var[:,i+1] = Y_var[:,i] + dx*(x_var_dot[:,i])

    result = X_var + Y_var
    ax = plt.axes(projection='3d')
    ax.plot_surface(x_var, y_var, result, cmap='viridis', edgecolor='none')
    ax.set_title('Surface plot')

    '''
    scaler = 1/(10*(x_var_dot**2 + y_var_dot**2)**0.5)
    mat_var[0,0] = 0
    for i in range(1,x_var.shape[0]):
        for j in range(1,y_var.shape[0]):
            mat_var[i,j] = mat_var[i-1,j-1] + dx*(x_var_dot[i,j-1] ) + dy*(y_var_dot[i-1,j])

    '''
    #ax = plt.axes(projection='3d')
    #ax.plot_surface(x_var, y_var, -mat_var, cmap='viridis', edgecolor='none')
    #ax.set_title('Surface plot')
    #plt.plot(x_var[:,50], -integral(y_var_dot[50,:],0))
    #plt.plot(x_var[:,25],x_var_dot[x_var[:,25]<=0,25].tolist() + (-x_var_dot[x_var[:,25]>0,25]).tolist())
    #plt.plot(x_var[:,50],x_var_dot[:,50])
    #plt.plot([x_var[1, 50], x_var[-1,50]],[0,0])
    #print(x_var_dot[1,:].shape)
    #plt.plot(P)
    #plt.plot(d_y_dot)




# ███    ███  █████  ██ ███    ██
# ████  ████ ██   ██ ██ ████   ██
# ██ ████ ██ ███████ ██ ██ ██  ██
# ██  ██  ██ ██   ██ ██ ██  ██ ██
# ██      ██ ██   ██ ██ ██   ████



if __name__ == "__main__":
    m,n = 2,2
    x_var, y_var = var_creator(m,n,100)
    x_var_dot, y_var_dot = var_dot_calculate(x_var, y_var)
    print(x_var_dot.shape)
    potential_surface_plotter(x_var, y_var, x_var_dot, y_var_dot)
    #arrow_plotter(x_var, y_var, x_var_dot, y_var_dot)
    #arrow_norm_surface(x_var, y_var, x_var_dot, y_var_dot)
    #plt.xlim([-m,m])
    #plt.ylim([-n,n])
    plt.show()
