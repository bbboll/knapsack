# Knapsack Project
This project is part of a software practical held at [Robotics Lab IWR Heidelberg](http://joanna.iwr.uni-heidelberg.de/rlab/en/home) in winter semester 2016/17. The task was to develop a demonstration for the well-known [Knapsack Problem](https://en.wikipedia.org/wiki/Knapsack_problem) using a [Lego Mindstorm EV3](https://www.lego.com/de-de/mindstorms/about-ev3) brick running [ev3dev](http://www.ev3dev.org). Additional documentation is linked on the [practical page](http://joanna.iwr.uni-heidelberg.de/rlab/en/projects_list+sid=25).

# Code structure
The final code that was used for the demonstration can be found in `main/`. We tested different implementations for the knapsack solver with regard to their performance. Python and C++ implementations as well as [boost.python](http://www.boost.org/doc/libs/1_63_0/libs/python/doc/html/index.html) binding boilerplate can be found in `archive/`. In the end, a pure python implementation was used. We also wrote scripts for testing mechanical components of the robot. These can be found in `sensor_tests/`.

# Unit testing
The `main` directory contains code that runs on the EV3. Unit tests can be found in scripts with suffix `_test.py`. Run unit tests by passing the name of the testing module as well as the name of the tested (imported) module:

```{r, engine='bash', unit_test}
$ cd main/
$ python3 -m unittest -v knapsack_test knapsack
```

# Executing the program
Place a copy of the `main/` directory on the EV3 brick and execute `main/run.py`. A typical course of action involves [connecting to the brick via ssh](http://www.ev3dev.org/docs/tutorials/connecting-to-ev3dev-with-ssh/).