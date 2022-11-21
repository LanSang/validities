[![Taggart Bonham](https://miro.medium.com/fit/c/96/96/1*3muSOpFlGHoOaAhvaoBrzQ.png)](https://taggartbonham.medium.com/?source=post_page-----a214d823629d--------------------------------)[Taggart Bonham](https://taggartbonham.medium.com/?source=post_page-----a214d823629d--------------------------------)[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F2e2b1936481f&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fml-for-product-managers-a214d823629d&user=Taggart+Bonham&userId=2e2b1936481f&source=post_page-2e2b1936481f----a214d823629d---------------------follow_byline-----------)Jan 13, 2021

·15 min read[Save](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fa214d823629d&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fml-for-product-managers-a214d823629d&source=--------------------------bookmark_header-----------)# ML for Product Managers

## *Five steps to ship your company’s next big thing.*

![]()Photo by [Charles Deluvio](https://unsplash.com/@charlesdeluvio?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)So, you’re a PM and there’s been a lot of talk about how AI is revolutionizing the industry, how your company is data-driven, or how your product has a deep analytics focus. But what exactly does that mean? Without understanding how data-powered applications work, your PRD’s will be long on buzzwords and short on substance. We can talk ourselves in circles about the value of analytics, but without understanding how to productize machine learning, we’ll never actually ship.

This article will walk you through the five steps of building and deploying machine learning models, using time-series anomaly detection to demonstrate a real-world example. The best part: this distilled approach will apply to any product or feature (talk about transfer learning!)

At a high-level, these are the five steps to ship ML at scale.

1. **Determine the ML Approach**
2. **Build the Pipeline**
3. **Feature Engineering**
4. **Train your Model**
5. **Deploy**

# **1. Determine ML Approach from the Product Goal**

The product goal informs the technical approach. By first understanding our use case, we can explore how it fits into a ML paradigm.

**Product Goal:** Imagine your product is for an application owner, responsible for reporting on their app to the board. They just want to know how their app is performing and don’t have time to be overloaded with technical details. They’ve been frustrated by their app’s reliability and want real-time information, so they don’t get blindsided by outages.

From these customer conversations, we’ve uncovered the product goal: alert users if their app stops working.

**Sanity Checks:** Before diving down the ML rabbit hole, first ask:

1. *Are you really solving a valuable problem?*

Start with the press release to determine if the project is worth the investment. Our reads: hundreds of man-hours and countless customer conversations saved by removing the necessity for manual monitoring of application performance. Ultimately, this anomaly detection will free people from deploying resources to actively monitor their apps. This seems valuable.

2*. Do you really need ML?*

In many cases a heuristics-based approach can work better. For our example, this means creating a decision tree based on some combination of the HTTP response codes and response time thresholds to determine if an application is performing. A decision tree and manual thresholds would need to be made for every single metric — all services have their own definition of ‘normal’. Here, this rules-based approach won’t scale. To classify app performance at scale, we’ve confirmed that we need ML.

![]()Machine learning uses data to train a function (image by author)**ML Framing:** Now that we’ve validated the idea, let’s frame the product goal in terms of machine learning. Machine learning uses data to learn a function. The historic application behavior that we’ve already collected (the data) trains our model to predict if our app behavior is normal or not (the function). We can then continuously feed performance data through this trained model to determine if our app is working or not in real-time.

Reformulating our product goal, we want to detect behavioral anomalies in our application using performance information.

**Data Selection:** Data powers machine learning. To choose a model and understand if our outcome is even possible, we need to understand the available data. Data can be broken into [two categories](https://developers.google.com/machine-learning/crash-course/framing/ml-terminology) — features and labels. Labels are the output of a ML model, for us this is a Boolean result of normal or anomalous application behavior. Features are the other input variables responsible for this classification.

![]()A taxonomy of data (image by author)Since our function requires app performance data, we can use timing information (HTTP response times), performance data (HTTP response codes) as features. This data is generated from a [synthetic monitoring system](https://en.wikipedia.org/wiki/Synthetic_monitoring) — periodically pinging a specific web address and recording the response. Associated with this data is timing information (the timestamp from when the measurement was taken which can be used for seasonality). While our data contains these performance features, it does not contain any labels — no one has gone through for all past points and marked which are anomalous or not. The ‘label’ column in the picture does not exist for us, which limits the possible models we can use.

**Model Selection:** Different models are better suited to different tasks, all making different assumptions about the data. Before choosing a model, we must consider a number of factors that will impact deployment: data availability, latency, and ease of implementation.

*Data availability* means what data is available during training and prediction. The choice between the two main model types — supervised and unsupervised — depends on data availability. Whereas supervised models train on data containing features and labels, unsupervised models require just features. We have the performance metrics discussed above but no labels, which means we need to use an unsupervised approach.

*Latency* is the product requirement for prediction time. The two considerations here are stream or batch processing. Whereas stream processing models run instantly on the data, batch models run analytics for collected data at fixed intervals (allowing for methods with larger processing times). Merely showing users a marked-up graph with anomalies or making them dig around their metrics won’t reduce the need for operators’ eyes on screen. From the use case described, app owners want to minimize the time they have to spend staring at raw metrics. Our product requires a near-real time classification which points to stream processing.

*Ease of implementation* impacts how quickly we can develop a model. Training a complex, end-to-end pipeline is a delicate process. We must consider the performance-complexity tradeoff. While a more complicated model might give better results, it can also add significant amounts of development time. For implementation, we’ll start with an easy base-model that will enable quick development, iteration, and debugging.

Below is a model selection flowchart from [scikit-learn](https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html), a leading python ML library. More information about different model types is available [here](/all-machine-learning-models-explained-in-6-minutes-9fe30ff6776a).

![]()ML model choice flowchart (source: [Scikit-Learn](https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html))The lack of labels in our data requires that we use an unsupervised method, specifically a [clustering-based approach](https://scikit-learn.org/stable/modules/clustering.html). Because we are predicting a label for a known number of categories, we use [KMeans](https://aihub.cloud.google.com/p/products%2F0e0d2ed0-5563-4639-b348-53a83ac4ff4e). We’ll run KMeans where K=2, normal and anomaly. Below is a visual depiction of how KMeans groups raw data into known clusters.

![]()KMeans explained (Source: [Google AIHub](https://aihub.cloud.google.com/p/products%2F0e0d2ed0-5563-4639-b348-53a83ac4ff4e))To make the model more sophisticated, we could make use of the time-series aspect and use an [ARIMA](https://en.wikipedia.org/wiki/Autoregressive_integrated_moving_average) (Auto Regressive Integrated Moving Average) model or a RNN (recurrent neural network). However, we will start out with KMeans because of its ease of implementation in order to quickly build a base model. We can change to an ARIMA model later if we need additional performance or functionality.

**Create Metrics:** Metrics help us track product progress and compare different implementations. To judge our model, we’ll consider metrics for training performance, model performance and business performance. While we might look at training and model metrics early on to guide training, we ultimately live or die by business performance. Our product goal should be judged by end to end performance of business metrics.

*Training performance* is measured by the optimization metrics as part of the ML process. There are many in use depending on the model choice. For supervised methods, people typically use confusion matrices, ROC curves, or Calibration curves (more on those [here](/20-popular-machine-learning-metrics-part-1-classification-regression-evaluation-metrics-1ca3e282a2ce)). Because we’re using an [unsupervised approach](https://scikit-learn.org/stable/modules/clustering.html#clustering-performance-evaluation) we’ll use the silhouette coefficient. This is one of the only [clustering metrics](https://scikit-learn.org/stable/modules/clustering.html#clustering-performance-evaluation) we can use as it does not require labels in the training data. The [silhouette coefficient score](https://scikit-learn.org/stable/modules/clustering.html#silhouette-coefficient) relates to a model with better defined clusters (anomalous and normal).

*Model performance* are the metrics that evaluate the effectiveness of the ML approach. For many products, this means the percent of users who use the model versus the total number of users who could benefit from it. Because our product is an alerting system, model performance is ultimately tied to our ability to detect all anomalies. This ensures our customers (app owners) won’t get blindsided by missed errors. In ML terms, we are optimizing for [recall](/accuracy-precision-recall-or-f1-331fb37c5cb9), or the percent of anomalies caught.

We’ll need some form of user feedback to understand our model’s performance in production. This typically looks like a data collection mechanism in our frontend. User feedback could be as obtrusive as a thumbs up/down the user selects when viewing the predicted anomalies, or as frictionless as us intuiting the label based on actions taken on the frontend.

Implicitly assigning a label based on user interaction is called weak labeling. The bulk collection of these weak labels could ultimately let us use a more powerful supervised learning method instead. Every data-driven application must consider collecting user feedback as a top priority.

*Business performance* metrics reflect the model’s success against the product goals. We can create [guardrail metrics](/measuring-success-ef3aff9c28e4) too, ones that shouldn’t decline below a certain point.

Because we’re training our model to not miss any critical errors, we’ll likely present the user with an overwhelming number of alerts. This [alert fatigue](https://en.wikipedia.org/wiki/Alarm_fatigue) might make our model less useful in production because users will stop paying attention. To ensure that customers don’t start ignoring us, we ultimately care about the percent of relevant alerts. An implicit way of judging this is the percent of alerts presented that are acted on. In ML terms, this is called [precision](/beyond-accuracy-precision-and-recall-3da06bea9f6c). When coupled with recall as a guardrail metric, to ensure that we’re not missing high importance anomalies, we have a robust system for understanding the performance of our data.

*Other factors* to consider are speed and freshness. Speed is how long inference takes and freshness measures how well our training data compares to real-time data. Training data needs to be similar to input data for accuracy. When the distribution of live data shifts, the model needs to be retrained too.

**Exploratory Data Analysis (EDA):** Before we train a model, we need to have a good understanding of the underlying data. Using visualization tools like Google’s [Data Studio](https://datastudio.google.com/) can help us test assumptions about values and distributions, identify key variables, and detect structure in the data. To dig in deeper, we can use a [Jupyter notebook](https://jupyter.org/) and [pandas](https://pandas.pydata.org/), a python data analysis tool.

Examining our data, we see that the maxes are much larger than the 75th percentile, indicating that it could be a meaningful dataset to use anomaly detection on — the anomalies should pop out.

Digging in deeper to the http request time, we see a primary left cluster that is normally distributed (log-normal in the graph), with a few points off to the right. This exploratory data analysis gives us further confidence in our KMeans approach. In fact, we could develop a simple heuristic, if the http request time is greater than 1.25 seconds, then it is anomalous.

![]()Distribution of http response times (image by author)# **2. Build the Pipeline**

End to end pipelines allow for easy iteration. The faster our model fails, the faster we can make progress. Evaluating model performance quickly identifies the next area for improvement.

*For technical information on deploying pipelines, refer to* [*various*](https://cloud.google.com/blog/products/data-analytics/anomaly-detection-using-streaming-analytics-and-ai)[*tutorials*](https://aws.amazon.com/sagemaker/pipelines/) *from Google Cloud Platform (GCP) or Amazon Web Services (AWS).*

![]()The training and inference pipelines (image by author)ML needs a training and inference pipeline. The training pipeline (discussed later) creates our model , and the inference pipeline makes the predictions.

**Build an Inference Pipeline:** Start with deploying an inference pipeline. By quickly delivering a basic model, we can begin to collect usage data that enables further training and performance gains. This initial models is based on simple heuristics from subject matter expert (SME) knowledge.

Using a HTTP request time of 1250 ms as a threshold, let’s run our training data through this Running our training data through this basic model. Because of the spread in the data, we’ll plot the log of request time to make the results more consumable.

![]()Anomaly detection on training dataset using threshold (image by author)**Test Workflows:** After we can serve our simple model, let’s investigate our assumptions about the user experience and model results.

User experience is an important consideration because usability will drive usage of our model. Asking *what’s the best way to present our model? How can we ensure that results are presented usefully? What data would actually be helpful if returned?* forces us to consider our frontend design. Spamming users with about anomalies with no notion of causal context contributes to alert fatigue and instantly turns people away from our product. Instead, useful results contain data about significance of an anomaly and the specific factors that caused the anomalous classification.

Model results are a necessary consideration as well. Ask: *are we getting non-trivial results? Is the training data accurate and representative? How can we remove bias?* Initial runs show that the seriously bad anomalies get picked up, but much of the variation and nuance remains unexamined. Because there are many other metrics that comprise an anomalous classification (not just HTTP request time), we need to develop a better model that considers these features.

# **3. Feature Engineering**

Understanding your data will lead to the biggest performance gains. Be efficient in your exploration, starting small with a dataset that’s easy to work with. Looking at your dataset to learn about its features is the easiest way to develop a solid model and feature engineering pipeline. This typically consumes the majority of development time.

Ensure that your data is formatted, with clear inputs and outputs that will be available at prediction time. Make sure that the data fields aren’t missing, corrupted, or imprecise by manually verifying labels or feature values. Examine the data quantity (to make sure you have at least 10k examples), generating synthetic data if needed. Look into clusters and summary statistics. Examining our training set, we can drop all examples without meaningful (empty or na) timing data.

Create features from patterns like seasonality, [feature crosses](https://developers.google.com/machine-learning/crash-course/feature-crosses/video-lecture), or other meaningful patterns you observe. We can vectorize to create new features from raw data and [reduce the dimensionality](/a-complete-guide-to-principal-component-analysis-pca-in-machine-learning-664f34fc3e5a) (representing vectors in fewer dimensions while preserving as much structure as possible). These features make it easier to detect non-linear relationships in neural networks. Make sure that the transformations and process for creating new features is saved, as it must run on input data at prediction time too, or the model will not function properly.

We’ll create features for every hour of the day and day of the week as well as a feature cross between the two. Further, we’ll create a new feature called ‘total’ that is the sum of tlsHandshakeMs, httpRequestTimeMs, and the rest of the other timing metrics.

Creating additional models can aid the training process. An ‘[error model](/how-to-do-error-analysis-to-make-all-of-your-models-better-a13c4ca643a)’ can be trained to detect what types of examples your model fails on. A ‘labeling model’ can be used to find the best examples to label next if you’re working with a supervised training model. This model detects labeled versus unlabeled examples, allowing you to label those unlabeled examples most different from the labeled examples. Because we’re sticking with a simple, unsupervised approach, we can ignore creating these models for now.

# **4. Train your Model**

Now that we have our engineered features, we can train our model by splitting our data, judging prediction performance, and evaluating feature performance.

**Split Data:** To ensure we can validate the results of the trained model, we need to set aside data. Specifically, 70% of our data is used in training, 20% in validation, and 10% for testing. The training data optimizes the weights of the model, the validation set [tunes the hyperparameters](/hyperparameter-tuning-c5619e7e6624) (network depth, number of filters per layer, and weight decay), and the test set is how we can evaluate the model.

Make sure that validation and test datasets are as close to production as possible to prevent [data leakage](/data-leakage-in-machine-learning-10bdd3eec742) (future data used as a training feature, duplicates between sets means outsized performance from overfitting). Ensure that the data is [split](/data-splitting-technique-to-fit-any-machine-learning-model-c0d7f3f1c790) properly.

**Debug:** Abnormally high performance typically indicates data leakage or bugs. Google has [written extensively](https://static.googleusercontent.com/media/research.google.com/en/pubs/archive/aad9f93b86b7addfea4c419b9100c6cdd26cacea.pdf) on potential tests for a ML system. To debug a model,

1. First, ensure the model is wired properly so that the data flows through from input to prediction
2. Next, make sure that the model can fit the training data
3. Finally, check if the model can fit unseen data, assuming it’s within a reasonable range

**Judge Performance:** Choose an appropriate cost function to optimize your model. Examining your cost function on test and training data helps estimate the [bias-variance trade-off](/understanding-the-bias-variance-tradeoff-165e6942b229) in the model, the degree to which our model has learned valuable generalized information without just memorizing specific details of the training set. Specifically, examine:

![]()Confusion Matrix for our anomaly detection use case (image by author)* [Confusion Matrix](/understanding-confusion-matrix-a9ad42dcfd62): performance measurement for machine learning classification problem where output can be two or more classes. It is a table with 4 different combinations of predicted and actual values
* [ROC Curves](/understanding-auc-roc-curve-68b2303cc9c5): shows how capable a model is of distinguishing between classes. Product Managers benefit from adding vertical or horizontal lines that correspond to allowed false positive (FP) or false negative (FN) rates based on product requirements
* Calibration Curves: fraction of TP relative to confidence level

**Evaluate Features:** Inspect which features aid classifications, by examining the classifier. If using a neural net, use black-box explainers such as [LIME](/understanding-model-predictions-with-lime-a582fdff3a3b) or [SHAP](/explain-any-models-with-the-shap-values-use-the-kernelexplainer-79de9464897a).

Because we’re using unsupervised methods, we can ignore all of this. As our data doesn’t contain labels, we can’t actually validate a model with these methods. Therefore, we send all data into training. Instead, we can use the [silhouette score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html) to check our output. On our KMeans model, this metric returns a 0.802 (where 1 is best and -1 is worst). Visualizing the classified labels shows that this unsupervised approach turned out reasonable results.

![]()Anomaly detection on training dataset using KMeans (image by author)The benefits of the simple model are made clear in our latency metrics. On a machine with 4 vCPUs and 15 GB of RAM, training took an average of .516 seconds. Inference for all the training data took .004 seconds. That’s well below any reasonable human reaction time.

However, our model is creating a lot of alerts. This underscores the necessity of collecting user feedback. If we had data on which anomalies were helpful, we could further tune our model with supervised methods toward only providing actionable alerts — the ones our users actually want.

# **5. Deploy**

Now that the model’s trained, we perform a final validation, build a production environment, and start monitoring. Here’s a high-level look at the necessary components.

![]()Components of a ML production environment (image by author)*Final validation* is the last sanity check before moving a model to production. Ask: *What assumptions is your model making from the training data? How was the training data collection? Does that differ meaningfully from production data? Is the dataset representative enough to produce a useful model?*

It also requires considering the intended use and scope. Confirm the data used is authorized for collection, usage, and storage. Remove training bias by ensuring no measurement errors, corrupted data, and proper representation of all feature classes. Eliminate systematic bias and modeling concerns by employing feedback loops, and benchmarking on all subsets of training data. Defend against adversaries by deploying monitoring systems that detect shifts in usage activity.

*Build a production environment* that is reliable to properly run your model, by engineering for:

* **Failures** (I/O checks): Sanitize input data by ensuring it falls within the range and distribution of training data. Create a second ‘failure detection model’ that predicts most likely failed inputs or a ‘filtering model’ that pre-screens inferences. If these models indicate a potentially dubious result, fallback on a simple model or heuristic that provides a plausible output.
* **Performance**: Speed up performance with caching if applicable (a least recently used or LRU cache is commonly used when dealing with repeated inputs). Make sure to manage model and data lifecycle management (when to retrain the model based on indications of drift), reproducibility, resilience, and pipeline flexibility.
* **Feedback:** Gathering implicit feedback is crucial for judging performance. Consider looking at actions users perform to infer whether a model provided useful results.
* **CICD:** To implement CICD for machine learning, consider deploying in shadow mode (in parallel to existing model, checking results against production model). Either can use A/B testing or [multi-armed bandit](https://en.wikipedia.org/wiki/Multi-armed_bandit) (explore/exploit for multiple models in production).

*Monitor models* to inform resilience of production environment. Specifically, look at the accuracy and usage over time. Accuracy over time to informs the refresh rate, or when the model is retrained. Most models need to be updated regularly to maintain a level of performance. Monitoring can detect when a model is no longer fresh and needs to be retrained. Usage can show patterns of abuse (for example, an anomalous number of logins). Similarly, monitor the metrics outlined previously for performance and business metrics.

So, when are you going to ship your next big thing?

