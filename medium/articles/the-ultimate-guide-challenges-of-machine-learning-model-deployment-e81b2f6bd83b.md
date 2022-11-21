[![Yuqi Li](https://miro.medium.com/fit/c/96/96/1*TyfR7p7_5W6ItNXNotK2LA.jpeg)](https://medium.com/@yuqil725?source=post_page-----e81b2f6bd83b--------------------------------)[Yuqi Li](https://medium.com/@yuqil725?source=post_page-----e81b2f6bd83b--------------------------------)[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F5df6cc724b80&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fthe-ultimate-guide-challenges-of-machine-learning-model-deployment-e81b2f6bd83b&user=Yuqi+Li&userId=5df6cc724b80&source=post_page-5df6cc724b80----e81b2f6bd83b---------------------follow_byline-----------)Jan 11

·8 min read[Save](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fe81b2f6bd83b&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fthe-ultimate-guide-challenges-of-machine-learning-model-deployment-e81b2f6bd83b&source=--------------------------bookmark_header-----------)# The Ultimate Guide: Challenges of Machine Learning Model Deployment

<person role="Engineer Amazon, co-founder AI-startup">
https://www.linkedin.com/in/yuqiliofficial/?originalSubdomain=ca
</person>


# Motivation



> “Machine learning model deployment is easy”
> 
> 

This is a myth that I’ve heard so many times. As a data scientist with an engineering background, I also had this point of view until actually developed a machine learning deployment (or [MLOps](https://aipaca.ai/)) project. Technically, deploying a machine learning(ML) model could be very simple: start a server, create an ML [inference](https://hazelcast.com/glossary/machine-learning-inference/#:~:text=Machine%20learning%20(ML)%20inference%20is,as%20a%20single%20numerical%20score.&text=ML%20inference%20is%20the%20second,data%20to%20produce%20actionable%20output.) API, and apply the API to an existing application. Unfortunately, this workflow is so easy to come up that people tend to underestimate the complexity. In fact, some of my ML engineer friends complained that their jobs are not understood by so many people such as engineers from different teams, product managers, executive teams, and even customers.

![]()Don’t judge the complexity of an MLOps project by its tip. Photo by [SIMON LEE](https://unsplash.com/@simonppt?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)By this story, I wish more people could understand the difficulties behind MLOps. I would like to wear the engineer pants and share with you the ultimate guide to the challenges of ML model deployment.

*Background: ML engineers work closely with data scientists. For instance, Data scientists build ML models, and ML engineers implement the models.*

# Phase 1: When a model is just handed over to ML engineers

![]()Photo by [ETA+](https://unsplash.com/@etaplus?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)
> **“The Model Literally Doesn’t Work on Production Servers”**
> 
> 

When data scientists pass their models to ML engineers, the model may just not work on a different machine. This problem is usually caused by either **software** **environment change** or **poor code quality**.

Containers such as [Docker](https://www.docker.com/) and [K8s](https://kubernetes.io/) are able to solve most of the reproduction issues by aligning software environments across machines. However, model containerization is not a skill set that every data scientist (DS) has. If this case happened, DS and ML engineers would require an extra amount of time to exchange knowledge.

On the other hand, the compilation between server and ML frameworks can also lead to system errors. For example, even though Flask + Tensorflow is a combination used in many tutorials, there was a time we found that a flask server environment was not friendly to Tensorflow 2 as the environment is getting more complex. It took us a while to figure out a workaround.

Data scientists are not programmers. Following [PEP 8 guidelines](https://www.python.org/dev/peps/pep-0008/) when writing code is not necessary for data science. The “poor code quality” claimed by an ML engineer could come from the different coding habits between scientists and engineers. Instead of traditional IDE such as VS Code, Jupyter Notebook is a more popular code editing tool for data scientists. The programming logic in Notebook is very dissimilar to common software development. Therefore, when the code model is migrating out from Jupyter Notebook, it could become buggy.

If the production servers were using machines with different specs (e.g., OS, CPU types, GPUs) than development servers, the MLOps project would rise to a higher complexity level.

# Phase 2: When Teams Start to Collaborate

Assuming that the ML model from the data science team now is successfully runnable on production environments, it’s time to migrate it to the existing application. However, where and how to use the model in the application to solve the actual business problem is a new topic that a cross-team collaboration is required.

![]()Photo by [Jason Goodman](https://unsplash.com/@jasongoodman_youxventures?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)
> **“Why should we care …”**
> 
> 

Cross-team communication comes with many challenges because of diffused responsibility and priority. **Engineers care about software efficiency, system stability, and ease of maintenance**. Nevertheless, **the majority of DSs care more about the ML model performance and rigor.** To maximize model performance, **t**hey always take the advantage of various data science tools. I’ve seen my DS colleagues pre-processed data by SQL, started the model pipeline by R, followed by Sklearn, and ended by Pytorch. Of course, this structure won’t be appreciated by engineers.

While DS and ML engineers are arguing what should be more prioritized, product managers (PMs) come into the stage and ask the two teams to keep an eye on the roadmap because **PMs’ responsibility is to ensure product deliverables are released on time**.

***“Interesting, the ticket to deploy ML models is triggering a team debate …”***

There is no fixed solution to avoid the tangle. Software efficiency, ML model performance, roadmap, which one is more significant? The answer is shifted business to business and is never perfect.

# Phase 3: When the model is about to be released

Teams finally compromised for each others’ needs. The engineering team also successfully add the model inference feature into the application. Everything looks good, doesn’t it?


> **“Wait a mintue, how much traffic should the model hosting server support?”**
> 
> 

![]()Overwhelming system log. Photo by [Markus Spiske](https://unsplash.com/@markusspiske?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)When it comes to user throughput problems, and if a company is resourceful, the most recommended solution is to purchase a cluster of powerful servers that are capable enough to handle all traffic load even at peak. However, machines used to hold ML models are scarce and expensive. An on-demand p3.16xlarge AWS server with 8 V100 cores has a pricing of $24.48 per hour, which is $17625.6 monthly.

Sadly, the above solution is only affordable by a few companies. For the rest of the companies, scaling computing power by need is more practical, but it is challenging even for senior ML engineers. Data search, concurrency, consistency, and speed are the four common problems in a scaling system. What’s worse, ML scalability is more difficult due to the lack of server capacity: assuming that the most commonly used cloud server in your project is called server A, in a traditional scaling system, you only need to consider the number of server A that you should scale to. However, in machine learning, server A does not always have the capacity even in large cloud platforms such as AWS because it is scarce. Your scaling strategy should also involve other kinds of servers with higher capacity. [Load tests](https://en.wikipedia.org/wiki/Load_testing) need to be conducted for all combinations among the kinds. New cloud platforms may also be added so that if server A is not available on one platform you still have the chance to get one by looking up the others. As a result, there were few ML projects that finally developed a mature scaling system.

# Phase 4: When the Model Has Been Deployed

Congratulation! You finally deployed the model, but it has been not the time to leave yet.


> **“What? The challenge hasn’t ended?”**
> 
> 

Even if you are an experienced ML engineer being in the industry for 10 years, your ML infrastructure won’t be functioning all the time. In fact, if you are experienced, you should have been more worried about the ML system deterioration than I.

![]()Instable stacked stones. Photo by [Colton Sturgeon](https://unsplash.com/@coltonsturgeon?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)The deterioration comes from two aspects: engineering aspects and data science aspects.

In the engineering aspect, internal software iteration could be the main reason that turns the machine down, especially when the model deployment module is highly integrated with the rest of the application. When one piece of software gets updated, it may break the other joint pieces. Isolating the module could be a solution, but the downside is that development speed turns slower because less work is reused. Similarly, introducing and upgrading external software packages also haven negative impactors on system stability. For instance, R packages are very “famous” for breaking model scripts when their versions get upgraded.

In the worst case, engineers could make mistakes. There was a time that [Google Photo engineers accidentally deployed a bad performing model](https://www.theverge.com/2018/1/12/16882408/google-racist-gorillas-photo-recognition-algorithm-ai), which recognized black friends as “gorillas”.

<quote label="shift">
In the data science aspect, [data shift](https://www.section.io/engineering-education/correcting-data-shift/) is a BIG killer of model performance over time. 
</quote>
Data shift is defined as the change of the underlying relationship between input and output data from an ML model. If a data shift happened, data scientists would need to retrain the old model. The [feedback loop](https://www.clarifai.com/blog/closing-the-loop-how-feedback-loops-help-to-maintain-quality-long-term-ai-results) is one of the solutions to overcome data shift. It detects performance change and retrains the deployed model by newly collected data. Yes, you are right. There is also a downside to the solution. The model may be severely biased and the bias problem is hard to be identified.

*“Let’s say a grocery store used an ML model to predict the inventory change in the next month. The model predicted that bottled water is the most popular goods in the following month so the store owner took its suggestion and stocked more bottled water. Because of having more bottled water, the best selling good of the following month is bottled water indeed, and this data was fed again to the ML model as the newly collected data. As a result, the feedback loop made the model very biased toward bottled water and always asked the owner to get more bottled water… of course, this prediction was not appropriate.”*

To detect the deterioration, a monitoring system is essential in model deployment, which is also the last challenging point. The monitor is required to be real-time, detect anomaly events, send alerts, collect ML metrics, track model performance, and so forth.

# The End

This blog described the challenges that an engineering team could face while deploying ML models. I described the challenges in a time series. As a summary:

1. Challenges in phase 1: when migrating from development to production environments, models may behave differently.
2. Challenges in phase 2: when adding ML models into the existing application in the production, it is hard to meet the requirements from all teams.
3. Challenges in phase 3: building scalable computing power to serve model is essential but tough.
4. Challenges in phase 4: ML system always deteriorates over time; a monitoring system should be built.

[A common team configuration is 2–3 data engineers per data scientist](https://www.oreilly.com/radar/data-engineers-vs-data-scientists/) and the number could go above to 5 in some organizations with more complex data engineering tasks. This statement correlates to my experience that ML model deployment always takes longer than model development (Except the research led by academia who are aiming to bring earth-shaking change to the entire ML world). To keep the story concise, I still stayed high level when explaining some challenges. If you are interested in learning more details, please DM me by joining my Discord Community: <https://discord.gg/vUzAUj7V>.

# About Us

We are from [Aipaca](https://aipaca.ai) team building a serverless MLOps tool, Aibro, that helps data scientists train & deploy AI models on cloud platforms in 2 minutes. Meanwhile, Aibro adopted an exclusive cost-saving strategy built for machine learning that reduces cloud costs by 85%.

![]()AIpaca Inc. Image by the author