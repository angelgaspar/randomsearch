<div class=text-justify>

# Random search algorithm

A simple n-dimensional random search algorithm.

## Introduction

The Random search algorithm was the first method that based its optimization strategy on a stochastic process.
Only one solution ![equation](https://raw.githubusercontent.com/angelgaspar/randomsearch/master/docs/equations/png.latex-1.png)
is kept during the evolution process. In each iteration, the solution ![equation](https://raw.githubusercontent.com/angelgaspar/randomsearch/master/docs/equations/png.latex-1.png)
is modified by adding a random vector ![equation](https://raw.githubusercontent.com/angelgaspar/randomsearch/master/docs/equations/png.latex-2.png)
. In this way the new solution is modeled under the following expression:

![equation](https://raw.githubusercontent.com/angelgaspar/randomsearch/master/docs/equations/png.latex-3.png)

Considering that the solution ![equation](https://raw.githubusercontent.com/angelgaspar/randomsearch/master/docs/equations/png.latex-1.png) has *d* dimensions
![equation](https://raw.githubusercontent.com/angelgaspar/randomsearch/master/docs/equations/png.latex-4.png)
, each coordinate is modified ![equation](https://raw.githubusercontent.com/angelgaspar/randomsearch/master/docs/equations/png.latex-5.png)
by the random disturbance ![equation](https://raw.githubusercontent.com/angelgaspar/randomsearch/master/docs/equations/png.latex-6.png) modeled by a 
Gaussian probability distribution defined as:

![equation](https://raw.githubusercontent.com/angelgaspar/randomsearch/master/docs/equations/png.latex-7.png)

where ![equation](https://raw.githubusercontent.com/angelgaspar/randomsearch/master/docs/equations/png.latex-8.png) and
![equation](https://raw.githubusercontent.com/angelgaspar/randomsearch/master/docs/equations/png.latex-9.png), represent the standard deviation and the mean value, 
respectively for dimension *i*. Since the value of ![equation](https://raw.githubusercontent.com/angelgaspar/randomsearch/master/docs/equations/png.latex-10.png)
adds a modification around ![equation](https://raw.githubusercontent.com/angelgaspar/randomsearch/master/docs/equations/png.latex-11.png)
, the mean value is considered zero ![equation](https://raw.githubusercontent.com/angelgaspar/randomsearch/master/docs/equations/png.latex-12.png)
.

Once ![equation](https://raw.githubusercontent.com/angelgaspar/randomsearch/master/docs/equations/png.latex-13.png)
has been calculated, it is tested whether the new position improves the quality of the previous solution
![equation](https://raw.githubusercontent.com/angelgaspar/randomsearch/master/docs/equations/png.latex-1.png). 
In this way, if the quality of ![equation](https://raw.githubusercontent.com/angelgaspar/randomsearch/master/docs/equations/png.latex-13.png) is better than
![equation](https://raw.githubusercontent.com/angelgaspar/randomsearch/master/docs/equations/png.latex-1.png), the value of
![equation](https://raw.githubusercontent.com/angelgaspar/randomsearch/master/docs/equations/png.latex-13.png) is accepted as the new solution, otherwise
![equation](https://raw.githubusercontent.com/angelgaspar/randomsearch/master/docs/equations/png.latex-1.png) remains unchanged.

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