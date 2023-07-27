# PBQP Inteference Graph Generator
---
#### A python script to create PBQP graphs from c/c++ codes. The main goal is generate a dataset for machine learning models to solve register allocation

---

`llscript.py`:
- Compile c/c++ codes on directory and generates .ll files with mem2reg option

##### Flags
- `--dir/ -d` - Path to root directory for C/C++ files search.
- `--output/ -o` - Path to output directory.
- `--subdirectorys/ -s` - Iterate all subdirectories and search for C/C++ files.
- `--keepfolders/ -k` - Keep folders structure in output directory if `--subdirectorys` is True.
- `--clean/ -c` - Remove temporary .ll files.
- `--name/ -n'` - Name for output files. Files name will be:  "name_0", "name_2", "name_3", ... "name_\[number_of_files\]". Default is original files names.

---

`ir2graphs.py.py`:
- Generate .json files with PBQP interference graphs from .ll files with mem2reg option

##### Flags
- `--dir/ -d` - Path to directory with .ll input files.
- `--output/ -o` - Path to output directory.
- `--subdirectorys/ -s` - Iterate all subdirectories and search for .ll files.
- `--keepfolders/ -k` - Keep folders structure in output directory if `--subdirectorys` is True.
- `--costfunc/ -f` - Name of python file with cost function for array/matrix generation. Needs to be in same directory.
- `--regcost/ -r` - Path to .json file with the registers cost array.
- `--array/ -a` - Display cost array of nodes on .json file.
- `--matrix/ -m` - Display cost matrix of edges on .json file.
- `--clear/ -c` - Remove files in output directory.
- `--onlyfunction/ -of` - Save each function in a separeted file.