[![Heather Couture](https://miro.medium.com/fit/c/96/96/1*MObk0z8Cac9uwu44YCrGFg.jpeg)](https://medium.com/@hdcouture?source=post_page-----d74f3de43285--------------------------------)[Heather Couture](https://medium.com/@hdcouture?source=post_page-----d74f3de43285--------------------------------)[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fe36b7f8e7180&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2F5-things-ive-learned-from-high-impact-machine-learning-projects-d74f3de43285&user=Heather+Couture&userId=e36b7f8e7180&source=post_page-e36b7f8e7180----d74f3de43285---------------------follow_byline-----------)Oct 12, 2020

·6 min read[Save](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fd74f3de43285&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2F5-things-ive-learned-from-high-impact-machine-learning-projects-d74f3de43285&source=--------------------------bookmark_header-----------)![]()Image by [Skitterphoto](https://pixabay.com/users/skitterphoto-324082/) for [Pixabay](https://pixabay.com/photos/water-drop-single-impact-splash-5105776/)# 5 Things I’ve Learned from High Impact Machine Learning Projects

<person role="Founder, Computer Vision Startup">
https://www.linkedin.com/in/hdcouture/
</person>

## The majority of machine learning projects fail. How can you insure the success of your high impact project?

I’ve been working on computer vision and machine learning projects for about fifteen years now — most recently on pathology and remote sensing applications. Here are just a few of the things I’ve learned.

**1. Data matters — and it can be messy**

Machine learning depends on training data. In the case of supervised learning, both data and an associated set of labels that the model will predict on novel examples.

The number of training examples is a critical factor in being able to train a good model. When too few training examples are available to train a complex model, the model simply over-fits — it does not generalize to unseen data. But with medical imaging applications, a few hundred images is often all we get. A couple thousand images might be considered a large dataset. This makes training a good model challenging and may require specialized techniques.

But quantity isn’t the only factor. I’m currently working on a project to predict power plant emissions from satellite images. The quality of our ground truth data really matters. We need to be sure that the geolocation of each power plant is correct and that this location correctly maps with a database describing the type of fuel the plant is burning and with a different database that provides a time series of emissions readings. If any of these mappings are incorrect, then garbage in translates into garbage out.

Quantity and quality of data are both critical to a successful machine learning solution. And, in many cases, neither is easy to achieve.

**2. It takes a team — there’s much more to it than just building a machine learning model**

As you can see from the power plant example above, there is a great deal of data processing infrastructure required to form a set of observations for training a model. Plus a whole different infrastructure to pull remote sensing images of each power plant. This is all required before even getting to the machine learning model itself. Gathering data from different sources, cleaning it, flagging peculiarities for a more detailed inspection, assembling it into a neat form.

Most projects that I work on employ a cross-disciplinary set of experts in their respective fields. Not just machine learning scientists or engineers, but also data analysts and software engineers.

![]()Image by [mohamed\_hassan](https://pixabay.com/users/mohamed_hassan-5229782/) for [Pixabay](https://pixabay.com/photos/paper-business-finance-document-3213924/)Our power plant project includes multiple remote sensing scientists and power plant experts. Many pathology projects that I work on are a collaboration with pathologists, geneticists, epidemiologists, biostatisticians — and many others, depending on the project.

Communication becomes key with such diverse teams but is necessary to build scalable and robust infrastructure for machine learning.

**3. The algorithm can make the difference — especially when creating an impact**

Point number 3 I’ve finally gotten to modeling!

You will read many articles out there claiming that simple algorithms are sufficient; it’s better to focus on the data pipeline.

This may be true for many applications. Let’s say for increasing advertising revenue. A simple machine learning algorithm may get you there and increase sales by 10% — or, even better, 50%. That’s great!

<quote label="metrics">
But what if you’re working on an application that can make self-driving cars safer, mitigate climate change, or better treat cancer? Is it worth spending the time and money to perform a task even a little bit better than was previously possible? I’d say so.

The difference between a mediocre algorithm and superior one could be life and death to some individuals.
</quote>

<quote label="features">
I’ve also worked on tasks where a simple algorithm could not distinguish between two types of cancer — but a new algorithm (deep learning, in this case) could do so with reasonable accuracy. The key was a more powerful feature extraction method.
</quote>

For high impact applications, both the data pipeline and the model should be worth the effort. Start with simple machine learning algorithms first and advance from there.

Some applications require more specialized algorithms to handle unique complications like gigapixel images, weak labels, or heterogeneity within the images.

**4. Model validation and generalization are critical**

Proper validation of model performance is key to understanding a model’s ability to generalize to unseen data.

For pathology, this might entail testing on samples that were collected at a different hospital, processed by a different lab, or imaged by a different scanner. These factors can all change the appearance of tissue in an image. A model trained on images from one lab may do well on other images from that lab but not perform well when tested on those from a different lab.

However, it’s not only image acquisition that can affect performance. Training and testing on a different population of patients can also pose problems. Perhaps the training population tends to have cancers that were diagnosed at a later stage. The model may not have seen very many low grade tumors and so perform poorly on a test set.

Generalization ability does not only apply to medical data. For the power plant emissions project described above, we train models on a select few countries for which we have ground truth emissions data. Yet our model is expected to generalize to all power plants globally. We need to be careful in selecting features to train our model, and we also need to look for ways to validate our predictions globally. This may take the form of gathering annual emissions estimates by country to check against even if we can’t validate our individual predictions.

In the absence of an independent test and with a relatively small amount of data available, cross-validation is a good starting point to assess model performance. However, a separate test set will be necessary to truly understand how the algorithm will perform for its intended use case.

**5. Consider the use case**

![]()Image via [Shutterstock](https://www.shutterstock.com/image-photo/ai-artificial-intelligence-modern-medical-technology-1053956597) under license to Heather CoutureFinally, it is important to develop a machine learning solution with its end use case in mind. While this is true for all applications, it is particularly critical for medical use cases.

This point is also connected with validation. <quote label="data">While an initial proof of concept may be validated on a simple test dataset, ultimately it will need to be tested in a real setting.</quote> And this should not simply be a comparison of algorithm performance versus human expert performance.

How will the AI be used? Will it identify image regions for a pathologist or radiologist to review in more detail? Will it check over a doctor’s result and notify of possible errors? Or will it perform a different task such as screening for more complex visual features and provide the result to a pathologist to interpret?

Point number 2 about a cross-disciplinary team is also relevant here. That team should include those who understand the possible use case and can ensure the algorithm is properly assessed in that setting.

For medical applications, the machine learning algorithm should enable us to make better decisions that, ultimately, improve patient care and outcomes.

Are there other important lessons that I missed? Please share your insights in the comments.

**About the author**

[Heather D. Couture](https://www.linkedin.com/in/hdcouture/) is the founder of [Pixel Scientia Labs](https://pixelscientia.com), which guides R&D teams to fight cancer and climate change more successfully with AI.

Contact her to learn how to maximize the impact of your images and algorithms.

