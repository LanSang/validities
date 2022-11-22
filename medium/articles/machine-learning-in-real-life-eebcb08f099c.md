[![Rebecca Vickery](https://miro.medium.com/fit/c/96/96/1*rhvwW5suGypWKG_iJqFWcA.jpeg)](https://rebecca-vickery.medium.com/?source=post_page-----eebcb08f099c--------------------------------)[Rebecca Vickery](https://rebecca-vickery.medium.com/?source=post_page-----eebcb08f099c--------------------------------)[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F8b7aca3e5b1c&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fmachine-learning-in-real-life-eebcb08f099c&user=Rebecca+Vickery&userId=8b7aca3e5b1c&source=post_page-8b7aca3e5b1c----eebcb08f099c---------------------follow_byline-----------)Sep 6, 2019

<person role="Data science lead">
	https://www.linkedin.com/in/rebecca-vickery/?originalSubdomain=uk
</person>

·7 min read·Member-only

[Save](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Feebcb08f099c&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fmachine-learning-in-real-life-eebcb08f099c&source=--------------------------bookmark_header-----------)# Machine Learning in Real Life

## What it is really like to develop a model for a real-world business case

![]()Photo by [Ben White](https://unsplash.com/@benwhitephotography?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/search/photos/world?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)Have you ever taken part in a Kaggle competition? If you are studying, or have studied machine learning it is fairly likely that at some point you will have entered one. It is definitely a great way to put your model building skills into practice and I spent quite a bit of time on Kaggle when I was studying.

If you have previously taken part in a machine learning competition then your workflow may have looked a little something like mine did:

1. Download some data (probably one or several CSV files).
2. Perhaps do a little cleaning, or chances are the data set may already be clean enough.
3. Carry out some preprocessing such as converting categorical data into numerical data.
4. Run the data through a variety of suitable models until you find the best one.
5. Spend a long time on hyperparameter tuning, feature engineering and model selection as a very small improvement might mean you leap several places up the leader board.
6. The end
However, if you are developing a machine learning model for a real-world business application the process will look quite different. The first time I deployed a model in a business scenario these differences were quite surprising in particular how much time was spent at certain stages of the workflow. In the following post, I wanted to describe the process for developing a model in a business setting and discuss these differences in detail and explain why they exist.

The workflow, in a business case, will have a lot more steps and may look a little something like this.

1. Translate a business question into a data question.
2. Consider how a machine learning model can connect to the existing tech stack.
3. Spend a lot of time extracting, transforming and cleaning data.
4. Spend a lot of time on exploratory analysis, preprocessing and feature extraction.
5. Build the model.
6. Select the best model that can be integrated into the existing tech stack with the least amount of engineering.
7. Optimise the model until it is ‘good enough’ considering the business value.
8. Deploy the model.
9. Monitor the model in production.
10. Retrain when necessary.
11. Build version 2.
12. Continue until there is no longer a business use for the model.
In the rest of this post, I am going to go into a little more detail on each of these steps.

## You will need to translate a business question into a data question

In a Kaggle competition, the problem to solve will be clearly defined upfront. For example in one of the latest competitions called ‘[Severstal: Steel Defect Detection](https://www.kaggle.com/c/severstal-steel-defect-detection/overview)’ you are given some curated data and the problem is clearly stated in the form of a data problem.


> Today, Severstal uses images from high frequency cameras to power a defect detection algorithm. In this competition, you’ll help engineers improve the algorithm by localizing and classifying surface defects on a steel sheet.
> 
> 


In a real business problem, it is unlikely that you will necessarily be asked to build a specific type of model. It is more likely that a team or product manager will come to you with a business problem. This might look something like this, and sometimes the problem may not even be this well defined.


> The customer service team want to reduce the time it takes the business to reply to customer emails, live chats and phone calls in order to create a better experience for customers and improve customer satisfaction metrics.
> 
> 

From this business request, you will need to work with the team to plan out and design the best solution to this problem before you can make a start on building the actual model.

## Data will not be clean

The data you work with will almost certainly not be clean. There will usually be missing values to work with. Dates might be in the wrong format. There may be typos in values, incorrect data and outliers. Before you get anywhere near actually building the model the chances are that a lot of time will be spent in removing erroneous data, outliers and handling missing values.

## You may have to get data from different sources

Similarly, all the data you need may not be from one simple source. For a data science project, you might need to source data from a combination of any of the following: SQL queries (sometimes across multiple databases), third-party systems, web scraping, API’s or data from partners. Similar to data cleaning this part can often be a very time-consuming part of the project.

## Feature selection is very important

In a machine learning competition generally, you have a given data set with a finite number of variables that you can use in your model. Feature selection and engineering are still necessary but you have a limited number of variables to select from in the first place. When working on a real-world problem you will more than likely have access to a vast range of variables. As a data scientist, you will have to select the data points that are likely to result in a good model to solve the problem. Therefore you will need to use a combination of exploratory data analysis, intuition and domain knowledge to select the right data to build the model from.

## Building the model is the smallest part of the process

Having spent all this time in selecting, extracting and cleaning the data the time you spend actually building the model will be very small in comparison. For version 1 of a model in particular, where you may want to use the model as a baseline test, then you may in the first instance only spend a small amount of time on model selection and tuning. Once the business value has been proven you might then invest more time in optimising the model.

## You will spend less time than you think tuning the model

In a Kaggle competition, it is not unusual to spend weeks on tuning a model to get a small improvement in the model score. As this small improvement is likely to boost you quite a few spaces up the leader board. For example in the current Severstal competition, the difference in score between position 1 and 2 on the leaderboard is currently only 0.002. It would definitely be worth spending time to improve your score by a very tiny amount as it might bag you the top prize.

![]()[Kaggle.com](https://www.kaggle.com/c/severstal-steel-defect-detection/leaderboard)In business, the time that you spend on tuning a model is a cost. The company has to pay your wage for the number of days or weeks that you spend on this task. As with everything there needs to be a return on this investment in the form of business value. It is quite unlikely that a business use case for a model would provide enough value to justify spending days on improving the accuracy of a model by an increment of 0.002. In reality, you will tune the model until it is ‘good enough’ rather than ‘the best’.

## You won’t necessarily use the best model

<quote label="tradeoffs">
This leads me onto my next point which is that you won’t always use the best model or the newest deep learning methods. Quite often you will be able to deliver more business value with a simpler model such as linear regression. Which takes less time (and therefore costs less to build) and is more explainable.

Your model will have to connect to some kind of endpoint such as a website. The existing tech stack for this endpoint will have a lot of bearing on the type of model you will deploy. There will often be a compromise from both data scientists and software engineers on minimising the engineering work at both ends. If you have a new model which would mean a change to an existing deployment processes or extensive engineering work then you would have to have a very good business case for deploying it.
</quote>

## The work doesn’t stop there

Once in production, the model will need to be monitored to ensure that it is performing as well as it did during training and validation and to check for model degradation. 
<quote label="data">
For a number of reasons the performance of a model usually degrades over time. This is due to the fact that data will change with time, as customer behaviour changes for example, and therefore your model may start to not perform as well on this new data. For this reason, models will also need to be retrained regularly to maintain business performance.
</quote>

Additionally, most businesses will have a test and learn cycle for deploying machine learning models. So your first model will usually be version 1 to form a baseline for performance. After that you will make improvements to the model, maybe changing features or tuning the model, to deploy a better version and test against the original model.

Both of these processes may be ongoing until the business case no longer exists for this model.

## Conclusions

This post was partly inspired by this tweet from Chip Huyen.

![]()Part of the reason why it is hard to recruit for machine learning roles is that many of the realities of deploying machine learning in business that I have discussed here are not taught in these courses. That is why I am such a fan of the practical first approach to learning and why I think that industrial placements, internships and junior data science roles are so important.

There is light at the end of the tunnel however as technology in this space is rapidly evolving helping to automate processes such as data cleaning and model deployment. However, we still have a way to go so it is still vitally important for data scientists to develop software engineering skills, improve communication skills, and to have a resilient and persistent mindset, alongside the typical data scientist skillset.

Thanks for reading!

