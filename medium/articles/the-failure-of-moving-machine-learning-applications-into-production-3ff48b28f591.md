[![Bruce H. Cottman, Ph.D.](https://miro.medium.com/fit/c/96/96/1*f958A_bXr8chKfPyY4rXLQ.jpeg)](https://dr-bruce-cottman.medium.com/?source=post_page-----3ff48b28f591--------------------------------)[Bruce H. Cottman, Ph.D.](https://dr-bruce-cottman.medium.com/?source=post_page-----3ff48b28f591--------------------------------)[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fc7bcf6635d7d&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fthe-failure-of-moving-machine-learning-applications-into-production-3ff48b28f591&user=Bruce+H.+Cottman%2C+Ph.D.&userId=c7bcf6635d7d&source=post_page-c7bcf6635d7d----3ff48b28f591---------------------follow_byline-----------)Nov 24, 2020

·7 min read·Member-only

[Save](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F3ff48b28f591&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fthe-failure-of-moving-machine-learning-applications-into-production-3ff48b28f591&source=--------------------------bookmark_header-----------)# Avoid These Data Pitfalls When Moving Machine Learning Applications Into Production

How often have you heard “The Machine Learning Application worked well in the lab, but it failed in the field. “? It is not the fault of the Machine Learning Model!

![]()**Image 1. Failure. Source:** [**Unsplash**](https://unsplash.com/photos/cGXdjyP6-NU) **by cuttersnap**## Warning!

This blog is not yet another blog article (YABA) on DataOps, DevOps, MLOps, or CloudOps.

I do not mean to imply xOps is not essential.

For example, MLOps is both strategic and tactical. It promises to transform the “ad-hoc” delivery of Machine Learning applications into software engineering best practices.

[## A guide to MLOps for data scientists

### Part 1: The continuous ML lifecycle

charnaparkey.medium.com](https://charnaparkey.medium.com/a-guide-to-mlops-for-data-scientists-28d7e86cd50e)## **What are the Symptoms of the Problems of Deploying Machine Learning Applications?**

We know the symptoms: Most machine-learning models trained in the lab perform poorly on real-world data [1, 2, 3, 4].

[## Why 90 percent of all machine learning models never make it into production

### Companies are lacking leadership support, effective communication between teams, and accessible data

towardsdatascience.com](/why-90-percent-of-all-machine-learning-models-never-make-it-into-production-ce7e250d5a4a)[## Why is it So Hard to Integrate Machine Learning into Real Business Applications?

### You’ve played around with ML, almost won a Kaggle competition and now you need to build AI into a real biz up, see what…

towardsdatascience.com](/why-is-it-so-hard-to-integrate-machine-learning-into-real-business-applications-69603402116a)# **What is the critical Problem with Machine Learning Success?**

Machine Learning created profits in the year 2020 and will continue to increase profits in the future. However, many problems hold back the progress and success of Machine Learning application rollout to production.

I focus on what it is the most significant problem or cause: the quality and quantity of input data in Machine Learning models [1,4].

We realized the quantity of high-quality data was the bottleneck in predictive accuracy when we started showing near, or above, human-level performance in structured data, imagery, game playing, and natural language tasks.

How many times do we look at the Machine Learning application lifecycle’s conceptualization to realize a Machine Learning model is not at the beginning (Figure 2)**?**

![]()Fi**gure 2. A Machine Learning Lifecycle: . Image Source:** [**Bruce Cottman**](http://@dr-bruce-cottman)We can research and improve the tools of the Machine Learning application lifecycle. But that only lowers the cost of deployment.

We can change only two components of Machine Learning for a large effect on the quality of the output predictive data:

1. Change the Machine Learning model;
2. Change the training input data.

Arguably, the Machine Learning model’s choice is not a critical part of deploying a Machine Learning application.

We have a “*good enough*” process or pipeline to choose and change the Machine Learning model, given a training input dataset.

However, when achieving State-of-the-Art (SOTA) results, the input data seems to have the most significant impact on the output predictive data (Figure 2).

We seem to know the cause: input data that was garbage results in garbage output predictive data. New data input to a trained Machine Learning model determines the accuracy of the output.

We divide Machine Learning input data into four arbitrary categories, defined by the Machine Learning application output accuracy.

## Case 1: It works!

GPT-3 is an example [6]. GPT-3 trained with an enormous amount of data [6]. GPT-3 is frozen in time as a transformer that you access through an API.

## Case 2: Data Drift

Concept Drift is a change in what to predict. For example, the definition of “what is a spammer.”

We do not cover Concept Drift here. I do not think of it as a problem but rather as a change in the solution’s scope.

An example of Case 2: Data Drift, is that *Case 1: “It works!,* is a temporal phenomenon. GPT-3 may degrade to an undesirable output in the future or the past because all languages change over the years.

An example of different meanings, depending on the time, is “It’s hot!”.

GPT-3 can be re-trained using an enormous amount of data from that period.

Another example is that Kaggle uses a static, unchanging dataset for a competition.

Usually, Kaggle sponsors find out the winning Machine Learning application can not be used on their incoming business data, the real world, because of Data Drift.

At first blush, the Machine Learning application needs to adapt to the changing environment using learning.

Microsoft “learned” there are bad actors out that caused Tay, a Machine Learning application, to learn “bad” things [5].

Tay, a Machine Learning application, “learned” (training fine-tuned or re-trained) and then “degraded to an undesirable output “on troll data input.


> **Tay was an** [**artificial intelligence**](https://en.wikipedia.org/wiki/Artificial_intelligence)[**chatter bot**](https://en.wikipedia.org/wiki/Chatterbot) **that was originally released by** [**Microsoft Corporation**](https://en.wikipedia.org/wiki/Microsoft_Corporation) **via** [**Twitter**](https://en.wikipedia.org/wiki/Twitter) **on March 23, 2016; it caused subsequent controversy when the bot began to post inflammatory and offensive tweets through its Twitter account, causing Microsoft to shut down the service only 16 hours after its launch…. According to Microsoft, this was caused by** [**trolls**](https://en.wikipedia.org/wiki/Trolling) **who “attacked” the service as the bot made replies based on its interactions with people on Twitter [5]**
> 
> 

The solution seems to be *Controlling* the adaption to change, which is a rapidly evolving field[8].

Another major case, which I classify as Data Drift, is when is a new feature appears in the input data.

MLOps advocates robust monitoring of Machine Learning applications and issuing a warning when there is change. The Machine Learning application may or may not issue a predictive output.

Frightening if the Machine Learning application is aiding a radiologist by seeking cancerous nodes in your lungs in a MRI image.

## Case 3: Not Enough Data

Many of my colleagues and I suffer from never moving our Machine Learning application into production. We are reasonably confident we have a “good enough” Machine Learning model, but we need more input training data to result in an acceptable output prediction accuracy.

## Case 4: Data Leakage

Data leakage, where some part of the training dataset has “leaked” into the test data set,


> **… is that in many of these cases, it took a long time for people to realize that something was wrong. It’s really not easy. These things are really insidious.** [**https://www.infoq.com/presentations/ml-systems-failure-production/**](https://www.infoq.com/presentations/ml-systems-failure-production/)
> 
> 

Data leakage is considered a Machine Learning setup problem and not a quality or quantity data issue (Step 3, Figure 3 or Step 2, Figure 4).

## Case 5: Underspecified Data

*Case 2: Data Drift* and *case 3: Not Enough Data* are subsets of the all-encompassing *case 4: Underspecified*.

Case 4 includes training data distributions that are *not* representative of the future input production data.

The general for “*not good enough input data*” is that model’s widely inaccurate prediction of real-world input data.

For some underspecified data, a quick Exploratory Data Analysis (EDA) shows that the training data distribution is *not* representative of the future input production (real world) data.

You might then try different Machine Learning models. While not as good at predicting the training data’s holdout test set, you hope for better results on the real-world input data.

If this works, it is a happy coincidence, and with a high probability, the Machine Learning application will fail soon.


> Tip: Always perform an EDA on the training and incoming real world data.
> 
> 

We identify the root cause of this behavior as underspecification of the training data into the Machine Learning pipeline. In general, the training set, when fed into many distinct Machine Learning models, is underspecified when there is more than one acceptable predicted output[9].

Underspecification of training data is shown often in the Machine literature **[9]**. Low predictive data results in the need for deep ensembles, double descent, Bayesian deep learning, and loss analysis, to name a few.

# Summary

Figure 5 summarizes each case by high or low quality or high or low quantity training data and high or low-quality predictive output data. For brevity, the default train data quality is high unless specified as low.

Figure 5 is a general diagnosis guide. Diagnosis of cases may differ from the quality and quantity of training data input to the Machine Learning models.

![]()**Figure 5. Train data and Predict Data by Case. Image Source:** [**Bruce Cottman**](http://@dr-bruce-cottman)We assert that DataOps, DevOps, MLOps, and CloudOps can lower the cost of production deployment [4,7,10,11], but not significantly chang.e the output predictive data quality.

In this blog post, we overviewed four significant input data categories that cause the failure of moving machine learning applications into production or leaving in production [1–9]. They are:

1. Data drift;
2. Not Enough Data;
3. Data Leakage; and
4. Underspecified Data

An upcoming series of blog posts cover current fixes and future solutions.

# **Reference**

[1] [Beyond Accuracy: What Data Quality Means to Data Consumers](http://mitiq.mit.edu/Documents/Publications/TDQMpub/14_Beyond_Accuracy.pdf).

[2] [Netflix Never Used Its $1 Million Algorithm Due To Engineering Costs.](https://www.wired.com/2012/04/netflix-prize-costs/)

[3] [5 data breaches: From embarrassing to deadly](https://money.cnn.com/galleries/2010/technology/1012/gallery.5_data_breaches/index.html).

[4] [Andrew Ng: Bridging AI’s Proof-of-Concept to Production Gap](https://crossminds.ai/video/5f9a11f026cd723d6a05efa4/?playlist_id=5f31d2696d7639fd8a7fc0d8).

[5] [Tay (bot).](https://en.wikipedia.org/wiki/Tay_(bot)#Legacy)

[6] [Language Models are Few-Shot Learners](https://arxiv.org/pdf/2005.14165.pdf).

[7] [Why Machine Learning Models Crash And Burn In Production](https://www.forbes.com/sites/forbestechcouncil/2019/04/03/why-machine-learning-models-crash-and-burn-in-production/?sh=4b26a5552f43).

[8] [Adapting on the Fly to Test Time Distribution Shift](https://email.mg2.substack.com/c/eJxNkN1uwyAMhZ8mXEZASpJecDFp6mtEBJwUjZ8MzLq8_aCdtEnIFj7Yx3xaIewxnfKIGUnJkBZr5DRNQrALMfJi2CxmYvOyJQCvrJOYCpCjrM5qhTaG1sDpdR7IXWo9jCNs86qvfB4FH0YxbGqjTAk6sVWTZrOoYiwEDRK-IJ0xAHHyjnjkbnjr-K2eVdnUr5A-wMHZgymt5uJeE6ec1sRYDVTUoJJvTcOtoF9yLElDN7zvSTUT3Fx8dHxsmgdji69agEd2gAjpV9HKH8ruoWo25wKcEyubEWPsyikVjPasd-z4NFqnb9VdqN95n8uaUemPXkdPkjR15VQ01CuiV6G-2huxp1yBLTX7EiyeCwS1OjAvlviC_0SD5wHyb79XsQJm80WwaeKkeppYpwb5_4c_onCbDQ)

[9] [Underspecification Presents Challenges for Credibility in Modern Machine Learning](https://arxiv.org/pdf/2011.03395.pdf).

[10] [What is Site Reliability Engineering (SRE)?](https://landing.google.com/sre/)

[11] [Common problems taking ML from lab to production](https://medium.com/data-for-ai/common-problems-taking-ml-from-lab-to-production-a2e3cf30799a).

