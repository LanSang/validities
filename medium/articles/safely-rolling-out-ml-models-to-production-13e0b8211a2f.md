[![Oren Razon](https://miro.medium.com/fit/c/96/96/1*jczpDqjdHefdyJuvsuqAXw.jpeg)](https://medium.com/@orenrazon?source=post_page-----13e0b8211a2f--------------------------------)[Oren Razon](https://medium.com/@orenrazon?source=post_page-----13e0b8211a2f--------------------------------)[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F10e98e64e8b6&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fsafely-rolling-out-ml-models-to-production-13e0b8211a2f&user=Oren+Razon&userId=10e98e64e8b6&source=post_page-10e98e64e8b6----13e0b8211a2f---------------------follow_byline-----------)Nov 6, 2020

·13 min read[Save](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F13e0b8211a2f&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fsafely-rolling-out-ml-models-to-production-13e0b8211a2f&source=--------------------------bookmark_header-----------)## [Making Sense of Big Data](https://towardsdatascience.com/tagged/making-sense-of-big-data)

# Safely Rolling Out ML Models To Production

## Best CI/CD practices for the painless deployment of machine learning models and versions

![]()Orchestrating different (non ML) instruments. Source: UnsplashFor any data scientist, the day you roll out your model’s new version to production is a day of mixed feelings. On the one hand, you are releasing a new version that is geared towards yielding better results and making a greater impact; on the other, this is a rather scary and tense time. Your new shiny version may contain flaws that you will only be able to detect after they have had a negative impact.


> *ML is as complex as orchestrating different instruments*
> 
> 

Replacing or publishing a new version to production touches upon the core decision making logic of your business process. With AI adoption rising, the necessity to automatically publish and update models is becoming a common and frequent task, which makes it a top concern for data science teams.

**In this article, I will review what makes the rollout of a new version so sensitive, what precautions are required, and how to leverage monitoring to optimize your Continuous Integration (CI) pipeline, as well as your Continuous Deployment (CD) one to safely achieve your goals.**

ML systems are composed of multiple moving and independent parts of software that need to work in tune with each other:

![]()The “ML orchestra”. Image by author**Training pipeline**: Includes all processing steps that leverage your historical dataset to produce a working model: data pre-processing, such as embeddings, scaling, feature engineering, feature selection or dimensionality reduction, hyperparameter tuning, and performance evaluation using cross-validation or hold out sets.

* **Model registry**: A deployed model can take various forms: specific object serialization such as pickle, or cross-technology serialization formats such as PMML. Usually, these files are kept in a registry-based on shared file storage (S3, GCS,…), in a standard version repository (git) or in a dedicated service such as [MLFlow model registry](https://mlflow.org/docs/latest/model-registry.html).
* **Serving layer**: This is the actual prediction service. Such layers can be embedded together with the business logic of the application that rely on the model predictions or can be separated to act as a prediction service decoupled from the business processes it supports. In both cases, the core functionality is to retrieve the relevant predictions according to new incoming requests, using models from the model registry. Such a service can work in a batch or stream manner.
* **Label collection**: A process that collects the ground truth for supervised learning cases. It can be done manually, automatically, or using a mixed approach such as active learning.
* **Monitoring**: A centralized service that monitors the entire process and health of your live models, from the quality of inputs that get into the serving and up to the collected labels to detect drift, biases, or integrity issues.

Given this relatively high-level and complex orchestration, many things can get out of sync and lead us to deploy an underperforming model. Some of the most common culprits are:

## 1. Lack of automation

Most organizations are still manually updating their models. Whether it is the training pipeline or parts of it, such as features selection, or the delivery and promotion of the newly created model by the serving layer; doing so manually can lead to errors and unnecessary overheads.

## 2. A multiplicity of stakeholders

As a plurality of stakeholders and experts are involved, there are more handovers and thus more room for misunderstandings and integration issues. While the data scientists design the flows, the ML Engineers are usually doing the coding — and without being fully aligned (e.g. using different scaling methods), this may result in having unintentional behaviors.

## 3. Hyper-dynamism of real-life data

The empirical research is done in an offline lab environment, with historical datasets, and by simulating hold out testings. Needless to say, these environments are very different from the production one, for which only parts of the data are actually available. This might lead to data leakages or wrong assumptions that lead to bad performance, bias, or problematic code behavior once the model is in production and needs to serve live data streams. For instance, the newly deployed version’s inability to handle new values in a categorical feature while pre-processing it into an embedded vector during the inference phase.

## 4. Silent failures of ML models vs. traditional IT monitoring

Monitoring ML is more complex than monitoring traditional software — the fact that the entire system is working doesn’t mean it actually does what it should do. Without proper dedicated ml monitoring service in place, such failures can go “silently” and “under the radar” until the business damage was already done. You can read more on [what does it take to monitor ml models](/monitor-stop-being-a-blind-data-scientist-ac915286075f) and [whether you should build it yourself](https://www.superwise.ai/resources/thinking-about-building-your-own-ml-monitoring-solution-answer-these-questions-first).

# CIֿֿֿ/CD for ML in production

CI practices are about frequently testing the code bases of each of the software units, and the integrity of the different software artifacts working together by using unit/integration/system tests.


> *A new model version should be considered and treated as a software artifact*
> 
> 

The creation of a new model requires a set of unit and integration tests to ensure that the new “candidate” model is valid before it is committed into the model registry. **But in the ML realms, CI is not only about testing and validating code and components, but also testing and validating data, data schemas, and model quality**. While the focus of CI is to maintain valid code bases and modules’ artifacts, before building new artifacts for each module, the CD process handles the phase of actually deploying the artifacts (in our case, the new model version) into production.

# Best Practices for the CI phase

Here are some of the main best practices for the CI phase that impact the safe rollout of model/new version implementations:

## Data validation

Models are retrained/produced using historical data. For the model to be relevant in production, the training data set should adequately represent the data distribution that currently appears in production. This will avoid selection bias or simply irrelevance. To do so, before even starting the training pipeline, the distribution of the training set should be tested to ensure that it is fit for the task. At this stage, the monitoring solution can be leveraged to provide detailed reports on the distributions of the last production cases, and by using data testing tools such as [deequ](https://github.com/awslabs/deequ) or [TDDA](https://github.com/tdda/tdda), this type of data verification constraints can be automatically added to the CI process.

![]()Extracting data distributions from production using the monitoring service and comparing them to your training dataset (image taken from superwise.ai system)## Model quality validation

When executing the training pipeline and before submitting the new model as a “candidate” model into the registry, ensure that the new training process undergoes a healthy fit verification.


> *Even if the training pipeline is fully automated, it should include a hold-out/cross-validation model evaluation step.*
> 
> 

Given the selected validation method, one should apply tests to validate that the fitted model convergence doesn’t indicate overfitting, i.e.: seeing a reduced loss on the training dataset, while it’s increasing on the validation set. The performance should also be above a certain minimal rate — based on a hardcoded threshold, naive model as a baseline, or calculated dynamically by leveraging the monitoring service and extracting the rates of the production model during the used validation set.

![]()Cross-validation evaluation setup example. Image by author## Test cases — Robustness for production data assumptions

Once the model quality validation phase is completed, one should perform integration tests to see how the serving layer integrates with the new version, and whether it successfully serves predictions for specific edge cases. For instance: handling null values in the features that could be nullable, handling new categorical levels in categorical features, working on different lengths of text for text inputs, or even working for different image size/resolution,… Here also, the examples can be synthesized manually or taken from the monitoring solution, whose capabilities include identifying and saving valid inputs with data integrity issues.

## Model stress test

Changing the model, or changing its pre-processing steps or packages could also impact the model’s operational performance. In many use cases such as real time-bidding increasing the latency of the model serving might impact dramatically the business. Therefore, as a final step in the model CI process, a stress test should be performed to measure the operational aspects, such as average response time. Such a metric can be evaluated relative to a business constraint or relative to the current production operational model latency, calculated by the monitoring solution.

# Best Practices for the CD phase

The CD phase is the process of actually deploying the code to replace the previous versions. In traditional software engineering, this is usually carried out through a “[Blue-green](https://martinfowler.com/bliki/BlueGreenDeployment.html)” or a “[canary](https://martinfowler.com/bliki/CanaryRelease.html)” deployment — a methodology for gradually rolling out releases. First, the change is deployed to a small subset of cases, usually rolling out gradually to a subset of servers. Once it is established that the functionality works well, the change is then rolled out to the rest of the servers.

**Applying it to ML models, the CD process should basically be a gradual one to validate the model correctness and quality on live data, using production systems, before letting it kick in and take real automated decisions.** Such evaluation is often called “online evaluation”, as opposed to the tests achieved during the CI phase which are based on historical datasets and may be considered to be “offline evaluation”.

![]()The full CI/CD model lifecycle. Image by authorSuch model online evaluation may involve a few basic strategies:

## Shadow evaluation

Shadow evaluation (or often called “Dark launch”) is a very intuitive and safe strategy. In shadow mode, the new model is added to the registry as a “candidate model”. Any new prediction request is inferred both by the model versions, the one that currently used in production, and the new candidate version in shadow mode.


> *In shadow mode the new version is tested using a new stream of production data, but only the predictions of the latest “production model” version are being used and returned to the user/business.*
> 
> 

With shadow mode, there is no risk of exposure until the new version is indeed approved and works as expected. The benefits of the shadow mode are twofold:

1. The performance of the new version is evaluated before it is “live”,
2. You ensure that the new version works well in the production pipelines

With this method, the monitoring service should persist through both sets of predictions — and continuously monitor both models until the new model is stable enough to be promoted as the new “production version”. Once the new version is ready, the monitoring service signals to the serving layer that it needs to upgrade the model version. Technically this “promotion” can be done by updating a tag of “latest” for the new version and making the serving layer always work with the “latest” model version tag (similar to the “latest” concept in docker images). Or by working with an explicit model version tag, but this will require the serving layer to always check first what is the latest production-ready version tag, and only then to reload the relevant version and use it to perform predictions.

![]()The monitoring service is responsible for deciding when to promote the shadow model. Image by author
> We should compare the new “shadow” version to the current latest production model, using statistical hypothesis
> 
> 

Such a test should verify that the performance of the new version has the required effect size, a.k.a: the difference between the two version performance metrics, under a specific statistical power, a.k.a.: the probability of correctly identifying an effect when there is one. For example: If the latest version had a precision level of 91% in the past week, the new candidate version must have a 0 or more effect size so the new precision rate will be 91% at least.


> *The overall performance level is not the only metric to look at*
> 
> 

Before promoting the model though, additional factors could be important to monitor: the performance stability, meaning determining the variance in the daily precision performance in our last example, or checking performance constraints for specific sub-population. E.g. the model must have a 95% precision level at least for our “VIP customers. When the label collection takes time or might be missing completely, other KPIs can be used to test the new model as a proxy for its quality — i.e.: in loan approval use cases, where such feedback loops might take longer than 3–6 months. In these cases, the level of correlation between the predictions of the two versions can be used, as a new version should have a relatively high level of correlation relative to its predecessor. Another option is to test the level of distribution shift in the production data relative to its training dataset to ensure that the new version was trained on a relevant dataset relative to the current production distribution.

Aside from all its benefits, shadow evaluation has limitations and is only partially practical. This is what we will analyze below, as well as review alternative solutions.

## A/B Evaluation

In many ML scenarios, the predictions of the model actually impact the surrounding environment it operates in. Let’s take a recommendation model responsible for ranking the top 5 movie suggestions to offer. In most cases, the label depends on whether or not the user indeed watched one of the movies suggested. Here, the model’s prediction impacted the user’s behavior, and therefore the collected data. If a candidate shadow model outputs 5 very different movies, the fact that the user doesn’t select them doesn’t necessarily mean that they were bad recommendations — only the fact that the model was in shadow mode, and didn’t take any real-life action, made it impossible for the user to actually see these movies. In this scenario, the performance success cannot be compared. This is when an online A/B test evaluation is required.

In an A/B setup, both the current latest version and the new candidate version, which may be referred to as model A / “control” group and model B / “treatment” group, are actually active in production. Each new request is routed to one of the models, according to a specific logic, and only the selected model is used for prediction.

![]()A/B Routing example. Image by authorThese evaluations can be carried out for a certain amount of time, predictions, or until the statistical hypothesis — whether the new version is at least as good as the previous one — is validated. Similar to the shadow strategy, the KPIs to test can be the performance, stability or some other proxy,…It is important to note though, that the monitoring service should be in charge of the management and evaluation of the A/B tests.


> *The success of this method highly depends on the ability to split the A/B test groups correctly and carefully.*
> 
> 

A good practice for it is to do a random sample for a specific portion to get the “treatment”, meaning the prediction from the new version. For example, with the movie recommendation use case, any new request should have X (e.g. 10%) chance to be served by the new model version, until the test is done. Usually, the exposure factor is relatively low, as this strategy actually “exposes” the new model even before the qualitative tests are completed.

Such A/B configuration can be generalized also to A/B/C/… setups — where multiple models are compared simultaneously. Keep in mind though that testing a few models together side-by-side can increase the chances for False-Positive outcome, due to the higher number of tests. Besides, given the fact that we are testing a smaller amount of samples in each group, the statistical power of “small effect size” is reduced, and therefore should be considered carefully.

# Multi-armed bandit

Multi-armed bandit (MAB) is actually a more “dynamic” kind of A/B test experimentation, but also a more complex one to measure and operate. It’s a classical reinforcement learning where one tries to “explore” (try a new model version) while “exploiting” and optimizing the defined performance KPI. Such configuration is based on the implementation of the exploration/exploitation tradeoff inside the monitoring service. The traffic is being dynamically allocated between the two (or more) versions, according to the collected performance KPI — or other proxies as described earlier.

In this situation, the new version is exposed to a certain amount of cases. The more it equals or surpasses the previous version, and based on its performance KPI, more and more traffic will be directed to it.

![]()Dynamic multi-arm bandit routing based on monitored results. Image by authorSuch configuration seems ideal, as we try to optimize the “exposure” dynamically while optimizing our main metric. However, it requires advanced monitoring and automation capabilities to implement the multi-armed bandit solution, and adjust the traffic dynamically based on its results. Especially given the difficulties related to the definition of one clear KPI to be exploited by the system — performance, stability,...

# The virtue of monitoring for safe rollouts

By looking at the examples used in traditional software and implementing that onto our own ML paradigm, CI/CD best practices, we learn that there are many steps to be taken to have a better “roll out day”. All of these strategies rely on a strong monitoring component to make the processes more data-driven.


> *Safely rolling out models is about monitoring the orchestration of all the pieces of the ML infrastructure together*
> 
> 

Below we can see the safe delivery of a new version (V2, marked as a blue dot), yielding an improved ROC AUC performance in production.

![]()Screenshot of model monitored by superwise.aiLooking beyond, the health of your models in production also requires a thorough, and data-driven retraining strategy. While, the CI/CD paradigms address the “what” and the “how” of new models roll-out, the “when” is covered by the CT (Continuous Training) paradigm. This will be the focus in the next post of my colleague [Or Itzahary](https://medium.com/u/4b1a8c1d089a?source=post_page-----fd90478f97fc--------------------------------), so stay tuned!


> *From CI/CD to CT (Continuous training). CT is a new property, unique to ML systems, that’s concerned with automatically retraining and serving the models*
> 
> 

I hope you find this article helpful. If you have any questions, feedback or if you want to brainstorm on the content of this article, please drop a comment here or reach out to me on [LinkedIn](https://www.linkedin.com/in/oren-razon/?originalSubdomain=il)

I would like to thank my fellow colleagues [Pearl Lieberman](https://medium.com/u/86c5e042163c?source=post_page-----fd90478f97fc--------------------------------), [Or Itzahary](https://medium.com/u/4b1a8c1d089a?source=post_page-----fd90478f97fc--------------------------------), and [Ori Cohen](https://medium.com/u/4dde5994e6c1?source=post_page-----fd90478f97fc--------------------------------) for their insightful comments and ideas

[*Oren Razon*](https://www.linkedin.com/in/oren-razon/) *is the co-founder and CTO of* [*superwise.ai*](https://www.superwise.ai/) *a company that empowers data science & operational teams with the visibility and control to scale their AI activities using an advanced ML monitoring platform. Oren is an experienced ML practitioner, leading and consulting for large scale ML activities at startups and enterprises in the last 15 years.*

*I’m always looking for an excuse to read, write, talk, and share ideas on MLOps topics.*

