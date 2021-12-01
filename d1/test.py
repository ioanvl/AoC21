import pandas as pd
import os

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as file:
    lines = file.readlines()

frame = pd.DataFrame()
frame['x'] = [int(i) for i in lines]
print(sum(frame['x'].diff() > 0))

frame['x_sum'] = frame.rolling(3).sum()
print(sum(frame['x_sum'].diff() > 0))