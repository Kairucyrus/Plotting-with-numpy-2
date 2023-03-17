"""
Created by: Kairu Cyrus on: Friday 17,2023 22:54h rs
"""
import matplotlib.pyplot as plt
import numpy as np
def func(x):
    return x** 3 - 2*x - 5
x= np.arange(-20,20)
y =  x** 3 - 2*x - 5
plot = plt.plot(x,y)
plot.show()
