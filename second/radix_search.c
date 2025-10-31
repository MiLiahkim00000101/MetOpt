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
    delta = (b - a) / 4;
    clock_t start_time = clock();
    long long iterations = 0;
    double x_prev_prev = a, f_prev_prev = func(x_prev_prev), x_prev = a + delta, f_prev = func(x_prev), \
    x_curr = a + 2 * delta, f_curr = func(x_curr), x_min = a, f_min = f_prev_prev;
    
    while (1){
        iterations++;

        printf("%lf \t %lf\n", x_curr, b);

        if (fabs(a - b) < 2 * eps){
            x_min = (a + b) / 2;
            f_min = func(x_min);
            break;
        }
        if (f_curr >= f_prev_prev && f_prev_prev >= f_prev){
            a = x_prev_prev;
            b = x_curr;
            delta = (b - a) / 4;

            x_curr = x_prev;
            f_curr = f_prev;
            x_prev = x_prev_prev + delta;
            f_prev = func(x_prev);     
        }
        else{
            f_min = fmin(f_prev_prev, f_min);
            f_min = fmin(f_prev, f_min);
            f_min = fmin(f_min, f_curr);


            x_prev_prev = x_prev;
            x_prev = x_curr;

            f_prev_prev = f_prev;
            f_prev = f_curr;

            x_curr = x_curr + delta;
            f_curr = func(x_curr);
            
            if (x_curr > b){
                printf("%lf \t %lf", x_curr, b);
                printf("Выход за границы отрезка");
                return 1;
            }

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