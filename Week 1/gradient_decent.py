import numpy as np
def gradient_descent(X, y, theta, learning_rate, iterations):
    m = len(y)
    for _ in range(iterations):
        predictions = X.dot(theta)
        errors = predictions - y
        gradient = X.T.dot(errors) / m
        theta -= learning_rate * gradient
    return theta

# Example usage
if __name__ == "__main__":
    # Sample data
    X = np.array([[1, 1], [1, 2], [1, 3], [1, 4]])
    y = np.array([2, 3, 4, 5])
    theta = np.zeros(2)
    print(theta.shape[0]);
    print(X.shape[1])
    bias = np.ones((X.shape[0], 1))
    X = np.c_[bias, X]
    learning_rate = 0.01
    iterations = 1000

    # theta = gradient_descent(X, y, theta, learning_rate, iterations)
    # print("Theta:", theta)