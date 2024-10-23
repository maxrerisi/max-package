import os
import numpy as np
import random

def seed_everything(seed: int = 42):
    """
    Seeds the 3 conceivable randomizers used throughout this repository. Default seed 42 is passed as an argument wherever necessary.
    """
    random.seed(seed)
    os.environ['PYTHONASSEED'] = str(seed)
    np.random.seed(seed)