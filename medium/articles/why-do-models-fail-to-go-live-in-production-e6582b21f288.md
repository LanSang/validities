[![Giovanni Bruner](https://miro.medium.com/fit/c/96/96/1*mcNzp9g3XpSXOHQ21b7ZgA.png)](https://misclassified.medium.com/?source=post_page-----e6582b21f288--------------------------------)[Giovanni Bruner](https://misclassified.medium.com/?source=post_page-----e6582b21f288--------------------------------)[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F14f159c7c0&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fwhy-do-models-fail-to-go-live-in-production-e6582b21f288&user=Giovanni+Bruner&userId=14f159c7c0&source=post_page-14f159c7c0----e6582b21f288---------------------follow_byline-----------)Dec 13, 2020

·6 min read[Save](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fe6582b21f288&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fwhy-do-models-fail-to-go-live-in-production-e6582b21f288&source=--------------------------bookmark_header-----------)## [Office Hours](https://towardsdatascience.com/tagged/office-hours)

<person role="Head of Fraud Intelligence">
https://www.linkedin.com/in/giovanni-bruner-22300937/?originalSubdomain=it
</person>

# Why do models fail to go live in production?

<quote label="utility">
## Creating models is easier today. Creating models that have an impact in your organisation remains terribly hard.
</quote>

Last month I was asked to give a Conference talk on the subject of Data Science models so often failing to go live in production. After all, we have all come across “it works well on my machine” situations and we all have a general idea of why it’s often the case.

Many bloggers and commentators have provided thorough explanations of what leads a data science project to premature death, but here are my three favourites:

1. **Lack of commitment from management and lack of a proper data strategy**. Here, a usual pattern is for companies to hire data scientists thinking that they are in the business of black magic. Then, without a clear idea of what data scientists should be doing and without a real data strategy, they realise that the company money was badly wasted. Finally, they set the data scientists free to go somewhere else.
2. **Lack of integrated DevOps and siloed technology teams.** For a model to go into production you need engineers that are capable of doing so right? Sometimes it happens that a company hires plenty of data scientists but no data engineers that can take a prototype and transform it to a product in a production environment. Often the existing technology teams have no idea of what a machine learning pipeline actually requires. The consequence is that the models remain on the data scientists notebooks and machines, left there to die of a natural, melancholic death.
3. **The Data Science team is disconnected from business objectives.** Sometimes the Data Science team sits too far from the business, failing to have a clear understanding of how their company makes money (this is the flip side of problem number 1). When this happens framing problems in a way that makes business sense is difficult, data scientist tend to put too much focus on “cool” projects rather “useful” projects, getting a buy-in from business stakeholders becomes hard, frustration grows. The team is condemned to the irrelevance.

![]()Photo by [Franki Chamaki](https://unsplash.com/@franki?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)## What should you do to make sure your data science projects are impactful?

One answer to this question is straightforward: you need to make sure you have **the right people at the table** [1]. Yes, we know data scientists are meant to be the legendary unicorns everybody talks about, but real life especially in big corporates and heavily regulated markets is a different story. Who should sit at the Data Science table is clearly arguable, and everybody might have their own version, but I believe it’s at least necessary to have the key business stakeholders lined up on the project goals and budget, to have a strong blessing from Compliance and IT Security officers, to have somebody who is capable of creating a production pipeline from an engineering stand point and project managers or business analysts to function as a bridge between tech and business/operations.

![]()**Fig 1.** Who should sit at a Data Science project table**Ill defined problem statements** are another key issue. <quote label="formative">Getting the problem definition straight is harder than what people tend to think</quote>, as Thomas Wedell-Wedellsborg wonderfully argues in [this article](https://hbr.org/2017/01/are-you-solving-the-right-problems) [3]. Practitioners tend to rely too much on conceptual maps like the one in Fig 2, before spending a sufficient amount of time defining the problem.

![]()Fig 2. Machine Learning Algorithm Types [2]I’ve seen too many times **project definition** starting with a generically defined problem to solve, followed by a leap forward to which algorithm should be used. When this happens it’s highly likely that the downstream product will fail to see the light. Whether a supervised or unsupervised learning algorithm is to be used should not be the first questions to ask, it’s more useful to reflect on what use case type the problem we are trying to solve falls into.

![]()Fig 3. Project Definition FlowsTypical use case types with Machine Learning are listed in Fig 4. and each of them carries significant differences in the way features are built and in the kind of algorithm that is more appropriate.

![]()Fig 4. Some use case typeAs a mean of example let’s say that we are tasked with solving the problem of finding the right customer target for an e-mail campaign. The goal is to find the customers that are more likely to make an action following a nudge. This seems clear enough. <quote label="formative">The temptation could be to jump straight into reasoning on whether to use this or that gradient boosting classifier, however more work is needed on defining the problem.</quote> Do we want to find the right customers building a predictive algorithm for the target action? Or is it more appropriate to apply Causal Inference techniques to predict which customer will make the action **given** the nudge [4]? In some cases, where we run many campaigns that change all the time and building a model for each of them is intractable, is it more appropriate to build a Similarity model ?

As we can see, <quote label="formative">not giving enough time to analyse the use case type and to define (and re-define) the problem has the potential to lead to a broken product.</quote>

Having the right people at the table and being spot on in defining the problem will not be enough without **the right technology stack**. To be productive a Data Science team needs the freedom to experiment. This doesn’t mean that companies should let data scientists do tables full scan on production databases, but the team should be equipped with a laboratory environment where data exploration and models creation can happen quickly.

![]()Fig 5. Fast Prototype to Production EngineReferring to Fig 5. the Fast Prototype to Production Engine has three key components:

1. **A Data Scientist Lab.** The real spinning wheel of the engine, a place where things can be broken and made again, where creativity is welcomed and iterations can happen fast. It’s typically the combination of a data lake (where eventually data is compliant with data privacy laws) and an elastic computing environment. When it comes to programming languages the best choice are usually dynamically typed, interactive high level languages like Python or R.
2. **A Fast Deployment mechanism.** The Data Scientist Lab produces data artefacts to be put into production timely. This can happen through Api or by using Docker containers. It’s not necessary that the artefacts are perfect right the first time, what matters is how quickly we can put the product to the real world test.
3. Being able to deploy quickly is safe only if we have a **reliable feedback loop** mechanism. We need to be able to quickly identify model drifts and quality issues to act upon them. A feedback loop is necessary also for the model to learn and improve over time. It’s not uncommon to hear of models built two years before and never updated, which is a terribly bad practice.

## Conclusions

Building models that work in the real world is hard, making sure they become real products that make an impact is even harder. However this is the real challenge for the Data Science world in the coming years. Setting up the right team, with the right technology stack and the right commitment from management are necessary pre-conditions to succeed.

## References

[1] I took the idea of the Data Science table from #AI Expert Alessandro Giaume and Stefano Gatti, Franco Angeli, 2019, pp.79–95.

[2] <https://medium.com/analytics-vidhya/which-machine-learning-algorithm-should-you-use-by-problem-type-a53967326566>

[3] <https://hbr.org/2017/01/are-you-solving-the-right-problems>

[4] Nicholas J Radcliffe and Patrick D Surry. Real-world uplift modelling with significance based uplift trees. White Paper TR-2011–1, Stochastic Solutions, 2011

