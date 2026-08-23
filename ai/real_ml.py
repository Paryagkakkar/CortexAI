import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# Load dataset
df = pd.read_csv("../datasets/job_data.csv")

print(df.head())


# Select input and output
X = df[["Experience"]]
y = df["Salary"]


# Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# Create model
model = LinearRegression()


# Train model
model.fit(X_train, y_train)


# Make predictions
predictions = model.predict(X_test)


# Show actual values
print("Actual salaries:")
print(y_test.values)

print()


# Show predicted values
print("Predicted salaries:")
print(predictions)