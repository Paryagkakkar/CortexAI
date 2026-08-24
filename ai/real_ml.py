import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import ( mean_absolute_error,
mean_squared_error
)


# Load dataset
df = pd.read_csv("../datasets/job_data.csv")
df_encoded=pd.get_dummies(
    df,
    columns=["Job_Role"],
    dtype=int
)
X=df_encoded.drop("Salary_LPA",axis=1)
y=df_encoded["Salary_LPA"]
X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
model=LinearRegression()
model.fit(X_train,y_train)
predictions=model.predict(X_test)
print("Actual salaries:")
print(y_test.values)
print()
print("Predicted  salaries:")
print(predictions)
mae=mean_absolute_error(
    y_test,
    predictions
)
mse=mean_squared_error(
    y_test,
    predictions
)
rmse=np.sqrt(mse)

print()
print("Mean Absolute Error",mae)
print("mse:",mse)
print("rsme:"rsme)
