import math as m
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp


am_func = 0
am_der = 0

x_list = []
y_list = []

y_der_list = []

x = sp.symbols('x')

f = sp.exp(x) + x ** 2

dx = sp.diff(f)

f_func = sp.lambdify(x, f, 'numpy')
dx_func = sp.lambdify(x, dx, 'numpy')


def func(x):
    global am_func
    am_func += 1
    x_list.append(x)

    y = f_func(x)

    y_list.append(y)
    return y

def F(x):
    global am_der
    am_der += 1
    
    x_list.append(x)
    y_der = dx_func(x)

    y_der_list.append(y_der)
    return y_der





def visualize_func(a, b, eps):

    global x_list
    global y_list
    global am_func

    x_steps = np.array(x_list)
    y_der_steps = F(x_steps)
    y_steps = func(x_steps)

    # print(x_steps)
    # print(y_steps)


    x = np.linspace(a, b, int(1/eps))
    y = np.array([func(elem) for elem in x])
    y_der = np.array([F(elem) for elem in x ])
    fig, ax = plt.subplots(1, 2)

    # ax[0].plot(x_steps, y_steps, marker="none", color="red")

    # for idx, y_val in enumerate(y_steps):
    #     ax[0].plot(x_steps[idx], y_val, marker="none", color="red") # В чем проблема?


    
    # Рисуем хорды между последовательными точками
    for i in range(1, len(x_steps) - 1):
        x2 = x_steps[i]
        y2 = y_steps[i]
        
        # Рисуем хорду (линию между двумя точками на графике функции)
        ax[0].plot([x_steps[0], x2], [y_steps[0], y2], 'ro--', linewidth=1, markersize=4)

    ax[0].scatter(x_steps, y_steps, color="red", s=50, zorder=5, label='Точки метода')

    ax[0].plot(x, y, linewidth=2.0)
    ax[0].axhline(y=0, color="grey", linestyle="-")
    ax[0].axvline(color="grey", linestyle="-")
    ax[0].grid(True)

    ax[0].set(xlim=(a, b), ylim=(min(min(y), 0), max(max(y), 0)))


    ax[1].plot(x, y_der, linewidth=2.0)
    ax[1].axhline(y=0, color="grey", linestyle="-")
    ax[1].axvline(color="grey", linestyle="-")
    ax[1].set(xlim=(a, b), ylim=(min(min(y_der), 0), max(max(y_der), 0)))
    ax[1].grid(True)
    ax[1].stem(x_steps, y_der_steps, markerfmt="none")
     # Рисуем хорды между последовательными точками
    for i in range(1, len(x_steps) - 1):
        x2 = x_steps[i]
        y2 = y_der_steps[i]
        
        # Рисуем хорду (линию между двумя точками на графике функции)
        ax[1].plot([x_steps[0], x2], [y_der_steps[0], y2], 'ro--', linewidth=1, markersize=4)


    plt.show()

def main():

    a_start = -1
    b_start = 1
    a = a_start
    b = b_start
    eps = 1e-3
    iter = 0

    F_b = F(b)
    F_a = F(a)
    

    x_c = a - (F_a*(a - b) / (F_a - F_b))

    F_x_c = F(x_c)



    while abs(F_x_c) > eps:
        
        iter += 1

        if F_x_c > 0:
            b = x_c
            
            F_b = F_x_c
        else:
            a = x_c

            F_a = F_x_c

        x_c = a - (F_a*(a - b) / (F_a - F_b))

        F_x_c = F(x_c)
        

    print("Вычислений производной функции:", am_der)
    print("Количество итераций:", iter)
    print("Точка минимума:", x_c)
    print("Значение Минимума:", func(x_c))
    print("Априорный подсчет итераций:", "no info")
    visualize_func(a_start, b_start, eps)
    
if __name__ == "__main__":
    main()