[![Keith McNulty](https://miro.medium.com/fit/c/96/96/1*5jw92xZWkTltN6nnAF3D1A.png)](https://keith-mcnulty.medium.com/?source=post_page-----50b386b08bef--------------------------------)[Keith McNulty](https://keith-mcnulty.medium.com/?source=post_page-----50b386b08bef--------------------------------)[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fa859aab532a0&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fthree-key-fails-in-machine-learning-50b386b08bef&user=Keith+McNulty&userId=a859aab532a0&source=post_page-a859aab532a0----50b386b08bef---------------------follow_byline-----------)May 1, 2019

·5 min read·Member-only

[Save](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F50b386b08bef&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fthree-key-fails-in-machine-learning-50b386b08bef&source=--------------------------bookmark_header-----------)# Three key fails in Machine Learning

<person role="Senior executive, Analytics, McKinsey & Company">
https://keithmcnulty.org/
</person>

## The mythology that has been associated with Machine Learning can lead to poor judgment about when and how to apply it

I kind of had a backwards introduction to analytics. My first heavy involvement in any sort of dedicated analytics project was a Machine Learning project. I mean if you are going to do it, why not go the whole hog?

Not that I am complaining. It was an amazing learning experience. It taught me a great deal about technical approaches to advanced analytics. I learned about technology and data management. But most importantly I learned about how a myth has developed around the term *Machine Learning* when, in fact, there is nothing mythical about it at all. I remember having team meetings where uninitiated participants would describe what we were doing as ‘the dark arts’.

The reality is that there is nothing dark, mysterious or mythical about Machine Learning. Most statistical methods employed in Machine Learning approaches have been known for decades, or even centuries in the case of Bayesian approaches. The explosion of the term Machine Learning is all about the technology and how it enables us to apply these approaches to large datasets in ways that computing resources previously rendered challenging or downright impossible.

Nevertheless the mythology persists. There are plenty out there who believe, or are led to believe, that a Machine Learning project can perform some sort of ultra-modern magic that will defy all human approaches to the same problem. This is dangerous, because it can mean that individuals or teams embark on efforts which take up an lot of resource and time based on a belief that some sort of magic will occur, and without appropriate critical thought and human judgment.

Before I go on I want to clarify: I am not criticising Machine Learning *per se*. There are countless use cases where it brings value and efficiency and our lives today would not be the same if it were not for breakthroughs facilitated by Machine Learning. No, my point is that we should not believe that Machine Learning works in all situations, and we should be more circumspect about how and when we invest in these techniques.

To illustrate my point, here are my top three key fails that I have witnessed in Machine Learning projects.

![]()# 1. Poor objective setting

As per [another recent piece I wrote](/building-a-model-heres-the-first-question-you-should-ask-828befec5ac), it is essential to know and clarify the purpose of a Machine Learning project. Either you are building your model to *explain* something or you are building it to *predict* something. Most of the time, a model that is better at explaining a phenomenon is not optimal at predicting it. Also, models that predict something really well often have features that are really obvious and make up a large part of the predictive power, so that doesn’t give them great explanatory powers.

It’s critical that the purpose of a Machine Learning effort is clarified and agreed by all parties. We are building a model primarily to explain or primarily to predict. It can’t primarily do both. There should be no doubt on this.

![]()# 2. Poor experimental design

Imagine you are working for a sales company and you want to build a model to explain what drives successful rep sales. One of the things you already know and have known forever is that reps make more successful sales to existing customers than to new customers.

You gather all the data you can find, run your learning and then announce at a big meeting that the top three explanatory drivers of sales are:

* Whether the customer has bought before
* Whether this is a customer the rep has visited before
* Whether the customer rates the rep highly in feedback surveys

It’s patently obvious that all of these drivers relate to a factor we already know is important, and so the effort has provided no added value, and in fact by including this data the mathematics of the model is now dominated by a factor that we already knew about. This could have been avoided if someone considered how to design the effort up front. Perhaps we could have removed this data, or restricted the sample to clients outside this group.

# 3. Poor practical planning

Whether you are embarking on ML for explanatory or predictive purposes, few think of the consequences of success.

If you build a model that can help diagnose the reasons for absenteeism in the workforce, or one that can predict manufacturing problems, or whatever, you need to be able to deploy it practically. This is when you find out that some of the data sources used in the model were extracted from files that require massive manual manipulation. Or you discover that some of the inputs were imputed based on missing data.

The point is that if you are developing ML in the hope that it is deployed in the future to help diagnose or predict things more efficiently, you need to be sure that the input data can flow into the prediction engine easily. I have seen so many ML efforts that use data that has no chance of being easily engineered, and this creates a whole new headache which could have been better anticipated.

While Machine Learning offers so much potential for how we can understand data, we are still nowhere near a point where successful learning is guaranteed for any dataset. In fact, without strong design and planning, and without a good instinct of the structure of the data, a Machine Learning project can end up a gigantic waste of time and effort. By checking on the objectives, experimental design and practical planning, you’ll get a good sense of whether its worth it.

*Originally I was a Pure Mathematician, then I became a Psychometrician and a Data Scientist. I am passionate about applying the rigor of all those disciplines to complex people questions. I’m also a coding geek and a massive fan of Japanese RPGs. Find me on* [*LinkedIn*](https://www.linkedin.com/in/keith-mcnulty/) *or on* [*Twitter*](https://twitter.com/dr_keithmcnulty)*.*

