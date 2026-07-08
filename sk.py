from ucimlrepo import fetch_ucirepo
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
iris=fetch_ucirepo("iris")
x=pd.DataFrame(iris.data.features)
y=pd.DataFrame(iris.data.targets)
print(x.head())
print(y.head())