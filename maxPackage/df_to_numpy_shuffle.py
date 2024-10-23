import pandas as pd
import numpy as np

def load_data_to_numpy_randomized(df: pd.DataFrame, label_name: str = "LABEL"):
    """
    Convert dataframe to two numpy arrays (notated as X and y).
    Shuffle them according to a random permutation.
    Return the data as X, y.
    """


    X = df.drop(label_name, axis=1).to_numpy()
    y = df[label_name].to_numpy()

    p = np.random.permutation(len(y))
    X = X[p]
    y = y[p]
    return X, y