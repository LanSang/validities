[![Michael Potter](https://miro.medium.com/fit/c/96/96/1*14PpTkwzeaibnPN6STu4_Q.jpeg)](https://medium.com/@michaelpotter?source=post_page-----ba70df6957d--------------------------------)[Michael Potter](https://medium.com/@michaelpotter?source=post_page-----ba70df6957d--------------------------------)[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F6a1348462387&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fbuilding-ml-models-that-are-useless-ba70df6957d&user=Michael+Potter&userId=6a1348462387&source=post_page-6a1348462387----ba70df6957d---------------------follow_byline-----------)Feb 15

·9 min read[Save](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fba70df6957d&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fbuilding-ml-models-that-are-useless-ba70df6957d&source=--------------------------bookmark_header-----------)# Building ML Models That Are Useless

## Lessons from the Healthcare Industry

![]()Pictured: Possibly a machine learning model. Kind of looks like it might be running somewhere in a hospital right?? Photo by [Carlos Muza](https://unsplash.com/@kmuza?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)So you built an ML Model. Nice! Is it actually going to work? Not just in the Kaggle leaderboard sense, but in the literal staking-lives-on-this sense? The difference between these two was resoundingly demonstrated in a 2021 Nature paper [[1](https://www.nature.com/articles/s42256-021-00338-7)] showing that, of all the recently published Covid-19 diagnostic AI models, none of them strongly generalized to datasets outside of those they were trained on. In other words, although their leaderboard scores were nearly perfect, if any of them had actually been deployed in a hospital it would have been a mess.

This problem is near-and-dear to me since I work in the healthcare industry, and in that capacity I collaborated on the development of one such Covid-19 diagnostic AI model back in 2020. We never took our model to clinical deployment, as easier tests have since been developed that don’t require taking an X-Ray of everyone who comes into the clinic, but most of the development time spent on that model was spent looking for ways to avoid the kinds of generalization failures highlighted in the Nature paper.

![]()Pictured: Not the easiest way to figure out who has Covid-19. Photo by [National Cancer Institute](https://unsplash.com/@nci?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)So how do you know whether your model really works, or whether your model just looks like it works? The authors in [[1](https://www.nature.com/articles/s42256-021-00338-7)] argue that explainable AI (XAI) techniques are necessary in order to truly validate a model. I agree with the sentiment, though common XAI techniques can actually come with their own set of traps [[2](https://arxiv.org/pdf/1810.03292.pdf)][[3](https://arxiv.org/pdf/1811.10154.pdf)] which deserve a separate post. For this post, though, I want to focus on something more fundamental:


> If you want to know if your model actually works, you need to test it on (multiple) totally different datasets than you trained it on.
> 
> 

This doesn’t mean just taking your dataset and splitting off 20% for periodic evaluations and 10% for final testing. What I am suggesting is finding a set of independently collected samples and using them as a second (or third or fourth) dataset to validate your model. Obviously this is easier said than done — even in industrial scale companies with plenty of resources at their disposal. Aside from the obvious problem of locating this extra data, you’ll also have to maintain multiple data pipelines to manage it all (since these different datasets may require different pre-processing/normalization steps in order to get the inputs ready for your model).

The data management part of this problem can at least be made easier through some specific tools, so for the rest of this post let’s walk through a few code examples to accomplish this, which also illustrate some of the unanticipated benefits you can reap while developing with generalizability in mind.

![]()Pictured: A pretty good number, all things considered. Photo by [Marcel Eberle](https://unsplash.com/@marcel_eberle?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)Let’s make a neural network that classifies numbers. Why? Because there are a bunch of datasets for this so it should be pretty easy to illustrate the main point. We’ll use the [FastEstimator](https://www.fastestimator.org) (FE) framework since it works with both [TensorFlow](https://www.tensorflow.org) and [PyTorch](https://pytorch.org), and I don’t know which way you swing. But also because I helped write FE to try and make this and other industrial-flavor use-cases easier.

Time for the key steps of the traditional ML workflow (without following our new golden rule):

1. Find your Dataset. Let’s use USPS [[4](https://ieeexplore.ieee.org/document/291440)] since it has some numbers in it.
2. Design your model. This isn’t the point today, so let’s just use ResNet9 [[5](https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/He_Deep_Residual_Learning_CVPR_2016_paper.pdf)].
3. Train your model.
4. Publish a paper on your groundbreaking results.

To save some time, here’s the code for Steps 1–3:

Nothing too special here yetNow we just need to run our training and see how we did:

![]()USPS Validation Performance (Mathews Correlation Coefficient) vs Time. Mean +- Std. Dev over 5 runs. (Image by Author)Looks like we’re not doing too badly, with a final average test performance of 0.968. Let’s pause for a moment to dwell on two quick things here though. First, you always run multiple trials to get standard deviations right? Second, you’re not still using accuracy to measure your classification performance, right[[6](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6941312/)]?? Since the Mathews Correlation Coefficient (MCC) is criminally underrated, let’s highlight the point for anyone just skimming through.


> If you are using Accuracy or F1 score to validate your models, you should be using MCC instead.
> 
> 

In this case our testing dataset has a balanced class distribution, so our MCC and Accuracy values are basically the same (0.968 vs 0.971). Nonetheless, building good habits is important since real datasets are basically never balanced, especially in the healthcare domain. MCC will keep you from accidentally fooling yourself when 99% of your data is from healthy patients and your model has an amazing 99% accuracy.

Anyways, now we’re ready for Step 4 right? Not quite. Let’s apply our first golden rule from earlier, testing our model on some totally different datasets, just to be sure. How about MNIST [[7](http://yann.lecun.com/exdb/mnist/)] and the digits dataset provided by Scikit-Learn (hereafter SKL) [[8](https://archive.ics.uci.edu/ml/datasets/Optical+Recognition+of+Handwritten+Digits)]. I hear those have some numbers in them… FE will make it easy to keep things relatively clean:

A few lines of extra effort can go a long wayNotice how adding these extra datasets only required small changes to the pipeline in order to load and wrangle all of the data into the same size, while shared transformations like MinMax can remain as they were. Any metrics you choose to use will automatically be computed for each dataset individually, as well as across all of the datasets put together. Let’s see how well our model really performs now that we have some extra digit datasets in the mix:

![]()Training summary with multiple datasets. Mean +- Std. Dev over 5 runs. (Image by Author)As you can see, even though our network is pretty good on the USPS dataset (0.97), its performance on MNIST (0.78) and SKL (0.66) is pretty bad. When we consider all the datasets together our MCC is only around 0.80. For those of you who aren’t comfortable with MCC yet, the accuracies here virtually identical: 0.97, 0.79, 0.67, and 0.80 respectively (both MCC and accuracy cap at 1.0, but MCC tends to penalize you faster as you move away from perfect performance). In any case, whereas before we might have concluded that our network understands numbers pretty well, we now know that it really only understands USPS-style numbers. This definitely isn’t what we set out wanting to accomplish.

![]()This raises questions. Photo by [Evan Dennis](https://unsplash.com/@evan__bray?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)So what do we do? Our model turned out to be pretty useless. Maybe 80% doesn’t sound too bad, but if the postal service used our model to parse 5-digit zip codes, only 33% of the mail would get where it was supposed to go. Unless we’re starting a Failure-As-A-Service company, we’ll have to make some improvements.

One option would be to train on our MNIST and SKL datasets too. While this would be an easy way to improve performance on those specific datasets, then we would have to go out and find even more digit datasets to adequately test our generalization performance. That doesn’t sound very exciting, so let’s try something else instead.

Back in NeurIPS 2019, researchers from the US Army published a paper [[9](https://papers.nips.cc/paper/2019/file/cd61a580392a70389e27b0bc2b439f49-Paper.pdf)] proposing an alternative to the softmax layer of neural networks. Instead of using a softmax layer with a one-hot class encoding, they showed that neural networks can be made more robust against adversarial attacks simply by switching to a tanh output layer with classes being encoded using hadamard labels (though strong attacks can still break this defense [[10](https://arxiv.org/pdf/2002.08347.pdf)]). The details of this are super interesting, so I highly encourage you to check out the paper. This post isn’t a summary of their paper though, I’m just curious whether the method can also help us improve our generalization performance (adversarially robust models have been shown to have more interpretable feature maps [[10](https://arxiv.org/pdf/2002.08347.pdf)], which might in turn lead to better generalization). To test it we just need to make a slight modification to our final network layers, and add one additional pipeline pre-processing step to convert our class labels into a hadamard code representation.

Here I’m stitching changes on top of a TensorFlow model, but you could use PyTorch instead. FE handles both.Although the authors didn’t advertise this as a way to improve model generalization, let’s see how we did:

![]()Pro Tip: Having multiple graphs is a great way to impress management. (Image by Author)Looks like we’ve got ourselves some clear takeaways:

1. ***Our model is still technically useless to the postal service*** (you knew the title when you clicked)
2. If we only consider USPS performance, it would be unclear that the introduction of hadamard codes caused any improvement
3. Introducing hadamard codes actually did significantly improve our best MCC when considering all the datasets together

To see point 2 more clearly, let’s zoom in on the USPS performance graph:

![]()As before, orange is hadamard and blue is baseline. (Image by Author)If this was all the data that you had, you might say that hadamard is showing some initial promise, but in the end the test set performances were within 1 standard deviation of each other (0.967 baseline vs 0.973 hadamard).


> Since most people develop models considering only one dataset at a time, they would probably stop here and revert their changes without noticing the generalization benefits of the method.
> 
> 

Once we start looking at the performances on MNIST and SKL however, we can see a very different story. The generalization performance of the hadamard model is noticeably higher than that of the baseline architecture. This is reflected in the solid separation of the curves in the Combined MCC graph (the max overall MCC increased from 0.80 to 0.88, with MNIST peak performance rising from 0.77 to 0.84 and SKL peak performance rising from 0.66 to 0.82). Hadamard codes didn’t fully close our generalization gap, but they did help, and maybe gave us some extra adversarial robustness for free. I’ll take it.

So what next? Seems like we’re stuck on Step 3 and everyone knows that Step 4 is where the fame and glory is. Well, we’ve already found one technique that boosted our overall score by 0.08. If we can just manage to do that one more time we’ll have ourselves an ML model that actually generalizes well (read: isn’t useless). Realistically, we probably do want a better dataset to pull this off. There’s a large one called DIDA [[11](https://www.sciencedirect.com/science/article/pii/S2214579620300502?via%3Dihub)] from 2021 which could be worth taking a look at. That may not seem like a very satisfying conclusion, but hey, if I already had the perfect solution for model generalization I’d be the one working on Step 4 right now ;)

Much more importantly, we now have a method in place to easily test the impact of model modifications on our generalization performance. As we saw, without monitoring this explicitly, we could easily fail to notice the true utility of ideas we’re experimenting with. Now that we have it, we can make better decisions and be much more confident that, when we do finally get a testing score we’re satisfied with, our model won’t mercilessly betray us in production. Fame and glory here we come!

![]()They give trophies for best paper right? What?? Wait, what’s even the point then? Photo by [tommao wang](https://unsplash.com/@tommaomaoer?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)# References

[1] A. DeGrave, J. Janizek, and S. Lee, [AI for radiographic COVID-19 detection selects shortcuts over signal](https://www.nature.com/articles/s42256-021-00338-7) (2021), Nature Machine Intelligence  
[2] J. Adebayo, J. Gilmer, M. Mulley, I. Goodfellow, M. Hardt, and B. Kim, [Sanity Checks for Saliency Maps](https://arxiv.org/pdf/1810.03292.pdf) (2018), NeurIPS  
[3] C. Rudin, [Stop Explaining Black Box Machine Learning Models for High Stakes Decisions and Use Interpretable Models Instead](https://arxiv.org/pdf/1811.10154.pdf) (2018), NeurIPS Workshop  
[4] J. Hull, [A database for handwritten text recognition research](https://ieeexplore.ieee.org/document/291440) (1994), IEEE  
[5] K. He, X. Zhang, S. Ren, and J. Sun, [Deep Residual Learning for Image Recognition](https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/He_Deep_Residual_Learning_CVPR_2016_paper.pdf) (2016), CVPR  
[6] D. Chicco and G. Jurman, [The advantages of the Mathews correlation coefficient (MCC) over F1 score and accuracy in binary classification evaluation](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6941312/) (2020), BMC Genomics  
[7] Y. LeCun, L. Bottou, Y. Bengio, and P. Haffner, [Gradient-based learning applied to document recognition](https://ieeexplore.ieee.org/document/726791) (1998), IEEE  
[8] C. Kaynak, [Methods of Combining Multiple Classifiers and Their Applications to Handwritten Digit Recognition](https://archive.ics.uci.edu/ml/datasets/Optical+Recognition+of+Handwritten+Digits) (1995), MSc Thesis, Institute of Graduate Studies in Science and Engineering, Bogazici University.  
[9] G. Verma and A. Swami, [Error Correcting Output Codes Improve Probability Estimation and Adversarial Robustness of Deep Neural Networks](https://papers.nips.cc/paper/2019/file/cd61a580392a70389e27b0bc2b439f49-Paper.pdf) (2019), NeurIPS  
[10] F. Tramèr, N. Carlini, W. Brendel, and A. Mary, [On Adaptive Attacks to Adversarial Example Defenses](https://proceedings.neurips.cc/paper/2020/file/11f38f8ecd71867b42433548d1078e38-Paper.pdf) (2020), NeurIPS  
[11] H. Kusetogullari, A. Yavariabdi, J. Hall, and N. Lavesson, [DIGITNET: A Deep Handwritten Digit Detection and Recognition Method Using a New Historical Handwritten Digit Dataset](https://www.sciencedirect.com/science/article/pii/S2214579620300502?via%3Dihub) (2021), Big Data Research

