#include <time.h>
#include <stdio.h>
#include <math.h>

double func(double x);

int main(){
    double a, b, eps;
    a = -1;
    b = 1;
    eps = 1e-3;
    clock_t start_time = clock();
    long long iterations = 0, am_func_calc = 0;
    double x_min = a, x_curr = a, f_min = func(x_min), f_curr;
    am_func_calc++;
    
    while (x_curr <= b){
        x_curr += eps;
        f_curr = func(x_curr);
        am_func_calc++;
        if (f_curr < f_min){
            x_min = x_curr;
            f_min = f_curr;
        }
        iterations++;
    }
    clock_t end_time = clock();

    printf("Точка минимума: %lf \nЗначение Минимума: %lf \n\
Количество вычислений значения функций: %lld \n\
Время выполнения: %lf\n\
Количество итераций: %lld\n\
Априорный подсчет количества итераций: %lf\n", x_min, f_min, am_func_calc, \
(double)(end_time - start_time) / CLOCKS_PER_SEC, iterations, (double)((b - a) / eps));

    return 0;
}


double func(double x){
    return exp(x) + pow(x, 2);
}