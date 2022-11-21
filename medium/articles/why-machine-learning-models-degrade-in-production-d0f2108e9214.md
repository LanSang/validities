[![Alexandre Gonfalonieri](https://miro.medium.com/fit/c/96/96/1*jSd-IskscJuNIBfXi0dQyw.jpeg)](https://alexandregonfalonieri.medium.com/?source=post_page-----d0f2108e9214--------------------------------)[Alexandre Gonfalonieri](https://alexandregonfalonieri.medium.com/?source=post_page-----d0f2108e9214--------------------------------)[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F94354d6ab94d&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fwhy-machine-learning-models-degrade-in-production-d0f2108e9214&user=Alexandre+Gonfalonieri&userId=94354d6ab94d&source=post_page-94354d6ab94d----d0f2108e9214---------------------follow_byline-----------)Jul 25, 2019
<person role="AI consultant">
https://alexandregonfalonieri.medium.com/
</person>
·7 min read·Member-only

[Save](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fd0f2108e9214&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fwhy-machine-learning-models-degrade-in-production-d0f2108e9214&source=--------------------------bookmark_header-----------)# Why Machine Learning Models Degrade In Production

![]()After several failed ML projects due to unexpected ML degradation, I wanted to share my experience in ML models degradation. Indeed, there is a lot of hype around model creation and development phase, as opposed to model maintenance.

Assuming that a Machine Learning solution will work perfectly without maintenance once in production is a faulty assumption and represents the **most common mistake of companies taking their first artificial intelligence (AI) products to market.**


> *The moment you put a model in production, it starts degrading.*
> 
> 

# Why Do ML Models Degrade With Time?

As you may already know, data is the most crucial component of a successful ML system. Having a relevant data set that provides you with accurate predictions is a great start, **but how long will that data continue to provide accurate predictions?**

<quote label="data">In all ML projects, it is key to predict how your data is going to change over time.</quote> In some projects, we underestimated this step and it became hard to deliver high accuracy. In my opinion, as soon as you feel confident with your project after the PoC stage, a plan should be put in place for keeping your models updated.

Indeed, your model’s accuracy will be at its best until you start using it. This phenomenon is called concept drift, and while it’s been heavily studied in academia for the past two decades, it’s still often ignored in industry best practices.


> ***Concept drift:*** *means that the statistical properties of the target variable, which the model is trying to predict, change over time in unforeseen ways. This causes problems because the predictions become less accurate as time passes.*
> 
> 

![]()[Source](http://xplordat.com/2019/04/25/concept-drift-and-model-decay-in-machine-learning/?source=post_page---------------------------)The key is that, in contrast to a calculator, your ML system does interact with the real world. If you’re using ML to predict demand and pricing for your store, you’d better consider this week’s weather, the calendar and what your competitors are doing.

In the case of concept drift, our interpretation of the data changes with time even while the general distribution of the data does not. This causes the end-user to interpret the model predictions as having deteriorated over time for the same/similar data. Both data and concept can simultaneously drift as well, further vexing the matters…

I noticed, that models which are dependent on human behavior may be particularly prone to degradation. **Obviously, the risk can be anticipated based on the nature of your project. In most cases, a regular schedule of model review and retrain must be developed.**

Furthermore, most models are only able to capture patterns which reflect the training data they’ve seen. A good model captures the essential pieces of this data and ignores the non-essential. This creates **generalization** performance, but there are limits to the degree any model can prepare for this.


> ***Generalization:*** *refers to your model’s ability to adapt properly to new, previously unseen data, drawn from the same distribution as the one used to create the model. It is strongly related to the concept of overfitting. If your model is overfitted then it will not generalize well.*
> 
> 

![]()[Source](https://qph.fs.quoracdn.net/main-qimg-17ec84ff3f63f77f6b368f0eb6ef1890.webp?source=post_page---------------------------)The best test of generalization performance is to see how a model performs on real-world data over a long period of time. There are at least two major elements of this process.

# How to prevent model degradation?

It might sound obvious but it is crucial to monitor your ML performance after deployment. If monitoring all features sounds like a time-consuming task, we can monitor a few critical features whose change in data distribution might skew the model results terribly. I strongly recommend you to create a strategy (by identifying the right elements) for this process before reaching production.


> *Model monitoring is a continuous process.*
> 
> 

If you observe degraded model performance, then it’s time for restructuring the model design. The tricky part isn’t about refreshing the model and creating a retrained model but rather **thinking of additional features that might improve the model’s performance and make it more solid and accurate.**

Once the above steps have been completed, it is time to recreate the model with the new or modified set of features and model parameters. At this point, the goal is to identify an optimal model that delivers the best accuracy, which generalizes well to some data drifts.

I noticed that in some cases, a re-creation of models doesn’t improve model performance. In these situations, analyzing examples that the model got wrong and looking for trends that are outside your current feature set can help in identifying new features. **Creation of new features based on this knowledge can give models new experiences to learn.**

## Manual Learning

One solution that we frequently use to maintain models with **new data** is to train and deploy our models using the same process we used to build our models in the first place. **We call this Manual Learning.** As you can imagine this process can be time-consuming. How often do we retrain our models? Weekly? Daily? The answer depends on your ML application.

**It can happen that, as we are manually retraining models we may discover a new algorithm or a different set of features that provide improved accuracy.** Actually, it’s probably a good idea to review your process on a regular basis. As I mentioned earlier, you may find a different algorithm or a new set of features that improves your predictions, and this isn’t necessarily something a continuous learning system is good at.


> *Perhaps you can update the model each month or each year with the data collected from the prior period.*
> 
> 

This may also involve back-testing the model in order to select a suitable amount of historical data to include when re-fitting the static model.

## Weight Data

Another solution could be to weight data. Indeed, some algorithms allow you to weigh the importance of input data.

It could be interesting to use a weighting system that is inversely proportional to the age of the data such that more attention is paid to the most recent data (higher weight) and less attention is paid to the least recent data (smaller weight).

# Continuous learning

My favorite approach is to have an automated system that can continuously evaluate and retrain models. The benefit of a continuous learning system is that it can be completely automated.

![]()In general, sensible model surveillance combined with a well thought out schedule of model checks is crucial to keeping a production model accurate. Prioritizing checks on the key variables and setting up warnings for when a change has taken place will ensure that you are never caught by a surprise by a change to the environment that robs your model of its efficacy.

In the case of input variables where the data points have a high degree of independence, control charts, as used in **Statistical Process Control**, could be used to detect changes to the process.

# Handling model drift

I insist on this point but your ML success also depends on the way you plan for the maintenance of your trained models. In several projects, I realized how business leaders inexperienced with the way models work may not anticipate this need.


> *A productionized model includes monitoring and maintenance.*
> 
> 

Model performance on fresh data sets should be evaluated regularly. These performance traces should be visualized and compared regularly so that you can identify when it’s time to intervene. Several metrics for evaluating ML performance exist.

![]()Confusion Matrix**The reasons for model degradation can be discovered and modeled explicitly.** Recurrent temporal effects can be studied, understood, and exploited. This can be a project for the data science team to tackle once a model has gathered sufficient performance metrics. Well, assuming you’ve been tracking them.

A procedure for regularly considering performance metrics and triggering retraining or rebuilding of models is also necessary as without it you’ll be able to see the loss in performance but have no system in place for resolving it.

# Investment & Team

Beyond the tech aspect, I strongly recommend you to keep your best data scientists and engineers on the project after it’s in production. In contrast to classic software projects where, after deployment, your operations team handles it and engineers move on to build the next big thing, a lot of the technical challenge in ML and AI systems is keeping them accurate.

You will need to invest in order to maintain the accuracy of the machine learning products and services that your customers use. **This means that there’s a higher marginal cost to operating ML products compared to traditional software.**

# Maintenance Costs

To maintain high-quality models, algorithms should ideally be retrained with each data delivery. On the other hand, to optimize costs, it should be done as rarely as possible.

Obviously, certain machine learning development practices incur more technical debt, hence entail more future maintenance than others. Machine-learning-specific development debt-risk factors are diverse. They include the myriad probabilistic variables, data dependencies, recursive feedback loops, pipeline processes, configuration settings, and other factors that exacerbate the unpredictability of machine learning algorithm performance.

The more these complexities pile up, the more difficult it is to do the root-cause analyses necessary for effective maintenance.

You won’t be able to fully automate your way out of that maintenance burden. Under any scenario, tending to machine learning models demands the close scrutiny, critical thinking, and manual effort that only a highly trained data scientist can provide.

