[![Oscar de Felice](https://miro.medium.com/fit/c/96/96/0*xmSp_J_R-kJMTYPf.jpg)](https://oscar-defelice.medium.com/?source=post_page-----e9e0357525cc--------------------------------)[Oscar de Felice](https://oscar-defelice.medium.com/?source=post_page-----e9e0357525cc--------------------------------)[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F5b4c877fa451&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Ffrom-design-to-deploy-the-whole-lifepath-of-a-machine-learning-app-e9e0357525cc&user=Oscar+de+Felice&userId=5b4c877fa451&source=post_page-5b4c877fa451----e9e0357525cc---------------------follow_byline-----------)Mar 18, 2021

·26 min read[Save](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fe9e0357525cc&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Ffrom-design-to-deploy-the-whole-lifepath-of-a-machine-learning-app-e9e0357525cc&source=--------------------------bookmark_header-----------)# From Design to Deploy: The whole Lifepath of a Machine Learning app

## The step-by-step description to design, develop, deploy and maintain a Machine Learning application. Through an example. With code.

Why should you read a 25min reading time medium post? Well, here I tried to condense the complete path of a machine learning project, from data analysis to deployment on AWS EC2.

# Introduction

In the age of innocence, after following our first ML courses, we all thought that to be a data scientist, working on notebooks would have been enough.

Once we left kindergarten, we learnt that this is far from the truth.

Nowadays there is plenty of other skills a data scientist must have other than knowledge of machine learning algorithms (or more often library usage).

This post aims to go through an example (I will keep it easy on the model part) of a complete machine learning task example from design to deploy and maintain.

I do this because I have spoken and worked with dozens of data scientists, also not so junior in their career, and I got a picture of great confusion about the role. Data science is a great activity, but often data scientist codes are really difficult to bring in production (and even to read) because they have been written without thinking of the real-world use of the model.   
I find this is a matter of respect — for the whole stack of poor devils working on the model after the data scientist — provide a solid and simple model deploy.  
Furthermore, these days docker is a skill highly requested in all data science job offers, so why not take some time to see how dockerise a machine learning application?

![]()The ubiquitous image used to illustrate the machine learning project lifecycle. Image by [<https://www.jeremyjordan.me/ml-projects-guide/>]The figure above is nice, but I think it may appear a bit too abstract. I will use my poor drawing abilities to redesign it as follows.

![]()A simplified model lifecycle. Image poorly drawn by the author.The image above is also the schema we are going to follow in this post.

# Problem definition

To be concrete, let’s start by defining our problem. Imagine you work in a consulting company (as I do) and your colleague from sales comes to you saying “Hey dude, an estate agency wants a house price estimator, can we do that?”.  
I hope your answer would be “no problem”, hence we can start.

Before diving into the problem, let me make an observation. There should be an earlier (and important) step: data collection (that can be scraping, client database interrogation, etc.), that will be neglected here because this would lead us out of track.

# 0. Preliminary analysis

Under this part normally goes data collection, labelling, data analysis, some visualisation to better understand the kind of problem we are dealing with, data cleaning, etc.

Since these procedures are heavily influenced by the specific data to cope with, we keep it as simple as possible. We will briefly describe exploratory data analysis and that’s it.

## Data Collection

I know, I wrote I would have neglected this part. I did not lie.  
Here I imagine, the client gave us a nicely labelled dataset (this [one](https://www.cs.toronto.edu/~delve/data/boston/bostonDetail.html)). In real (tough) life you usually spend a lot of time labelling data yourself, but we are still living in fairy tales for now.

Hence, let’s start by simply import our data into a pandas dataframe.

The `print(df.head())` command prints the following

![]()One can look at print the quantity `boston_dataset.DESCR` to have a brief description of the features.


```
**CRIM**: Per capita crime rate by town  
**ZN**: Proportion of residential land zoned for lots over 25,000 sq. ft  
**INDUS**: Proportion of non-retail business acres per town  
**CHAS**: Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)  
**NOX**: Nitric oxide concentration (parts per 10 million)  
**RM**: Average number of rooms per dwelling  
**AGE**: Proportion of owner-occupied units built prior to 1940  
**DIS**: Weighted distances to five Boston employment centers  
**RAD**: Index of accessibility to radial highways  
**TAX**: Full-value property tax rate per $10,000  
**PTRATIO**: Pupil-teacher ratio by town  
**B**: 1000(Bk — 0.63)², where Bk is the proportion of [people of African American descent] by town  
**LSTAT**: Percentage of lower status of the population  
**MEDV**: Median value of owner-occupied homes in $1000s
```
The last one is our target, and it is not included in the dataframe. Indeed, it is accessible by `boston_dataset.target`.

## Exploratory data analysis

This is the part where you discover and familiarise yourself with your data.

First of all, it’s a good practice to see if there are any missing values in the data. We count the number of missing values for each feature using `isnull()`. In this case, you might not be surprised to discover there is no missing value.  
Now, we will use some visualisation to characterise the distribution of our data and to understand how target and feature variables are related.  
What we discover is that the distribution is more or less normal, with few outliers.

![]()To better study feature variables one option is the correlation matrix or correlation plots. Since we have quite a few of them, we prefer the correlation matrix, easier to visualise.

![]()What we can notice:

* Some of the features have a strong positive correlation, both between them and with the target variable. If we want to go for a linear model, then we reasonably select such features. By looking at the correlation matrix we can see that `RM` has a strong positive correlation with the target (0.7) whereas `LSTAT` has a high negative correlation with it (-0.74).
* For a linear regression model, it might be important is to check for multi-co-linearity. In our case, for example, `RAD` and `TAX` are really related (intuitively they can be exchanged without losing too much information).
* To capture higher correlation orders, one may study the correlation matrix of features squared, or at the third power, etc.
* One can reduce features with some other more systematic methods (like t-SNE, PCA, etc.) and study the correlation of the reduced features with the target variable.

Based on the above observations we could keep`RM` and `LSTAT` as our features. However, since this is not the interest of this post, we will ignore this and use all the features.

## Preparing data to feed the model

We can collect data into train test split using the popular method of sklearn.

There is one last step that is strongly advised to take: clean your data pipeline now. To do so, we will write a simple set of functions. The key-word is “*modular*” since you want to re-use this code in other projects and also you may want to maintain this model and maybe add/remove features.

Note how we used a dictionary to input arguments for the `import_data` function. This because we have in mind to feed such function with `json` or `yml` files through HTTP protocol.

Since I have already in mind the model I wanna use, I make this further consideration of data normalisation. Some problems may arise in feeding a neural network with data spreading over different intervals (both in size and central point). In principle, a well-trained model should adapt to such differences and encode them properly, however, this requires a lot of data and at the end of the story makes the model more difficult to train, less robust and eventually not precise.  
A widespread best practice to deal with such data is to do feature-wise normalization: for each feature in the input data (a column in the input data matrix), we will subtract the mean of the feature and divide by the standard deviation, so that the feature will be centred around 0 and will have a unit standard deviation.

Hence we modify the function above as follows,

# 1. Model building

At this stage, we design our model and train it in order to evaluate its performances. Normally, this part is done in a notebook without worrying too much about name conventions, functions, OOP, comments, etc.   
However, my advice (also here) is to be as much clean as possible, since this can save you from hours of “*converting code into something readable*” later.

## Algorithm design

Previously performed data analysis should drive this part. For example, a decision tree-based algorithm or an XGBoost would allow you to obtain great results.

Normally this part is made of a trial-error approach. Often you do not want to train your candidates model on the whole dataset (when you have a lot of data), so one solution might be to random sample your training data and train a bunch of models to compare their performances and choose the best one according to your chosen metric.

An aside, choosing the right metric for the problem is crucial. Of course, this is problem-dependent, however, here we can state the three properties a good metric has to satisfy:

1. It has to be **single-numbered**. You want to make easy comparisons.
2. It has to be **satisficing** with respect to some numerical performance property. *i.e.* It has to measure algorithm numerical performances.
3. It has to be **optimising**. *i.e.* It has to measure algorithm results.

The typical example is: we pick the model with the highest *F1*-score and inference time under 10 milliseconds.

Of course, this is an initial analysis. Usually, you may go through the complete training of a couple of different models before choosing the “right one”.  
Here, we pretend we have done everything properly and we refer to this great post for details.

[## Satisficing and optimizing metric

### There are different metrics for assessing a classifier‘s performance, they are called evaluation matrices. They can be…

medium.com](https://medium.com/structuring-your-machine-learning-projects/satisficing-and-optimizing-metric-24372e0a73c)Let’s say from our analysis we have chosen a Neural Network model. Again, my advice is to write your notebook cells always having in mind that you are going to convert this code in production, so be clean!

You can start to recognise a pattern. The config dictionary is going to be a json (or yml, or some other similar format) file.![]()Once the model is defined and compiled (if you are a PyTorch person, no need for compilation), we are ready to train it on our data.

## First Training

Let’s fit the model on our training data and measure the performance on test. To be rigorous, we should also have a validation set, but we will have time to worry about this later on. In this phase, we just want to end up with a working model and a measure of its performances. This is the overcited *quick-and-dirty* approach, that has nothing to do with how messy is your code.

## Model evaluation

It is always useful (even more in the regression case) to look at learning curves.

![]()![]()We can see how our model is still minimising the loss function. This would suggest increasing the number of epochs.  
We have also alternatives, *i.e.* increasing the modelisation power of our network, that is modifying its architecture, more hidden units and more hidden layers.  
We will try both in the next section.

To conclude, an attentive reader may have noticed how the test loss seems to be lower than the training one. This is an effect of the fact that Keras computes the two losses in a slightly different way. I refer to this post for details.

[## Why is my validation loss lower than my training loss? - PyImageSearch

### Ever wonder why your validation loss is lower than your training loss? In this tutorial, you will learn the three…

www.pyimagesearch.com](https://www.pyimagesearch.com/2019/10/14/why-is-my-validation-loss-lower-than-my-training-loss/#:~:text=The%20second%20reason%20you%20may,is%20measured%20after%20each%20epoch)## Hyperparameter choice and optimisation

In the previous section, we ended up with two possible options to improve our model.

We can try both ways and see which solution gives us the best results on the test-set. We are actually using our test set as a validation one.

The previous model configuration gave us the plot above. Let’s leave everything unchanged and just increase the number of epochs to 100.  
The only thing to do is modify the `config` variable as follows.


```
config = {  
 'data': boston\_dataset,  
 'train\_test\_ratio': 0.2,  
 'model\_config': {  
 'model\_name': 'house\_pricing\_model',  
 'layers': {  
 'first\_layer': 12,   
 'second\_layer': 5,   
 'output\_layer': 1  
 },  
 'activations': ['relu', 'relu', None],  
 'loss\_function': 'mse',  
 'optimiser': 'adam',  
 'metrics': ['mae']  
 },  
 'training\_config': {  
 'batch\_size': 10,  
 'epochs': 100  
 }  
 }
```
Everything else stays the same, we can reinitialise our model and run the train function again. We get,

![]()while learning curves look like

![]()![]()Great result! We cannot see overfitting issues and loss stabilises between around 85/90 epochs.

In order to give some meaning to the value of the error, we have to look at the target variable. `df.target.describe()` (and the histogram we plotted earlier) gives us the information we want.

![]()We can see how a mean absolute error of ~2.3 corresponds to an error of more or less the 10% on the average of our data.

*NOTE*: To make our error estimation more robust, we should operate k-fold cross-validation and take as mean absolute error value the average over the folds. We will neglect this here for the sake of readability.

Let’s try the other option and modify the number of hidden units and hidden layers.


```
config = {  
 'data': boston\_dataset,  
 'train\_test\_ratio': 0.2,  
 'model\_config': {  
 'model\_name': 'house\_pricing\_model',  
 'layers': {  
 'first\_layer': 64,   
 'second\_layer': 64,  
 'third\_layer': 32,  
 'output\_layer': 1  
 },  
 'activations': ['relu', 'relu', 'relu', None], # Regression problem: no activation in the last layer.  
 'loss\_function': 'mse',  
 'optimiser': 'adam',  
 'metrics': ['mae']  
 },  
 'training\_config': {  
 'batch\_size': 10,  
 'epochs': 100  
 }  
 }
```
We added a layer and increased the number of hidden units in each layer. Let’s train with such a configuration.

![]()Numbers are slightly improved! Let’s look at learning curves.

![]()![]()They are good, but we start to see the nemesis of any data scientist: overfitting. Around epoch 15/20 training loss became systematically lower than test loss, and such divergence grows with epochs.  
We can lower the number of epochs, or insert a Dropout layer to reduce the overfit. And so on, until we are happy with the result.

For our purposes, we will stop here and choose the following configuration.


```
config = {  
 'data': boston\_dataset,  
 'train\_test\_ratio': 0.2,  
 'model\_config': {  
 'model\_name': 'house\_pricing\_model',  
 'layers': {  
 'first\_layer': 64,   
 'second\_layer': 64,  
 'third\_layer': 32,  
 'output\_layer': 1  
 },  
 'activations': ['relu', 'relu', 'relu', None],   
 'loss\_function': 'mse',  
 'optimiser': 'adam',  
 'metrics': ['mae']  
 },  
 'training\_config': {  
 'batch\_size': 10,  
 'epochs': 17  
 }  
 }
```
**Optuna**

Another more efficient option is to look for the best hyperparameter configuration with a library. [*Optuna*](https://optuna.org/) is a library that does exactly this, recently they introduced also an experimental feature looking for the best model architecture. My advice is to try it out.

[## Using Optuna to Optimize TensorFlow Hyperparameters

### Automate the tuning of hyperparameters in TensorFlow using Bayesian Optimisation in Optuna

medium.com](https://medium.com/optuna/using-optuna-to-optimize-tensorflow-hyperparameters-57b6d4d316a2)Hyperparameter optimisation is a really fascinating topic and it would require a series of posts on its own, but for this article, let’s follow our guided-example and go on to build the training pipeline.

## Pipeline construction

Since I want to focus on the serving part, here I will keep the training pipeline simple, however, you can make this as involved as you want. For instance, one can build another app to build and train your model.  
Strictly speaking, one could also train the model in a notebook than save the model file and export it. This can be done, however, I would advise against it, because a notebook has no versioning system, you cannot check whether you introduced some non-compatibility issues, etc.

Here we will adopt a half-way solution: we will create a script, taking a config file as input (the only one you should modify in the successive versions of your model) and returning a saved model file.  
Since we put some attention in writing the cells of our notebook, the script is quite easy to create.

We will make use of an auxiliary library since our script will be executed by a command-line interface and we want to pass the config file path as an argument without touching the script code.

The script is really brief and very schematic.

Note that we imported an `utils` module, which is a collection of the functions we defined above. Note also that this is not the cleanest way to do things, we could (and normally we should) modularise even more, and even better, create classes collecting methods for our model.

As a bonus, you can transform this training script into a command, *i.e.* you will turn


```
python3 -m estimator train --conf config.json
```
into


```
estimator train --conf config.json
```
To do so, you can read this nice medium post.

[## Turning Python Scripts into CLI Commands

### In this article, we are exploring how you can turn your Python scripts into fully-fledged CLI commands

christopherdoucette.medium.com](https://christopherdoucette.medium.com/turning-python-scripts-into-cli-commands-aecf56dfda18)The `config.json` file contains all the information to define and train our model.

## Model training

Finally, we are ready to run the proper training of our chosen model. Once the model is fitted, we save it to export and serve it to the next-section-coming API.

This is automatically done by one single command in a command-line shell:


```
python3 -m estimator train --conf config.json
```
*NOTE*: To not make this too long post even longer, here I am not considering one of the greatest features in Keras: callbacks. One can set a metric and monitor it during training in order to automatically stop the fit when your model does not improve over epochs, or save automatically the best metric result, no matter in which epoch it has been reached, etc. A great source for reference is the [official documentation of Tensorflow](https://www.tensorflow.org/guide/keras/custom_callback).

# 2. Deploy

Now that your model is trained and saved somewhere locally, we are able to start the fascinating chapter of deployment.

By this dark and evil word, we simply mean making our model available and reachable (from users or other applications) in order to provide predictions.

The scheme is simple: we want to put our model somewhere, make it receive *requests* and give back predictions. In our example, we want to feed the model with houses (more appropriately with feature vectors describing houses) and get as *response* price predictions for the house fed in.

Since we do not want to be the only users or our model, we have to choose a protocol that is publicly (or at least to a certain list of users) accessible from outside our local system.

One of the major ideas in modern computer science is [*containerisation*](https://www.sumologic.com/glossary/container/)*.* By this, we mean bundling an application together with all of its related configuration files, libraries and dependencies required for it to run in an efficient and bug-free way across different computing environments. Going on this path, we split our complex applications into packages and then we compose containers together in other to make them without worrying about the system they are going to be executed on.

A great source to learn about containers is the nice medium post below.

[## A Brief Introduction to Containers

### Whether you’re new to development or a seasoned developer, containers have proven to be game-changing in building to…

medium.com](https://medium.com/cycleplatform/a-brief-introduction-to-containers-d34e64e61bc1)![]()An even poorlier drawn image by the author. We added the numbers referring to the steps below.In this spirit, and following the scheme in the figure above, we have to:

1. Create an API to serve our model. We will do this by using FastAPI.
2. Containerise our API. We will do this by Docker.
3. Push the docker image on some service. We are going to use AWS ECR.
4. Deploy the docker container containing the app on some service. We will make use of a virtual machine service: AWS EC2.

Note that these steps are more or less the same as any other software application to be deployed.


> Data scientist are (among other things) developers and must be able to follow the typical [software life-cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle).
> 
> 

Indeed one can follow these very same steps also and deploy the “hello world” API (*i.e.* the to-do list). This is actually a very nice exercise and can be used to practice such a procedure. To develop the to-do list API one can refer to the following article.

[## Making a Todo app from a beginners perspective. Part: 1 Intro to FastAPI

### The what why and how

surikavii.medium.com](https://surikavii.medium.com/making-a-todo-app-from-a-beginners-perspective-part-1-intro-to-fastapi-5006abbcb7a2)Do not get scared, these parts are quite straightforward. Here there is no analysis to take into account, no trial-error approach. The objects we are going to define here are mostly a copy-paste of code handed down for generations of fellow programmers.

## API Creation

We are going to use FastAPI, which is one of the possible web frameworks you can use to convert your Python code into an app communicating by HTTP protocol.

The advantage of FastAPI is that is fast (almost as a compiled language), easy to learn, widely used (a lot of online support), and it builds handy online documentation for your app.

So let’s build our app.  
We need to create the following directory structure:


```
├── \_\_init\_\_.py├── ai| ├── \_\_init\_\_.py| ├── regressor.py| └── services.py├── main.py├── model| └── model.h5└── schemas| ├── \_\_init\_\_.py└──└── schemas.py
```
This is not strictly necessary, you can have everything in the same file (may the gods forgive you), or you can use frameworks structuring your Python project for you, *e.g.* [cookie-cutter](https://github.com/cookiecutter/cookiecutter). However, I strongly advise following a fixed schema to get used to such structures.

We will explore each file individually.

Let’s start from the main, which is the file we are going to launch to execute our app.

**main.py**

You can see, the code is quite self-explanatory and even without knowing the exact implementation of the function you can say what this app does at high level. It receives data (of type `InputData` ) and returns a dictionary (actually a type `ResponseDataAPI`, see function decorator) containing input data and predictions.

In FastAPI decorators are used to define the HTTP methods, in our app we only need a get (to check the status of the app) and a post (to send the data and obtain predictions).

We can run the app locally by the terminal command


```
uvicorn main:app --reload
```
Opening a browser and going to the local address <http://127.0.0.1:8000/docs> we will see the automatic interactive API documentation (provided by [Swagger UI](https://github.com/swagger-api/swagger-ui)). You can access the alternative documentation page at <http://127.0.0.1:8000/redoc>.

![]()This is what you should see. Image by the author.There is plenty of functionalities to explore (and a good reference to look at is always the very well written [FastAPI documentation](https://fastapi.tiangolo.com/)), here I just want to mention two main aspects:  
*1.* The API comes automatically with a web interface. This allows you to show the working scheme of your model even to some non-tech fellow. And this comes for free.  
*2.* You have an URL that can be interrogated with json strings and responds in the same format. This is really useful to go in production, *i.e.* you can host this app on a web server and start integrating with other apps, that is the key to production procedures.

This second aspect may be explicitly interrogated by terminal


```
curl -X 'POST' \  
 '[http://127.0.0.1:8000/](http://127.0.0.1:8000/docs)v1/services/predict' \  
 -H 'accept: application/json' \  
 -H 'Content-Type: application/json' \  
 -d '[  
 {  
 "CRIM": "float",   
 "ZN": "float",   
 "INDUS": "float",   
 "CHAS": "int",   
 "NOX": "float",   
 "RM": "float",   
 "AGE": "float",   
 "DIS": "float",   
 "RAD": "float",   
 "TAX": "float",  
 "PTRATIO": "float",   
 "B": "float",   
 "LSTAT": "string"  
 }  
]'
```
Note we have to provide the examples in a json collecting all the features we have trained the model on. We may have changed the name, but because of a lack of imagination, we left them unchanged with respect to the initial dataset.

Thus, for instance, to get a prediction, we can give the terminal command


```
curl -X 'POST' \  
 '[http://127.0.0.1:8000/](http://127.0.0.1:8000/docs)v1/services/predict' \  
 -H 'accept: application/json' \  
 -H 'Content-Type: application/json' \  
 -d '[  
 {  
 "CRIM": 0.09178,   
 "ZN": 0.0,   
 "INDUS": 4.05,   
 "CHAS": 0,   
 "NOX": 0.510,   
 "RM": 6.416,   
 "AGE": 84.1,   
 "DIS": 2.6463,   
 "RAD": 5.0,   
 "TAX": 296.0,  
 "PTRATIO": 16.6,   
 "B": 395.50,   
 "LSTAT": 9.04  
 }  
]'
```
and the API response will be printed on the screen


```
{  
 "inputData":   
 [{  
 "CRIM": 0.09178,   
 "ZN": 0.0,   
 "INDUS": 4.05,   
 "CHAS": 0,   
 "NOX": 0.510,   
 "RM": 6.416,   
 "AGE": 84.1,   
 "DIS": 2.6463,   
 "RAD": 5.0,   
 "TAX": 296.0,  
 "PTRATIO": 16.6,   
 "B": 395.50,   
 "LSTAT": 9.04  
 }],  
 "predictions": [{"Prediction price 0": 26.900973}]  
}
```
**ai/regressor.py**

This is the file containing the class definition of our model. We define the `PriceEstimator` class and give a minimal amount of methods. Usually, you do not want someone can train your model from the API, hence there is no `train` method for this object. There is the `predict` one thou since you want to expose your model for predictions.

You can recognise the very same function we used in the data pipeline. The driving force of any programmer should be laziness.   
In this context, a cleaner approach would be to simply import the same function from the module we have defined earlier, although this, usually, you want to keep the training part of your code and the prediction part well separated.

**ai/services.py**

This file contains the code to return the prediction and the load of the model from a pretrained saved file. Note how we read the `MODEL_FOLDER` variable from the environment. This means (to run the app locally) that we have to add the model path to the environment. How you do this depends on the OS, a quick google search will give you the answer. On linux/mac this can be done in a terminal by


```
export MODEL\_FOLDER='path/to/your/model'
```
**schemas/schemas.py**

This file is the one defining the custom types (in Python any object is a type) of input and output of our app.

Everyone knows Python is a dynamically typed programming language, meaning the type of variables is not declared, bu inferred by their value, and can also change during the execution of a program.  
This behaviour is really handy since you do not bother in defining variable types, in keeping attention to never assign the same variable name to values of different types, etc. However, this is also one of the main reasons why Python is so slow in comparison with some other statically typed language, like C/C++, Go, etc.  
For a detailed discussion, one can read [this extremely interesting reference](http://gallium.inria.fr/~remy/mpri/cours1.pdf) or the [relative Wikipedia page](https://en.wikipedia.org/wiki/Type_system).

We already pointed out the reason we want to use a web framework like FastAPI is that it is almost as fast as a compiled language, this is reached by slightly modifying such behaviour about type declaration by allowing it.  
Hence, we will define and set a fixed type for input and output data.

This is done by the `[typing](https://docs.python.org/3/library/typing.html)` [library](https://docs.python.org/3/library/typing.html), which is not a real type declaration, but more a hint. In such a way, we allow the Python interpreter to allocate the right quantity of memory for the “declared” type.

We defined an example that can be shown on the interactive doc page of FastAPI.

Note how we defined here the types we declare in the main.py functions.

## Dockerise the FastAPI

We are now ready to dockerise our app.   
We already discussed why containers are crucial in the modern software industry. Here I just wanna synthesise a problem that docker solves.


> *A*: Look how cool my model is. I’ll send you the script, so you can execute on your machine.  
> *B*: Received, however it gives me an error while importing xxx library, I solved by Stack-Overflow, and now my numbers are different than yours.  
> *A*: Come and look at my screen, here it works as expected.
> 
> 

If A sent B a docker image, this would have never happened.

Let’s see how to dockerise our API. To dockerize the application, first, you need a Dockerfile

Dockerfiles describe how to assemble a private filesystem for a container, and can also contain some metadata describing how to run a container based on the image. (Recall the difference between image and containers, [here](https://phoenixnap.com/kb/docker-image-vs-container)).

We will also use a file called `requirements.txt`, a list of all the libraries we used in the project and their version. We want our app to run without compatibility issues on any machine.

As said, the following part can be presented really schematically and here I closely follow the excellent post below, just adapting commands to the present case.

[## Deploying FastAPI Web Application in AWS

### A step by step guide to deploy FastAPI application in AWS.

medium.com](https://medium.com/@meetakoti.kirankumar/deploying-fastapi-web-application-in-aws-a1995675087d)*i) Create a docker file*

Here we make our app run at the address [*http://0.0.0.0:5000*](http://0.0.0.0:5000).   
Note how we defined the model location as an environment variable: this is because our app reads such value from the environment.

*ii) Build Docker Image:*

This is done by a line command


```
docker build -t price\_estimator\_api:latest .
```
*iii) Run the docker image*

Now the easy part: let’s run the docker.


```
docker run -p 5000:5000 price\_estimator\_api:latest
```
You can verify the app running by opening a browser at the page [*http://localhost:5000/docs*](http://localhost:5000/docs)*.*

To learn more about Docker, you can look at the official tutorials.

[## Docker overview

### Docker is an open platform for developing, shipping, and running applications. Docker enables you to separate your…

docs.docker.com](https://docs.docker.com/get-started/overview/)## Push on Amazon Elastic Container Registry

Now that you verified that your app container is running locally, we are ready to move it to some accessible “place”. This can be any server with public (or at least non-local) access. Here we want to use the AWS EC2 service.

We do not want to bother thinking about machine configuration, scalability, etc. So we will put the docker image on a docker registry, the Amazon Elastic Container Registry (ECR). This is a fully-managed [Docker](https://aws.amazon.com/docker/) container registry that makes it easy for developers to store, manage, and deploy Docker container images.

First, in order to push docker images to ECS, you need to install and configure AWS CLI. Instructions are available on the AWS website.

[## Installing, updating, and uninstalling the AWS CLI version 2 on macOS

### AWS CLI versions 1 and 2 use the same aws command name. If you have both versions installed, your computer uses the…

docs.aws.amazon.com](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-mac.html)One way to configure the AWS CLI is getting access key ID and Secret Access Key from **Identity and Access Management (IAM) in the AWS console.**

You simply create new access keys and store them for future purposes.

![]()In a terminal, you can configure access.


```
aws configureAWS Access Key ID [None]: ***AKIAIOSFODNN7EXAMPLE***  
AWS Secret Access Key [None]:***wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY***  
Default region name [None]: ***eu-west-3***  
Default output format [None]:***json***
```
You are now ready to access ECR using the following command, provide **region** and **account id** details.


```
aws ecr get-login-password --region **region** | docker login --username AWS --password-stdin **aws\_account\_id.**dkr.ecr.**region**.amazonaws.com
```
You should see **“Login Succeeded”** on the console if everything goes well.

You can now push your image on the AWS registry.  
First, create a repository.


```
aws ecr create-repository --repository-name price\_estimator\_api
```
Tag your image in order to push on the registry.


```
docker tag price\_api:latest **aws\_account\_id**.dkr.ecr.**region**.amazonaws.com/price\_estimator\_api
```
Finally, run the command to push the image on ECR.


```
docker push **aws\_account\_id**.dkr.ecr.**region**.amazonaws.com/price\_estimator\_api
```
## Deploy on EC2

After pushing the docker image to AWS ECR, we are now ready to create Amazon EC2 instance which can serve your web application. AWS offers many instances in the free tier, I have chosen a Linux instance in this case (you can use other instances as well but do remember to change the configuration accordingly).

*i ) Go to Amazon Console; select Amazon Linux EC2 instance.*

*ii) Choose general purpose t2.micro instance type, for example.*

![]()*iii) Change the security settings by adding rules using custom TCP as type and port as 5000 (we exposed that port of the API) and click on review and launch the instance. These configurations are necessary for our web application to run.*

![]()*iv) Create a new key pair by selecting from the dropdown “*Create a new key pair*”, provide a name for the key pair, and download it.*

A key pair, consisting of a private key and a public key, is a set of security credentials that you use to prove your identity when connecting to an instance.

You should able to see the instance running.

You downloaded the key pair, so a `.pem` key. Suppose we gave the name `priceestimator.pem` , we can use such a file to log on to the EC2 by using a secure ssh connection.


```
ssh -i priceestimator.pem ec2-user@**ec2-18-221-11-226.us-east-2.compute.amazonaws.com**
```
One logged in, we install the docker on the EC2, configure AWS access to give rights to the machine to access our docker image, and pull the docker container to the machine.

AWS configuration starts as above,


```
aws configureAWS Access Key ID [None]: ***AKIAIOSFODNN7EXAMPLE***  
AWS Secret Access Key [None]:***wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY***  
Default region name [None]: ***eu-west-3***  
Default output format [None]:***json***
```
Then we run the following commands to add ec2 user to perform docker commands in Linux machine.


```
sudo groupadd dockersudo gpasswd -a ${USER} dockersudo service docker restart
```
Exit the instance and ssh into the EC2 instance again.


```
ssh -i priceestimator.pem ec2-user@**ec2-18-221-11-226.eu-west-3.compute.amazonaws.com**
```
Log into the Amazon ECR registry:


```
aws ecr get-login --region **region** --no-include-email
```
output


```
docker login -u AWS -p <password> -e none https://<aws\_account\_id>.dkr.ecr.<region>.amazonaws.com
```
Copy the output from the above and run it in the command line. Once you are successfully logged into AWS ECR, you can see “Login Succeeded” in the console.

Pull the docker image from AWS ECR on the EC2.


```
docker pull **aws\_account\_id**.dkr.ecr.**region**.amazonaws.com/price\_estimator\_api:latest
```
Run the docker container in the Linux Machine


```
docker run -p 5000:5000 **aws\_account\_id**.dkr.ecr.**region**.amazonaws.com/price\_estimator\_api
```
Finally, we can get the IPv4 Public IP from the instance details page and add port 5000 while launching it in the browser. This will show the API running on EC2.   
Now you can substitute such an IP address with a more human-readable URL.

Enjoy!

# 4. Maintenance

And finally the dessert: maintaining the deployed app is crucial. A change in data distribution may result in no predictive power of your model.

Now your model works fine, lucky you. You are happy and ready to repeat the story for another client and another model.

However, the real estate agency starts to get some houses to sell in a very different location. They use your model and they find your estimate completely wrong! They are angry at your company, your boss starts to tell you off about the awful job you have done.

How would you handle this?

Fortunately, by acting as you have done you can easily deploy a new model, by training on new data and make your model more accurate on the new data distribution. Let’s see how.

What we have done previously is not lost. We can load the current model and use it as a starting point for a new train. We make leverage of previously learnt weights and we simply train our model on new data. If necessary (you want to completely change your model, for some reason) you can also develop a new model. If you coded properly, nothing should change in the whole pipeline.

**Load the current model** **as pretrained** in `config.json`. Now you can relaunch the training script and get the newly trained model. Change the save model name to keep versioning.

**Save the new model** As before, we save the model in the folder the API is going to read. We can add the date-time reference in the naming convention in order to keep track of versions.

**Modify the Dockerfile** Since we version our app, we modify the `Dockerfile` to get the right model version to be deployed.

Finally, **push the Docker image** and make it run as above.

*NOTE:* It’s usually advisable to write the deploy part as a pipeline, that starts automatically at every push on some git repository. All git control systems offer the possibility to register safely some repository environment variables. One can set some secret AWS credentials there and automatise this part. For more information, look at the following tutorial, for example.

[## Get started with Bitbucket Pipelines | Bitbucket Cloud | Atlassian Support

### Bitbucket Pipelines is an integrated CI/CD service built into Bitbucket Cloud. Learn how to set up Pipelines.

support.atlassian.com](https://support.atlassian.com/bitbucket-cloud/docs/get-started-with-bitbucket-pipelines/)# Conclusions

First of all, let me congratulate you if you have read till here! This post has become a little longer than I expected.

To sum up, I tried to summarise, working through a concrete example, how the typical data science project develops, to my experience. I would like to warn you: this is not the complete story. There are a lot of points I missed and neglected, a lot of caveats, a lot of different requests, etc.

For instance, another possibility might be to not bother at all with containers and services and convert our model in some other language, easily runnable online.   
For a web app, for example, one may convert the model in JavaScript (making use for instance of TensorFlowJS or TorchJS running models on a browser) and then build a website to be hosted on some server. This is an example of a specific case. Indeed, this is accessible through a website, but what if you need an app to access this? Or some other non-human service?

Docker is a more general and widely used method, this is why I have chosen to present it here.  
Hence, without being complete, this post aimed to illustrate — in a schematic way — the lifecycle of a machine learning project.  
I hope this can be useful both to junior data scientists, often feeling lost in this wide world, and to more expert figures that can also give me some hint about the points I surely forgot.

I hope you enjoyed reading this!


> IMPORTANT: I publish this post also to get suggestions, to discuss and to be made aware of points of weakness in my coding. Please, signal any mistakes/reduntant code! 😫
> 
> 

🤯 ***Have you seen what happens if you click the “clap” button multiple times?***

