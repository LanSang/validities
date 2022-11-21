[![Ahmed Besbes](https://miro.medium.com/fit/c/96/96/1*SC35wIudR_HF3sA8F_n0yA.png)](https://ahmedbesbes.medium.com/?source=post_page-----91255ddd1311--------------------------------)[Ahmed Besbes](https://ahmedbesbes.medium.com/?source=post_page-----91255ddd1311--------------------------------)[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fadc8ea174c69&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2F9-common-mistakes-beginner-data-scientists-make-91255ddd1311&user=Ahmed+Besbes&userId=adc8ea174c69&source=post_page-adc8ea174c69----91255ddd1311---------------------follow_byline-----------)Dec 10, 2020

·8 min read·Member-only

[Save](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F91255ddd1311&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2F9-common-mistakes-beginner-data-scientists-make-91255ddd1311&source=--------------------------bookmark_header-----------)# 9 Common Mistakes Beginner Data Scientists Make

## Don’t fall into these pitfalls

In this article, I will cover 9 common mistakes data scientists make when they start their careers. I personally made some of them myself a few years ago and my hope with this post is that you learn from my experience and stop making them yourself.

*PS: you can find this discussion on this Youtube video as well.*

Video made by the authorWithout further ado, let’s start!

# 1 — **Not spending enough time understanding the problem**

![]()Photo by [Karla Hernandez](https://unsplash.com/@karlahrnndz?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)This probably is the area where junior data scientists are the most inexperienced. At the start of each project, they tend **to jump headfirst into the data and the code** without taking a step back and clearly thinking about the added value they could bring in.

What I learned from my experience in consultancy was that scoping the full delivery of a project right from the beginning is extremely useful later on to have a clear vision about what data science will bring at each step.

Spending time to understand the problem particularly helps:

* define the project's assumptions
* map the available data sources
* list the success metrics that translate the business needs
* provide a realistic roadmap to meet time constraints

There’s no magic in here really: a successful data science project goes along with a clear understanding of the problem and an organized method to solve it.

# **2 — Not knowing the basics**

![]()Photo by [Tijana Drndarski](https://unsplash.com/@izgubljenausvemiru?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)This goes without saying but I’m gonna say it anyway: **not having solid knowledge of probability, statistics, and machine learning will affect you in the long run.**

As a data scientist, you should **never** consider machine learning models as black boxes. You should at least be familiar with the basic concepts behind them: how they work, how they behave to particular types of data (missing data for example), and how their hyper-parameters impact the training.

If you need to rework your basics in statistics, machine learning, or deep learning, I suggest you have a look at these videos:

Statistics 110 — Harvard UniversityMachine learning course — CaltechMIT Introduction to Deep LearningYou can also have a look at this **awesome machine learning** repository: you’ll find in here tutorials, blog posts, tools, and virtually anything you need to learn and apply machine learning.

[## josephmisiti/awesome-machine-learning

### A curated list of awesome Machine Learning frameworks, libraries and software. - josephmisiti/awesome-machine-learning

github.com](https://github.com/josephmisiti/awesome-machine-learning)# 3 — Skipping Exploratory Data Analysis

![]()Photo by [Luke Chesser](https://unsplash.com/@lukechesser?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)I’ve seen many data scientists getting rapidly excited and jumping into the modeling part before properly and fully understanding the data.

This is, unfortunately, a very common mistake.

What junior data scientists don’t probably know is that effective exploratory data analysis (or EDA) **gives a strong edge** both in **data science competitions** and **real-life projects**.

Here’s what I use EDA for:

* spotting anomalies and errors in the data (missing values, outliers, typos)
* detecting correlations between variables and building the first intuitions about the problem
* visualizing unexpected relationships between the features
* formalizing the first questions to the domain experts before further iterations

I can’t remember how many times I had to go through the data again to better understand the problem or improve the score of a machine learning model.

Now I can understand that EDA can be a tedious and unpleasant process since it requires building charts, graphics, and taking time to understand them. There’s hopefully a great tool that can automate a large portion of this work.

It’s called [**pandas-profiling**](https://github.com/pandas-profiling/pandas-profiling)**.** It’s a python package that takes the data as input, in a dataframe object and then automatically generates a full report on it. There’s everything in this report, really: distributions, statistics, bar charts, outliers, correlation matrices, missing values, etc. What you’d make in a day or two is generated in a few minutes only so that you can focus on understanding the problem and designing the best solution to tackle it.

![]()pandas profiling — GIF by the author# 4 — Not spending enough time on feature engineering

![]()Photo by [Alain Pham](https://unsplash.com/@alain_pham?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)This mistake is linked to the way most data scientists build their models.

What I usually notice is, upon processing and cleaning a first version of the dataset, most data scientists quickly start running intensive grid-searches to optimize some model parameters on a given task. Although this may work in a substantial amount of time, it’s been proven that it’s not the most efficient way to get a better score.

What top machine learning practitioners recommend is spending more time building predictive features instead of waiting for a 2-hour-grid-search to find the parameters. This process is called **Feature Engineering**.

Let’s have an example here. Let’s say that you want to predict house prices and have among the features the number of rooms and the total number of windows. One additional feature that can be interesting to create is the ratio of these two variables which is equivalent to ***“the average number of windows per room”***.

Feature engineering is an art by itself and highly depends on the problem and its complexity. It may also require research, interaction with external parties like domain experts: it’s a cycle of trials and errors most of the time.

**Here’s what to keep in mind**: machine learning algorithms are now commodities that can be used off-the-shelf and at the end of the day, a stable and robust solution is more a matter of smart feature engineering than total brute force. So instead of looking for the most sophisticated state-of-the-art model, the solution may lie in building the right features.

If you want to automatically create features for your tabular data, there’s a fantastic tool specifically designed for this purpose. It’s called [featuretools](https://www.featuretools.com/) and it’s opensource.

[## Learn Data Science in a Flash!? | Data Driven Investor

### I was a trained classical pianist in my previous professional life. Remember those infomercials claiming that you could…

www.datadriveninvestor.com](https://www.datadriveninvestor.com/2020/07/23/learn-data-science-in-a-flash/)# 5 — Not talking to domain experts

![]()Photo by [Scott Graham](https://unsplash.com/@sctgrhm?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)This error is linked to the way we interact with the external world.

As data scientists, we may believe that our tools and algorithms can solve all the business problems at the hit of the jupyter cell and without going out from our comfort zone and leaving our chair. Well, as attractive as this sounds, **this is rarely the case.**

Interacting with domain experts is part of the data scientist’s job, and I can give you at least 2 reasons why:

* You need the domain experts because they give you insights and clues you cannot directly see in the data
* Domain experts need to interact with you as well because you’re building a solution for them and thus need to learn how to use it from you

It works both ways!

# 6 — Not thinking of a model as part of a life-cycle

This is something that is widely disregarded by data scientists, probably because more than half of the projects don’t make it to production and stay at the Proof Of Concept (POC) level.

![]()Diagram made by the authorA machine learning model lifecycle starts from the business need, then goes through the following steps:

* data exploration
* model training
* model evaluation and testing with the appropriate metrics
* model deployment with minimum performance standards (latency)
* model monitoring and further training and feedback

Each step has its own technical requirements. Even though, as a data scientist, you’re mostly asked about data exploration and training, having the global picture in mind can help you make the right choices in an early fashion.

Let me give you an example: if you know that the infrastructure of your client has limited resources, you can, from the beginning, have this constraint in mind while building your model: you could, for instance, choose a less complex architecture to make the inference faster.

# 7 — Thinking deep learning and big data is key to everything

![]()Image by authorTrue story. I’ve seen data scientists saying things like:

* We probably need more data
* We definitely need to install Tensorflow and go deep. This would probably work better

Although these can be valid solutions, they can, however, be impractical to implement for different reasons.

You may for example not have access to more data to improve your model or you may simply not afford an infrastructure with GPUs to train deep learning models.

But most importantly here, **you should consider simple solutions that achieve 80% of the work first**. Simple models are often underrated and, surprisingly, they do most of the job when properly tweaked.

Being attracted to fancy models and sophisticated solutions is a pitfall a lot of data scientists fall into. Don’t get me wrong, I’m all for trying new models and techniques, but you should at least start with baselines and see how they work. Then, you can judge if it’s worth the time to explore more complex ones.

# **8 — Considering that data science is different from software engineering**

![]()Image by the authorA common misconception among data scientists is thinking that it’s not part of their job to produce quality code that gets delivered to the other team members.

When data scientists stick to some tools such as jupyter notebook to the point of overusing them for everything, they neglect best practices that’d sure improve their code otherwise. We’re talking proper code versioning with GIT, unit testing, continuous integration and continuous delivery (CICD), virtualization and orchestration with Docker, deploying on a cloud infrastructure…

These are software engineers' skills and there’s no reason why we shouldn’t learn them as well. As a data scientist, I consider myself a software engineer as well: I’m asked to build models, APIs, or applications. And at the end of the day, these artifacts are deployed to the client infrastructure.

# 9 — Neglecting communications skills

![]()Photo by [Icons8 Team](https://unsplash.com/@icons8?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)This probably is one of the most important mistakes data scientists make.

It’s one thing to solve a data science problem, it’s another thing to efficiently communicate on it to a non-technical audience.

When being a data scientist in an organization, presenting your findings to a business stakeholder is part of your job, and being able to make the shift from a technical talk to highlighting a business value expressed in human terms is extremely valuable.

You’ll most likely always present your work to a business sponsor. These people are not technical and they never will be as your team. They only listen to what matters to them. So my advice here: be clear, concise, and straight to the point.

# Conclusion

Thanks for reading and spending time with me! I hope you found these tips useful. This list is, by no means, an exhaustive one. So if you’re aware of other common mistakes data scientists do as well, feel free to write them in the comments.

For more content, you can follow me on my [blog](https://ahmedbesbes.com) or my youtube [channel](https://www.youtube.com/channel/UCP1M7FpkpNljH4r6ORiRg6g).

