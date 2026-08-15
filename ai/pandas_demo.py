import pandas as pd

df = pd.read_csv("../datasets/students.csv")

result = df.groupby("Branch")["Marks"].mean()
print(result)