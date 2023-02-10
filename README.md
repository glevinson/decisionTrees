## Notes on code files

We've included the following additional files for running our code:
- `manipulate_data.py` 
  - we used this file as to run driver code to test our functions. For some reason, example_main led us to issues in find_majority_label, though we cannot figure out why. We've added comments to the function on the error.  
- `max_info_gain.py` 
  - this file contains all the functions we use in `fit` and `predict`
- `classificationV2.py`
  - this file contains our improved classifier object and its various methods.
- `evaluation.py`
  - this file contains all the functions we used for answering parts 3 and 4.
- `node.py`
  - this file contains our custom `Node` class, which our classifiers are made up of.

## How to run code

1) Input the path to your own dataset in ```main.py``` (we are expecting a text file).
```
if __name__ == "__main__":
    np.random.seed(2)
    
    # LOAD DATASET
    dataset = np.loadtxt([THE DIRECTORY TO YOUR DATASET])

```

2) Run ```python main.py```
