[![Praatibh Surana](https://miro.medium.com/fit/c/96/96/1*I889HaYiJYfmhSIfeBRDWg.png)](https://praatibhsurana.medium.com/?source=post_page-----2247bbca8a61--------------------------------)[Praatibh Surana](https://praatibhsurana.medium.com/?source=post_page-----2247bbca8a61--------------------------------)[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Ff711d3de8cba&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fan-introduction-to-machine-learning-engineering-for-production-part-1-2247bbca8a61&user=Praatibh+Surana&userId=f711d3de8cba&source=post_page-f711d3de8cba----2247bbca8a61---------------------follow_byline-----------)Jun 15, 2021

·4 min read[Save](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F2247bbca8a61&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fan-introduction-to-machine-learning-engineering-for-production-part-1-2247bbca8a61&source=--------------------------bookmark_header-----------)![Image credit : Canva]()(Image by Author from [Canva](https://www.canva.com/))# An Introduction to Machine Learning Engineering for Production /MLOps — Concept and Data drifts

## A brief introduction to data drift, concept drift, and challenges faced in MLOps and some best practices to tackle them.

It’s safe to say that a majority of us starting out with Machine Learning/Deep Learning are able to easily develop basic models and also achieve decent results. However, speaking from personal experience, we rarely have any sort of exposure to the deployment of our models, especially if we’ve had little to no experience with frameworks like Flask, Django, etc.

Many machine learning courses go over the basics of algorithms, code snippets, and libraries needed to tackle certain types of problems. However, I had not particularly found any courses specifically for production-related topics. That was until DeepLearning.ai released their [specialization](https://www.coursera.org/programs/manipal-education-tguaf/browse?currentTab=CATALOG&productId=UTg2EeldEeq3QQ5dqWzZRQ&productType=s12n&query=MLOps&showMiniModal=true) on this very topic! This article (or series of articles probably) is essentially a summary of what the [first course](https://www.coursera.org/learn/introduction-to-machine-learning-in-production) in this specialization talks about along with a mixture of my opinions on this subject.

Every ML/DL project can roughly be divided into 4 phases - namely **scoping**, **data**, **modeling**, **deployment**. Now, before we look at each phase (probably in subsequent articles) and what the best practices might be, it is important to understand the challenges faced in a real-world setup when it comes to the production of scalable models.

![]()**Phases of Project Development in ML** (Image by Author)Two scenarios that often occur after a model has been deployed are **concept drift** and **data drift.**

* Concept drift refers to a *change in relationships* between input data, ‘x’ and output data ‘y’ over a period of time. **Eg-** Consider a housing price prediction model. In an anomalous situation such as the pandemic, there is a sudden change in real estate prices and hence, the model may not make accurate predictions anymore. A home that costs 50 lakh INR in a normal scenario might now cost 75 lakh INR for the same set and quantity of features like bedrooms, ACs, area in square feet, etc.
</quote>

![]()**Concept Drift** (Image by Author)* Data drift refers to a *change in the input features*. Mathematically, it is a change in the distribution of variables that causes their meaning to change. **Eg-** Consider a model that handles bank transactions. Usually, there must be some sort of transaction limit and anything above a certain threshold might cause the credit cards to get blocked for safety purposes. However again, consider the situation of the pandemic where there have been instances of increased spending (or hoarding of essentials) due to limited availability of essentials. This would cause a normal ML model to block everyone’s cards to restrict transactions. Hence the model is not performing as desired due to a change in the normal number of transactions (input features).

![]()**Data Drift** (Image by Author)Apart from these challenges faced post-deployment, some key questions that need to be asked before deploying your model are -

* Is the model going to be used in real-time or not?
* Is the internet going to be accessible to the device where the model is being deployed?
* Is the model going to be deployed on an edge device or cloud?
* What is the kind of compute resources that are needed?

If these questions can be answered, it makes your life as a Machine Learning Engineer a lot easier and there is lesser time lost in making changes midway through the project. Surprisingly, I also found some of these questions useful while starting out with any research-oriented projects.

Now, because I’ve told you about the challenges faced, it only makes sense to discuss possible feasible solutions to tackle them. These can be roughly summarized as follows -

* Retrain your model using all available data, both before and after there is a change/drift.
* It can be helpful to fine-tune model hyperparameters to try and adjust to the new patterns that your model might be encountering. Also, this is relatively easier than the data-related approach. One advantage is that model deployment does NOT have to be a one-time process, rather it is **iterative** in nature. Every few weeks/months, you can roll out an improved version of your model and this is almost always the case as now your model has more experience with real-world data.
* Lastly, if you feel that you have acquired enough new data to work with, drop the old data. The fresher the data, the easier you will find it to train your model to fit the problem statement (in most cases).

There you go! That was a brief introduction to MLOps and there is a lot more to cover but I think this is a good place to end this article. In the following articles, we will discuss more in detail the 4 phases of developing and deploying a model and further dive into techniques used to ensure smooth operation.

If you’ve made it this far and want to learn more about MLOps, feel free to check out my [**GitHub repository**](https://github.com/praatibhsurana/Machine-Learning-Engineering-for-Production). I will keep updating it with relevant material and Jupyter notebooks!

REFERENCES

1. <https://machinelearningmastery.com/gentle-introduction-concept-drift-machine-learning/>
2. <https://www.explorium.ai/blog/understanding-and-handling-data-and-concept-drift/>
3. [https://towardsdatascience.com/machine-learning-in-production-why-you-should-care-about-data-and-concept-drift-d96d0bc907fb0](/machine-learning-in-production-why-you-should-care-about-data-and-concept-drift-d96d0bc907fb0)
4. <https://youtu.be/06-AZXmwHjo>
5. <https://www.coursera.org/learn/introduction-to-machine-learning-in-production>
