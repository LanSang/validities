[![Rahuldeb Das, Ph. D](https://miro.medium.com/fit/c/96/96/1*qM-uKgAjbo1xTG2wyOnqNA.jpeg)](https://rahuldeb-das.medium.com/?source=post_page-----f1f333022fb7--------------------------------)[Rahuldeb Das, Ph. D](https://rahuldeb-das.medium.com/?source=post_page-----f1f333022fb7--------------------------------)[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fb190dcd34e15&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fhow-data-scientists-build-machine-learning-models-in-real-life-f1f333022fb7&user=Rahuldeb+Das%2C+Ph.+D&userId=b190dcd34e15&source=post_page-b190dcd34e15----f1f333022fb7---------------------follow_byline-----------)Sep 17, 2020

·17 min read·Member-only

[Save](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Ff1f333022fb7&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fhow-data-scientists-build-machine-learning-models-in-real-life-f1f333022fb7&source=--------------------------bookmark_header-----------)# How Data Scientists Build Machine Learning Models in Real Life

## Steps for successful completion of a predictive model

![]()Photo by [Photos Hobby](https://unsplash.com/@photoshobby?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/robot-hand?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)The web is already flooded by data science and machine learning related resources nowadays. There are numerous blogs, websites, YouTube videos, and forums that are providing useful information regarding data science related topics. Now it has become tedious to choose the right material for any data science quest.

When I started my journey in data science, a few years back, I faced the same dilemma. But one thing I observed in most of these resources they are not complete. You have to traverse through a number of resources to get exhaustive information.

Also, I saw a lack of real-life perspective of the articles written on machine learning models. So I thought of writing a post on the overall picture of building a machine learning model for any use case in real-life.

To perform any data science project, a data scientist needs to go through several steps. Broadly these steps can be presented as:

1. Formulation of the data science problem from the given business problem

2. Data source exploration and data collection

3. Exploration of the variables (EDA)

4. Model building

5. Model evaluation

6. Model deployment

Steps 1 and 2 depend on the context of the problem. Step 6 depends more on the business requirement and the available infrastructure. And steps 2, 3, 4, and 5 are the sole responsibilities of a data scientist.

In this post, I shall discuss how to build a classification model end-to-end. I shall take you through the entire journey of a data scientist in any project that requires building a classification model. I shall try to organize this post in such a way that it can be readily adapted for similar situations.

I used a Random Forst model to describe the methods. Even if you use any other classifier, the execution will be pretty similar.

# 1. Formulation of a science problem from a given business problem

Usually, data science problems arise from business requirements. Business executives face various challenges in their process related to — product sales, profit margin, customer loyalty, procurement decisions, market share, and many other areas.

These business problems will come to you as few business questions or as some observations by the business executives which they would like to verify.

As a data scientist, it is your duty to convert those business problems into a data science problem and provide the answers meaningfully.

In this post, I shall consider a simple problem of social network advertisement. The data set provides some variables that indicate the profiles of the customers. Also, it indicates the customers who have purchased the product.

The aim of this assignment will be, based on the customer information, to predict who will purchase the product in the future.

So, as a data scientist, you need to understand that it is a classification problem with two classes — purchased and not-purchased.

# 2. Data source exploration and data collection

In real-life, data source exploration and data collection isn’t a simple task. In any organization, you will hardly find a single source where you will find all of your required data. Usually, you will find multiple disconnected sources of data and some of them will be hard to access because of infrastructure-related issues or because of restricted access.

Data collection from external sources also can be tricky because of cost issues and technical challenges.

In this post, I have limited scope to demonstrate these issues. The data set for this discussion ‘social-network-ads’ is downloaded from [here](https://www.kaggle.com/rakeshrau/social-network-ads).

# 3. Exploration of the variables (EDA)

Before jumping into Exploratory Data Analysis (EDA) you should always take a first look at the data. You should check few things — data volume, nature of different data coming from various sources, compatibility of the data sets, the mapping between them, data quality, data consistency — and most importantly the meaning of each variable and their business implications.

Now it’s time to get the hands dirty with python codes using “social-network-ads” data. Since I have used single data set to keep this discussion simple, I have limited scope to illustrate all the aspects of the first look at the data I mentioned here.

The whole code can be executed in a jupyter notebook or any other python IDE of your choice. We will require several python libraries to complete this classification exercise. I shall first mention all the packages we need.

![]()It is always a good idea to check your current working directory. If required change it to your preferred one.

![]()## First look at the data

Have a first look at your data that will be used to build the model. You will know how many variables you are dealing with and what those variables represent.

![]()This is a small data set with only four hundred observations and five variables. Out of them, the “User ID” will not contribute to model development.

You should check for blank spaces in variable names. If you find any such cases, change the variable names. Blank spaces in variable names cause problems in the scripts. In this data, “User ID” had a blank space, and I changed it to “UserID”.

## The data types of the variables

Check the data type of each variable you are working with. The most common issues that arise in any data is with the date variable. I saw most of the time the date variables become “object” data type. Make sure you have converted it to date format. My current data does not contain any date-variable. Also, sometimes numerical variables become “object” types when some of their values contain characters or if some of them have missing values.

![]()## Splitting the data into train, validation, and test set

Before you process your data, split it into train, validation, and test set. Your model should only see the train set to train itself. The validation set should be only used to tune the parameters of the model by checking its performance on the validation set. The test set is used to check the performance of the model on the unseen data.

All the statistical techniques you will use to process your train set should be used to process the validation and the test set. Also, the values of the statistics, you have estimated from the train set, should be used for the validation set and the test set.

For example, if you have normalized a variable X of the train set by mean ***m***and standard deviation ***s****,* the same values should be used to normalize X in the validation set and the test set.

Now, the size of the train, validation, and test set depends on the available data volume. 80–10–10 or 70–20–10 are commonly used percentages of splitting train, validation, and test set when the data set is not large. But, if you have enough data, like millions, then keeping 2% or 1% or even 0.5% is good enough for the validation or test set.

![]()From this data, I created a train set by taking 80% of the data. Kept 15% for the validation set and 5% for the test set.

## Distribution of the variables

Now it’s time to explore the train set and to understand the variables in hand.

A summary statistics of the variables will be helpful to understand their nature. You will have a rough idea about their distributions like — the range, whether they are skewed in nature, frequently appeared categories, etc.

![]()In this data, the gender distribution is dominated by the females. The customer’s ages vary from 18 to 60 with an average of 38.

Visualizations always help in understanding variables in greater depth.

![]()A significant amount of customers are aged around 40. A large segment of customers falls in the lower salary buckets. As expected, the number of customers purchased in much lower than the total number of customers.

Checking the extent of the class imbalance is always a good idea for classification problems.

![]()In the train set, the ratio of purchased vs not-purchased is 38:62. So, the class imbalance is not that significant here.

## Missing values and outliers

Missing values is a sure (almost) phenomenon in real-file data. There are various techniques to deal with missing data — imputation by mean or median for a numeric variable, imputation by mode for a categorical variable, K- Nearest-Neighbors (KNN), regression, etc. Each of them works depending on the context.

In the current industry scenario, if some variable is present in your data, there can be two situations. Either you will have enough values of the variable or there will be no values at all. I hardly see a scenario in between.

There are reasons for it. Organizations understood the importance of building processes and infrastructure to store data from different business operations. If they find some information crucial and there is a way to record it, they will store it properly. You will get enough information about it. But sometimes it becomes difficult to record a particular kind of information because of human bias or because of technical challenges. In this case, you will hardly get any information.

So, I personally try out the deletion of missing values if I have enough data. If a variable has a significant amount of missing values, then dropping the variable may be a good idea. I only try imputation techniques when it is absolutely necessary.

Another frequently observed characteristic of real-life data is the presence of outliers. You can use upper and lower whiskers to determine outliers. Sometimes people treat lower 2.5 percent and upper 2.5 percent data as outliers. You need to check if they are really outliers before taking any action on them.

You can cap the outliers with some estimated upper and lower boundaries from the variables.

![]()In this data set, there are no missing values. As the response variable in this data is categorical in nature, the concept of outliers is not suitable here.

## Feature creation

For most machine learning problems feature creation is a mandatory exercise. Sometimes the data available for model building does not contain enough variables. The available variables may not have sufficient explanatory power to boost the capability of the model. The data we are dealing with has only three variables — age, salary, and gender.

From these three variables, it will be difficult to build a model that will have enough predictive power. There may exist certain other factors that influence purchase decisions. Now, as we don’t have other information about the customers, we can use these variables judiciously to extract maximum possible explanatory power. For this, we need to create new variables (features) from the existing ones.

There may exist another situation where we will have enough variables, but none of them showing adequate explanatory power. In that case, we need to create additional features form the original variables. Also, we may need to combine some variables intelligently to create new ones.

![]()![]()Here, customers are aged between 18 to 60. Instead of using age as variables, if we can identify the age buckets in which customers have different purchase pattern, it will have more explanatory power in determining whether a customer is going to purchase. Once we have identified the age buckets, we can form dummy variables for those buckets and use them as features.

In this histogram, we see that the distribution of ages among the customers who have purchased differs from the customers who haven’t. The red rectangles, which represent the number of customers who have purchased, are higher in lower to middle age buckets. But the blue rectangles are higher for the high age buckets, which indicates the chance of not-purchased is more for higher age groups.

![]()The understanding from the above histogram led to generate a new variable “age\_group” that contains the age buckets instead of actual variable values. It will help us build new dummy variables for each age bucket.

![]()The same applies to the variable “EstimatedSalary” too. The salary of the customers varies from 15000 to 150000. I divided the range into nine buckets. Here you may have to experiment on how many buckets you should form. The target is to bring out an adequate number of buckets that differentiates the salary distribution between the purchased and not-purchased customers.

![]()The variable “salary\_group” is formed based on the pattern observed in the histogram.

![]()The distribution of gender does not differ significantly over customers’ purchased status. You must have noticed that female customers are slightly more inclined towards purchasing the products.

Once we explored all the variables in the data set, it’s time to finalize the features for the classification model. The features you will create for the train set, has to be exactly repeated for the validation set and the test set.

![]()Thus we have created all the features and dummy variables for the model. I dropped the original variables, keeping only the dummies. While creating dummy variables I dropped one dummy variable from each group to avoid the dummy variable trap.

When we create dummy variables for any categorical variable, a dummy is created from each category. The Linear combination of all the dummies from a variable is always 1. As a result, they will be perfectly correlated with the intercept of the model. This is called the dummy variable trap. We avoid this by dropping one dummy for each categorical variable.

![]()![]()It is always a good idea to check the correlation structure of the variables. Multicollinearity makes it difficult to understand the significance of the features in the model.

Correlation among the created features does not seem to be very strong in our case.

![]()And the train set is finally ready for model building.

# 4. Model building

Before we train the model, we need the validation data to be ready for model validation. The same methods needed to apply to the validation set that we used for the train set.

At the same time, we can prepare the test data too and keep it for future use.

![]()We created similar age buckets and salary buckets as we did for the train set. One thing you must check that all the classes of the target variable should be present in the validation set. If not, repeat the train-validation-test split.

![]()We have created the same features for the validation set and the test set.

There are several algorithms for dealing with classification problems. It is not very convenient to know beforehand which model will perform better. We always try several models and compare their performances. In real-life scenarios, performance parameters can be prediction accuracy, execution time, and resource consumption.

![]()Here I have used a Random Forest model as a classifier. Random Forest builds several decision trees by sampling features from the train set. Each of these trees classifies the observations. Random Forest combines these decisions and extracts the most likely one. This is method is called bagging.

![]()I have used default parameters to build the model. You can further optimize the classifier using the parameters like — *n\_estimators, max\_depth, min\_samples\_split,* min\_samples\_leaf, etc.

Save your model as a pickle file for future use. You should save the models with proper version names so that you can distinguish them when you will revisit them.

![]()I saved the model in my work directory and then loaded it again as I am using a single notebook.

# 5. Model evaluation

We arrived at a point where we have to answer a few questions like — How good the model is? Does it match our expectations? If not, what to do?

![]()To check the model, I have used the validation data set. The target classes of the validation set have been predicted. To judge how good the model is, we need to use some metrics of judgment.

The confusion matrix is a good way to represent the model performance. It shows the counts of positive and negative classes in the actual data and predicted results. Here positive class means the class with the label “Purchased” which is denoted by 1.

![]()![]()The above function provides a way to represent the confusion matrix with nice visualization. The function can visualize the confusion matrix with normalization (percentage figures) or without normalization (counts).

![]()This matrix represents the true label and predicted label with their counts. For 17 observations out of 19, the true and predicted labels are the same for the class 1. That means, out of 19 customers who have purchased the model can predict 17. The same for the class not-purchased is 37 out of 41.

To make it more concise, we have metrics like — precision, recall, F1-Score, accuracy, etc. For the classification models with imbalance class (the distribution of classes is not uniform), precision and recall are the matrics we rely on. The higher the measures are, the better the model is.

Precision is calculated by the ratio of two values. The number of customers for whom the model has predicted as “purchased”. And the number of customers who actually have purchased the product.

Recall expresses — among the customers who have actually purchased, how many of them have been correctly identified by the model.

Now, it is difficult to maximize precision and recall together. F1-Score is a measure that saves us from this situation. It is the harmonic mean of precision and recall. It helps us to keeps a balance between them.

![]()The model algorithm does not provide the target classes directly. It provides the probability of belonging to each class. If the probability of positive class is more than 0.5 then it is labeled as 1 otherwise 0.

This threshold value of probability can be optimized. We can check among all the thresholds which one provides the best classification result. It can be done by the precision-recall curve.

![]()So, instead of predicting the classes directly, I have extracted from the model the probabilities for each observation of the validation set. Using the precision-recall curve, the best threshold of probability has been found as 0.332714.

![]()The graph visualizes the best threshold in the precision-recall curve. It optimizes both precisions and recalls for the predictions.

There are several other methods of model evaluation and parameter tuning. I could not get into all those to keep the discussion simple.

Model training and evaluation are recursive processes. You need to revisit the training and evaluation number of times to take it to a satisfactory level. Every time you need to tune the parameters of the model if the evaluation process does not reveal satisfactory results. I avoided this part in this article.

Now, it time to check how the model performs on the unseen test data. It will resemble how the model is going to perform if it is deployed into a real-life application.

## Model evaluation on the test set

Before using the model for prediction on the test set, you must check the shape of the test set. Ensure that the number of features present in the test set is equal to the number in the train set.

![]()In our case, three features were missing in the test set. Those are the dummy variables created from the estimated salary. As those salary buckets were absent in the test set, I inserted the dummies with zeros for them.

![]()![]()I used the threshold probability, estimated in the validation set, to predict for the observation in the test set.

![]()The confusion matrix shows that all the customers with the “Purchased” label have been predicted correctly. So, the recall value is 1.

![]()The F1-Score for the set is 0.85. I would say that the model is providing us a decent performance. And we achieved that with a pretty straightforward and simple approach.

An 85% F1-Score could be an excellent performance in many situations. However, the required accuracy from a model depends on various factors.

# 6. Model deployment

Once you are satisfied with your model performance, you should check it with the business executives. You need to have a detailed discussion about the implication of your results and if it aligns with the business understandings.

Also, you need to confirm with business executives about the desired accuracy level. Decisions have to be made on deployment strategy, frequency of model revision, mode of delivery of the output, etc.

It may happen that your model output will be consumed by other applications or even it might go to the business people in the form of a CSV file.

The way I represented the code in this article is more of a discrete manner. In real-life situations, we prefer to segment the script in different blocks and to use classes and functions to organize them.

Also, a separate script module is required to be prepared for the inference of the model. This script will fetch the data from a particular data storage, draw inference on the data, and save the output in a specified output location.

You will need a scheduler for the model to run after a specific interval. If other applications are depending on the output of this model, you need to synchronize them in the right order.

It is really hard to bring all the aspects of the machine learning projects in a single article. I tried my best to cover most of them. I might have missed some facts to mention here. But I believe I have been able to bring a summary of the entire journey in front of you.

Data science is an emerging field. Many aspirants are joining the data science industry in the pursuit of becoming a data scientist. I hope this article will help them get a fair idea about the steps a data science project involves.

**You can download the notebook from** [**here**](https://github.com/rahuldeb-das/classification-model/blob/master/Classification_model_example.ipynb)**.**

**References:**

1. <https://machinelearningmastery.com/roc-curves-and-precision-recall-curves-for-imbalanced-classification/>

2. <https://stackoverflow.com/questions/19233771/sklearn-plot-confusion-matrix-with-labels/48018785>

Thank you for reading my article. If you liked this article, you might like my other articles. Here are some of them.

[## How to Learn New Programming Language With No Books and Tutorials

### A tested recipe for fast learning

medium.com](https://medium.com/swlh/how-to-learn-new-programming-language-with-no-books-and-tutorials-862e8cf77d8f)[## How To Set Up Your System for Object Detection Models

### You should start from the end to do it right at your first attempt

towardsdatascience.com](/how-to-set-up-your-system-for-object-detection-models-2e0726212c4e)