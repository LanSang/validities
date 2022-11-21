[![Christian Freischlag](https://miro.medium.com/fit/c/96/96/2*vcYKirJodH4oKn1Hglhr_Q.jpeg)](https://medium.com/@christian.freischlag?source=post_page-----86d409b7eb03--------------------------------)[Christian Freischlag](https://medium.com/@christian.freischlag?source=post_page-----86d409b7eb03--------------------------------)[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fb7bf9b5093a4&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2F4-blockers-and-4-unlockers-for-successful-machine-learning-projects-86d409b7eb03&user=Christian+Freischlag&userId=b7bf9b5093a4&source=post_page-b7bf9b5093a4----86d409b7eb03---------------------follow_byline-----------)Oct 28, 2020

·5 min read·Member-only

[Save](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F86d409b7eb03&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2F4-blockers-and-4-unlockers-for-successful-machine-learning-projects-86d409b7eb03&source=--------------------------bookmark_header-----------)# 4 Blockers and 4 Unlockers for successful machine learning projects

## How to build reliable and useful machine learning systems

![]()Photo by [Yann Allegre](https://unsplash.com/@yann_allegre) on [Unsplash](https://unsplash.com/photos/wHOjM1LGi24)Machine Learning projects are known to fail frequently, according to [Gartner](https://www.gartner.com/en/newsroom/press-releases/2018-02-13-gartner-says-nearly-half-of-cios-are-planning-to-deploy-artificial-intelligence) 85% of all AI projects fail and even [96% deal with problems](https://www.techrepublic.com/article/96-of-organizations-run-into-problems-with-ai-and-machine-learning-projects/). When it comes to new technologies a high degree is normal, but these numbers are alarming. That might be that requirements for machine learning are not met, no value is added or the model did not make it to production for engineering reasons. Often it is possible to identify potential problems beforehand. This article is about early identification of such pitfalls based on my experience in applied machine learning for the last five years.

# General requirements

Machine learning projects should automate decisions. This can be just about anything, from the final decision what is shown on an image (image classification), which recommendations a user gets (recommender systems) or which machine needs to be maintained (predictive maintenance).

To make machine learning projects successful there are some major requirements, which can be assessed beforehand. These four are potential blockers (Quantity, Quality, Complexity, Explainability)

*At this point it should be mentioned that this article is not about research, but applied machine learning.*

## Quantity

The most important aspect for the reasonableness of a ML project is the amount of decisions that have to be made (and how much time is saved). <quote label="utility">It is not worthwhile to develop a machine learning system that automates rare decisions or even frequent ones, which in total hardly cost any time. The development effort is simply too expensive.</quote> Training an image recognition model that can perform a visual inspection of objects a few times a day is rarely worthwhile. Machine Learning is a tool for optimizing **frequent** and **repetitive** tasks.

## Quality

Often there are tasks that are frequent and repetitive but cannot be performed without human supervision. If, for example, the quality requirements of a model are that high that a human is always needed (e.g. regulations), machine learning will hardly optimize anything. Although there are so-called human-in-the-loop systems, these are more complex and costly and require a ML model to reliably classify uncertainty, which is [currently usually not reliable](https://ai.googleblog.com/2020/01/can-you-trust-your-models-uncertainty.html).

For the most tasks it’s **not possible** **to reach** **human performance**. Superhuman performance can even rarely expected in fully controlled environments and very narrow tasks. To estimate if a model can reach the threshold, look what others already did. Usually conferences for applied machine learning are very useful. Be careful with research papers, they can not always be applied to real world data.

## Complexity

AI and ML are buzzwords and sometimes they are used, where a well-adapted process and rule-based systems solve the underlying task. A lot of so-[called AI is actually not AI](https://www.cnbc.com/2019/03/06/40-percent-of-ai-start-ups-in-europe-not-related-to-ai-mmc-report.html). It is usually much more sensible to rely on manually crafted rule-based systems (based on stats) first and use ML only, if they fail or get too complex. Domains, where these rule based systems fail are: Computer Vision, Natural Languange Processing, Speech Recognition, Sequence Modelling etc.

## Explainability

Any ML model can only be as good as the data on which it was trained. AI is not black magic that can predict the future, even if the media often give the impression that it does. Machine learning systems learn by example and allow a certain degree of generalization. In the end the data can always explain, how the model makes the decision, even if it’s not that simple.

A model that has been trained to distinguish between cats and dog images will only recognize cats and dogs. Such a model generalizes the breed, proportions, lighting conditions, etc. But if you let such a model categorize a coffee cup, it will see it as either a dog or a cat, because it knows nothing else.

Even if you try to predict stock market crashes, you may be able to train a model that identifies all past crashes. The point is that the next crash is very unlikely like the previous ones and therefore all these models fail in practice.

The examples here may be obvious, but sometimes it’s just impossible to know, if the data contains the information needed or not. Machine learning models do not have common sense or world knowledge, that’s still up to us. What they are supposed to predict must be **present in the data** and must also match the patterns that algorithms can find.

# Running models

The previous points are rather abstract and conceptual. The following points are more technical and engineering related.

## Technical complexity

The technical infrastructure a model needs and the general complexity of the model itself drives the time to build such a model. For example, it is much easier to use traditional methods like SVM, KNN and decision trees, because they can be easily integrated via existing frameworks and libraries written in the same programming language as the surrounding system. To involve some state-of-the-art neural networks, there is usually much more complexity involved. If it is not about image recognition, text or speech (…), <quote label="tradeoffs">the improvement is usually **out of proportion to the effort**.</quote>

## Making predictions

It makes a huge difference whether a model must provide predictions on demand, i.e. in “real time”, or whether the model is used in a batch processing. As with other software systems, the question here is not only about **scalability and availability**, but also about the use case.

A process that uses a model to make millions of predictions once a day, can schedule much faster if the ML model is available locally and does not need to be accessed via an API. On the other hand, a recommendation system is activated on demand and must offer low latency. Microservices are not always the best solution.

The **amount of training data** also plays a major role. Large deep learning models like to train for several weeks with several terabytes of data. Obviously, such a model is much more complicated to handle than a random forest that is trained directly from the database. or a simple CSV file.

## Maintenance and Monitoring

Monitoring and maintainability are a key concept. As soon as the model is productive and stopped working, you will notice this much too late without proper monitoring. By shifting from hard-coded rules to data-driven models, **errors become less visible**. Therefore, in addition to typical metrics of production software systems, further ML-specific monitoring is required.

## Half-life

Machine learning **models are rarely infinitely valid**. <quote label="data">Usually the data changes after some time and the model loses its validity.</quote> With automatically re-trained models, or online learning systems, this aspect is practically free, but all other models need to be re-trained from time to time (model-drift).

An image recognition system that needs to be trained every two weeks due to new objects to be recognized, but that has a training time of two weeks is possibly not the optimal approach.

# Conclusion

I hope I could encourage some readers to think about these points. There are many pitfalls and obstacles, when building an AI-driven system, conceptually and technical. Making sure quantity, quality, complexity and explainability requirements are given and the technical souroundings are set, the probabilty for a successfull project is maximized.

