# Install conda
Create a enviornment for the project
```
$ conda create -n aoc2021 
$ conda activate aoc2021 
$ conda install pytest
```

Add `__pycache__` and `.pytest_cache` to `.gitignore`

# Tests
Tests methods are prefixed with test_ and included in each assignment file (Xa.py and Xb.py)
Run test in the directory it belongs e.g.:
```
$ cd 1
$ pytest 1a.py
$ pytest 1b.py
```
