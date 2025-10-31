import math as m

am_func = 0
def func(x):
    global am_func
    am_func += 1
    return m.exp(x) + x ** 2


def main():
    a_start = -1
    b_start = 1
    a = a_start
    b = b_start
    eps = 1e-3
    iter = 0

    x1 = 3 / 4 * a + 1 / 4 * b
    x2 = 1 / 2 * a + 1 / 2 * b
    x3 = 1 / 4 * a + 3 / 4 * b
    f_x1 = func(x1)
    f_x2 = func(x2)
    f_x3 = func(x3)

    while abs(b - a) >= eps * abs(a + b) / 2 and abs(b - a) >= eps:
        
        iter += 1

        min_f = min(f_x1, f_x2, f_x3)

        if min_f == f_x1:
            a = a
            b = x2
            x2 = x1
            f_x2 = f_x1
            
        elif min_f == f_x2:
            a = x1
            b = x3
            x2 = x2
            
        elif min_f == f_x3:
            a = x2
            x2 = x3
            f_x2 = f_x3
            b = b
        
        x1 = (a + x2) / 2
        x3 = (b + x2) / 2
        f_x1 = func(x1)
        f_x3 = func(x3)

    print("Вычислений функции:", am_func)
    print("Количество итераций:", iter)
    print("Точка минимума:", (a + b) / 2)
    print("Значение Минимума:", func((a + b) / 2))
    print("Априорный подсчет итераций:", m.ceil(m.log2((b_start - a_start) / eps)))

if __name__ == "__main__":
    main()