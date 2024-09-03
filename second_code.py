# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 12:18:05 2024

@author: pbrown2
"""

import numpy as np
import matplotlib.pyplot as plt

# Step 1: Define the functions
def f1(n):
    return 0.5 * n * (n - 1) + 10

def g1(n):
    return n ** 2

def f2(n):
    return np.sqrt(n**5 + 3*n + 1)

def g2(n):
    return 5 * n ** 2

def f3(n):
    return np.log(n)

def g3(n):
    return np.sqrt(n)

def f4(n):
    return np.log2(n)

def g4(n):
    return np.log10(n)

# Generate n ranges
n1 = np.arange(1, 11)
n2 = np.arange(1, 10**6 + 1)
n3 = np.arange(2, 11)
n4 = np.arange(2, 10**6 + 1)

# Function to save plots
def save_plot(x, y1, y2, filename, xlabel='n', ylabel='Function values', title='', labels=('f(n)', 'g(n)')):
    plt.figure(figsize=(10, 6))
    plt.plot(x, y1, label=labels[0])
    plt.plot(x, y2, label=labels[1])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.savefig(filename)
    plt.close()

def save_ratio_plot(x, y1, y2, filename, xlabel='n', ylabel='Ratio', title=''):
    plt.figure(figsize=(10, 6))
    plt.plot(x, y1 / y2, label='f(n) / g(n)')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.savefig(filename)
    plt.close()

# Deliverable 1
save_plot(n1, f1(n1), g1(n1), 'plot_fn_gn_1_to_10.png', title='Plot of f(n) and g(n) from n=1 to n=10')
save_plot(n2, f1(n2), g1(n2), 'plot_fn_gn_1_to_10e6.png', title='Plot of f(n) and g(n) from n=1 to n=10^6')

# Deliverable 2
save_ratio_plot(n1, f1(n1), g1(n1), 'ratio_fn_gn_1_to_10.png', title='Ratio f(n) / g(n) from n=1 to n=10')
save_ratio_plot(n2, f1(n2), g1(n2), 'ratio_fn_gn_1_to_10e6.png', title='Ratio f(n) / g(n) from n=1 to n=10^6')

# Deliverable 3
save_plot(n1, f2(n1), g2(n1), 'plot_fn2_gn2_1_to_10.png', title='Plot of f(n) and g(n) from n=1 to n=10', labels=('f(n) = sqrt(n^5 + 3n + 1)', 'g(n) = 5n^2'))
save_plot(n2, f2(n2), g2(n2), 'plot_fn2_gn2_1_to_10e6.png', title='Plot of f(n) and g(n) from n=1 to n=10^6', labels=('f(n) = sqrt(n^5 + 3n + 1)', 'g(n) = 5n^2'))
save_ratio_plot(n1, f2(n1), g2(n1), 'ratio_fn2_gn2_1_to_10.png', title='Ratio f(n) / g(n) from n=1 to n=10')
save_ratio_plot(n2, f2(n2), g2(n2), 'ratio_fn2_gn2_1_to_10e6.png', title='Ratio f(n) / g(n) from n=1 to n=10^6')

# Deliverable 4
save_plot(n3, f3(n3), g3(n3), 'plot_fn3_gn3_2_to_10.png', title='Plot of f(n) and g(n) from n=2 to n=10', labels=('f(n) = log(n)', 'g(n) = sqrt(n)'))
save_plot(n4, f3(n4), g3(n4), 'plot_fn3_gn3_2_to_10e6.png', title='Plot of f(n) and g(n) from n=2 to n=10^6', labels=('f(n) = log(n)', 'g(n) = sqrt(n)'))
save_ratio_plot(n3, f3(n3), g3(n3), 'ratio_fn3_gn3_2_to_10.png', title='Ratio f(n) / g(n) from n=2 to n=10')
save_ratio_plot(n4, f3(n4), g3(n4), 'ratio_fn3_gn3_2_to_10e6.png', title='Ratio f(n) / g(n) from n=2 to n=10^6')

# Deliverable 5
save_plot(n3, f4(n3), g4(n3), 'plot_fn4_gn4_2_to_10.png', title='Plot of f(n) and g(n) from n=2 to n=10', labels=('f(n) = log2(n)', 'g(n) = log10(n)'))
save_plot(n4, f4(n4), g4(n4), 'plot_fn4_gn4_2_to_10e6.png', title='Plot of f(n) and g(n) from n=2 to n=10^6', labels=('f(n) = log2(n)', 'g(n) = log10(n)'))
save_ratio_plot(n3, f4(n3), g4(n3), 'ratio_fn4_gn4_2_to_10.png', title='Ratio f(n) / g(n) from n=2 to n=10')
save_ratio_plot(n4, f4(n4), g4(n4), 'ratio_fn4_gn4_2_to_10e6.png', title='Ratio f(n) / g(n) from n=2 to n=10^6')