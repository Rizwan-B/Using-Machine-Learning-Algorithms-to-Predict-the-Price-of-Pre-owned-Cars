import numpy as np 

class linearRegression():

    # Constructor to initialize the learning rate and the number of iterations
    def __init__(self, learning_rate, iterations):
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.weights = None

    # Fits the linear regression model to the given training data.   
    def fit(self, X_train, Y_train):
        X = np.insert(X_train, 0, 1, axis=1)
        
        # Initialize the weights to zero
        self.weights = np.zeros(X.shape[1]) 
        
        # Performs gradient descent for the specified number of iterations
        for i in range(self.iterations):
            Y_pred = np.dot(X, self.weights)
            error = Y_train - Y_pred
            gradient = - (2 * (X.T).dot(error)) / X.shape[0] # Calculates the gradient
            self.weights = self.weights - self.learning_rate * gradient # Updates the weights
        
        return self
        
    def predict(self, X_test):
        X_test = np.insert(X_test, 0, 1, axis=1) # Adds a column of 1's to the input data for the bias term
        return np.dot(X_test, self.weights)