# distance_classification
MLPR Test for lab 5 (Tanmay made us do it)


Report

What are the common distance metrics used in distance-based classification algorithms? Ans-: 
Euclidean Distance: The geometrical distance between two points. 
Manhattan Distance: The sum of absolute differences between coordinates. 
Chebyshev Distance: The greatest absolute difference between coordinates in any dimension. 
Minkowski Distance: A generalization of these distances controlled by a parameter pp.

What are some real-world applications of distance-based classification algorithms? 
Image Recognition: Classifying images based on pixel data, such as in facial recognition. 
Recommendation Systems: Identifying similar users or products, as seen in platforms like Netflix and Amazon. 
Text Categorization: Organizing documents by topic using text embeddings.

Explain various distance metrics. 
Euclidean distance measures the direct straight-line distance between points and is widely used. 
Manhattan distance is more suitable for grid-like data structures and plays a key role in L1-regularized models. 
Minkowski distance serves as a flexible generalization of both Euclidean and Manhattan distances, allowing for adjustable metrics. 
Chebyshev distance focuses on the largest absolute difference across dimensions, making it particularly useful in scenarios where maximum deviation matters.
Mahalanobis distance considers correlations between features, making it valuable for analyzing multivariate data.

What is the role of cross validation in model performance? 
Cross-validation helps evaluate a model’s performance by splitting the dataset into multiple training and validation sets, reducing bias and variance. It ensures the model generalizes well to unseen data by preventing overfitting or underfitting.

Explain variance and bias in terms of KNN? Ans :- In K-Nearest Neighbors (KNN), a low value of K (e.g., K=1) leads to high variance, as the model closely follows training data and is sensitive to noise. 
A high K value increases bias, as the model oversimplifies patterns by averaging over many neighbors, missing finer details.
