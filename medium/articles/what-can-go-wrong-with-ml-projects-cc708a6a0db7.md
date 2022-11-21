[![Omer Mahmood](https://miro.medium.com/fit/c/96/96/1*W4bUsfXtIJ1PovwSZS4bLw@2x.jpeg)](https://medium.com/@omermx?source=post_page-----cc708a6a0db7--------------------------------)[Omer Mahmood](https://medium.com/@omermx?source=post_page-----cc708a6a0db7--------------------------------)[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F62cd989987f6&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fwhat-can-go-wrong-with-ml-projects-cc708a6a0db7&user=Omer+Mahmood&userId=62cd989987f6&source=post_page-62cd989987f6----cc708a6a0db7---------------------follow_byline-----------)Oct 4, 2021

·9 min read·Member-only
<quote label="Head of engineering division, Google">
https://www.linkedin.com/in/omahmood/
</quote>

[Save](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fcc708a6a0db7&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fwhat-can-go-wrong-with-ml-projects-cc708a6a0db7&source=--------------------------bookmark_header-----------)# What can go wrong with ML projects?

## 5 common things, and how to avoid them

![]()Photo by [Tomas Tuma](https://unsplash.com/@tomastuma?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/stuck?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)# The TL;DR

Kicking off a project that incorporates Machine Learning (ML) can be a tricky business. In this post we will explore some of the pitfalls you might encounter early on in your journey, and more importantly, how to avoid them.

💡 **I have listed them in the order you are likely to encounter them. But you don’t need to read in sequence, jump to what is most relevant to you.**

# (1)️ Your problem is not a good fit for machine learning

Just because ML exists, it doesn’t always mean we should use it! ML is not magic, and it certainly isn’t a silver bullet for solving all your business problems. But, when applied to the right use cases, it can deliver promising results.

Before deciding if using ML is the right approach for solving your problem, consider first if some good old-fashioned data analysis could provide the answers you need instead.

Often with a little data aggregation, filtering and summarisation you can usually identify simple patterns or trends in data, such as ‘how did sales of our widget in Q2 compare to Q1’?

We tend to use ML when the pattern in the data is less obvious, such as ‘what product do my customers have a higher propensity to buy from a catalogue of 1000s or even 100,000s of products’?

Below I have listed some common buckets of problems and related use cases that are suitable for ML:

* **Predictive analytics** — Fraud detection, preventative maintenance, click through rate, demand forecasting, next best customer action
* **Handling unstructured data** — Annotate video, identify eye disease, classifying and triaging e-mails
* **Enabling automation** — Schedule maintenance, reject transaction, count retail footfall, scan medical forms
* **Personalisation** — Customer segmentation, targeting, product recommendation

🧐 Still unsure if your problem is a good fit for ML? Take a look at the [Introduction to Machine Learning Problem Framing](https://developers.google.com/machine-learning/problem-framing), part of Google’s free online Machine Learning Crash Course.

# (2) ️Jumping into development without a prototype

It can be tempting to start integrating the first ML model you train into the final solution or application you are building.

An important point to realise is that ML model development is an iterative process. It’s impossible to know all the variables that could impact model performance at the beginning of a project.

A quick prototype can tell you so much about hidden requirements and potential implementation challenges earlier on, before they become blockers to getting your model into production.

For example you might encounter missing or dirty data. Does one type of model produce better results than another? Are you even focussing on the correct prediction target?

It is better to start with a simple model and continue to refine it until you’ve reached your goals, or a baseline you are happy with.

🛠 There are many tools you can use to create rapid ML model prototypes, here are three of my favourites:

* [**BQML**](https://cloud.google.com/bigquery-ml/docs/) — If you’re familiar with SQL you can use simple, short statements to create, evaluate and get predictions from ML models. This happens right where the data tables reside using BigQuery. BigQuery is a fully managed, serverless data warehouse from Google Cloud.
* [**Jupyter Notebooks**](https://jupyter.org/) — “The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualisations and narrative text”[1]. The beauty of a notebook is that you can execute blocks of code independently rather than compiling and running an entire program every time you want to test or change an element of your ML model code. If you don’t want the hassle of managing the infrastructure, you can launch [managed notebook instances using Vertex AI](https://cloud.google.com/vertex-ai/docs/general/notebooks) on Google Cloud. There are also some handy python libraries, such as [Lazy Predict](https://lazypredict.readthedocs.io/en/latest/readme.html#) that can be used in combination with a notebook to help rapidly down-select the best model to move forward with.
* [**AutoML**](https://cloud.google.com/automl) — Another Vertex AI offering, AutoML enables developers with limited machine learning expertise to train high-quality models specific to their business needs. AutoML provides a code-free user interface that enables you to ingest training datasets, train a model and evaluate its performance. Under the hood, it’s actually using ML to determine the best ML model to use for your problem 🤯. It also makes it easy to eventually serve the model should you choose to deploy it into production. There are also some other vendors out there such as DataRobot and H20.ai that give you a bit more flexibility and insight into the algorithms their own AutoML is comparing, presenting the results in a leaderboard format.
# (3) ️You have imbalanced datasets

This is a common scenario when you are trying to train an ML model that is supposed to classify instances of the exception, rather than the rule — think for example fraud detection in banking transactions.

You may have verified instances of fraudulent transactions in your training dataset. But because real instances tend to be less common, you will find that your dataset is imbalanced.

Considering our fraud detection problem, let’s say the ratio of non-fraudulent to fraudulent transactions is 5,000:1. If the dataset contains a million examples, then the dataset contains only about 200 examples of fraudulent transactions, which might be too few examples for effective training.

This data imbalance has a direct impact on your model’s ability to accurately classify fraudulent transactions.

What you can do about it:

* **Adjust Weights** — Our goal is to identify fraudulent transactions, but you don’t have very many of those positive samples to work with, so you would want the ML classifier you choose to assign more importance (or weight) to the few examples that are available. Most common ML classifiers allow you to pass weights for each class through a parameter. These will cause the model to “pay more attention” to examples from an under-represented class.[2]
* **Oversampling and Undersampling** — This is a technique that can be used to adjust the distribution of a dataset so it is more balanced. Going back to our fraud detection scenario, you might oversample (reuse) those 200 examples of fraudulent transactions multiple times, possibly yielding sufficient examples for useful training. Undersampling has the opposite effect i.e. deleting samples from the majority class, in our case non-fraudulent transactions.

⚠️ You need to be careful about [overfitting](https://en.wikipedia.org/wiki/Overfitting) when oversampling and undersampling training data.

* **Synthetic data generation** — Another option is to just create the data you need programmatically. This might be harder in some cases, especially if you don’t know what characteristics make up the under represented class in your training dataset. Depending on the programming language you are using to build your ML model, there are many freely available libraries to help to generate synthetic data. For example in Python, the popular [Scikit-learn](https://scikit-learn.org/stable/), SymPy or Pydbgen can be used to generate synthetic data.

🧐 Want a more practical, code based example? Take a look at this tutorial on the TensorFlow website: [Classification on imbalanced data](https://www.tensorflow.org/tutorials/structured_data/imbalanced_data?hl=en)

# (4) Model training is taking too long

Model training is the process of learning from the input data to build an ML model.

For many real-world datasets that can contain millions of rows, training can take hours, days and sometimes longer.

After your model has been trained, you can evaluate its accuracy (see Section 5 for more on this!) to see if you’ve made an improvement over previous training iterations.

When you or your team is trying to rapidly iterate on new ideas and techniques, training times can be a huge bottleneck for projects and hamper innovation.

What you can do about it:

* **Train models without managing the infrastructure** — If you are training your ML model on a laptop or common workstation, chances are that the scale of your hardware is what’s limiting your ability to train models quickly. One option is to use managed cloud based services, for example [Vertex AI](https://cloud.google.com/vertex-ai/docs/start/introduction-unified-platform?hl=ru). Basically Google Cloud handles the process of spinning up a virtual machine instance, tailored to your training needs. You just need to bring the code required to train your ML model. Or alternatively use [AutoML](https://cloud.google.com/vertex-ai/docs/training/automl-console?hl=ru) for a code free approach!
* **Tap into accelerators like** [**GPUs**](https://en.wikipedia.org/wiki/Graphics_processing_unit) **and** [**TPUs**](https://cloud.google.com/tpu) — Most ML frameworks such as TensorFlow are designed to take advantage of specialised hardware suited to massively distributed processing. If you need to process millions of rows of data, it’s far more efficient to do that in parallel chunks rather than one chunk at a time! GPUs and TPUs specifically for Tensorflow can help us achieve this objective. GPUs can be added to physical hardware or specified as part of a virtual machine configuration in the cloud. TPUs are very specialised hardware, available exclusively through Google Cloud.
* **Improve model quality with automated** [**hyperparameter tuning**](https://en.wikipedia.org/wiki/Hyperparameter_optimization) — If the code for building an ML model is like the ingredients for baking a cake in an oven, you can consider hyperparameter tuning as the adjustments you make on the knobs of that oven. The values of hyperparameters can impact the time it takes to train a model, you can choose to tune them based on specific objectives. While lots of machine learning libraries include some aspect of hyperparameter tuning capability. Going one step further, [Vertex Vizier](https://cloud.google.com/blog/products/ai-machine-learning/optimize-your-ml-model-quality-with-vertex-vizier) for example offers automated hyperparameter tuning, making the most optimal adjustments to the ‘oven knobs’ so you don’t have to.

🚀 If you don’t have the ability to scale up your compute resources, another option is to experiment with a smaller subset of your dataset. You might be able to train a model that is good enough without needing to train it using every single row. Used in combination with the rapid prototyping tools mentioned in Section 2; you can still make fast progress by comparing the training times before committing to a larger training dataset or algorithm.

# (5) ️Model accuracy not good enough

Sometimes you might feel stuck because your ML model is not yielding predictions that are accurate enough to meet your goals or business objectives.

Do you feel like you’ve hit a brick wall, and can’t improve accuracy any further?

What you can do about it:

* **Improve domain expertise for the problem you’re trying to solve** — perhaps you’re asking the wrong questions, perhaps the target variable you’re trying to predict isn’t going to solve the problem. Sometimes it can help to take a step back and consult with others, especially domain experts. They will likely have a better understanding for how the problem is solved today (without machine learning), and can provide guidance on what heuristics and measures of success look like. That way you can have a sensible benchmark against which to judge the effectiveness of an ML based approach.
* **Include more, varied training data** — I discussed in previous posts about how data is the lynchpin of ML models. Go back to your data sources, can you find more training examples or different features that would improve the accuracy of your ML model? Question whether the data you have is fit for solving the problem.
* **Feature engineering** — This is the process of modifying the features or input variables for your ML model. For example your training data might include raw output from a log file of bank transactions, but you don’t necessarily need every character in order to extract the data that will most influence your model. You could tap into your domain expert to help you figure out what those attributes might be.
* **Remove features that might be causing overfitting; start with a smaller less complex model, and add features more gradually —** overfitting is when you’ve created a model that matches the training data so closely that it fails to make correct predictions on new data. There are some simple ways to mitigate the effects of overfitting, first identify it by randomly splitting the training data into training and test datasets and compare the results — if your model performs well on the training set but poorly on the test set there’s a good chance you have overfitting. If you have identified overfitting, try retraining the model with a larger dataset.

For more advanced techniques to help address model accuracy, take a look at cross-validation, regularisation, and ensembling (links in Further Reading).

If you’ve found your way here because your own ML project has hit a roadblock, the aim of this post was to give you some new avenues to investigate. **Hopefully it gets you moving in the right direction again!**

**Until next time** 👋🏼

# 📚 Further Reading & Learning

* 🎥 [My explanation of TPUs](https://www.youtube.com/watch?v=2kSo7Az4ZOs) and how you can use them to speed up training TensorFlow models (yes things have moved on a bit it was recorded, but it does provide a nice visual explanation).
* 📑 [Overfitting in Machine Learning: What It Is and How to Prevent It](https://elitedatascience.com/overfitting-in-machine-learning)
* 📑 [How to Handle Imbalanced Classes in Machine Learning](https://elitedatascience.com/imbalanced-classes)
* 📑 [Best Practices for Feature Engineering](https://elitedatascience.com/feature-engineering-best-practices)

# 📇 References

[1] <https://jupyter.org/>

[2] <https://www.tensorflow.org/tutorials/structured_data/imbalanced_data>

