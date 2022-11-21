[![Radoslaw Białowąs](https://miro.medium.com/fit/c/96/96/1*aeGAWUcoGvpXOCfINLBP3g.png)](https://medium.com/@radoslaw.bialowas?source=post_page-----28ce74bfc732--------------------------------)[Radoslaw Białowąs](https://medium.com/@radoslaw.bialowas?source=post_page-----28ce74bfc732--------------------------------)[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Ffd194204a239&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fmachine-learning-in-production-why-is-it-so-difficult-28ce74bfc732&user=Radoslaw+Bia%C5%82ow%C4%85s&userId=fd194204a239&source=post_page-fd194204a239----28ce74bfc732---------------------follow_byline-----------)Dec 3, 2021

·10 min read·Member-only

[Save](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F28ce74bfc732&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fmachine-learning-in-production-why-is-it-so-difficult-28ce74bfc732&source=--------------------------bookmark_header-----------)## [Notes from Industry](https://towardsdatascience.com/tagged/notes-from-industry)

# Machine Learning in Production: Why Is It So Hard and So Many Fail?

## Did you struggle to deploy and maintain your models? Most companies do and here is why

![]()Jupyter notebook is not a production solution ([source](https://www.reddit.com/r/mlops/comments/o8w2e4/you_know_the_deal_if_you_dont_post_content_ill/?utm_source=share&utm_medium=ios_app&utm_name=iossmf))According to a [collective paper](https://valohai.com/assets/files/practical-mlops-ebook.pdf) analyzing the development of machine learning in more than 300 organizations, these projects are some of the biggest challenges for companies. Other [research](https://www.ibm.com/analytics/au/en/technology/data-science/download/Forrester_Wave_for_Multi-Modal_PAML_Solutions_Sep2018.pdf) also shows that data scientists regularly complain that their models are only sometimes or never delivered into production.

What is the reason for the difficulties causing a wave of disappointment and forgotten projects? Let’s consider what has changed. In a classic IT project, the code version determines the software version. In machine learning projects, the version of the model is defined by the version of the code and the version of the data. Is it possible that introducing a few tables into the equation has had such a drastic effect on the complexity, and therefore success, of projects?

Reacting to code change has resulted in the development of DevOps specializations and hundreds of competing services, more or less facilitating continuous integration and continuous delivery. A project with machine learning, on the other hand, is about **reacting to changes in code and in data**, which at least squares difficulty, as I’m going to prove to you in this article.

# Because the feedback loop is longer

Working with data brings entirely new challenges. While software can generally be developed locally along with an immediate feedback loop on how a new line of code affects the end result. You write a test, check that only the green lights are on, and move on. In machine learning, the feedback loop starts at the same place, but may end in a few hours when you’re done training the model.

Even if you’re working on a dataset that isn’t large, and your model doesn’t require a bunch of graphics cards, you’ll probably be doomed to wait a few hours while you tune hyperparamters. What’s more, the training has to take place cyclically anyway (more on this later in this article), so there is an additional process to be transferred to a remote environment.

Another limitation of working on a local machine is the size of the dataset. To fill the hard drive of even a few years old laptop with tabular data (and there are most such projects with machine learning), the dataset would have to have billions of rows with hundreds of columns. However, we have projects using audio, image and videos. While it is possible to experiment and develop a model on a slice of the dataset, which is common practice, the final evaluation is done on the entire dataset.

Moreover, there is a growing voice in the ML community not to perform experiments on a local machine, even if it is possible because ultimately the training process has to land in the cloud anyway. The sooner it gets there, the better.

# Version code, data and models

No one can imagine a commercial project without a version control system anymore. Thanks to it, we can conveniently collaborate and go back in time. Since it is the version of the code that creates the version of the software, with a version control system we can build any variant of the application at any time. This is not the case with machine learning.

First of all, the result of the work is not code, but a model. This one, in turn, results from the version of the code that creates and trains the model, and the data it uses. Therefore, if you want to have the same time machine when you develop projects with machine learning, you need to version the code, the data, and ideally the models as well.

![]()A version of code and data create a model version ([source](https://valohai.com/assets/files/practical-mlops-ebook.pdf))**Hey, wait for a second. Have you been reading for a while, do you like this article? Don't hesitate to clap and follow. It takes only 2 seconds to help. Done? Thanks!**

# Why should I version models, not just the data?

You have created a new model and delivered it into production. Everything works well, but only for a while. Perhaps the model misbehaves on the new data, or it is too complex, making it harder to handle more traffic. You need to undo the changes. What will be the effect of this if you don’t version the models? Do you need to train new models on a previous version of the code and data? How long will this take: 5 minutes or 2 days? Even if less than a quarter of an hour, what if problems arise while you are training the model?

Model versioning is an insurance policy for which you pay a monthly installment in the form of a bill for cloud storage services. The cost depends on the number of versions you want to store and the size of the model. Let’s estimate its cost. Suppose you are working on a mature project that versioned as many as 1,000 deep machine learning models, each weighing 500 MB. The monthly contribution is about $23.

# Test data at least as well as the model

It’s worthwhile to rise to the surface sometimes and discover the obvious, rather than drowning in detail all the time. You will probably agree that the pace of reading is the pace of looking. You can’t read faster than you move your eyeballs. In the context of ML, it is obvious that the model will only be as good as the data used to train it. Although this is a truism, more than once at the sound of this (seemingly) cliché I have noticed a twinkle in the eye of the person I was talking to. What’s the moral of this? **Test the data at least as well as the model.**

The data we feed into a model has come a long way. It has probably visited many places in the ecosystem, and during that journey, it has been cared for sometimes better and sometimes worse. We, on the other hand, come to draw conclusions from these weary wanderers. Moreover, we don’t know what data will come to us in the future. We can and should automate testing it. Importantly, data testing should be consistent for training and during live prediction. It is supposed to show errors and failures that may happen to the original producers in the future.

The problem is that while the model can predict from faulty data, the question is when this behavior will be caught. It doesn’t matter to the model whether the house has 3 or minus 8 bedrooms. However, not all tests are so obvious. For example, if the expected data is text in English, the test would be to make sure that the most frequent words are “the”, “a”. If other words appear more often, it may mean that we are not dealing with the expected language.

## **Testing models**

Although most species of models are deterministic (the same input always produces the same output), they are also more difficult to test because their essence is to dynamically discover important features of constantly changing data. Models need to be refreshed regularly because there is more data all the time and the nature of the data is constantly changing. What does this mean in practice? That a future property valuation model will suggest a different price for the same house.

When measuring the quality of a model, the fit to the data is checked. If it is too poor, we simply have a poor model. It then cannot draw good conclusions from the data it was given to learn, let alone even future data it has never seen — it is called underfit. The opposite situation, that is, when the fit is too strong, is not good either. The model performs decently on the data it was given to training, but it cannot make good inferences on data it has not seen before — it is called overfit. Too weak and too strong fits are fuses from the perspective of the entire dataset and is measured at the training stage. These two values are among the most important when it comes to model evaluation. **The problem lies in testing and detecting disturbing behavior for specific cases.** The solution is monitoring.

# Reacting in real-time

![]()Unexpected problems in production meme (image by author)Defining troubling behavior or instabilities in a model and writing tests to detect them before deployment to production is a standard package. But detecting anomalies in production, especially when the model is responding in real-time, is a different cup of tea because the model will encounter data it has never seen before and must respond immediately. Again, the problem may lie in the data itself, which is flowing in from another part of the system and unattended as opposed to training data, or in the nature of the model, which is simply not ready for the new data. Moreover, a single prediction that deviates exceptionally may nevertheless be correct. So how do we monitor the model to utilize its potential while still responding to its degenerate behavior?

In a classical application, we monitor both hardware (RAM, CPU) usage and the application itself by measuring the number of requests per second. Based on these metrics, we can react in real-time, for example by scaling the application or detecting suspicious behavior resulting from both errors in the system and well-wishing users by blocking a given IP address.

Monitoring the model also involves observing its behavior over time. The behavior, or the predictions it returns, is compared to a baseline value. For example, for a model that predicts real estate prices, the average house price in the training set was £400,000, and for the last 100 predictions returned yesterday, the average value is £500,000, which would set off alarm bells. In other words, **model monitoring is comparing the statistical attributes of the input data and the predictions against the statistical attributes during supervised learning.**

Even if the prediction is correct (i.e., the average house price is maintained at the correct level for a long period of time), it is also important what influenced that particular prediction. Going back to the topic of real estate, let’s assume that our model predicted a house price of £400,000. However, it turned out that this decision was influenced more by the garage area instead of the number of bedrooms. There was no house in the training data that has a 120 sq. ft. garage. After all, that can’t happen in production!

The area of interpreting and explaining model decisions is a specialization in itself but is associated primarily with justifying model behavior during model tuning and evaluation rather than as a tool for monitoring live production systems.

# Continuous delivery and continuous training

While it is very satisfying to work on code that functions in a vacuum, the reality is that only software that is delivered to production can feed the budget.

Continuous Integration and Continuous Delivery are a set of practices designed to automate deployments and day-to-day code work so that every change reaches the remote environment without additional friction. In a textbook application, the only reason to build and deploy a new version is a change in the code. This one can be triggered by introducing new functionality or fixing a bug. We change the code, stand in front of the production gates, show the green stickers collected from test runner, and if no other color is entangled, the application begins to live in the real world. You don’t have to deploy the same version of code if the database it supports grows twice as large. When a new collection of china appears in the online store, there is no reason to compile the code that is responsible for serving cups to our e-commerce.

With models and this time is different. Models get old, and after a while they become useless. This time — for a change — it’s through data. Data in which new patterns emerge, trends change, and products arrive. The model that recommends movies will not recommend those that it has not seen at the stage of training (not in all implementations of recommender systems), and the navigation supported by AI will not suggest a route for a new section of the highway. The solution to this problem is cyclic, regular model training. As you can see, it’s not just the code changes that cause new models to be trained. This means that you need to create and maintain an additional process.

# Summary

Is all this really necessary if you want to do machine learning? No, it’s necessary to increase your chances of getting to the finish line and to minimize your maintenance costs. A new specialization of MLOps araises to solve the problems described above so that statistics and neural network specialists can focus on their work.

While not every ML project needs to interpret live predictions, while almost every is more complex than a traditional application, most should version the data and implement a continuous training process.

It is a good idea to realize this before starting the project. Jupyter notebook is not a production solution. By answering the important questions before we start, we can avoid burying months of work or at least guard against mistakes, saving us days or weeks.

# **Call to action**

What is your point of view? How is your ML project doing? Is it in production? Let me know in the comments section.

Do not hesitate to clap and follow. This is also a way of telling me you see things the same way.

*The original Polish version was published on* [*https://radekbialowas.pl*](https://radekbialowas.pl/uczenie-maszynowe-na-produkcji-dlaczego-to-takie-trudne/)

[Some rights reserved](http://creativecommons.org/licenses/by/4.0/)

