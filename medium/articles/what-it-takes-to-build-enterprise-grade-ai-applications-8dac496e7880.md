[![Caroline Zaborowski](https://miro.medium.com/fit/c/96/96/1*ZM9rtQH4W1KjXSABwQD8PA.jpeg)](https://medium.com/@carolinezunckelzaborowski?source=post_page-----8dac496e7880--------------------------------)[Caroline Zaborowski](https://medium.com/@carolinezunckelzaborowski?source=post_page-----8dac496e7880--------------------------------)[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F8a86e2b0874b&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fwhat-it-takes-to-build-enterprise-grade-ai-applications-8dac496e7880&user=Caroline+Zaborowski&userId=8a86e2b0874b&source=post_page-8a86e2b0874b----8dac496e7880---------------------follow_byline-----------)Aug 15

·13 min read[Save](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F8dac496e7880&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fwhat-it-takes-to-build-enterprise-grade-ai-applications-8dac496e7880&source=--------------------------bookmark_header-----------)# **What it takes to build enterprise-grade AI applications**

<quote label="chief_technology_office">
	https://www.linkedin.com/in/caroline-zaborowski-b3060ab/?originalSubdomain=za
</quote>

## The power of end-to-end thinking

![]()Sonasoft © 2022AI has often been called the fourth industrial revolution. It is undoubtedly revolutionizing the way businesses operate. But building enterprise-grade AI applications is extremely challenging. My data science career has been focussed on helping companies deliver robust AI solutions. This is especially true in my current role at [Sonasoft](https://www.sonasoft.com/) where I spend my time building end-to-end AI applications.

Over time, I have learned exactly what it takes to deliver reliable and robust AI at scale and I wanted to share some of these insights.

# What actually is enterprise AI?

When most people think of AI they envisage things like self-driving cars, computer-generated art, or advancing drug discovery by predicting protein structures from their amino-acid sequence. These require the development of deep learning and large-scale neural networks at the cutting edge of AI research. But how relevant are they to big business? Well, if your business is building cars or selling drugs, they are 100% relevant. However, for most businesses, they are unnecessarily complex and expensive to build and deploy. So, that raises the question. What actually can AI do for most businesses?

A few years ago, [McKinsey](https://www.mckinsey.com/~/media/mckinsey/featured%20insights/artificial%20intelligence/notes%20from%20the%20ai%20frontier%20applications%20and%20value%20of%20deep%20learning/notes-from-the-ai-frontier-insights-from-hundreds-of-use-cases-discussion-paper.ashx) analyzed hundreds of AI use cases across a number of industry verticals. Their findings were quite striking. The most valuable use cases for AI came when it was used to boost existing business intelligence and analytics. In other words, the best AI use cases for big business are, frankly, the most mundane ones. This shouldn’t come as a surprise though. Firstly, if you already have a good understanding of your data, then you are likely to create much more robust AI solutions. Secondly, what matters for many businesses is things like improved efficiency, cost savings and the resulting better margins. These are usually achieved through compounding incremental changes rather than one-off revolutionary transformations.

In my experience, three forms of AI have the greatest impact for enterprises:

1. **Forecasting.** Many aspects of business rely on having accurate estimates of future outcomes. How much stock will be needed next week to meet demand? What is the price going to be next month? All these things can be answered with forecasting models that combine historical data with current state to predict some near future state.
2. **Anomaly detection**. Often in business you need to spot rogue or anomalous events. For instance, is this transaction legitimate, or might it be fraudulent? Should this file be being accessed, or is a hacker trying to steal my data? This is where anomaly detection models come to the fore.
3. **Classification.** Sales teams need to classify which leads are the strongest versus which should be ignored. Equally, if you are in the business of lending money, you need to know which people are good credit risks or not. These are just a couple of examples where classification models can help you make better decisions.

As all the above show, one of the key wins for AI is in helping businesses to make decisions informed by reliable and statistically significant data insights, with data being the operative word.

# Data is fundamental

I cannot overemphasize enough the fundamental role of data in the delivery of AI-driven uplift. The success of Enterprise AI will be dictated by the quantity, quality, and scope of data to which you have access. Many AI applications rely on supervised learning, for which you need accurately labeled data. Even when you are using unsupervised learning for anomaly detection, the more data you have, the more accurate your results. And deep learning algorithms are generally data hungry, requiring huge volumes of training data to ensure that their many parameters are tuned so as to ensure that the final model can generalize well to unseen scenarios.

Of course data volume is not a sufficient qualifier. [CRISP-DM](/why-using-crisp-dm-will-make-you-a-better-data-scientist-66efe5b72686) is a widely used framework for data mining and data science projects. Two out of the six steps are related directly to the data; data understanding and data preparation. It is my firmly held belief that the data scientist must understand how the data was acquired and should be involved in as much of the data engineering process as possible. Whenever I work on a new enterprise AI project for a company, I always insist on access to all their data. And I mean ALL their data. I also talk to their subject matter experts (SMEs) to understand what the data is, where it comes from, etc. If you don’t have the option to collect and engineer the final dataset yourself, it’s critical that you spend time understanding the process and any decisions that went into sampling it, paying special attention to potential sources of data leakage.

![]()Sonasoft © 2022The next critical step is to get a holistic view across all the data to determine whether it is suitable for AI. Key things I look out for include:

* **What are the characteristics of the data?** Does it require supervised learning, and if so, what is the nature of the target? Knowing if the label you are trying to predict is imbalanced or not will have important consequences for data preprocessing steps. It will also influence the choice of the metric used to assess performance of the resulting model.
* **What role does time play in the data?** Timestamping the data as much as possible goes a long way to ensuring that you avoid including features that could only be available after the target value has been predicted.
* **Are there any gaps in the data?** If so, are they significant or not? Understanding the source of these gaps and their nature (missing at random “MAR” or missing not at random “MNAR”) will dictate the appropriate treatment, each of which has its pros and cons.
* **Does there appear to be any seasonality or other time-based pattern in the data?** If so, how can this be best exploited?
* **Do any correlations stand out?** If so, can the SMEs provide a plausible explanation for these? This is important to distinguish true relationships from spurious noise.
* **Might any external data help augment this data?** For instance, is this data affected by the weather at all?

All time spent evaluating the potential of the data to address the identified business problem is time well spent. This mitigates the risk of wasted time and resources further downstream. I will only move onto data engineering once I’m confident that this has been done with due care and attention to avoid making ill-placed assumptions and introducing bias.

# Avoiding assumptions and bias

Us humans are error-prone and biased, which is why it is no surprise that the data we collect suffers from the same issues. There are many sources of flawed data, such as collection practices which result in incomplete data, historical inequalities being inbuilt in current data, or data which reflects poorly evidenced assumptions. Often company culture and beliefs about data can be so strongly held that you aren’t even aware that you are making an assumption. For example, “We always see an increase in revenues at the end of the month because that’s when people are paid.” That may very well be true, but it might also be because your system always takes subscriber direct debits on the last working day of the month. This assumption might lead to the exclusion of high value features from your model.

Naturally, machine learning algorithms reflect the biases of their makers or the data used to train them, and in some situations can even amplify them. This is commonly known as algorithmic bias. One of the most well known cases of algorithmic bias was evidenced in the [COMPAS system](https://en.wikipedia.org/wiki/COMPAS_(software)#Accuracy) which was developed to predict whether or not a perpetrator was likely to recidivate. The algorithm’s performance was optimized for overall accuracy yet gave false positive predictions for recidivism for African American ethnicities at double the rate when compared to that of Caucasian ethnicities.

Even when bias in data is identified, too often a naive approach is taken to address it. For example, if you suspect gender bias is present, you might choose to suppress gender within the data used to train the model. However, this cannot be relied upon to remove the actual bias because gender may be influencing other features in the data. Even the biggest multinationals can get caught out by this, as Apple discovered when they first launched their credit card. Despite having a system that ignored the applicant’s gender, it still gave women lower credit limits due to training on historically biased dataset and to [inferring gender](https://www.wired.com/story/the-apple-card-didnt-see-genderand-thats-the-problem/) from other data.

AI solutions must be expected to achieve the same level of trustworthiness as we demand from human decision-makers. It’s up to their human developers to ensure this is delivered. Data scientists need to recognise these typical traps and then proactively look for the resulting bias. Bias testing should be a part of every AI product development cycle, assessing both the incoming data and the final model outcomes. Once any bias has surfaced, the ethics of likely outcomes should be considered in the context of the use case. Then, the fairness policy and objectives of the enterprise should dictate the appropriate steps to mitigate against it.

# Performance means scalability rather than perfection

Every data scientist wants to deliver value. Value is commonly (and mistakenly) defined as a model that gives the best possible performance across as broad a range of input data as possible. On the face of it this might seem laudable. After all, an inaccurate AI model is going to be at best useless and at worst damaging. However, this is a case of shades of gray. There is no such thing as a perfect model, and focusing on looking for one causes many issues. Firstly, it is likely to slow down the process dramatically which can impact support for the AI program all together. But worse, it also often sacrifices real-world model performance. There’s no point in developing a huge neural network model if your production environment lacks hardware support for neural networks. <quote label="prediction">Lastly, the most accurate solution is not necessarily the one which will deliver the best improvement in the bottom line of the business. The benefit of a correct prediction is almost never equal to the cost of a wrong prediction and ignoring this asymmetry can severely impact the net value delivered.</quote>

Instead of chasing perfection, you should seek to find a model that is good enough for the use case at hand, with “good enough” being defined against a well thought out benchmark. Upgrades to the solution can come later with a more exhaustive model competition and smarter hyperparameter tuning. And well before you are thinking about deployment, you need to ask yourself a few important questions:

* Is the model able to run fast enough at scale?
* Can you deploy the model into your existing backend systems?
* Will you be able to connect the required data feeds?
* How will you access the model outputs and make use of them?

<quote label="utility">
Of course, you also need to do your homework in terms of understanding how the resulting model outputs will be utilized and the benefits and risks involved. Taking this approach will see a far more rapid and *real* return on your business’ investment and a higher chance of support from senior management, which is vital for seeing an AI transformation program to completion.</quote>

<quote label="utility">
The take home is that any AI application should be built with its business impact in mind. This requires many more considerations than just how well the model performs for a given choice of evaluation metric.</quote> So, treat your AI applications just like any other mission-critical software that you develop and build them to be robust, scalable and maintainable.

# Monitor all things

MLOps (Machine Learning Operations) is an approach which takes the principles behind DevOps and applies them to the field of machine learning. The objective is to streamline the process of productionizing AI applications. But seeing an AI application deployed into production is not the end of the AI lifecycle. MLOps also pertains to the monitoring and maintaining (or operation) of deployed solutions. Once a solution is deployed, you need to make sure it keeps performing as expected. This is a critical step required to ensure success. There are a few areas which require focus.

## Data integrity

Having data which is consistently accurate and reliable is absolutely critical for maintaining the performance of AI applications. But maintaining a high level of data integrity is hard given the dynamic nature of the complex systems involved. Detection of poor data is not straightforward as a deployed application may continue to produce results despite any data issues. So, you need to actively monitor for data for issues such as too many missing values, range violations and type mismatches.

## System health

AI applications are inherently processor and data heavy. That makes them vulnerable to backend performance problems. Monitoring for deviations in trends in CPU, memory, disk and network usage is critical in order to identify issues which may impact keeping the solution fully operational.

## Model drift

<quote label="drift">
Even highly accurate models tend to suffer from a slow degradation in performance with time. This happens because they were trained with a given set of data acquired under a set of conditions which inevitably change as time goes on. This is known as model drift and there are various types.
</quote>

**Concept drift** describes a change in the relationship between the input data features of the model and the target variable. For instance, imagine you have a model that helps improve the efficiency of stock distribution. When the model was trained, it was based on your existing manual stock distribution. But once the model is running, the underlying relationships between the model features and actual stock levels change. This is because you are no longer relying on manual approaches. In other words, there is a drift purely as a result of the model existing. This drift is typically accompanied by a drop in the performance of the solution as it signals a change in the relationship being modeled. Monitoring if evaluation metrics differ from the expected performance levels set in the development phase could signal concept drift.

**Label drift** is measured as a change in the likelihood of real values of the target variable compared with that seen in training. For instance, the onset of the pandemic saw a higher default rate on mortgage payments. This would have manifested as label drift in the case of a model predicting the likelihood of debt servicing. Understanding how the distribution of ground truth is changing should assist with understanding the changes taking place.

However, both concept and label drift can only be monitored if the labels associated with the model’s predictions are made available for comparison. Given that ground truth may only be returned a long time after the prediction is made and utilized, it’s important to look for other drifts which don’t depend on labels which can give clues to near term performance issues.

**Feature drift** refers to changes in the nature of the input data features in the production data relative to expectations set during training. These changes in the data usually reflect the prevalence of business or environmental conditions previously unseen or seen less frequently when the model was trained. For instance, changes to credit lending criteria within a bank would trigger feature drift in the creditworthiness being utilized by a debt servicing model.

**Prediction drift**, or monitoring the change in the distribution of the predicted output, can assist with detecting multivariate change in the nature of the input data features. The approval of lending to traditionally less creditworthy clients post deployment would lead to a shift in the probability distribution of debt servicing outcomes with a higher overall likelihood of default.

Monitoring and remedying the above typically requires specialist tools. There are a host of AI and MLOps platforms designed to assist, although they usually require an experienced data scientist. The key thing is to quickly determine the root cause of any problems. This should be the key performance metric you consider when you are selecting an MLOps tool. This will reduce the impact of poor model performance on business operations leveraging the model’s data products.

# AI is an end-to-end problem

All too often I see companies thinking they can solve AI in a piecemeal fashion. They realize that AI will help them so they sign up for an AI platform that promises to transform their business for them. Then they try to develop a working AI model. They quickly discover they need expert assistance, so they employ a team of data scientists. After a few months they have a working model which the DevOps team is asked to integrate into production. At this point they hit all sorts of pain. Once deployed, the team thinks that the model can be left to get on with things by itself. But within a few months, they find that the model’s predictions are no longer delivering business value.

![]()Sonasoft © 2022Building successful enterprise AI applications actually requires an end-to-end approach. At every stage in the process you need to remember that your application will need to be deployed. It needs to get its data in a timely fashion. It needs to be able to run at scale in your production systems. It needs to deliver actionable results to the people that need them. Above all, it must seamlessly merge with your existing business processes. This end-to-end view is what makes the difference between success and failure.

# Ensure the whole team is on board

The final requirement for any successful enterprise AI project is buy-in from the rest of the company. AI has suffered something of a bad reputation in the last couple of years. One widely cited statistic is that [87% of AI projects don’t make it to production.](https://venturebeat.com/2019/07/19/why-do-87-of-data-science-projects-never-make-it-into-production/)

There are various factors contributing to this statistic. For a start, there is wide mistrust of AI, with many employees believing that it will lead to a machine taking over their jobs, or more biased and less accurate decisions than human-led systems. This typically stems from a lack of effort to make AI explainable. The term [explainable artificial intelligence (XAI)](https://en.wikipedia.org/wiki/Explainable_artificial_intelligence) refers to a set of processes and methods that help humans to understand, and therefore trust, the results generated by AI solutions. Exploiting XAI and taking the time to show that the ultimate objective is to help them do their job better should go a long way to improving buy-in.

Secondly, many people make unrealistic claims regarding how well AI can perform. They promise things like halving your costs, or doubling productivity. The reality is in most well-run companies, AI will find you an extra 10% to 20% edge. But that will probably translate to a huge increase in profitability.

Lastly, AI transformation often requires a change in company culture, and this has to come from the very top. That might mean helping to educate the CEO and CTO about the potential uplift of AI applications and the risk of falling behind competitors by delaying the inevitable.

# Conclusions

AI is definitely a game-changing technology. But building and deploying successful enterprise AI applications is hard. If you want to build a successful AI application plan carefully, build for production, and set realistic expectations. And always treat it as an end-to-end problem to increase your chances of getting it right.

