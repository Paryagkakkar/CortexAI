import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("../datasets/students.csv")
sns.scatterplot(x="marks",y="branch",data=df)
plt.show()