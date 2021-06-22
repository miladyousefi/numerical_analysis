import math
from prettytable import PrettyTable
table = PrettyTable()
table.align="r"
table.field_names=['iterations','x_n=(a+b/2)','f(x_n)']
def bisect(f,a,b, TOL):
    if (f(a)*f(b) >= 0):
        print("You have not assumed the right interval.")
        return
    mid = a
    iterations = 0
    while ((b-a) >= TOL):
        mid = (a+b)/2
        result = f(mid)
        # Check if middle point is root
        if (result == 0):
            break
        # Decide the side to repeat the steps
        if (result*f(a) < 0):
            b = mid
        else:
            a = mid
        iterations += 1
        table.add_row([iterations,"{:0.5f}".format(mid),"{:.8}".format(result)])
    print(table)
    print(f'Root: {mid:.7f}\nIterations: {iterations}')

if __name__ == '__main__':
    f = lambda x: 3*x*math.exp(x)-1
    bisect(f, 0.25, 0.27, 0.0001)
    
