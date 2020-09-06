<div class=text-justify>

# Random search algorithm

A simple n-dimensional random search algorithm.

## Introduction

The Random search algorithm was the first method that based its optimization strategy on a stochastic process.
Only one solution ![equation](https://latex.codecogs.com/png.latex?x%5E%7Bk%7D)
is kept during the evolution process. In each iteration, the solution ![equation](https://latex.codecogs.com/png.latex?x%5E%7Bk%7D)
is modified by adding a random vector ![equation](https://latex.codecogs.com/png.latex?%5CDelta%20x)
. In this way the new solution is modeled under the following expression:

![equation](https://latex.codecogs.com/png.latex?x%5E%7Bk&plus;1%7D%20%3D%20x%5Ek%20&plus;%20%5CDelta%20x)

Considering that the solution ![equation](https://latex.codecogs.com/png.latex?x%5E%7Bk%7D) has *d* dimensions
![equation](https://latex.codecogs.com/png.latex?%5Cleft%20%28%20x%5Ek_1%2C%20x%5Ek_2%2C...%2C%20x%5Ek_d%20%5Cright%20%29)
, each coordinate is modified ![equation](https://latex.codecogs.com/png.latex?%5Cleft%20%28%20%5CDelta%20x%20%3D%20%5Cleft%20%5C%7B%20%5CDelta%20x_1%2C%20%5CDelta%20x_2%2C...%2C%20%5CDelta%20x_d%20%5Cright%20%5C%7D%20%5Cright%20%29)
by the random disturbance ![equation](https://latex.codecogs.com/png.latex?%5CDelta%20x_i%5Cleft%20%28%20i%20%5Cepsilon%20%5Cleft%20%5B%201%2C2%2C...%2Cd%20%5Cright%20%5D%20%5Cright%20%29) modeled by a 
Gaussian probability distribution defined as:

![equation](https://latex.codecogs.com/png.latex?p%5Cleft%20%28%20%5CDelta%20x_i%20%5Cright%20%29%20%3D%20%5Cfrac%7B1%7D%7B%5Csigma_i%5Ccdot%20%5Csqrt%7B2%5Cpi%20%7D%7Dexp%5Cleft%20%28%20-0.5%5Ccdot%20%5Cfrac%7B%5Cleft%20%28%20x_i%20-%20%5Cmu_i%20%5Cright%20%29%7D%7B%5Csigma%5E2_i%7D%20%5Cright%20%29%20%3D%20N%5Cleft%20%28%20%5Cmu_i%2C%20%5Csigma_i%20%5Cright%20%29)

where ![equation](https://latex.codecogs.com/png.latex?%5Csigma_i) and
![equation](https://latex.codecogs.com/png.latex?%5Cmu_i), represent the standard deviation and the mean value, 
respectively for dimension *i*. Since the value of ![equation](https://latex.codecogs.com/png.latex?%5CDelta%20x_i)
adds a modification around ![equation](https://latex.codecogs.com/png.latex?x%5Ek_i)
, the mean value is considered zero ![equation](https://latex.codecogs.com/png.latex?%5Cleft%20%28%20%5Cmu_i%20%3D%200%20%5Cright%20%29)
.

Once ![equation](https://latex.codecogs.com/png.latex?x%5E%7Bk&plus;1%7D)
has been calculated, it is tested whether the new position improves the quality of the previous solution
![equation](https://latex.codecogs.com/png.latex?x%5E%7Bk%7D). 
In this way, if the quality of ![equation](https://latex.codecogs.com/png.latex?x%5E%7Bk&plus;1%7D) is better than
![equation](https://latex.codecogs.com/png.latex?x%5E%7Bk%7D), the value of
![equation](https://latex.codecogs.com/png.latex?x%5E%7Bk&plus;1%7D) is accepted as the new solution, otherwise
![equation](https://latex.codecogs.com/png.latex?x%5E%7Bk%7D) remains unchanged.

## Installation
### GitHub

To install this library from GitHub run the following commands in the terminal:

    $ git clone https://github.com/angelgaspar/randomsearch.git
    $ cd randomsearch
    $ python setup.py install

### PyPi
  
If you have pip installed run the following commands in the terminal:

    $ pip install randomsearch

### Usage

This is an usage example:

```python
import randomsearch as rs


def your_function(x):
    return -(x[0] ** 2 + x[1] ** 2) + 4


a, b = rs.optimize(function=your_function, dimensions=2, lower_boundary=[-14, -14], upper_boundary= [10, 10], max_iter=10000, maximize=True)
print(a, ",", b)
```
    Note: The optimize function returns the best fitness and the best solution.
    If you want to minimize a function maximize should be False. 

</div>