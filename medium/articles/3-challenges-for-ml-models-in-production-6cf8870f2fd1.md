[![Soner Yıldırım](https://miro.medium.com/fit/c/96/96/2*i9nJ2AW_szQp4jOe4qntjw.jpeg)](https://sonery.medium.com/?source=post_page-----6cf8870f2fd1--------------------------------)[Soner Yıldırım](https://sonery.medium.com/?source=post_page-----6cf8870f2fd1--------------------------------)[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F2cf6b549448&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2F3-challenges-for-ml-models-in-production-6cf8870f2fd1&user=Soner+Y%C4%B1ld%C4%B1r%C4%B1m&userId=2cf6b549448&source=post_page-2cf6b549448----6cf8870f2fd1---------------------follow_byline-----------)Jun 9

·4 min read·Member-only

[Save](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F6cf8870f2fd1&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2F3-challenges-for-ml-models-in-production-6cf8870f2fd1&source=--------------------------bookmark_header-----------)# 3 Challenges for ML Models in Production

## These should not be overlooked.

![]()Photo by [Dwayne Hills](https://unsplash.com/@dhillssr?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/factory?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)A big portion of machine learning (ML) models never make it into production. It is one thing to create a model in a Jupyter notebook but deploying it into production and maintaining it as a continuous service is another world. It is a process that involves many interrelated steps which can be grouped under the term machine learning operations, [MLOps](/from-jupyter-notebooks-to-real-life-mlops-9f590a7b5faa).

MLOps is so important that I think it is the next big thing in data science, or it is already a big thing 😊. In order to generate long-term business value with machine learning, we need to adhere to MLOps principles from data acquisition to model monitoring.

Maintaining ML models in production has some challenges, which need to be addressed and properly handled to make the entire system reliable and robust. In this article, we will go over 3 of such challenges.

## 1. No human intervention

ML models are highly likely to make better predictions than us. They work much faster and more scalable than us. On the other hand, one shortcoming of ML models is that they do not have common sense. Therefore, it is possible for an ML model to produce unrealistic results.

The heart of ML models is the training data. They reflect the structure and relationships that exist in the data it was trained on. ML models are much better than us in revealing the dependencies in the data. However, when they encounter something new, they might produce absurd results.

Since it is likely to have no human intervention in an ML system in production, there is always the risk of having results that do not make sense.

The impact of such risks varies depending on the application. In the case of a recommendation engine, it won’t be critical. However, if we have a forecast engine that automatically feeds the supply change, then things might go really wrong.

These risks should not be considered as a deficit. We just need to keep them in mind. We can overcome this challenge by retraining our models frequently, checking the results based on some limits, and monitoring the models in production.

## 2. Data changes

The world constantly changes. The only thing that does not change is the change itself.


> The only constant in life is change — Heraclitus.
> 
> 

<quote label="data">Everything changes with the world, and so is the data. It is inevitable to have previously unseen data points and we expect our model to produce results for them.<quote label="">

Consider a spam email detection model. Scammers change their strategies and create new kinds of spam emails. A model that was not trained on these new examples is likely to fail catching them. This concept is called data drift and can cause serious issues if not handled properly.

Another change that has an impact on model accuracy is called concept drift. It occurs when the relationship between the dependent variables and the target variable changes. A typical example of concept drift can be observed in a fraud detection model. If a transaction that was not classified as fraud in the past can be fraud now.

Both data and concept drift can be handled with implementing robust and reliable monitoring system and feedback loops. We can then decide when to retrain our models.

## 3. Communication between stakeholders

It takes different sets of skills to build an ML system. In general, data scientists, data engineers, software engineers, DevOps engineers, and subject matter experts participate in the machine learning life cycle.

Subject matter experts, in collaboration with data scientists, define the business problem to be solved with machine learning. They set up KPIs for measuring the performance of the model.

The primary responsibility of data engineers is data acquisition and ETL operations. Software engineers and DevOps engineers handle the IT related tasks.

The roles and tasks may vary depending on the company. What does not change is that robust and effective communication between different stakeholders are required to make things work. Otherwise, we end up having unnecessary time gaps which can even make the project fail.

ML models need to be deployed into production in order to generate business value. It is definitely not an easy task. It goes beyond the skills of a data scientist to create such a system. However, knowing the risks associated with maintaining an ML model in production and taking preventive actions can make things easier.

*You can become a* [*Medium member*](https://sonery.medium.com/membership) *to unlock full access to my writing, plus the rest of Medium. If you already are, don’t forget to* [*subscribe*](https://sonery.medium.com/subscribe) *if you’d like to get an email whenever I publish a new article.*

[## Join Medium with my referral link - Soner Yıldırım

### As a Medium member, a portion of your membership fee goes to writers you read, and you get full access to every story…

sonery.medium.com](https://sonery.medium.com/membership)Thank you for reading. Please let me know if you have any feedback.

