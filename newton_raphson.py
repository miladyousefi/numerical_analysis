import math
e = math.e
pi = math.pi

def newton_raphson(f, df, x, TOL):
    error = 1
    iterations = 0
    while error > TOL:
        new_x = x - f(x)/df(x)
        error = abs(new_x - x)
        x = new_x
        iterations += 1
        print(f'x{iterations}: {x}')
    print(f"Newton's Estimate = {x:.15f}\nIterations: {iterations}")

def modified_newton(f, df, ddf, x, TOL):
    error = 1
    iterations = 0
    while error > TOL:
        f_x = f(x)
        d_x = df(x)
        new_x = x - (f_x*d_x)/(d_x*d_x - f_x*ddf(x))
        error = abs(new_x - x)
        x = new_x
        iterations += 1
        print(f'x{iterations}: {x}')
    print(f"Modified Newton Estimate = {x:.15f}\nIterations: {iterations}")

def fibonacci_estimate():
    values = [1, 22, 7, 42, 33, 4, 40]
    total = 0
    for i in range(len(values)):
        total += values[i]/(60**i)
    print(f"Fibonacci's Estimate = {total:.15f}")

if __name__ == '__main__':
    f = lambda x: x**2-3
    df = lambda x: 2*x
    ddf = lambda x: 2
    newton_raphson(f, df, 1.5, 1e-5)
    modified_newton(f, df, ddf, 1.5, 1e-3)
