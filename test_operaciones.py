import pytest
from operaciones import *

# Pruebas unitarias de la funcion "sumar"
def test_sumar1():
    res=sumar( [1, 2, 3] )
    assert res==6

def test_sumar2():
    res=sumar( [10, 15, 20] )
    assert res==45

def test_sumar3():
    res=sumar( [] )
    assert res==0

def test_promediar():
    res = promediar([12, 25, 10, 15])
    assert res == 15.5