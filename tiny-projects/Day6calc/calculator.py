def add(a, b): return a + b
def subtract(a,b): return a - b
def multiply(a,b): return a * b
def divide(a,b): 
    if b == 0: 
        return None 
    return a / b

def percent_of(x, y): return (x / 100) * y
def increase_by_percent(value, percent): return value * (1 + percent / 100)
def decrease_by_percent(value, percent): return value * (1 - percent / 100)

def bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)

def kg_to_lb(kg): return kg * 2.20462
def lb_to_kg(lb): return lb / 2.20462

def c_to_f(c): return (c * 9/5) + 32
def f_to_c(f): return (f - 32) * 5/9