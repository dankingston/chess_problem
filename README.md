# Chess Problem Solver
Finds the number of permutations for placing chess pieces on an M x N board without the pieces threatening eachother.

Run the solver with parameters for width, height and quantity of each of the pieces:
```
python solver.py -M 6 -N 9 --kings 2 --queens 1 --bishops 1 --rooks 1 --knights 1
Number of solutions: 20136752
```
Note: The above problem takes around 3 minutes to solve and uses no more than 4GB of RAM.


## Requirements
Install the python requirements:
```
pip install requirements.txt
```

Redis can optionally be used as a solution store. To install redis:
```
sudo apt install redis
```
Then use the parameter `--store redis` to store solutions in redis instead of in python memory.
The redis store is slower but more stable.


## Tests
Tests can be run using:
```
PYTHONPATH=. pytest tests
```

## Notes
* The performance is CPU-bound, so could potentially be improved by using multiprocessing.
* Some memory could be saved by hashing the 'hash_key' of the board. This would be at the expense of visible solutions.
* Code is PEP8 compliant with a max-line-length of 100.
