[![Sharan Kumar Ravindran](https://miro.medium.com/fit/c/96/96/1*1DT6HRN4ddYXJh_byccShA.png)](https://rsharankumar.medium.com/?source=post_page-----25fdc218a62--------------------------------)[Sharan Kumar Ravindran](https://rsharankumar.medium.com/?source=post_page-----25fdc218a62--------------------------------)[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F9fc8dfce153b&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Finvaluable-data-science-lessons-to-learn-from-the-failure-of-zillows-flipping-business-25fdc218a62&user=Sharan+Kumar+Ravindran&userId=9fc8dfce153b&source=post_page-9fc8dfce153b----25fdc218a62---------------------follow_byline-----------)Nov 5, 2021

·9 min read·Member-only

[Save](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F25fdc218a62&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Finvaluable-data-science-lessons-to-learn-from-the-failure-of-zillows-flipping-business-25fdc218a62&source=--------------------------bookmark_header-----------)# Invaluable Data Science Lessons To Learn From The Failure of Zillow’s Flipping Business

## What went wrong?

![]()Photo by [Daniel Tausis](https://unsplash.com/@greatmalinco?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/burning--house?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)# Introduction

Zillow is an online real estate company founded in 2006. It generated a revenue of $2.7 Billion in 2019. They have been doing so many things better for a very long time. This article is not about the things that went well. We would focus on the recent mistakes. That has led the company to stop its flipping business and cut its workforce by 25%.

First, What is a flipping business in real estate? When someone purchases a property with the intention of re-selling for a profit in the future. The company generally purchases a property for a comparatively lower value. Spend money on renovations and other improvements. Then sell the property for a higher price. It has been a popular technique used to make some quick money.

As you can understand the most important factor here is to predict the price of a property accurately. So that the property could be bought for a lower price and sold for a profit.

As per the [article here](https://www.zdnet.com/article/zillow-machine-learning-and-data-in-real-estate/), Zillow had about 43 million homes in their database in 2006 and they were able to predict the price of a property at 14% median absolute percent error. By 2017, they had about 110 million homes in their database. The error rate had reduced to 5%. The model used to predict the house price, had thousands of sophisticated statistical models and a huge amount of data.

# What went wrong?

For many reasons, the precision of their model started to degrade. This led to buying properties for a price much higher than its selling price. As per the [news here](https://www.npr.org/2021/11/03/1051941654/zillow-will-stop-buying-and-renovating-homes-and-cut-25-of-its-workforce), Zillow lost in excess of $300 million from its flipping business in the third quarter of 2021. As per this [Bloomberg article](https://www.bloomberg.com/news/articles/2021-11-01/zillow-selling-7-000-homes-for-2-8-billion-after-flipping-halt), Zillow is now looking forward to selling about 7000 homes valued at $2.8 Billion.

Below are some tweets that show how big the loss could be,

[Here is another article](https://vip.graphics/zillow-opendoor-housing-bubble-2021/?ref=twitter) that has many examples where Zillow is trying to sell a property at a price lower than their purchase price.

Based on these data it is clear the main reason for failure here is the inability to predict the price accurately. There are many lessons for data scientists from this failure. I will elaborate on the possible reason based on the content available in the public domain.

# 1. Data Quality

The primary factor for a machine learning model to perform well is good quality data. When the input to machine learning algorithm is garbage you can’t expect much from it.

[## 5 Reasons Zillow's Estimates Could Be Wrong

### Zillow is one of the most popular real estate databases online. Founded in 2006 by former Microsoft executives Rich…

www.investopedia.com](https://www.investopedia.com/articles/personal-finance/111115/zillow-estimates-not-accurate-you-think.asp)As per the above article, there are definitely possibilities for data quality issues. Zillow had been relying on both the data shared by the users and publicly available datasets. It would be too harsh to say the data quality is garbage in the case of Zillow. Especially because their model is doing good in a number of cases. But here the impact of the error is huge. Let me explain this with an example,

Zillow is looking to buy a property ‘ABC’, then plans to invest some money in improvements and sell it in a few weeks for a profit. Let’s say Zillow’s Zestimate evaluates the property ‘ABC’ at $500,000. If the model had a 10% error, it means that the actual price should have been $450,000. Now, Zillow has bought the property at a $50,000 premium. It will be very difficult for Zillow to make a profit on this property.

As mentioned in the above example, for every percent the model deviates from accurate prediction. The value attached to predictions is going off by a large value. A 10% error on a million-dollar property is $100,000. Just a few such properties could cause losses of over a million. Also, an error in predicting the price of a property in a suburb impacts the price of other nearby properties and in general the valuation of properties in the area itself.

A simple error in the data like the number of rooms in the property, distance from the nearest school, and other issues with key attributes could easily cause prediction errors. It could easily create a snowballing effect.

**Lesson**: In any data science problem, there should be a lot of focus on the quality of the data. It will be good to have metrics in place to measure the quality of data. In scenarios like Zillow where a small error could result in a big error, there should be a way to at least partially verify the data quality. This could help in catching quality issues before it causes a huge impact.

# 2. Dependency on Algorithms

Algorithms are good. They are very insightful. It helps a lot in decision-making. It is also true that they are prone to errors and issues. It is not recommended to rely completely on algorithms. Especially when you are solving a problem that has many uncertainties.

Housing price depends on a large number of factors. There are too many external factors that could have an impact on the housing price. It is not possible to monitor these external factors and incorporate them into the models. Because every change needs to be tested before being put to use.

When the use-cases don’t have a huge monetary impact. It is OK to proceed with some errors with the predictions. For example, let’s say we want to predict the lifetime value of a customer. A 10% error in the lifetime value of a customer would not severely impact the financials. But similar to the housing price there are scenarios when a small error is unacceptable.

**Lesson**: In scenarios where we can’t afford any deviations in the prediction. The model outputs should be used as a supplement to help the business user make a decision. For example, in the case of underwriting for an insurance company. The underwriting process has a huge financial impact. The model outputs should supplement with information but should not be made to make decisions. The decision should still be made by an underwriter. Because the underwriter is the domain expert, who can pick up things that could be potentially missed by the algorithm.

Next time when you are solving a data science problem. Always ask questions about the importance and the impact. If the risk is high then there should be a team of experts who oversees the model output and make a decision.

# 3. Gaming the system

When there is money involved then it is always possible for users to try and cheat the system.

[## The $300m flip flop: how real-estate site Zillow's side hustle went badly wrong

### nline shopping can be dangerous, as the US property website Zillow has belatedly come to realize. While many of us…



www.theguardian.com](https://www.theguardian.com/business/2021/nov/04/zillow-homes-buying-selling-flip-flop)The above article clearly articulates the possibility of the system being exploited. It is clear that few housing prices in a suburb could drive the property prices in the suburb up or down. Those who understand this could artificially increase the prices of homes in a suburb.

Want to know how? Let’s say there is an agent who holds many properties in a suburb. At first, the agent would sell some of the properties at an artificially higher price to a known internal contact. Then once the impact cascades to the other properties in the suburb. They sell the other properties at a bigger margin.

**Lesson**: The only way to ensure the system is not being exploited is by having a fraud prevention team. The fraud prevention team would have captured all the properties that have been sold way above or below the market price. To ensure those impacts are not being passed on to the model.

# 4. Selective Focus

It is clear in the case of Zillow there has been so much focus on the property and its price prediction. There hasn’t been enough focus on the buyers. It is ultimately a person who invests in the property. Not having a good understanding of the buyer could be problematic.

It is important for a real estate company to understand buyer behavior. Without knowing the buyers the demand can’t be accurately measured. Hence the price itself can’t be accurately predicted.

**Lesson**: Any data science problem should be analyzed from all possible angles. They should be studied in a holistic way. Also, it is not enough if you study before the model are put to use. The holistic data analysis should be continued even after the model is put to use. There could be changes to the circumstances.

To explain this in a simple way, let’s say we want to predict the customers who are churning. Having an internal focus to understand the various reasons why a customer is churning is one thing. This will tell a lot of information about the issues that make the customer churn. But, there could be other factors like competition offering better discounts. So, without approaching the problem from different angles it will not be possible to make a confident decision. In this example, it will not be enough if the focus is on the customers and the service provided. It also needs analysis on the interactions, sentiment on social media, competition strategies, and much more.

# 5. External Factors

The external factors play a huge role in any problems. In the case of housing price prediction as well there are so many external factors that could impact the price of a property.

For example, let’s say Zillow plans to buy a property ‘ABC’ for $500,000 and plans to invest $50,000 in renovations and plans to sell the property for a profit at $600,000.

For simplicity let us assume the buying price of $500,000 is accurate and reflects the current market price. Now, the planned budget for the renovations was $50,000 but due to external factors the demand for labor has increased and hence the renovations cost also increases by $25,000. On top of that due to unprecedented events like Covid, the demand for the house reduces. This now causes the price of the property to come down. Hence forcing Zillow to sell the property at a loss. Also, holding the property for a long time is not ideal as it would attract additional maintenance costs.

There are many properties owned by Zillow that are now being sold for a loss. There are many external factors playing a huge role. It is not always possible to identify all the external factors. But an effort should be made to incorporate these events into the model. Also, effort should be taken to diversify the risk.

In the case of Zillow, it is clear as per the [article here](https://www.bloomberg.com/news/articles/2021-11-01/zillow-selling-7-000-homes-for-2-8-billion-after-flipping-halt), they were adding too many properties to their portfolio than the properties being sold. Adding so many properties increased the demand for the labor required for renovations. Increased demand for labor increased the labor cost. Hence further worsening the situation.

# Final Note

There have been so many data science applications adding huge value to the business. Some of them help businesses in making money. Some of them help in solving a problem. Some of them help in improving the experience. But it is true there are some that fail too. Some of those failed don’t cause much damage whereas some create huge damages, like Zillow.

Mental models are very helpful in properly analyzing a business problem. It also helps in structuring the thought process so as to arrive at the best solution. Here is an article about using the first principles of thinking to solve a data science problem

[## How to use First Principle Thinking to solve Data Science Problems?

towardsdatascience.com](/how-to-use-first-principle-thinking-to-solve-data-science-problems-db94bc5af21)# Other References

[## The $300m flip flop: how real-estate site Zillow's side hustle went badly wrong

### nline shopping can be dangerous, as the US property website Zillow has belatedly come to realize. While many of us…

www.theguardian.com](https://www.theguardian.com/business/2021/nov/04/zillow-homes-buying-selling-flip-flop)# To stay connected

* If you like this article and are interested in similar ones, [follow me on Medium](https://rsharankumar.medium.com/). Become [a Medium member](https://rsharankumar.medium.com/membership) for access to thousands of articles related to career, money, and much more.
* I teach and talk about various data science topics on my YouTube Channel. [Subscribe to my channel here](https://www.youtube.com/c/DataSciencewithSharan).
* Sign up to [my email list here](https://chipper-leader-6081.ck.page/50934fd077) for more data science tips and to stay connected with my work
