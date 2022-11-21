[![Praatibh Surana](https://miro.medium.com/fit/c/96/96/1*I889HaYiJYfmhSIfeBRDWg.png)](https://praatibhsurana.medium.com/?source=post_page-----43fd22567366--------------------------------)[Praatibh Surana](https://praatibhsurana.medium.com/?source=post_page-----43fd22567366--------------------------------)[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Ff711d3de8cba&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fan-introduction-to-machine-learning-engineering-for-production-mlops-phases-in-mlops-43fd22567366&user=Praatibh+Surana&userId=f711d3de8cba&source=post_page-f711d3de8cba----43fd22567366---------------------follow_byline-----------)Jul 5, 2021

·7 min read[Save](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F43fd22567366&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fan-introduction-to-machine-learning-engineering-for-production-mlops-phases-in-mlops-43fd22567366&source=--------------------------bookmark_header-----------)![]()(Image by Author from [Canva](https://www.canva.com/))# An Introduction to Machine Learning Engineering for Production/MLOps — Phases in MLOps

## A discussion on the phases in the production of a machine learning model- namely scoping, data, modeling, and deployment.

Welcome back! This will be the second article in this series on MLOps. Previously, we briefly looked at challenges faced in production and some simple solutions to tackle these challenges. If you haven’t got the chance to look at my previous article, you can check it out [here](/an-introduction-to-machine-learning-engineering-for-production-part-1-2247bbca8a61).

Now, as we had discussed previously, the production part can roughly be divided into 4 phases. In this article, let’s explore these phases and what each of them really means.

# 1. Scoping

Scoping helps determine feasible solutions to a problem, put very simply. Let’s consider an example wherein you are working on a handwriting recognition project for your company. Now, some initial steps while approaching this problem could be looking at benchmark papers/open-source implementations of this problem. Often, this is a good starting point for most projects as there is almost always someone before you who might have tried to tackle the same problem statement. After this, you might feed your data to this open-source model and fine tune it or take some chunks from the open-source model and make your own model. Basically, looking at these pre-existing solutions gives you a basic understanding of what level of accuracy is achievable. This is what scoping entails. Some key points covered in scoping are -

* Brainstorming business problems
* Brainstorming AI solutions to said problems
* Assess feasibility and potential of solutions (I find this extremely important)

So this is what scoping essentially is. It helps you or your team get a better idea of the problem at hand and how to go about solving it.

# **2. Data**

It is common knowledge that data rules the AI world, pretty much. Our models, at least in the case of supervised learning, are only as good as our data. It is important, especially when working in a team, to be on the same page with regards to the data you have. Consider the same handwriting recognition task that we defined earlier. Suppose you and your team decide to discard poorly clicked images for the time being. Now, what is a poorly clicked image? It might be different for your teammate and it might be different for you. In such cases, it is important to establish a set of rules to define what a poorly clicked image is. Maybe if you struggle to read more than 5 words on the page, you decide to discard it. Something of that sort. This is an *extremely* important step even in research as having ambiguity in data and labels will only lead to more confusion for the model.

Another important thing to be taken into consideration is the type of data you are dealing with, i.e, structured or unstructured. How you work with the data you have largely depends on this aspect. Unstructured data includes images, audio signals, etc and you can carry out data augmentation in these cases to increase the size of your dataset. However, data augmentation would not be advisable with structured data. Same with labeling- as humans, we find it easier to label unstructured data as compared to structured data.

Some key points to remember while working with data are-

* Clean labels are critical
* Labelers must agree on a standard procedure for labeling to ensure uniformity
* Use human-level performance (we will talk more about this soon) as a benchmark only for tasks on unstructured data
* Make sure you take your time while collecting data but also start working with the model simultaneously. Let the data collection approach be iterative in nature.

# **3. Modeling**

What many people might assume to be the most important phase, however, this is not true. I still find the data phase to be a lot more important. Having said that, I do admit that modeling is an important phase as well. It revolves around fine tuning, developing your model, and trying to achieve certain levels of accuracy. Unlike simple projects wherein doing well on dev/test sets might be an indication that the model is doing good, this is not the case with MLOps. This is because the real-world data that the model will interact with when deployed could cause the model to behave in ways different from what might be intended and hence it’s important to know how to proceed with your model.

There are some key steps to ensuring you get the modeling part correct. They can be roughly summarized as follows-

* **Establishing a baseline**: Something that’s often overlooked (made this mistake personally, please don’t make this mistake \*screams internally\*), establishing a baseline is incredibly important as it helps give you an idea of how to proceed. It basically involves going through previous research in relevant areas or looking at products of other companies doing the same thing and seeing how good their models are. This along with knowing the compute resources required/available can help you replicate some state-of-the-art (SOTA) results. Something that’s good with the DL community is that a good chunk of all SOTA papers are open source. This makes it easy to not only establish baselines but also build similar or in some cases, even better models. For unstructured data, you can use human-level performance as a criterion to judge your model. Consider the handwriting recognition task given earlier - If an open-source model is able to read words with an error rate of ~20%, then this is your baseline for the task. If you feel that you have the means to replicate SOTA papers, then you can also use their results to establish your baselines. It’s all subjective.
* **Data-centric approach**: Something that is fast gaining traction in the community, data-centric approaches involve focusing on data instead of solely the model. Efforts are made to try and ensure that the quality of data is high and maintained. Although not something that’s common in research, data-centric approaches are in my opinion, the one definitive way to improve your model’s results. Ensuring that your data covers important test cases, is defined consistently, and is distributed equally as far as possible are all part of a data-centric approach. Personally, in the projects I’ve worked on, I’ve always seen a slight improvement in accuracies on unseen data whenever I’ve tried taking a data-centric approach. It could be something as small as fixing the light conditions in images before feeding them to the model etc.
* **Experiment Tracking/Version Control**: A well know step in DevOps, version control helps us keep track of changes and lets us revert back to previous working versions in cases where our applications might throw up errors. In MLOps, it is important to track your **code** for the algorithm used, **hyperparameters**, **changes to the dataset** (if any), and the kind of **results obtained** for a certain set of hyperparameters, etc.

# 4. Deployment

Now that we have our model ready, what’s next? Deployment of course! This involves releasing your model in a real-world setting or integrating it into the application/edge device it was developed for. Now even in deployment, there are certain types of deployment. These are-

* **Shadow Deployment**: In this type of deployment, the model is deployed but the final decision is taken by a human, irrespective of what the model predicts. This is done usually to gauge how well the model is doing and where it is failing.
* **Canary Deployment**: In this type of deployment, the model is exposed to only a small fraction of the data on which it is allowed to make decisions. For example, the model might only be exposed to 10 out of every 1000 images. Depending on how the model performs, the traffic is gradually increased or the model is pulled back and adjustments are made.
* **Blue-Green Deployment**: In this type of deployment, the traffic is gradually migrated from the old or *blue* version to the new or *green* version. This helps prevent any sort of downtime and in case of any bugs/errors, the application can easily be rolled back to the previous stable version or the blue version.

The next thing to look at is the monitoring of our deployed models. Remember, deployment is an iterative process. Hence, there is always room for improvement and the only way one can improve is if they monitor their model even post deployment. There are many softwares that can be used to monitor metrics etc. I will probably talk about these in a future article. For now, let’s focus on some key points to look at to ensure the smooth functioning of our deployed model-

* Take into account the kind of server load and monitor the same
* Go through all possible cases where your model could fail or where something could go wrong and then try and rectify these cases or ensure proper error handling
* Along with your team, decide few key metrics to judge your model’s performance
* Don’t be stubborn with your performance metrics, be open to change, and always try and work on identifying metrics that fit your model the best
* Ensure that not only the model but also the ML pipeline is being monitored. Sometimes errors could be caused due to a small mistake in a preprocessing step and this might lead to the downfall of the entire system (been there, messed up an input shape and tried to resolve the error by looking solely into the model’s code ;-;)
* Have an idea of how fast the real-world data can/might change for the problem statement you are tackling.

There you go! That’s all I have to say about the phases of MLOps. If you’ve made it this far and want to learn more about MLOps, feel free to check out my [**GitHub repository**](https://github.com/praatibhsurana/Machine-Learning-Engineering-for-Production). I will keep updating it with relevant material and Jupyter notebooks!

**References**

1. <https://www.redhat.com/en/topics/devops/what-is-blue-green-deployment>
2. <https://www.coursera.org/learn/introduction-to-machine-learning-in-production>
3. <https://cloud.google.com/blog/products/ai-machine-learning/key-requirements-for-an-mlops-foundation>
4. <https://blog.ml.cmu.edu/2020/08/31/3-baselines/>
5. <https://blog.tensorflow.org/2021/01/ml-metadata-version-control-for-ml.html>
