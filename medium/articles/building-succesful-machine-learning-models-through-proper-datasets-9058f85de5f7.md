[![Praveen Nellihela](https://miro.medium.com/fit/c/96/96/1*gmHZuvYu8lZgmQYl7S_P6w.jpeg)](https://medium.com/@praveennellihela?source=post_page-----9058f85de5f7--------------------------------)[Praveen Nellihela](https://medium.com/@praveennellihela?source=post_page-----9058f85de5f7--------------------------------)[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F359bd37be9f3&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fbuilding-succesful-machine-learning-models-through-proper-datasets-9058f85de5f7&user=Praveen+Nellihela&userId=359bd37be9f3&source=post_page-359bd37be9f3----9058f85de5f7---------------------follow_byline-----------)Sep 6

·13 min read·Member-only

[Save](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F9058f85de5f7&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fbuilding-succesful-machine-learning-models-through-proper-datasets-9058f85de5f7&source=--------------------------bookmark_header-----------)# How to Build a Proper Dataset

## Because bad data leads to bad models

![]()Photo by [Tabea Schimpf](https://unsplash.com/@tabeaschimpf?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/map?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)# Why does a proper dataset matter?

Fundamentally, a machine learning model is something that configures itself to predict an outcome, based on the training data. If you feed the model training data that does not represent the data the model will face when actually being used, you cannot expect anything but flawed predictions. This article will give you insights on creating a good dataset that is able to represent data the model will face when it is being used in the real world.

But before we start building great datasets, first, we must understand the **components** of a dataset (classes, labels, features, and feature vectors). Then, we will move on to **data preparation**. This is where we **handle missing features** and **scale features**. Next, we discuss why and how we should **partition the dataset.** Finally, we will look at why we should have a **final look** at our data and how to find problems that could still exist, such as **outliers** and **mislabeled** **data**.

Let’s get started.

# Components of a dataset

## Classes and Labels

In classification tasks, the input features are mapped to discrete output variables. For example, by considering the input data, the model predicts whether the output is a “dog”, “cat”, “horse” etc. These output variables are defined as **classes**. An identifier called a **label** is given to each input in the training data to represent these classes.

![]()How a classification model classifies input data into classes.To a model, the inputs are just numbers. A model does not care or know the distinction between an image of a dog or a voice sample. This also applies to the labels. As a result, classes can be represented in any way we want. In practice, we often use integer values starting with 0 to map the labels to their respective class. An example is shown below.


```
┌───────┬────────────┐  
│ Label │ Class │  
├───────┼────────────┤  
│ 0 │ person │  
│ 1 │ bicycle │  
│ 2 │ car │  
│ 3 │ motorcycle │  
│ 4 │ airplane │  
│ 5 │ bus │  
│ 6 │ train │  
│ 7 │ truck │  
│ 8 │ boat │  
│ 9 │ traffic │  
└───────┴────────────┘  
The table is an exerpt from the [COCO dataset](https://cocodataset.org/#home), showing its classes and labels.
```
In the above example, every input that represents a bicycle is labeled 1 and every input representing a boat is labeled 8. You may now wonder, what exactly are we labeling? What is actually the input of a person or a boat? This is where the all-important **features** come in.

## Features and Feature Vectors

Features are the inputs used by the model to produce a label as output. These are numbers, as mentioned above, and represent different things depending on the task. For example, in the [iris dataset](https://www.kaggle.com/datasets/uciml/iris) which contains data about three species of Iris flowers, the **features** are the dimensions of the sepals and petals.


```
The **four available features** in the iris dataset for the iris flower species known as Setosa are shown below.   
(only the first 5 rows of the dataset are shown)  **Sepal.Length Sepal.Width Petal.Length Petal.Width** Species   
1 5.1 3.5 1.4 0.2 setosa  
2 4.9 3.0 1.4 0.2 setosa  
3 4.7 3.2 1.3 0.2 setosa  
4 4.6 3.1 1.5 0.2 setosa  
5 5.0 3.6 1.4 0.2 setosa
```

> Note: The ***classes*** in the above dataset are the different species of Iris flowers, **Setosa**, **Virginica**, and **Versicolor** with ***labels*** 0, 1 and 2 given to these classes respectively.
> 
> 

Thus, features are simply the numbers that we will use as inputs to the machine learning model. When the machine learning model is trained, the model learns relationships between the input features and the output labels. We make an assumption here that there actually is a relationship between the features and the labels. In cases where there are no relationships to learn, the model may fail to train.

Once training is concluded, the learned relationships are used to predict output labels of input **feature vectors** (sets of features given as input) with **unknown** class labels. If the model continues to make bad predictions, a reason might be that the features used to train the model were not adequate enough to identify a good relationship. This is why choosing the correct features matters at the start of any machine learning project. More information on choosing good features and why bad features should be ignored can be found in my post below.

[## Feature Selection: Choosing the Right Features for Your Machine Learning Algorithm

### Sometimes, less is more

towardsdatascience.com](/feature-selection-choosing-the-right-features-for-your-machine-learning-algorithm-379bda9f3e05)Features can be of different types, such as floating point numbers, integers, ordinal values (natural, ordered categories where the difference between values are not always the same), and categorical values (where numbers are used as codes, e.g male=0 and female=1).


> Recap: features are numbers that represent something we know, that can help build a relationship to the output label. Take a look at some rows of the Iris dataset below, now showing all components, features class and labels. Each row containing all four features is one feature vector.
> 
> 


```
 Features   
 \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Class Label  
 | | | |  
**Sepal.Length Sepal.Width Petal.Length Petal.Width Species**   
 5.1 3.5 1.4 0.2 setosa 0  
 7.1 3.0 5.9 2.1 virginica 1  
 4.7 3.2 1.3 0.2 setosa 0  
 6.5 3.0 5.8 2.2 virginica 1  
 6.9 3.1 4.9 1.5 versicolor 2
```
# Preparing the data

Now that we have a good grip on what a dataset contains, there are two important things to consider before we start building our great dataset:

* How to handle missing feature values
* Feature Scaling

## Dealing with missing features

You may come across cases where there are missing features in your data, for example, you may have forgotten to make a measurement, or some data for a sample has been corrupted. Most machine learning models do not have the ability to accept missing data, so we must fill in these values with some data.

There are two approaches you can take in such scenarios. You could either add a value that falls far outside the feature’s range with the basis that the model will pay less significance to it or, use the mean value of the features over the data set in place of the missing value.

In the example below, some features are missing, indicated by blank spaces.


```
**Sepal.Length Sepal.Width Petal.Length Petal.Width Label**   
 5.1 3.5 1.4 0  
 7.1 5.9 2.1 1  
 4.7 3.2 0.2 0  
 3.0 5.8 2.2 1  
 6.9 3.1 4.9 1.5 2
```
The mean for all the features is calculated and shown in the table below


```
**Sepal.Length Sepal.Width Petal.Length Petal.Width**   
 5.95 3.2 4.5 1.5 
```
By replacing the missing values with the mean values, we can obtain a dataset that can be used to train a model. This is not better than having real data but should be good enough to use when data is missing. An alternative if the dataset is large enough is to use the mode (most occurring value) by identifying it through a generated histogram.

## Feature scaling

Oftentimes, feature vectors that are made of different features can have multiple different ranges. For example, while a set of features will be between 0 and 1, another feature can have values between 0 to 100,000. Another will be between -100 to 100. As a result, some features will dominate others because of their larger range, which causes the model to suffer in accuracy. To overcome this problem, **feature scaling** is used.

To understand this concept as well as to reinforce what we learned in the above sections, we will create a synthetic data set and look at it.


```
┌────────┬─────┬──────┬──────┬───────────┬────────┬───────┐  
│ **Sample** │ **f1** │ **f2** │  **f3**  │ **f4** │  **f5** │ **Label** │  
├────────┼─────┼──────┼──────┼───────────┼────────┼───────┤  
│ 0 │ 30 │ 3494 │ 6042 │ 0.000892 │ 0.4422 │ 0 │  
│ 1 │ 17 │ 6220 │ 7081 │ 0.0003064 │ 0.5731 │ 1 │  
│ 2 │ ***16 │ 3490 │ 1605 │ 0.0002371 │ 0.23*** │ 0 │  
│ 3 │ 5 │ 9498 │ 7650 │ 0.0008715 │ 0.8401 │ 1 │  
│ 4 │ 48 │ 8521 │ 6680 │ 0.0003957 │ 0.3221 │ 1 │  
│ 5 │ 64 │ 2887 │ 6073 │ 0.0005087 │ 0.6635 │ 1 │  
│ 6 │ 94 │ 6953 │ 7970 │ 0.0005284 │ 0.9112 │ 0 │  
│ 7 │ 39 │ 6837 │ 9967 │ 0.0004239 │ 0.4788 │ 1 │  
│ 8 │ 85 │ 9377 │ 4953 │ 0.0003521 │ 0.5061 │ 0 │  
│ 9 │ 46 │ 4597 │ 2337 │ 0.0004158 │ 0.8139 │ 0 │  
└────────┴─────┴──────┴──────┴───────────┴────────┴───────┘  
The first column is the sample number.   
Each row of a sample is an input to the model, given as a **feature vector.**A feature vector is represented by 5 **features** for each sample  
- feature set is {f1, f2, f3, f4, f5}  
- Typically the full feature vector is refered to with the uppercase letter (F).  
- Feature vector for sample 3 can be refered to as F3.   
One feature vector is highlighted in bold for sample 2 in the table.  
The last column is the **label**. There are two **classes**, represented by the labels 0 and 1.Notice how samples start with 0. This is because we work with Python and Python is 0 indexed.
```
Now to the scaling part. You can see in our synthetic data table that different features have different ranges. Let's look at all the features and consider their minimum, maximum, average, and range values.


```
┌──────────┬───────────┬───────────┬──────────┬────────────┐  
│ Feature │ Range │ Minimum │ Maximum │ Average │  
├──────────┼───────────┼───────────┼──────────┼────────────┤  
│ f1 │ 89 │ 5 │ 94 │ 44.4 │  
│ f2 │ 6611 │ 2887 │ 9498 │ 6187.4 │  
│ f3 │ 8362 │ 1605 │ 9967 │ 6035.8 │  
│ f4 │ 0.0006549 │ 0.0002371 │ 0.000892 │ 0.00049316 │  
│ f5 │ 0.6812 │ 0.23 │ 0.9112 │ 0.5781 │  
└──────────┴───────────┴───────────┴──────────┴────────────┘Notice how the features have widely varying ranges. This means that we should carry out feature scaling.
```
Let’s look at two ways of scaling. First, we consider the easiest method, known as **mean centering**. This is done by subtracting the average value of the feature over the whole dataset. Average over the whole set simply means the sum of each value divided by the total number of values.

For f1, the average value is 44.4. Therefore, to center f1, we replace each sample value belonging to the f1 feature with the value-44.4. For sample 0, it's 30–44.4, for sample 2, it's 17–44.4, and so on. Doing this for all values, we get the table below.


```
┌────────┬───────┬─────────┬─────────┬─────────────┬─────────┐  
│ Sample │ f1 │ f2 │ f3 │ f4 │ f5 │  
├────────┼───────┼─────────┼─────────┼─────────────┼─────────┤  
│ 0 │ -14.4 │ -2693.4 │ 6.2 │ 0.00039884 │ -0.1359 │  
│ 1 │ -27.4 │ 32.6 │ 1045.2 │ -0.00018676 │ -0.005 │  
│ 2 │ -28.4 │ -2697.4 │ -4430.8 │ -0.00025606 │ -0.3481 │  
│ 3 │ -39.4 │ 3310.6 │ 1614.2 │ 0.00037834 │ 0.262 │  
│ 4 │ 3.6 │ 2333.6 │ 644.2 │ -0.00009746 │ -0.256 │  
│ 5 │ 19.6 │ -3300.4 │ 37.2 │ 0.00001554 │ 0.0854 │  
│ 6 │ 49.6 │ 765.6 │ 1934.2 │ 0.00003524 │ 0.3331 │  
│ 7 │ -5.4 │ 649.6 │ 3931.2 │ -0.00006926 │ -0.0993 │  
│ 8 │ 40.6 │ 3189.6 │ -1082.8 │ -0.00014106 │ -0.072 │  
│ 9 │ 1.6 │ -1590.4 │ -3698.8 │ -0.00007736 │ 0.2358 │  
└────────┴───────┴─────────┴─────────┴─────────────┴─────────┘  
The synthetic data set we created, after mean centering.   
Note that now, the average value for each feature is 0. In other words the center for each feature is 0 and values can be above or below this center.
```
Mean centering can be sufficient for feature scaling. But we can go a bit further. Notice how the ranges are not the same even if we conduct mean centering. By performing what's called **normalization**, or **standardization,** we can change the spread of data around the mean (standard deviation) to be in the same range. In other words, we change the standard deviation to 1. Because we also perform mean centering, when normalizing data, the features will have a mean of 0 in addition to the standard deviation being 1.

This can be done simply, if we have a feature value x, by replacing x with value z where:

![]()The equation [to calculate standard score.](https://en.wikipedia.org/wiki/Standard_score)where: *μ* is the [mean](https://en.wikipedia.org/wiki/Mean) and *σ* is the [standard deviation](https://en.wikipedia.org/wiki/Standard_deviation) of each feature across  
the dataset.

Fortunately, since we are working with Python and Numpy, this can be done by a single line of code.


```
# Assuming the data is stored in the numpy array F  
**F = (F - F.mean(axis=0)) / F.std(axis=0)**
```
This will provide the following table:


```
┌────────┬───────┬───────┬───────┬───────┬───────┐  
│ Sample │ f1 │ f2 │ f3 │ f4 │ f5 │  
├────────┼───────┼───────┼───────┼───────┼───────┤  
│ 0 │ -0.51 │ -1.14 │ 0 │ 1.89 │ -0.63 │  
│ 1 │ -0.98 │ 0.01 │ 0.43 │ -0.89 │ -0.02 │  
│ 2 │ -1.01 │ -1.14 │ -1.84 │ -1.21 │ -1.62 │  
│ 3 │ -1.41 │ 1.4 │ 0.67 │ 1.79 │ 1.22 │  
│ 4 │ 0.13 │ 0.99 │ 0.27 │ -0.46 │ -1.19 │  
│ 5 │ 0.7 │ -1.4 │ 0.02 │ 0.07 │ 0.4 │  
│ 6 │ 1.77 │ 0.32 │ 0.8 │ 0.17 │ 1.55 │  
│ 7 │ -0.19 │ 0.28 │ 1.64 │ -0.33 │ -0.46 │  
│ 8 │ 1.45 │ 1.35 │ -0.45 │ -0.67 │ -0.33 │  
│ 9 │ 0.06 │ -0.67 │ -1.54 │ -0.37 │ 1.1 │  
└────────┴───────┴───────┴───────┴───────┴───────┘  
Now we see that all features are similar to each other, compared to our original dataset. 
```
# Partitioning the dataset

Since we followed the steps above, we now have a good set of feature vectors. But wait! There is something we need to do before we can train our model with it. We should not use the entire dataset to train our model, because we need to split the dataset into two, or ideally three, subsets. These subsets are called **training data**, **validation data,** and **test data**.

The **training data** is used to train the model.

The **test data** is used to evaluate the accuracy and performance of the trained model. It is important that the model *never* sees this data during training because then, we will be testing the model on the data it has already seen.

The **validation data** is not needed for every model. However, it can help when the models are deep learning models. This dataset is used similarly to how the test data is used during the training process. It tells us how well the training process is going and provides information about when to stop training and whether the model is suitable for the data.

In summary, **training** and **validation** **data** are used to build the model. The **test data** is held back to evaluate the model.

## How much data should be put in each set?

It is considered standard practice to split 90% of the set into training and 5% each for validation and test data according to some literature, while others suggest 70% for training and 15% each for validation and test for smaller datasets or 80% for training and 10% for validation and test.

It is important to preserve the prior probabilities in the dataset. If a class exists in real-world cases with a chance of 20%, this should be reflected in our dataset as well. This should also extend to the subsets that we create. How can we do this? There are two ways:

* Partitioning by class
* Random sampling

## Partitioning by class

This method can be used when you are working with small datasets. First, we determine how many samples are present for each class. Next, for each class, we set aside the chosen percentages and merge everything together.

For example, assume we have 500 samples, with 400 belonging to class 0 and 100 from class 1. We want to do a 90/5/5 split (90% training data, 5% test, and 5% validation). This means we randomly select 360 samples from class 0 and 90 samples from class 1 to create the training set. From the remaining unused 40 samples of class 0, 20 randomly selected samples will go to validation data and 20 to test data. From the remaining unused 10 samples of class 1, 5 each will go into validation and test datasets.

## Random sampling

If we have sufficient data, we do not need to be very precise and follow the above method. Instead, we can randomize the entire dataset and split our data according to the necessary percentages.

But what if we have a small dataset? We can use methods such as **k-fold cross-validation** to ensure that issues with this method, such as imbalances in train and test data can be mitigated. Have a look at my post below if you would like to learn more about this method.

[## What is K-fold Cross Validation?

### Let’s say that you have trained a machine learning model. Now, you need to find out how well this model performs. Is it…

medium.com](https://medium.com/@praveennellihela/what-is-k-fold-cross-validation-5a7bb241d82f)# Having a final look at our data

Now, we have performed a lot of operations to ensure that our data set is sufficiently good to train a model. We made sure that it has good features, that there are no missing features, and that the features are normalized. We also partitioned the dataset into subsets in a proper manner.

The final important step is to have one last look at the data to make sure everything makes sense. This allows us to identify any **mislabeled data** and **missing or outlier data**. These errors can be identified by loading the data into a spreadsheet or for larger sets, using Python scripts to summarize the data. We should look at values such as the mean, median, and standard deviation as well as maximum and minimum values to see if there are any unusual data. We can also generate [boxplots](https://en.wikipedia.org/wiki/Box_plot) to identify outliers.

![]()An example boxplot for [Michelson experiment](https://en.wikipedia.org/wiki/Michelson%E2%80%93Morley_experiment#Michelson_experiment_(1881)) By User:Schutz — Own work, [Public Domain](https://commons.wikimedia.org/w/index.php?curid=1501411),After performing all the above steps, we can be confident that our dataset is a proper dataset that can help a model train well and in turn, produce accurate and reliable predictions on real-world data. It might seem like a lot of effort, but always remember, if you feed your machine learning models garbage, they will only output garbage. You should always ensure that your dataset is sufficiently good enough.

# Summary

In this post, we looked at why a good dataset is important. We then looked at what makes a dataset by looking at the components such as classes and features. We went over data preparation and how to handle missing features and scale features. Next, we discussed why and how we should partition the dataset**.** Finally, we looked at why we should have afinal look at our data and how to find problems that could still exist, such as outliers and mislabeled data.

If you found this post useful, consider [subscribing](https://medium.com/@praveennellihela/subscribe) to me and [joining medium](https://medium.com/@praveennellihela/membership). Your membership supports me and other writers you read directly.

Thank you for reading! See you in a future post.

