import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# 1. Load dataset
df = pd.read_csv("../datasets/job_data.csv")

print("Original Data:")
print(df.head())

print()


# 2. Convert Job_Role into numerical columns
df_encoded = pd.get_dummies(
    df,
    columns=["Job_Role"],
    dtype=int
)

print("Encoded Data:")
print(df_encoded.head())

print()


# 3. Separate Features (X) and Target (y)

X = df_encoded.drop("Salary_LPA", axis=1)

y = df_encoded["Salary_LPA"]


print("X shape:", X.shape)
print("y shape:", y.shape)

print()


# 4. Split data into training and testing data

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


print("Training data:", X_train.shape)
print("Testing data:", X_test.shape)

print()


# 5. Create the Linear Regression model

model = LinearRegression()


# 6. Train the model

model.fit(X_train, y_train)


# 7. Make predictions

predictions = model.predict(X_test)


# 8. Display actual and predicted values

print("Actual Values:")
print(y_test.values)

print()

print("Predicted Values:")
print(predictions)

print()


# 9. Calculate evaluation metrics

mae = mean_absolute_error(y_test, predictions)

mse = mean_squared_error(y_test, predictions)

rmse = np.sqrt(mse)

r2 = r2_score(y_test, predictions)


# 10. Display evaluation results

print("----- Model Evaluation -----")

print("MAE:", mae)

print("MSE:", mse)

print("RMSE:", rmse)

print("R2 Score:", r2)