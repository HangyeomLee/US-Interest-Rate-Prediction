# US-Interest-Rate-Prediction
# Project Description:
This project aims to predict US interest rates based on economic indicators such as inflation, unemployment rate, Real GDP, and the Effective Federal Funds Rate using Support Vector Machines (SVM) and deep learning techniques. Understanding the relationship between interest rates and economic indicators is crucial for predicting interest rate movements, which can have significant implications for businesses and consumers in the economy.

# Relationship between Interest Rates and Economic Indicators:

# Inflation: 
Central banks often increase interest rates to combat high inflation. Hence, finding a correlation between inflation and interest rates can help in predicting future rate movements.
# Unemployment Rate: 
Central banks usually attempt to stimulate the economy by lowering interest rates when unemployment is high, leading to an inverse relationship between the two.
# Real GDP: 
Real GDP indicates economic growth. Typically, strong economic growth results in central banks raising interest rates to control inflation.
# Effective Federal Funds Rate: 
This rate influences other interest rates in the economy. As such, understanding its relationship with the target interest rate is vital for accurate predictions.

# Methods: SVM and Deep Learning

# Support Vector Machines (SVM): 
SVM is a type of supervised learning algorithm suitable for classification or regression tasks. It works by finding the optimal hyperplane that can separate two classes or predict a continuous value. In this project, SVM is used for its ability to handle high dimensional data and its effectiveness in small to medium-sized datasets.
# Deep Learning: 
Deep learning is a subset of machine learning that uses neural networks with several hidden layers to model complex patterns in data. For this project, deep learning can model the complex and nonlinear relationships between the economic indicators and interest rates.

# Hyperparameter Optimization:

# Grid Search: 
A grid search is an exhaustive search for the optimal set of hyperparameters. It works by evaluating the model's performance on each combination of hyperparameters specified within predefined ranges. However, grid search can be computationally expensive, especially for large hyperparameter spaces.
# Bayesian Optimization: 
An alternative to grid search, Bayesian optimization is a more efficient method for finding the optimal hyperparameters. It builds a probabilistic model of the objective function (model performance) and uses this model to make decisions on the next set of hyperparameters to evaluate. This results in fewer evaluations and quicker convergence to the optimal solution.
By understanding the connections between interest rates and economic indicators, and utilizing the best-suited machine learning methods and optimization techniques, this project aims to accurately predict future US interest rate movements.
