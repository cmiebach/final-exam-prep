# predict_species.py — Predict iris species from flower measurements
#
# Usage:
#   python predict_species.py <sepal_length> <sepal_width> <petal_length> <petal_width>
#
# Example:
#   python predict_species.py 5.1 3.5 1.4 0.2

import sys
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris


def train_model():
    """Train a logistic regression model on the iris dataset."""
    iris = load_iris()
    X = iris.data
    y = iris.target
    model = LogisticRegression(max_iter=1000)
    model.fit(X, y)
    return model, iris.target_names


def predict_species(model, target_names, values):
    """Predict the species for the given feature values."""
    prediction = model.predict(values)
    return target_names[prediction[0]]


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python predict_species.py <sepal_length> <sepal_width> <petal_length> <petal_width>")
        print("Example: python predict_species.py 5.1 3.5 1.4 0.2")
        sys.exit(1)

    # Parse command-line arguments (all strings → convert to floats)
    values = np.array([float(arg) for arg in sys.argv[1:]]).reshape(1, -1)

    # Train and predict
    model, target_names = train_model()
    species = predict_species(model, target_names, values)

    # Display results
    print("Input values:")
    print(f"  sepal_length: {values[0][0]}")
    print(f"  sepal_width:  {values[0][1]}")
    print(f"  petal_length: {values[0][2]}")
    print(f"  petal_width:  {values[0][3]}")
    print("--------------------")
    print(f"Predicted species: {species}")
