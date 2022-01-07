import matplotlib  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
import numpy as np
import pandas as pd
import seaborn as sns  # type: ignore
from IPython.display import display  # type: ignore
from tqdm.notebook import tqdm  # type: ignore

from project import DATA_DIR

pd.set_option('display.max_columns', 500)

# Graphics
sns.set()
sns.set_context('talk')
matplotlib.rcParams['figure.figsize'] = (12, 8)

tqdm.pandas()
