import math as m
import numpy as np
import matplotlib.pyplot as plt

am_func = 0

x_list = []
y_list = []

def func(x):
    global am_func
    am_func += 1
    x_list.append(x)
    y = m.exp(x) + x ** 2
    y_list.append(y)
    return y

def visualize_func(a, b, eps):

    global x_list
    global y_list
    global am_func

    x_steps = np.array(x_list)
    y_steps = np.array(y_list)

    x = np.linspace(a, b, int(1/eps))
    y = np.array([func(elem) for elem in x])
    fig, ax = plt.subplots()

    # ax.scatter(x_steps, y_steps, color=["red", "black"] * am_func, marker="x")
    ax.plot(x_steps, y_steps, marker="none", color="red")

    ax.plot(x, y, linewidth=2.0)
    ax.axhline(y=0, color="grey", linestyle="-")
    ax.axvline(color="grey", linestyle="-")
    plt.grid(True)
    plt.stem(x_steps, y_steps, markerfmt="none")

    ax.set(xlim=(a, b), ylim=(min(min(y), 0), max(y)))

    plt.show()

def main():

    a_start = -1
    b_start = 1
    a = a_start
    b = b_start
    eps = 1e-3
    tau = (-1 + m.sqrt(5)) / 2
    ro = b - a
    eps_n = tau * ro
    iter = 0

    x1 = a + ro * (1 - tau)
    x2 = a + ro * tau

    f_x1 = func(x1)
    f_x2 = func(x2)


    while eps_n > eps:
        
        iter += 1

        if f_x1 <= f_x2:
            b = x2
            x2 = x1
            f_x2 = f_x1
            ro = b - a
            x1 = a + ro * (1 - tau)
            f_x1 = func(x1)
        else:
            a = x1
            x1 = x2
            f_x1 = f_x2
            ro = b - a
            x2 = a + ro * tau
            f_x2 = func(x2)
        
        eps_n *= tau

    print(eps_n)
    print("Вычислений функции:", am_func)
    print("Количество итераций:", iter)
    print("Точка минимума:", (a + b) / 2)
    print("Значение Минимума:", func((a + b) / 2))
    print("Априорный подсчет итераций:", m.ceil(m.log(2 * eps/ (b_start - a_start)) / m.log(tau)))
    visualize_func(a_start, b_start, eps)
    
if __name__ == "__main__":
    main()