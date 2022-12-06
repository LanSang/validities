[![Sandeep Uttamchandani](https://miro.medium.com/fit/c/96/96/1*71wo4Rv3wEcf39RfKNo73Q.jpeg)](https://modern-cdo.medium.com/?source=post_page-----c36678065a75--------------------------------)[Sandeep Uttamchandani](https://modern-cdo.medium.com/?source=post_page-----c36678065a75--------------------------------)[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F2570cf937eb2&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2F51-things-that-can-go-wrong-in-a-real-world-ml-project-c36678065a75&user=Sandeep+Uttamchandani&userId=2570cf937eb2&source=post_page-2570cf937eb2----c36678065a75---------------------follow_byline-----------)Dec 31, 2020

·21 min read·Member-only

<person role="O'Reilly author, Founder">
https://modern-cdo.medium.com/
</person>

[Save](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fc36678065a75&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2F51-things-that-can-go-wrong-in-a-real-world-ml-project-c36678065a75&source=--------------------------bookmark_header-----------)# 98 things that can go wrong in an ML project

## Are any of these landmines hiding in your real-world ML initiative?


> [87%](https://dzone.com/articles/top-10-reasons-why-87-of-the-machine-learning-proj) of ML projects fail today!
> 
> 

These numbers should be taken with a grain of salt. Irrespective of the actual number, it does reflect reality — I have [seen](https://www.amazon.com/Self-Service-Data-Roadmap-Democratize-Insight-ebook/dp/B08HSSBC7F) a significant percentage of ML-based projects never get into production!

GIF via [giphy](https://giphy.com/gifs/wreckedtbs-funny-tbs-yNFg0qdiJTX1sCTjNc)
> The goal of this blog is to share my experiences on things that can go wrong in an ML project (they added up to 98!). The motivation with this post is for you to potentially avoid these landmines in your role as a [data engineer](https://hackernoon.com/7-gotchas-data-engineers-need-to-watch-out-for-in-an-ml-project-ev6t33mx), data scientist, ML engineer, [data-business leader](https://medium.com/wrong-ml/the-chief-data-officers-scorecard-for-digital-transformation-a030c86d667c?source=friends_link&sk=454a85e0e58d424281256e1951022d59) driving an ML initiative.
> 
> 

![]()Experiences divided into 6 phases of any ML project. Depending on your role, feel free to read the respective sections in this blog (Image by author)This is a long post divided the post into 6 categories. Feel free to read categories that relate best to your role as a data engineer, data scientist, ML engineer, [data-business leader](https://www.linkedin.com/pulse/identifying-unicorn-managers-within-cdo-team-uttamchandani-ph-d-/):

* [**ML Problem definition**](#6988): The formative stage of defining the scope, value definition, timelines, [governance](https://medium.com/wrong-ml/why-data-rights-governance-is-non-trivial-to-implement-in-the-real-world-a075cb06883a?source=friends_link&sk=fef2a65a48c62458f7a8c364d49a17f8), [resources](https://medium.com/wrong-ml/8-dq-traits-to-spot-talent-for-your-data-team-114ab7c368e9?source=friends_link&sk=91697bea1fffbcd511a30e01bbfaeed4) associated with the deliverable.
* [**Dataset Selection**](#c076): This stage can take a [few hours or a few months](https://medium.com/wrong-ml/challenges-with-clickstream-datasets-in-the-real-world-4b0798572215?source=friends_link&sk=bc98b511f12607873c91bf19632346dc) depending on the overall data platform [maturity and hygiene](https://medium.com/wrong-ml/the-secret-ingredient-in-successful-ml-projects-data-culture-347829b51f03?source=friends_link&sk=52663e6152877ab612eac303ac71f9b5). Data is the lifeblood of ML, so getting the [right and reliable datasets](https://medium.com/wrong-ml/challenges-in-finding-relevant-data-attributes-for-building-ml-models-97ae420a079f?source=friends_link&sk=352c947d6559574e3697468a9012e20a) is supercritical.
* [**Data Preparation**](#3873): Real-world data is messy. Understanding data properties and [preparing properly](https://medium.com/wrong-ml/why-data-wrangling-is-difficult-to-estimate-f6a54ec3f73c?source=friends_link&sk=ad348030415fcc8d884bb4c35e1b1d0c) can save endless hours down the line in debugging.
* [**ML Model Design**](#841a): This phase involved [feature selection](https://medium.com/wrong-ml/why-creating-ml-model-features-is-challenging-in-the-real-world-79c8e6cd91d9?source=friends_link&sk=2d4eb7a9961e021c8e2564044209ab87), decomposing the problem, and formulating the right model algorithms.
* [**Model Training**](#45cb): Building the model, evaluating with the hold-out examples, and online experimentation.
* [**Operationalize in Production**](#271d): This is the post-deployment phase involving [observability](https://medium.com/wrong-ml/observability-data-pipelines-99eda62b1704?source=friends_link&sk=994fc87e78cc2fcdb28fbdae1f53ebcb) of the model and ML [pipelines](https://medium.com/wrong-ml/re-think-your-data-pipelines-in-the-decoupled-era-5b032bc8b779?source=friends_link&sk=577cf9c5ceb0b3da0d34b7317f7f53ec), refresh of the model with new data, and [tracking](https://medium.com/wrong-ml/taming-data-quality-with-circuit-breakers-dbe550d3ca78?source=friends_link&sk=5aff64c334b54728eb363db2fd26d4b0) success metrics in the context of the original problem.

![]()Breakdown of number of experiences covered in each of the categories (Image by author)# **ML Problem definition**

1. ***“Vague success metrics of the ML model”*** Implementing an ML model to increase customer happiness. How do you define *“happiness?”* Instead, focus on the most paired down metric that is measurable and sensitive to the desired outcome. An intermediate or proxy metric to happiness can be time spent to accomplish a repeating workflow (such as creating an invoice in an accounting software) or the number of times the referral link is shared.

GIF via [giphy](https://giphy.com/gifs/rickandmorty-season-1-adult-swim-rick-and-morty-fu2rIw18eIDz1YCrCT)2.***“<quote label="Model metrics need to be aligned with business goals">Even if we had the perfect model — no clue of how it will be used within existing workflows”*** This is very common. More often we focus on going from data to insights, but miss out on the last mile from insight to the outcome. Simply predicting customer churn is of little value till is applied to the customer success process to proactively reach out and manage these customers.</quote>

3.***“Building a 100% accurate model — no clarity on the acceptable trade-offs such as precision versus recall”*** ML models are often considered to be “magic.” If you have a model predicting patients with a potential of heart attack, what are you optimizing: precision or recall. In this example, a high recall that minimizes False Negatives is more important than minimizing False Positive.

4.***“Using a hammer to kill an ant — not checking the performance of simpler alternatives”*** <quote label="tradeoffs">With the buzz around ML, simpler alternatives or heuristic models are often overlooked. I have seen examples where the existing heuristics are meeting the success metric by 99%, yet there will be a request to build an ML model. </quote>Also, in thinking ML models, also consider Human in Loop alternatives.

5.***“Not all ML problems are worth solving — <quote label="tradeoffs">the impact may not be worth the effort</quote>”*** To deliver a well-tuned robust ML model deployed in production can range from 6–24 months depending on the complexity. Being clear about the strategic value of the project is critical.

6. ***“Drowning the business team in technical mumbo jumbo”*** Discussing the [AUC](/understanding-auc-roc-curve-68b2303cc9c5) or normalized entropy is of little value to business users. Instead, spending time explaining the significance and what these mean in the context of the business outcome or success criteria.

7. **“Underestimating project costs — ignoring data costs”** <quote label="tradeoffs">ML is data-dependent — acquiring and labeling data requires sizeable teams. Data sets are expensive to maintain.</quote> The cost of data is often ignored in project costs and can also lead to incorrect attrition decisions.

8. **“Treating AI Ethics as a nice-to-have”** It is important to treat ethics as both a software design consideration and a policy concern. In every aspect of the ML pipeline, evaluate the ethical considerations aligned with the values of the team — from data collection to decision making, to validation and monitoring of performance and effectiveness.

9. **“Not leveraging past metrics during project formulation”** During the initial project formulation stage, I have often seen misalignment across the business, engineering, and data teams on resources allocation, milestones, and timeline. Oftentimes, data scientists and project managers from similar past projects are missing in this decision making it guesswork driven rather than leveraging data metrics.

10. **“Not managing stakeholder expectations”** Oftentimes, ML projects start with unrealistic high expectations based on very little understanding of data availability, data quality, business workflow, team resources, end-to-end product deployment. Business stakeholders seldom are given a view of the risks and cost of incorrect predictions from the standpoint of user experience.

11. **“Not defining criteria to kill the project”** Often, fundamental gaps are discovered in the data and business problem. Even though there is enough evidence, there are no clear criteria defined to pull the plug on the project. Instead, the teams should be encouraged to put projects “on ice” with clear documentation on when to review the project (for example, when certain data attributes are collected for a period of time). Partial projects can provide valuable lessons that can be applied in other current or future projects

12. **“Not preparing for the appropriate ML project complexity”** Not all ML projects have the same complexity in terms of training, deployment, maintenance. One way to judge the complexity is whether the training and inference are online versus offline. Offline training and offline inference models are the easiest ML models. Online training differs in the time window for model refresh ranging from a few weeks to an order of minutes. Models that are online training and online inference require very robust ML pipelines with drift monitoring and alerting.

13. **“Not decomposing the problem”** Instead of thinking of the business problem as one single ML model, most often the solution involves utilizing a sequence of models and methods.

14. **“Optimizing on the model perpetually”** Improving the model can be an endless endeavor. Resources to improve the model come at an opportunity cost as they are not working on other projects. A strategy that helps is to limit the number of resources and evaluate the status of the project at the end of a time-bound window. In the evaluation, you can decide to allocate another increment of time-bound resources, or declare the outcome is good enough for now. Often times, allocating additional resource increments only if you see traction.

15. **“Assuming Petabytes of data available == Successful ML project”** During the planning process, the fact that there is a large amount of data is taken by business stakeholders as a proxy that an accurate ML model can be built. The size of the data is not a guarantee for a successful ML project — data quality, missing data facts, incomplete representation of the truth we are aiming to model, and several other aspects decide the fate of the project.

# Dataset Selection

GIF via [giphy](https://giphy.com/gifs/l4RKhOL0xiBdbgglFi)16. ***“I thought this dataset attribute*** [***means something else***](https://medium.com/wrong-ml/schema-on-read-curse-of-data-lakes-our-5-antidotes-1386199d262f?source=friends_link&sk=cff1d1104f9f82f495f1bf453327d76c)***”*** Data attributes are typically never documented. Prior to the big data era, data was curated before being added to the central data warehouse. This is known as *schema-on-write.* Today, the approach with data lakes is to first aggregate the data and then infer the meaning of data at the time of consumption. This is known as *schema-on-read.*

17. ***“5 definitions exist for the same business metric —*** [***which one to use***](https://unraveldata.com/resources/standardizing-business-metrics-democratizing-experimentation-at-intuit/)***”*** Derived data or metrics can have multiple sources of truth and business definitions. For instance, even basic metrics such as “new customers” have multiple definitions corresponding to what qualifies a customer as a new customer.

18.***“Where is the dataset I need for my model?”*** Given the siloed nature of data, different datasets are managed and cataloged by multiple teams. A lot of tribal knowledge within the data team on datasets and corresponding contact person.

19.***“The data warehouse is stale”*** Raw data is copied to the Data Lake and ETl’ed into Data Warehouses. Given ETL pipeline errors, the business metrics in the warehouse can be stale and not refreshed in a timely fashion.

20.***“Need to instrument the application for more clickstream events — it will take months”*** Managing instrumentation for adding beacons — more details in this [blog](https://medium.com/wrong-ml/challenges-with-clickstream-datasets-in-the-real-world-4b0798572215).

21.***“Assuming all the datasets have the same quality”*** This is a classic mistake. Not all datasets are reliable. Some of them are updated and managed by source teams very closely while other datasets are abandoned or not regularly updated or have flaky ETL pipelines.

22.***“Customer changed preference to not use their data for ML. Why are those records still included”*** Data rights are now becoming critical. It is [important to track and enforce](https://medium.com/wrong-ml/why-data-rights-governance-is-non-trivial-to-implement-in-the-real-world-a075cb06883a) during ML model training and re-training.

23.***“Uncoordinated schema changes at the data source”*** Very common, there are schema changes at the source that are uncoordinated with downstream processing. The changes can range from schema changes (breaking existing pipelines) to difficult to detect sematic changes to the data attributes. Also, when business metrics change, there is a lack of versioning of the definitions.

24. ***“Not unit testing the input data”*** In traditional software development projects, it is a best practice to write unit tests to validate code dependencies. In ML projects, a similar best practice should be applied to continuously test, verify, and monitor your input data.

25. ***“Watch out for biased datasets”*** Datasets do not capture the ultimate truth from the statistical standpoint. They only capture the attributes that the application owners required at that time for their use-case. It is important to analyze datasets for bias and dropped data. Understanding the context of the dataset is supercritical.

26. ***“Letting datasets become orphans without stewards”*** Datasets are useless if they cannot be understood. Trying to reverse engineer the meaning of columns is often a ‘losing battle.” The key is to aggressively document the dataset attribute details as well as ensuring that there is a data steward responsible for a dataset to update and evolve the documentation details.

# **Data Preparation**

GIF via [giphy](https://giphy.com/gifs/schittscreek-comedy-pop-tv-xUOwG4ZJBYTfPrpnbO)27. ***“Don't forget data expires?”*** Data has an expiry date. Records of customer behavior from 10 years back may not representative. Additionally, ensuring data is [IID](https://en.wikipedia.org/wiki/Independent_and_identically_distributed_random_variables) (Independent and Identically Distributed) for model training, as well as taking into account the seasonality of data.

28. ***“Systematic data issues making overall dataset bias”*** If errors in the dataset are random, they are less harmful to model training. But if there is a bug such that a specific row or column is systematically missing, it can lead to a bias in the dataset. For instance, device details of customer clicks are missing for Andriod users due to a bug, the dataset will be biased for iPhone user activity.

29. ***“Unnoticed sudden distribution changes in the data”*** <quote label="data">Datasets are constantly evolving. Analysis of the data distribution is not a one-time activity required only at the time of model creation. Instead, there is a need to continuously monitor datasets for drifts, especially for online training.</quote>

30. ***“Using all the data for training — each model iteration can take days”*** While more data helps to build an accurate model, sometimes data is huge with billions of records. Training on a larger dataset takes both time and resources. Each training iteration takes longer slowing down the overall project completion. There is a need to use data sampling effectively.

31. “***We are using the best polyglot datastores — but how do I now write queries effectively across this data?***” There is no silver bullet datastore. Typically polyglot persistence is used with specialized datastores for Key-Value, Document, Graph, Time-series data, etc. While heterogeneity delivers the best performance, data teams have a learning curve to effectively build pipelines to analyze and join data across datastores.

32. ***“Ignoring seasonality in sales or customer behavior data”*** Before using a dataset, verify the properties of iid, stationary (not changing over time), and ensure the same distribution during training and testing. Seasonality is often missed which is a classic violation of stationarity.

33. ***“Not randomizing before splitting training and test data”*** Very often, without randomization, we may end up with all fall data in training and summer data in the test. This can lead to loss-epoch graphs that require unnecessary debugging. A low-hanging fruit that is often missed.

34. ***“Test examples have duplicates in the training set”*** Oftentimes, we have been excited by really high accuracy numbers. Double checking often reveals that many of the examples in the test set are duplicates of examples in the training set. In such scenarios, the measurements of model generalization are non-deterministic.

35. ***“Not Qualifying the test set”*** Ensuring test sets yield statistically meaningful results and representative of the data set as a whole.

36. ***“Using Normalization instead of Standardization for scaling feature values”*** To bring features to the same scale, use normalization (MinMaxScaler) when the data is uniformly distributed and standardization (StandardScaler) when the feature is approximately Gaussian.

37. ***“Improper handling of outliers”*** Based on the problem, outliers can either be a noise to ignore or an important to take into account. Outliers typically arising from collection errors can be ignored. Machine learning algorithms differ in their sensitivity to outliers — AdaBoost is more sensitive to outliers compared to XgBoost which is more sensitive than a decision tree that would simply count an outlier as a false classification. Proper handling of outliers requires understanding if they can be ignored and picking the appropriate algorithm based on sensitivity.

38. ***“Arbitrary sample selection within a large dataset”*** Given very large datasets, sampling is typically arbitrary. Paying special attention to leveraging techniques such as [importance sampling](https://en.wikipedia.org/wiki/Importance_sampling).

# ML Model Design

GIF via [giphy](https://giphy.com/gifs/89a-3d-design-art-bpmNf92LmkoMw)39. ***“Leverage feature crossing before jumping to non-linear models”*** Linear learners scale well for massive data and easier to maintain in production. For problems that are not inherently linear, I have seen Feature crossing as an effective approach for several problems i.e., adding cross features when data is not linearly separable in the input space isespecially effective with massive input data sets.

40. ***“Model accuracy too good to be true — check for feature leakage”*** Improper feature values can lead to feature leakage — the [blog](https://medium.com/wrong-ml/why-creating-ml-model-features-is-challenging-in-the-real-world-79c8e6cd91d9) with more details.

41. “***Relying on flaky pipelines for generating time-dependent features”*** Time-dependent features such as “product views so far” needs a low latency robust pipeline to calculate values. Often times, bugs in these pipelines are very difficult to debug in the context of the overall model behavior.

42. ***“Lack of balance between bias (underfitting) and variance (overfitting)”*** Watching out for a simplified model that is underfitting the data (bias) to the other extreme of a complex high dimensional model with sensitivity to the slightest variation of the data (variance). Striking the right balance is required for an effective model in production.

43. ***“Compromising interpretability prematurely for performance”*** ML projects pre-maturely fast forward into applying deep-learning. In early iterations of an ML project, an interpretable model is more important than a black box performant one. An interpretable model helps generate the next set of hypotheses about the features and data properties. The key is to start with simple models and not optimizing prematurely. Simpler models are easier to debug and iterate.

44. ***“Adding new features without justification on how they increase the model quality”*** <quote label="tradeoffs">Adding features that encode new information will improve model performance, but at the cost of increased model complexity (as well as complexity on testing, deployment, maintenance of corresponding ML feature pipelines). New features added to the model should be justified using correlation matrices or training the models and analyzing results with and without the feature.</quote> In software engineering terminology, adding new features after the model is performing reasonably should be treated as a “code freeze phase” with every feature change reviewed carefully.

45.***“Skipping Feature scaling”*** Without feature scaling, the model pays too much attention to the features having a wider range. This is important for model correctness.

47. ***“Always using deep learning instead of traditional feature engineering”*** For problems with weak baselines and good intuition, better to focus on simpler models applying the intuitions of feature engineering rather than black-box deep learning. Deep learning is good for problems with a significant amount of data, and compute bandwidth.

48. [***“Not applying hashing for sparse features”***](https://dzone.com/articles/feature-hashing-for-scalable-machine-learning)

49. ***“Not attempting to reduce the dimensionality of models”*** High dimensional models are difficult to manage in training and production deployment. It is important to reduce the number of dimensions associated with the model using techniques such as [PCA](https://en.wikipedia.org/wiki/Principal_component_analysis), [LDA](https://en.wikipedia.org/wiki/Linear_discriminant_analysis).

50. *“****Not applying a business lens to Classification Threshold tuning”*** “Tuning” a threshold for logistic regression is different from tuning hyperparameters such as learning rate. Choosing a threshold involves assessing the cost of making an incorrect prediction. <quote label="formative">For instance, mistakenly labeling a transaction as fraudulent will lead to delay in processing and involve wasted effort in human analysis. However, labeling a fraudulent transaction as non-fraudulent will lead to financial loss to the business. Better to optimize the threshold for recall instead of precision.</quote>

51. ***“Treating regularization as a nice-to-have in logistic regression”*** Without regularization, the asymptotic nature of logistic regression would keep driving loss towards 0 in high dimensions. Applying techniques such as L2/L1 regularization or early stopping is a must-have.

52. ***“Shy in using embeddings”*** Using [embedding](/neural-network-embeddings-explained-4d028e6f0526) to translate large sparse vectors into a lower-dimensional space (while preserving semantic relationships) is an important optimization that is sometimes overlooked.

53. ***“Using guesswork for deciding model freshness requirements”*** Instead of applying heuristics or rules-of-thumb, it is important to evaluate the performance degradation of the model as a function of the refresh interval. I have seen projects where once a month refresh would suffice but the team is doing daily or weekly refresh which is expensive. On the other extreme, a delayed refresh can lead to a negative impact. Picking the right refresh based on data analysis is the key

54. ***“Not using features that apply to a very small fraction of your data”*** This one is a classic mistake. Often times, I have dismissed features that did not have a good coverage only to find out that while they had a low coverage overall, the feature was present in 95% of the positive examples. The takeaway, do not dismiss low coverage features early.

55.***“Lots of features in the model but too little data”*** It is important to be realistic w.r.t. the number of features you are adding to the model relative to the cardinality of data examples available for learning. It is possible to build on even small datasets if you are building a simple model. The key is to avoid scenarios of building complex models with limited data.

56. ***“Unclear model scope”*** Being clear with the scope of the model w.r.t coverage of feature values. For instance, if the prediction model is trained for first-time visitors rather than repeat users in a specific region.

# **Model Training & Tuning**

57. ***“Ad-hoc tuning is faster compared to a scientific approach”*** Oftentimes, tuning of hyperparameters & model architecture tends to be ad-hoc. While it appears to be faster, following a scientific approach always pays off based on my experience.

58. ***“A model that won’t converge”*** During model training, there are scenarios when the loss-epoch graph keeps bouncing around and does not seem to converge irrespective of the number of epochs. There is no silver bullet as there are multiple root-causes to investigate — bad training examples, missing truths, changing data distributions, too high a learning rate. The most common one I have seen is bad training examples related to a combination of anomalous data and incorrect labels.

59. ***“Loss value reduces and then increases significantly with epochs”*** Sometimes there are scenarios where the model seems to be converging but suddenly the loss value increases significantly. There are multiple reasons for this kind of exploding loss — the most common one I have seen is outliers in the data that are not evenly distributed/shuffled in the data. Shuffling, in general, is an important step including patterns where the loss is showing a repeating step function behavior.

60. ***“Improper tracking of details related to model versions and experiments”*** This is accidental complexity — not being able to track the details leads to wasted work and moving in circles. Results from model experiments are tracked with cryptic names such as *tmp\_1, tmp\_2,* etc. Given the lack of details, new members joining the team often revisit the exploration that has already been done in the past.

61. ***“Ignoring the specificity and sparsity trade-off”*** Instead of building a generic model, imagine building a model for a specific geographic region or specific user persona. Specificity will make the data more sparse but can lead to better accuracy for those specific problems. It is important to explore these trade-offs during tuning.

62. ***“Loss value is reducing but recall/precision not improving”*** Typically TF Keras and other ML libraries have a default classification threshold of 0.5. With this threshold, sometimes the recall value gets pegged at 0 as the classification probability will never get higher than the positive classification threshold, especially for problems with a large class imbalance. It is important to Investigate ROC AUC.

63. ***“Prematurely jumping to online experimentation”*** Having clear thresholds defined on when the offline validation is meeting the success criteria to start experimenting with online validation.

64. ***“In multi-class classification, not prioritizing specific per-class metrics accuracy”*** For multi-class prediction problems, instead of tracking just the overall classification accuracy, it is often useful to prioritize accuracy of specific classes and iteratively work on improving the model class-by-class. For instance, in classifying different forms of fraudulent transactions, focus on increasing the recall of specific classes (such as foreign transactions) based on business needs.

65. ***“Not paying attention to infrastructure capacity”*** Sometimes, there is only so much optimization that can be done in models and feature engineering. Given large datasets, the infrastructure capacity can become the limiting factor.

66. ***“Evaluating models using different datasets”*** This one falls in the obvious category but is sometimes overlooked. Models can be trained using different datasets but an apples-to-apples comparison requires using the same test dataset.

67. ***“Reporting model accuracy for the overall data”*** Instead, <quote label="metrics">it is more useful to segment the dataset in cohorts (based on business definition) and evaluate the model performance for different clusters.</quote>

68. ***“Training results not reproducible”*** To reproduce specific training results, it is important to snapshot the code (algo), data, config, and parameter values. Over recent times, the problem of reproducibility has been addressed in MLFlow, TFX, and multiple other solutions.

69. ***“Long time before first online experiment”*** No matter how complex the problem, the goal should be to have the first A/B experimentation of the model within the first 3 months even if the overall project takes 18–24 months. It helps uncover several aspects of the problem or dataset assumptions and speeds up the development of the final model.

70. ***“Model behaves differently in online experimentation compared to offline validation”*** This is typically representative of over-fitting or inconsistencies in online-offline feature generation.

71. ***“Ignoring*** [***feedback loops***](/dangerous-feedback-loops-in-ml-e9394f2e8f43)***”*** A feedback loop typically arises when a model is trained with a given set of features that are correlated with the outcome from another model.

72. ***“Making multiple changes within an experiment”*** Besides ML model changes, tracking the product or engineering changes is equally important. The goal should be to not bundle multiple changes being it difficult to correlate cause and effect.

73. ***“Ad-hoc framework to analyze the results of the experiment”*** Having a consistent way to analyze the results of the experiment is supercritical. Often times, a lot of time is spent on understanding the metrics collected from the experiment.

74. ***“No backup plan if the experiment goes south”*** Critical to proactively measure if the experiment is causing a negative impact on the test group and reverting the changes.

75. ***“Not calibrating the model ”*** In addition to accuracy, [model calibration](https://medium.com/analytics-vidhya/calibration-in-machine-learning-e7972ac93555) should be used. It's an easy sanity check measure of predicted probabilities with the observed distribution of classes.

76. ***“Always manually tuning hyperparameters”*** Hyperparameters play an important role in model performance. The ideal combination of hyperparameter values is data-dependent requiring experimentation and tuning. Traditionally, this is done manually with trial-and-error. Oftentimes, automated hyperparameter tuning service available in cloud services such as [Google,](https://cloud.google.com/ml-engine/docs/tensorflow/hyperparameter-tuning-overview) [AWS](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-ex.html), [Azure](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-tune-hyperparameters) is quite effective and helps improve the overall team productivity.

77. ***“Ignoring prediction bias”*** Prediction bias is the difference in the average of predications and average of labels in the dataset. Prediction bias serves as an early indicator of model issues — a big nonzero prediction bias is indicative of a bug somewhere in the model. Interesting [facebook paper](https://research.fb.com/wp-content/uploads/2016/11/practical-lessons-from-predicting-clicks-on-ads-at-facebook.pdf) in the context of ads CTR. Typically, the bias is useful to measure across prediction buckets.

78. **“*Calling it a success just on model accuracy numbers*”** Accuracy of 95% means 95 of 100 predictions were correct. Accuracy is a flawed metric with a class imbalance in the dataset. Instead investigate deeply into metrics such as precision/recall and how it correlates to overall user metrics such as spam detection, tumor classification, etc.

79. **“*Not understanding the impact of regularization Lambda*”** Lambda is a key parameter in striking the balance between simplicity and training-data fit. High lambda → simple model → possibly *underfitting*. Low Lambda → complex model → potential *overfitting* your data (won’t be able to generalize to new data). The ideal value of lambda is one that generalizes well to previously unseen data — data-dependent and requires analysis.

80. ***“Tuning hyperparameters at the same time”*** Sounds like a common sense which is sometimes uncommon. Changes to regularization parameters can be confounded with the effects from changes in the learning rate, etc. During tuning, sequence the tuning on different parameters.

81. ***“Using the same test set over and over”*** More the same data is used for parameter and hyperparameter settings, the lesser confidence that the results will actually generalize. It is important to collect more data and keep adding to the test and validation sets.

82. ***“Setting batch size hyperparameter small”*** For datasets with a very large number of examples that cannot fit in memory, reducing the batch size helps. Setting a *very* small batch can cause instability. The typical strategy is to start with a large batch size value, and then decrease the size until there is degradation.

83. *“****Not paying attention to initiation value in neural networks****”* Given non-convex optimization in NN, [initialization matters](https://www.deeplearning.ai/ai-notes/initialization/).

84. ***“Not tracking the results of failed experiments”*** During the model building experients, a wide range of data, models, and configurations (parameter and hyperparameters) are explored. Typically, failure experiments are not well documented and seen as a waste of time. It is important to capture the context such that new team members can leverage the learnings and mot reinvent the wheel.

85. ***“Assuming wrong labels always need to be fixed”*** When wrong labels are detected, it is tempting to jump and get them fixed. it is important to first analyze misclassified examples for root-cause. Often times, errors due to incorrect labels may be a very small percentage. There might be a bigger opportunity to better train for specific data slices that might be the predominant root-cause.

# **Operationalize**

GIF via [giphy](https://giphy.com/gifs/usnationalarchives-space-nasa-apollo-11-kvl2YhR110qsBrHid2)86. ***“ETL Pipeline SLA was 8 am. It’s now 4 pm and still processing — why is my metrics processing slow today ”***

87. ***“Metrics processing pipelines completed successfully but results are wrong?”*** This is typically due to missing job dependencies. Oftentimes, the processing of metrics would start even before the raw data ingestion has completed. This leads to incorrect results.

88. ***“Measuring model performance as a whole instead of data slices”*** Evaluating model performance across the entire dataset is a border-line vanity metric. Instead, report on model performance across various data slices. Checking the model across the data slices helps remove bias and uncovers valuable insights about the dataset, model, and the truth we are aiming to model.

89. ***“Tracking pipeline logic only to control training-serving skew”*** The typical reason for skew in model performance during training and inference is due to a discrepancy in handling data in the training and serving pipelines. But there are other aspects such as changes in data properties between training and serving as well as potential feedback loops.

90. ***“Using two different programming languages between training and serving”*** Avoid scenarios where training and serving pipelines are written in different languages.

91. ***“Response time to generate an inference is too high”*** The model endpoint may be saturated due to limited resources. With the automation of model deployment solutions, this is less relevant today.

92. ***“Data quality issues at source, or ingestion into the lake, or ETL processing”*** Quality issues need to be [proactively tracked](https://quickbooks-engineering.intuit.com/managing-data-issues-as-incidents-226f5f1c9e72?source=friends_link&sk=7eca658f035039a9db05473ca21c25b6) to ensure the correctness of inferences as well as for online model training.

93. ***“Cloud costs jumped up 3X this month”*** Given the linear pay-per-use pricing model in the cloud, ML costs can quickly get out of control. I recall the team spending 200K over the weekend running on high-end GPUs.

94. ***“Skipping model optimization phase in Neural Networks”*** In the initial phases, the focus is on generating the most accurate model. Once the model quality is reasonable, it is important to have a dedicated focus to try decreasing depth and width (overfitting) before deployment. One useful technique is halving the width at each NN layer. This will naturally impact model quality — the optimization phase is dedicated time in the project to balance quality with model depth and width.

95. ***“Not testing the correctness of the ML pipeline”*** There is a lot of focus on testing of ML model correctness. What about testing the ML pipeline? Starting with quality validation of input data, validating features, validating model deployment, etc. 95%+ of issues I have seen in production are related to ML pipelines!

96. ***“No checks and bounds for data and concept drift”*** For models deployed in production, it is critical to have the right processes in place. For instance, DDL monitoring at sources for concept drift.

97. ***“Adding unnecessary calibration layers”*** Sometimes to balance model bias (such as prediction bias for different data slices), a quicker shortcut is to add a calibration layer on the top of the model to manage these scenarios. In software engineering terminology, this is a classic example of “tech debt.” Such systems are difficult to update, debug and manage in production.

98. ***“Slow poisoning of the model”*** It is easier to detect 0–1 kind of errors with data and ML pipelines. The problems that are the most difficult to debug are ones where a table is being updated intermittently or systematic errors happening sporadically on certain table attributes. In such scenarios, the models will degrade gradually and adjust to the changes. The key is investing in [robust monitoring](https://medium.com/wrong-ml/taming-data-quality-with-circuit-breakers-dbe550d3ca78) for every aspect of the pipeline and data attributes.


> **If you are interested in more battle scars learned from real-world data and AI/ML/DataOps, checkout** [**Unravel Data**](https://unraveldata.com/)**, as well as check out my** [**book**](https://www.amazon.com/Self-Service-Data-Roadmap-Democratize-Insight-dp-1492075256/dp/1492075256) **and** [**podcast**](https://open.spotify.com/show/5tt1lS8NlGaziNGRSxZd4y)**.**
> 
> 

My interview on Data Standard Podcast sharing ML project experiences listed in this blog