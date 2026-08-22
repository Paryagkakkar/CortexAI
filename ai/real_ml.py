import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# Load dataset
df = pd.read_csv("../datasets/job_data.csv")


# Convert Job_Role into numbers
df_encoded = pd.get_dummies(
    df,
    columns=["Job_Role"],
    dtype=int
)


# Features and target
X = df_encoded.drop("Salary_LPA", axis=1)

y = df_encoded["Salary_LPA"]


# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create model
model = LinearRegression()


# Train model
model.fit(X_train, y_train)