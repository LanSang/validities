[![Satyam Kumar](https://miro.medium.com/fit/c/96/96/1*q9jnqYZgM2JU8G3Q8_hWdQ.jpeg)](https://satyam-kumar.medium.com/?source=post_page-----2fbb36985108--------------------------------)[Satyam Kumar](https://satyam-kumar.medium.com/?source=post_page-----2fbb36985108--------------------------------)[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F3d8bf96a415f&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fessential-guide-to-machine-learning-model-monitoring-in-production-2fbb36985108&user=Satyam+Kumar&userId=3d8bf96a415f&source=post_page-3d8bf96a415f----2fbb36985108---------------------follow_byline-----------)Dec 6, 2021

·4 min read·Member-only

[Save](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F2fbb36985108&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fessential-guide-to-machine-learning-model-monitoring-in-production-2fbb36985108&source=--------------------------bookmark_header-----------)# Essential guide to Machine Learning Model Monitoring in Production

## Techniques to detect data drift

![]()Image by [Mediamodifier](https://pixabay.com/users/mediamodifier-1567646/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=3078546) from [Pixabay](https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=3078546)Model Monitoring is an important component of the end-to-end data science model development pipeline. The robustness of the model not only depends upon the training of the feature engineered data but also depends on how well the model is monitored after deployment.

Typically a machine learning model's performance degrades over time, so it's essential to detect the cause of the decrease in performance of the model. The main cause of the same can be drift in the independent or/and dependent features which may violate the model’s assumption and distribution about the data.

In this article, we will discuss various techniques to detect the data drift independent or independent features in the production inference data.

# Why Model Monitoring is Required?

![]()(Image by Author), Model training, validation, and monitoring workflowThere are various reasons why the performance of the model degrades over time:

* Inference Model Performance < Baseline Model Performance
* Inference Data Distribution is different from Baseline Data Distribution
* Change in Business KPI

The above mentioned are the key reasons why a model performance degrades over time. The deployed model needs to be monitored after deployment to measure the model performance and data distribution. After the cause of the model decaying is decided, the existing model is retrained with the updated dataset.

# How to perform Model Monitoring?

The actual target class label for the inference data is mostly not present upfront. So it’s difficult to measure the model performance using the standard evaluation metrics such as precision, recall, accuracy, log-loss, etc.

Sometimes it takes time till the actual target class label is made available. But one can also measure the robustness of the model by observing the data distribution. There are various techniques to measure the data drift in the independent and dependent features.

# Measure drift of Independent Features:

There are various aspects to monitor the drift in the independent features.

## 1. Monitor Distribution of each feature:

If we observe a change in the distribution of engineered or raw features of the inference data, we can expect a decline in model performance. Some of the popular statistical techniques to measure the deviation are:

* KL (Kullback Leibler) Divergence Test
* KS (Kolmogorov Smirnov) Test
* Chi-square Test

## 2. Monitor the Statistical Features:

One needs to monitor the statistical features of the inference and baseline data, to observe the divergence in the dataset. Some of the statistical features are:

* Range of possible values (quantiles, mean, max, min)
* Number of missing or NULL values
* Histogram distribution of numerical features
* Distinct Values of Categorical features

## 3. Monitor the distribution of multivariate features:

Machine learning models develop some interactions between the features to make predictions. If the pattern or distribution between the features is changed then it may lead to a decrease in model performance. The technique to detect the multivariate feature distribution is:

* Cramer’s Phi Test

# Measure drift of Dependent Features:

The dependent feature (target label) for the inference target class maybe not be present upfront in production. Once the dependent feature is present, there are various techniques to measure the drift and come to a conclusion of whether the model performance has deteriorated or not.

## 1. Distribution of Target Class:

For the classification task, the target class label is categorical in nature. The idea is to compare the distribution of target class labels between the inference data and base data.

For regression tasks, the histogram plot, or statistical feature of the continuous target label can be used to measure the drift in the data.

## 2. Monitor Inference Model Performance:

Once the actual target class label is made available, then the model drift can be detected by evaluating and comparing the performance of the model on standard metrics. If the model metrics show less than expected numbers, the model needs to be re-trained.

# Conclusion:

In this article, we have discussed various techniques to detect the drift in the inference dataset, after deployment of the model in production. Model drift may result in deterioration of the model performance over time. So it’s important to monitor the performance of the model after productionizing it.

# References:

[1] Vivek Kumar YouTube Playlist: <https://www.youtube.com/playlist?list=PLmpREe1kbYUk348hS7W2EzUyWtgCSN54J>

*Loved the article? Become a* [*Medium member*](https://satyam-kumar.medium.com/membership) *to continue learning without limits. I’ll receive a small portion of your membership fee if you use the following link, with no extra cost to you.*

[## Join Medium with my referral link - Satyam Kumar

### As a Medium member, a portion of your membership fee goes to writers you read, and you get full access to every story…

satyam-kumar.medium.com](https://satyam-kumar.medium.com/membership)
> Thank You for Reading
> 
> 

