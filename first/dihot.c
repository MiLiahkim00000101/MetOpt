#include <time.h>
#include <stdio.h>
#include <math.h>

double func(double x);

long long am_func_calc = 0;

int main(){
    double a, b, eps, delta;
    double a_start = -1, b_start = 1;
    a = a_start;
    b = b_start;
    eps = 1e-3;
    delta = 1e-7;
    clock_t start_time = clock();
    long long iterations = 0;
    double x_min = a, x_1, x_2, f_1, f_2, f_min;
    
    while (1){
        x_1 = (a + b) / 2 - delta;
        x_2 = (a + b) / 2 + delta;
        f_1 = func(x_1);
        f_2 = func(x_2);
        if (f_1 < f_2){
            a = a;
            b = x_2;
        }
        else{
            a = x_1;
            b = b;
        }
        iterations++;
        if (b - a < 2 * eps){
            x_min = (a + b) / 2;
            f_min = func(x_min);
            break;
        }
    }
    clock_t end_time = clock();

    printf("Точка минимума: %lf \nЗначение Минимума: %lf \n\
Количество вычислений значения функций: %lld \n\
Время выполнения: %lf\n\
Количество итераций: %lld\n\
Априорный подсчет количества итераций: %lf\n", x_min, f_min, am_func_calc, \
(double)(end_time - start_time) / CLOCKS_PER_SEC, iterations, (double)(log2((b_start - a_start) / (2 * (eps - delta)))));

    return 0;
}


double func(double x){
    am_func_calc++;
    return exp(x) + pow(x, 2);
}