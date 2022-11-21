[![Aparna Dhinakaran](https://miro.medium.com/fit/c/96/96/1*VbKXdndNnweCZQQa2TohWw.png)](https://aparnadhinak.medium.com/?source=post_page-----29e85e701688--------------------------------)[Aparna Dhinakaran](https://aparnadhinak.medium.com/?source=post_page-----29e85e701688--------------------------------)[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Ff32f85889f3a&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fwhat-is-ml-observability-29e85e701688&user=Aparna+Dhinakaran&userId=f32f85889f3a&source=post_page-f32f85889f3a----29e85e701688---------------------follow_byline-----------)May 27, 2021

·8 min read[Save](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F29e85e701688&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fwhat-is-ml-observability-29e85e701688&source=--------------------------bookmark_header-----------)## [Notes from Industry](https://towardsdatascience.com/tagged/notes-from-industry)

<person role="Startup founder">
	https://www.linkedin.com/in/aparnadhinakaran/
</person>

# What is ML Observability?

<quote label="deployment">
## Building machine learning proof of concepts in the lab is drastically different from making models that work in the real world.
</quote>

As more and more teams turn to machine learning to streamline their businesses or turn previously impractical technologies into reality, there has been a rising interest in tools and people who can help bring a model from the research lab into the customer’s hands. Google built TFX, Facebook built FBLearner, Uber built Michaelangelo, Airbnb built Bighead, and these systems have allowed these times to scale their MLOps.

Outside of these large tech companies, the truth is, building machine learning proof of concepts in the lab is drastically different from making models that work in the real world. Let’s start by taking a quick look at some things that can go wrong in applying a model to a real world problem.

# **What Can Go Wrong?**

1. **Training Serving Skew**

<quote label="data">
When deploying a model, there is a good chance that your model does not perform as well as it did when validating it offline. These handoffs to production don’t always go well, and is commonly referred to as training/serving skew.


One potential culprit is that the data your model was trained on is statistically different from the data you see in production. Another possibility is the feature transformation code is not consistent between your training environment and your production environment. This can be more common than one might think. Oftentimes, notebooks containing feature transformation code are passed around and changed without much version control, which can lead to confusion about exactly what kind of transformations were used to create features for the model. If the way that features are created is not consistent between the training and production environment, your model’s performance can take a big hit right out of the gate.
</quote>

![]()Training Serving Skew. Image by Author.**2. Changing Data Distributions**

<quote label="data">
In addition to this potential discrepancy between training and production data and feature transformations, it’s possible that the distribution of data that your model is exposed to changes over time, commonly referred to as data drift or feature drift. This drift can be gradual or can happen overnight and cause your model’s performance to degrade.
</quote>

![]()Changing Distributions. Image by Author.**3. Messy Data**

Another thing to watch out for by is the fidelity of your data sources. Things don’t stay constant like code. You’re dealing with data. In the research lab, thousands of hours often go into creating high quality data sets with minimal noise and accurate labels. In the real world you often have no such guarantee of quality or freshness. If you rely on external sources of data, you can be at the mercy of it’s reliability.

Check out this piece for more [failure modes](https://arize.com/the-models-shipped-what-could-possibly-go-wrong/) for ML models.

# **How Does Observability Help?**

ML Observability is the practice of obtaining a deep understanding into your model’s performance across all stages of the model development cycle: as it’s being built, once it’s been deployed, and long into its life in production.

Observability is the key difference between a team that flies blind after deploying a model and a team that can iterate and improve their models quickly.

1. **Time to Detection**

The first key goal of ML observability is about surfacing these problems to your in a timely manner. You can resolve a problem until you know about it, and you don’t want your customers to suffer for days or weeks until you recognize that something is up. Therefore, a good ML observability solution helps reduce the time that it takes to detect a problem in your model.

This can mean different things in different contexts. If you are building your model, a good observability tool might help a model builder find problems with their model quicker, facilitating a tighter iteration loop; however, in the context of a production scenario, an ML observability tool might monitor key performance metrics that can notify a model owner when something is going wrong.

**2. Time to Resolution**

Although detecting a problem is the first step, this is not where ML observability stops. Once a problem is detected, an observability tool needs to facilitate the resolution of the problem. The key mark of a good observability tool is how quickly a team can get to the root cause to resolve.

Going back to what we talked about previously, there are a number of ways a model’s performance can regress. A good ML observability solution needs to guide the model owner to the input data distribution, feature transformation, or model prediction expectation that changed and provide a course of resolution.

For example, if you see that your input features to your model have steadily drifted over time, and it’s leading your model to mispredict of a particular set of examples, an ML observability tool could notify you, recommend a way to augment your training sets, and prompt you to retrain your model.

![]()ML Engineer Lifecycle. Image by Author.# **How Can I Achieve ML Observability?**

![]()Evaluation Store. Image by Author.Now you might be thinking that ML observability sounds awesome, but how does my team actually go about achieving this? ML observability can be achieved through the application of an Evaluation Store. An Evaluation Store’s job is to help you validate models, debug issues with a model’s predictions, surface your worst performing slices of data, and give you recommendations about how and when to retrain your model.

To take a deeper dive into what the evaluation store does, let’s explore how the evaluation store fit’s into each piece of the ML model lifecycle.

**Pre-Launch Validation**

During the training and validation stage of model building, an Evaluation Store plays the key role of tracking a model’s performance for each defined slice in the training data. When the model’s performance changes significantly for a particular slice, or potentially a new interesting slice of data emerges from the testing results, an evaluation store’s job is to inform the model builder. In addition, during training and validation, the evaluation store should detect if the input data differs significantly from the production data to help avoid the training-production skew problem we alluded to before.

Moving onto model deployment, an evaluation store can also help you select which model is most appropriate to promote to production. By tracking the predictions that a model would have made in production for a set of candidate models, the evaluation store can compile results about which model would have performed best across various slices of data.

**Monitoring**

When the model is deployed to production, the evaluation store keeps track of all of the input features and output predictions to provide alerts when any of these distributions change significantly. On top of that, an evaluation store needs to keep track of the predictions and ground truth for each input example in production.

In some model applications, ground truth is readily available immediately after the model makes it’s prediction — think search results, the user clicks the most relevant link and you now know if the link you put on top really was the most relevant to the user.

However, in other scenarios ground truth can be delayed or missing entirely. An evaluation store’s job in these more tricky scenarios is to help teams keep track of proxy metrics that correlate with a model’s performance, and provide alerts to the model owner when the distribution in these proxy metrics shifts significantly.

**Root Cause**

After a problem is detected with the model in production, the evaluation store can surface which key distributions in input data, features, ground truth / proxy metrics have contributed to a change in the model’s performance. Since an evaluation store is keeping track of this model metadata all of the time, it can detect drifts over time for each of these distributions and call out the biggest contributing factors.

Having the ability to detect and classify a model regression into failure modes can help provide guidance for how a model owner should go about fixing the problem. For example, let’s imagine that you have a model that is attempting to predict which TV show to promote to a user to maximize the likelihood for them to watch the show. Unbeknownst to you, a large number of young users have started to use your product, and their preferences are not well reflected in the training data.

An evaluation store would be able to detect and surface a significant change in your model’s performance, and point you to a change in your input data and feature distributions. You could then drill into which features have changed most drastically and see that the distribution of the “age” feature has shifted to the younger side around the time of the model regression.

At this point, you can use your evaluation store to find examples of these new younger users, augment your training sets with these examples, and retrain your model to better take these new users into account.

**Improve Models**

As datasets get larger to power bigger models and problem spaces widen, one key role of an evaluation store is to surface slices of data where a model performs poorly. Armed with this insight of what opportunities exist to improve a model’s performance, a model builder can augment their training sets, add new features, retrain their model, or head back to the drawing board with these new learnings in mind.

# **Conclusion**

In conclusion, ML observability achieved through the application of an evaluation store can help your team throughout the whole process of validating, monitoring, troubleshooting, and improving your models. Through introspection into your models’ performance over time, ML observability can help your teams identify gaps in training data, surface slices of examples where your model is underperforming, compare model performances side by side, validate models, and identify issues in production. Stop flying blind, and take your ML efforts to the next level.

## Contact Us

If this blog caught your attention and you’re eager to learn more about [Machine Learning Observability](https://arize.com/platform-overview/) and [Model Monitoring](https://arize.com/model-monitoring/), check out our other [blogs](https://arize.com/blog/) and resources on [ML Monitoring](https://arize.com/ml-monitoring/)! Feel free to [reach out](https://arize.com/contact/) to us with any questions or comments, and find our open positions [here](https://arize.com/careers/) if you’re interested in joining a fun, rockstar engineering crew to help make models successful in production!

