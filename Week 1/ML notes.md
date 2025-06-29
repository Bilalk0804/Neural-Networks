# ML notes

Logistic Regression is a widely-used machine learning algorithm for binary classification problems. It's a simple yet effective algorithm that models the relationship between input features and a binary outcome using the logistic (sigmoid) function.

Key Concepts
Hypothesis Function: Logistic regression predicts the probability of the dependent variable (output) belonging to a particular class, typically 0 or 1.



Assumptions
The dependent variable is binary (can be extended to multiclass classification using Softmax Regression).
Features are linearly separable for the algorithm to perform optimally.
No strict assumptions about the distribution of the independent variables.
Implementation (Using Python)
Here's how to implement logistic regression with Scikit-learn:

python
Copy code
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Sample dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Logistic Regression Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
Advantages
Simple and easy to implement.
Computationally efficient for small to medium datasets.
Provides probabilistic predictions.
Disadvantages
Limited to linear decision boundaries.
Struggles with outliers or highly correlated features.
Assumes the relationship between the independent variables and the log-odds of the dependent variable is linear.
Logistic regression is a great starting point for classification problems, especially when interpretability is important.