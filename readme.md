# PBQP inteference graph generator
---
#### A python script to create PBQP graphs from c/c++ codes. The main goal is generate a dataset for machine learning models to solve register allocation

---

`llscript.py`:
- Compile c/c++ codes on directory and generates .ll files with mem2reg option

##### Flags
- `--dir/ -d` - Path to directory with .ll input files.
- `--output/ -o` - Path to output directory.

---

`ir2graphs.py.py`:
- Generate .json files with PBQP interference graphs from .ll files with mem2reg option

##### Flags
- `--dir/ -d` - Path to directory with .ll input files.
- `--output/ -o` - Path to output directory.
- `--array/ -a` - Display cost array of nodes on .json file.
- `--matrix/ -m` - Display cost matrix of edges on .json file.
