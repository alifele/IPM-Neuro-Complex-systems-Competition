import numpy as np
import matplotlib.pyplot as plt


def var_dot_calculate(x_var, y_var):
    '''
    Note that the x_var and y_var must be in the shape of m*m which is created
    be the outer (it is also used for the surface plots)
    '''

    x_var_dot = x_var - x_var**2 - x_var*y_var
    y_var_dot = 3*y_var - x_var*y_var - 2*y_var**2

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
            plt.arrow(x_, y_, x_var_dot[i,j]*scaler[i,j], y_var_dot[i,j]*scaler[i,j], head_width=0.03, color='k',
            alpha = 0.5, head_length=0.15)
            #plt.plot(x_, y_)
            #print(x_, y_)




if __name__ == "__main__":
    m,n = 5,5
    x_var, y_var = var_creator(m,n,80)
    x_var_dot, y_var_dot = var_dot_calculate(x_var, y_var)
    arrow_plotter(x_var, y_var, x_var_dot, y_var_dot)
    plt.xlim([-m,m])
    plt.ylim([-n,n])
    plt.show()
