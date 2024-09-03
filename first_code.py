# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 12:00:50 2024

@author: pbrown2
"""

import numpy as np
import matplotlib.pyplot as plt

# Step 1: Define the functions
def f1(n):
    return 0.5 * n * (n - 1) + 10

def g1(n):
    return n ** 2

# Step 1: Plot f(n) and g(n) for n from 1 to 10
n1 = np.arange(1, 11)
plt.figure(figsize=(10, 6))
plt.plot(n1, f1(n1), label='f(n) = 0.5 * n * (n - 1) + 10')
plt.plot(n1, g1(n1), label='g(n) = n^2')
plt.title('Functions f(n) and g(n) from n=1 to n=10')
plt.xlabel('n')
plt.ylabel('Function values')
plt.legend()
plt.grid(True)
plt.show()

# Step 1: Plot f(n) and g(n) for n from 1 to 10^6
n2 = np.arange(1, 10**6 + 1)
plt.figure(figsize=(10, 6))
plt.plot(n2, f1(n2), label='f(n) = 0.5 * n * (n - 1) + 10')
plt.plot(n2, g1(n2), label='g(n) = n^2')
plt.title('Functions f(n) and g(n) from n=1 to n=10^6')
plt.xlabel('n')
plt.ylabel('Function values')
plt.legend()
plt.grid(True)
plt.show()

# Step 2: Plot f(n)/g(n) for n from 1 to 10
plt.figure(figsize=(10, 6))
plt.plot(n1, f1(n1) / g1(n1), label='f(n) / g(n)')
plt.title('Ratio f(n) / g(n) from n=1 to n=10')
plt.xlabel('n')
plt.ylabel('Ratio')
plt.legend()
plt.grid(True)
plt.show()

# Step 2: Plot f(n)/g(n) for n from 1 to 10^6
plt.figure(figsize=(10, 6))
plt.plot(n2, f1(n2) / g1(n2), label='f(n) / g(n)')
plt.title('Ratio f(n) / g(n) from n=1 to n=10^6')
plt.xlabel('n')
plt.ylabel('Ratio')
plt.legend()
plt.grid(True)
plt.show()

# Define new functions
def f2(n):
    return np.sqrt(n**5 + 3*n + 1)

def g2(n):
    return 5 * n ** 2

# Plotting for Deliverable 3
# Functions plot from n=1 to 10
plt.figure(figsize=(10, 6))
plt.plot(n1, f2(n1), label='f(n) = sqrt(n^5 + 3n + 1)')
plt.plot(n1, g2(n1), label='g(n) = 5n^2')
plt.title('Functions f(n) and g(n) from n=1 to n=10')
plt.xlabel('n')
plt.ylabel('Function values')
plt.legend()
plt.grid(True)
plt.show()

# Functions plot from n=1 to 10^6
plt.figure(figsize=(10, 6))
plt.plot(n2, f2(n2), label='f(n) = sqrt(n^5 + 3n + 1)')
plt.plot(n2, g2(n2), label='g(n) = 5n^2')
plt.title('Functions f(n) and g(n) from n=1 to n=10^6')
plt.xlabel('n')
plt.ylabel('Function values')
plt.legend()
plt.grid(True)
plt.show()

# Ratio plot from n=1 to 10
plt.figure(figsize=(10, 6))
plt.plot(n1, f2(n1) / g2(n1), label='f(n) / g(n)')
plt.title('Ratio f(n) / g(n) from n=1 to n=10')
plt.xlabel('n')
plt.ylabel('Ratio')
plt.legend()
plt.grid(True)
plt.show()

# Ratio plot from n=1 to 10^6
plt.figure(figsize=(10, 6))
plt.plot(n2, f2(n2) / g2(n2), label='f(n) / g(n)')
plt.title('Ratio f(n) / g(n) from n=1 to n=10^6')
plt.xlabel('n')
plt.ylabel('Ratio')
plt.legend()
plt.grid(True)
plt.show()

# Define new functions
def f3(n):
    return np.log(n)

def g3(n):
    return np.sqrt(n)

# Handle the case for n starting from 2
n3 = np.arange(2, 11)
n4 = np.arange(2, 10**6 + 1)

# Plotting for Deliverable 4
# Functions plot from n=2 to 10
plt.figure(figsize=(10, 6))
plt.plot(n3, f3(n3), label='f(n) = log(n)')
plt.plot(n3, g3(n3), label='g(n) = sqrt(n)')
plt.title('Functions f(n) and g(n) from n=2 to n=10')
plt.xlabel('n')
plt.ylabel('Function values')
plt.legend()
plt.grid(True)
plt.show()

# Functions plot from n=2 to 10^6
plt.figure(figsize=(10, 6))
plt.plot(n4, f3(n4), label='f(n) = log(n)')
plt.plot(n4, g3(n4), label='g(n) = sqrt(n)')
plt.title('Functions f(n) and g(n) from n=2 to n=10^6')
plt.xlabel('n')
plt.ylabel('Function values')
plt.legend()
plt.grid(True)
plt.show()

# Ratio plot from n=2 to 10
plt.figure(figsize=(10, 6))
plt.plot(n3, f3(n3) / g3(n3), label='f(n) / g(n)')
plt.title('Ratio f(n) / g(n) from n=2 to n=10')
plt.xlabel('n')
plt.ylabel('Ratio')
plt.legend()
plt.grid(True)
plt.show()

# Ratio plot from n=2 to 10^6
plt.figure(figsize=(10, 6))
plt.plot(n4, f3(n4) / g3(n4), label='f(n) / g(n)')
plt.title('Ratio f(n) / g(n) from n=2 to n=10^6')
plt.xlabel('n')
plt.ylabel('Ratio')
plt.legend()
plt.grid(True)
plt.show()

# Define new functions
def f4(n):
    return np.log2(n)

def g4(n):
    return np.log10(n)

# Plotting for Deliverable 5
# Functions plot from n=2 to 10
plt.figure(figsize=(10, 6))
plt.plot(n3, f4(n3), label='f(n) = log2(n)')
plt.plot(n3, g4(n3), label='g(n) = log10(n)')
plt.title('Functions f(n) and g(n) from n=2 to n=10')
plt.xlabel('n')
plt.ylabel('Function values')
plt.legend()
plt.grid(True)
plt.show()

# Functions plot from n=2 to 10^6
plt.figure(figsize=(10, 6))
plt.plot(n4, f4(n4), label='f(n) = log2(n)')
plt.plot(n4, g4(n4), label='g(n) = log10(n)')
plt.title('Functions f(n) and g(n) from n=2 to n=10^6')
plt.xlabel('n')
plt.ylabel('Function values')
plt.legend()
plt.grid(True)
plt.show()

# Ratio plot from n=2 to 10
plt.figure(figsize=(10, 6))
plt.plot(n3, f4(n3) / g4(n3), label='f(n) / g(n)')
plt.title('Ratio f(n) / g(n) from n=2 to n=10')
plt.xlabel('n')
plt.ylabel('Ratio')
plt.legend()
plt.grid(True)
plt.show()

# Ratio plot from n=2 to 10^6
plt.figure(figsize=(10, 6))
plt.plot(n4, f4(n4) / g4(n4), label='f(n) / g(n)')
plt.title('Ratio f(n) / g(n) from n=2 to n=10^6')
plt.xlabel('n')
plt.ylabel('Ratio')
plt.legend()
plt.grid(True)
plt.show()