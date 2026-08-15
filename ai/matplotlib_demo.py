import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("../datasets/students.csv")
branch_count=df["Branch"].value_counts()
print(branch_count)
plt.bar(branch_count.index,branch_count.values)
plt.xlabel("Branch")
plt.ylabel("Count")
plt.title("Students in branches")
plt.show()