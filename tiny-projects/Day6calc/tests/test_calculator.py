import pytest

from calculator import *

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(10, 4) == 6

def test_multiply():
    assert multiply(3, 5) == 15

def test_divide():
    assert divide(10, 2) == 5
    assert divide(10, 0) is None

def test_percent_of():
    assert percent_of(20, 50) == 10

def test_increase_by_percent():
    assert increase_by_percent(100, 10) == pytest.approx(110)

def test_decrease_by_percent():
    assert decrease_by_percent(200, 25) == pytest.approx(150)
    
def test_bmi_metric():
    assert round(bmi (70, 1.75), 2) == 22.86

def test_weight_conversions():
    assert round(kg_to_lb(1), 5) == 2.20462
    assert round(lb_to_kg(2.20462), 5) == 1

def test_temperature_conversions():
    assert c_to_f(0) == 32
    assert round(f_to_c(32), 2) == 0
