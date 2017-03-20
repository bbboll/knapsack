# Project structure
This is an umbrella project, incorporating seperate python and native implementations of our knapsack solver as well as sensor tests and the main runscripts.

# Unit testing
The `main` directory contains the code that actually runs on the EV3. Unit tests can be found (Go-style) in scripts containing the suffix `_test.py`. Run unit tests by passing the name of the testing module as well as the name of the tested (imported) module:

```{r, engine='bash', unit_test}
$ cd main/
$ python3 -m unittest -v knapsack_test knapsack
```

Note that the `tests/` directory contains sensor tests we ran on the robot, not unittests.

# Documentation
The `doc/` directory contains a `Makefile` for automatic generation of documentation from docstrings and `.rst` files contained in `doc/source`. Output formats for this documentation may be specified:
```{r, engine='bash', doc_make}
$ cd main/
$ make html
$ make latex
```