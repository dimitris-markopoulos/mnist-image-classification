# MNIST Digit Classification Project

This repository contains my work on classifying MNIST handwritten digits, specifically focusing on distinguishing between digits 3, 5, and 8. I've implemented and compared several classification algorithms:

⊳ Logistic Regression (One-vs-Rest)

⊳ Multinomial Regression

⊳ Naive Bayes (Gaussian and Bernoulli)

⊳ Linear Discriminant Analysis

⊳ Linear SVM (One-vs-Rest)

Furthermore, I have implementented Group LASSO Multinomial Regression to perform feature selection on the 28x28 image and determine which pixels are significant in classification of the image to digits 3, 5, or 8.  I have implemented this strategy with multiple grouping methods and provided results in notebook 2.

## Key Findings:

Achieved 93.8% accuracy with Multinomial Regression
Demonstrated why Bernoulli Naive Bayes (87.3%) significantly outperforms Gaussian Naive Bayes (47.8%) for this dataset
Created detailed confusion matrices and performance visualizations for all models

## Technologies Used:

⊳ Python (scikit-learn, pandas, numpy)

⊳ Data visualization (matplotlib, seaborn)

⊳ Statistical analysis and model evaluation
