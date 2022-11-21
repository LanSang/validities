[![Emeli Dral](https://miro.medium.com/fit/c/96/96/1*6rBQFw_1M7kMoJVt6gg6lw.jpeg)](https://medium.com/@emeli.dral?source=post_page-----391435c8a299--------------------------------)[Emeli Dral](https://medium.com/@emeli.dral?source=post_page-----391435c8a299--------------------------------)[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Ff21493d48f9f&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fmonitoring-machine-learning-models-in-production-how-to-track-data-quality-and-integrity-391435c8a299&user=Emeli+Dral&userId=f21493d48f9f&source=post_page-f21493d48f9f----391435c8a299---------------------follow_byline-----------)Jan 19, 2021

·13 min read[Save](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F391435c8a299&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fmonitoring-machine-learning-models-in-production-how-to-track-data-quality-and-integrity-391435c8a299&source=--------------------------bookmark_header-----------)# Monitoring Machine Learning Models in Production

## How to Track Data Quality and Integrity

![]()Image by Author.As the saying goes: garbage in is garbage out. Input data quality is the most crucial component of a machine learning system. Whether or not you have an immediate feedback loop, your model monitoring always starts here.

# What Can Go Wrong With The Data?

There are two types of data issues one encounters. Put simply:  
1) something goes wrong with the data itself; or  
2) the data changes because the environment does.

Let us start with the first category. It alone has plenty.

# #1 Data processing issues

A machine learning application usually relies on upstream systems to provide inputs. The most trivial — but frequent — occasion is when the production model does not receive the data. Or, it receives corrupted or limited data, all due to some pipeline issues.

## Let’s take a marketing example.

The data science team in a bank developed a mighty machine learning system to personalize promo offers sent to clients each month.

This system uses data from an internal customer database, clickstream logs from the internet banking and mobile app, and call center logs. Also, the marketing team manually maintains a spreadsheet where they add this month’s promo options.

All the data streams are merged and stored in a data warehouse. When the model is run, it calculates the necessary features on top of the joint table. The model then ranks the offers for each client based on the likelihood of acceptance and spits the result.

![]()*A simplified pipeline jungle for the promo personalization use case. (*Image by Author).This pipeline uses multiple data sources. And, a different functional owner maintains each of them. Quite some opportunity to mess with it!

## Here is an incomplete list of the nasty things to happen:

* **Wrong source.** A pipeline points to an older version of the marketing table, or there is an unresolved version conflict.
* **Lost access.** Someone moved the table to a new location but did not update the permissions.
* **Bad SQL.** Or not SQL. Whatever you use to query your data. These JOINSs and SELECTs might work well until the first complication. Say, a user showed up from a different time zone and made an action “tomorrow”? The query might not hold up.
* **Infrastructure update.** You got a new version of a database and some automated spring cleaning. Spaces replaced with underscores, all column names in lowercase. All looks fine until your model wants to calculate its regular feature as “Last month income/Total income”. With hard-coded column titles. Ouch!
* **Broken feature code.** I dare to say, the data science code is often not production-grade. It can fail in corner cases. For instance, the promo discounts were never more than 50% in training. Then marketing introduces a “free” offer and types 100% for the first time. Some dependent feature code suddenly makes no sense and returns negative numbers.

When data processing goes bad, the model code can simply crash. At least, you’ll learn about the issue fast. But if your Python code had some *“Try…Except”* clauses, it might execute on incorrect and incomplete input. The consequences are all yours.

The promo example we looked at has batch inference. It is less dramatic. You have some room for error. If you catch the pipeline issue on time, you can simply repeat the model run.

In high-load streaming models, the data processing problems multiply (think e-commerce, gaming, or bank transactions).

# #2 Data schema change

In other cases, data processing works just fine. But then a valid change happens at the data source. Whatever the reason, new data formats, types, and schemas are rarely good news to the model.

On top of this, the author of the change is often unaware of the impact. Or, that some model even exists down there.

## Let’s go back to the promo example.

One day, the call center’s operational team decides to tidy up the CRM and enrich the information they collect after each customer call.

They might introduce better, more granular categories to classify calls by the type of issue. They would also ask each client on their preferred communication channel, and start to log this in a new field. And since we are here: let’s rename and change the order of fields to make it more intuitive for new users.

Now, that looks neat!

![]()Image by Author.But not so to the model.

**In technical terms, this all translates to lost signal.**

Unless explicitly told so, the model will not match new categories with the old ones or process extra features. If there is no data completeness check, it will generate the response based on partial input it knows how to handle.

## This pain is well-known to anyone who deals with catalogs.

For example, in demand forecasting or e-commerce recommendations. Often, you would have some complex features based on category type. Say, “laptop” or “mobile phone” is in “electronics.” That is expensive. Let’s make it a feature. “Phone case” is in “accessories.” That is sort of “cheap.” We’ll use that too.

Then, someone reorganizes the catalog. Now, “mobile phone” and “phone case” are both under “mobile.” A whole different category, with a different interpretation. The model will need to learn it all over again or wait until someone explains what happened.

**No magic here.** If catalog updates occur often, you’d better factor it into the model design. Otherwise, educate the business users and keep track of sudden changes.

![]()*Yes, real-world machine learning can be that brittle. (Image credit:* [Pixabay](https://pixabay.com/photos/danbo-domino-macro-2495978/)*)*## **Some more examples:**

* An update in the original business system leads to a change of unit of measurements (think Celsius to Fahrenheit) or dates formats (DD/MM/YY or MM/DD/YY?)
* New product features in the application add the telemetry that the model never trained on.
* There is a new 3rd party data provider or API, or an announced change in the format.

**The irony is, domain experts can perceive the change as operational improvement.** For example, a new sensor allows you to capture high granularity data at a millisecond rate. Much better! But the model is trained on the aggregates and expects to calculate them the usual way.

**Lack of clear data ownership and documentation makes it harder.** There might be no easy way to trace or know whom to inform about an upcoming data update inside an organization. Data quality monitoring becomes the only way to capture the change.

# #3 Data loss at the source

The data not only changes. It can also be lost, due to some failure at the very source.

![]()*Sometimes your pipelines may lead to nowhere. (Image credit:* [*Unsplash*](https://unsplash.com/photos/4XvAZN8_WHo)*).***For example, you lose the application clickstream data due to a bug in logging.** The physical sensor breaks and the temperature is no longer known. External API is not available, and so on. We want to catch these issues early since often they mean the irreversible loss of the future retraining data.

**Such outages may affect only a subset of data.** For instance, users in one geography or a specific operating system. This makes the detection harder. Unless another (properly monitored!) system relies on the same data source, the failure can go unnoticed.

**Even worse, a corrupted source might still provide the data.** For example, a broken temperature sensor will return the last measurement as a constant value. That is hard to spot unless you keep track of “unusual” numbers and patterns.

As with physical failures, we can’t always resolve the issue immediately. But catching it on time helps quickly assess the damage. If needed, we can update, replace, or pause the model.

# #4 Broken upstream models

In more complex setups, you have several models that depend on each other. One model’s output is another model’s input.

This also means: one model’s broken prediction is another model’s corrupted feature.

## **Take a content or product recommendation engine.**

It might first predict the popularity of a given product or item. Then, it makes recommendations to different users, taking into account the estimated popularity.

These would be separate models, basically looped into each other. Once the item is recommended to the user, it is more likely to be clicked on, and thus more likely to be seen as “popular” by the fist model.

## **A more tech-y example: a car route navigation system.**

First, your system constructs possible routes. Then, a model predicts the expected time of arrival for each of them. Next, another model ranks the options and decides on the optimal route. Which, sort of, influences the actual traffic jams. Once cars follow the suggested routes, this creates a new road situation.

![]()Image by Author.Other models in logistics, routing, and delivery often face the same issue.

These linked systems bear an obvious risk: if something is wrong with one of the models, you get an interconnected loop of problems.

# Monitoring data quality and integrity

As we can see, a whole bunch of things can go wrong with the input data for machine learning model.

We want these things never to happen, but let’s be realistic. So, our goal is to catch them on time instead.

![]()*Simple things that break complex systems.* *(Image credit:* [Unsplash](https://unsplash.com/photos/Wpnoqo2plFA)*).***Usually, data reliability and consistency fall under data engineering.** You might even have some checks or monitoring systems at the database level. Is there anything else to keep an eye on?

**The deal is that with machine learning systems, we do not care about overall data quality.** We want to track a particular data subset consumed by a given model. Sometimes exclusively. It does not matter that 99% of data in the warehouse is correct; we want to check our piece.

Feature processing code is also a separate moving piece to monitor. This requires a custom set-up.

So, on the data quality and integrity side, MLOps meets DataOps. We’d better double-check.

There are a few data-related things to look at:

# #1 Model calls

The first question to answer is whether the model even works. For that, look at the number of model responses. It is a basic but useful check to add on top of software monitoring.

Why? The service itself might be operational, but not the model. Or, you might rely on a fallback mechanism, like a business rule, more often than planned.

If your model is used from time to time, this is less useful. But if there is a “normal” usage pattern, it is a great sanity check. For example, your model is deployed on the e-commerce website or fed every day with new sales data. You know then what consumption to expect.

Looking at the number of model calls is an easy way to catch when something is **very** wrong.

![]()*Here, the number of model calls felt to zero overnight. Maybe the service went down?***Depending on the model environment, you might want to check requests and responses separately.** Was the model not asked (e.g., because a recommendation widget crashed) or failed to answer (e.g., the model timed out and we had to use a static recommendation instead)? The answer would point to where you should start debugging.

Now, let’s look at the data.

# #2 Data schema

As we explained above, data schemas might change. Be it due to bad practices or best intentions; we want to detect it.

Our goal is to learn when the features get dropped, added, or changed.

The straightforward way is to perform a feature-by-feature check and investigate:

**1/ If the feature set remains the same.** In the case of tabular data: how many columns are there? Is anything missing, or anything new?

**2/ If the feature data types match.** Did we get categorical values instead of numerical somewhere? For example, we had numerical features ranging from 1 to 10 at a given column. Now when we query it, we see values like “low,” “medium,” and “high.” We should be able to catch this.

![]()*Schema validation error. (Image by Author).*In the end, you want a quick summary view that the incoming dataset is shaped as expected.

# #3 Missing data

We also want to detect any missing data.

**Often, there is some acceptable share of the missing values.** We do not want to react at each empty entry. But we want to compare if the level of missing data stays within the “normal” range, both for the whole dataset and individual features. Are any critical features lost?

**It is important to keep in mind since missing values can come in many flavors.** Sometimes they are empty, and sometimes they are “unknown” or “999”s. If you do a simplistic check for the absent features, you might miss those other ones. It’s best to scan for standard expressions of missing data, such as “N/A,” “NaN,” “undefined,” etc. Having an occasional audit with your own eyes is not a bad idea, either.

**If you have a limited number of features, you might visualize them all in a single plot.** That is how we did it, color-coding the share of missing values:

![]()Image by Author.**You can also set a data validation threshold to define when to pause the model or use a fallback.** For example, if too many features are missing. The definition of “too many,” of course, depends on your use case and model’s cost of error.

**One useful tip is to single out your key driving factors.** You can do that based on model feature importance or SHAPley values. Or, combine either method with your domain knowledge on what matters.

**The idea is to set up different monitoring policies.** You always need your critical features to run the model. With auxiliary ones, the absence is not a show-stopper. You just take a note and later investigate it with the data owner.

# #4 Feature values

Just because the data is there, it does not mean it is correct.

**Examples:**

* After a slip in excel crunching, the “age” column has values ranging from 0,18 to 0,8 instead of 18 to 80.
* A physical sensor breaks and shows some constant value for a week.
* Someone dropped a minus sign during feature calculation, and you see negative sales numbers.

In all the cases, the model works, the data is available — but is corrupted.

To detect this, you want to monitor the feature statistics and distribution.

![]()We compare feature distribution in training and production using Evidently library (image by Author).**1/ Feature value range.** For numerical features, check if the values stay within a reasonable range. For categorical attributes, define a list of possible values and keep an eye for novelties.

**How to do this?**

* You can directly define your expectations (min-max ranges, or possible values at a given column) by looking at the training distribution.
* Or, rely on common sense: we know the possible values for “age” or “outside temperature.”
* If there is more context, you can involve domain experts to define “normal” for the specific input.

It also helps to state when nulls are allowed explicitly.

**2/ The key feature statistics.** For numerical features, you can look at the average, mean, min-max ratio, quantiles.

The latter would help catch the cases like this broken sensor. Formally, it stays within the range, but the measurement is completely static:

![]()Image by Author.**For categorical inputs, you can check their frequencies.** If you work with texts, the equivalent might be % of the vocabulary words, for example.

**The goal is then to monitor the live dataset for compliance** and validate the data at the input. This way, you can catch when there is a range violation, unusual values, or a shift in statistics.

# #5 Feature processing

One more aspect to consider is **where** to run your data validation checks.

**When the data is wrong, the first question is why.** In an ideal world, we want to locate the error as soon as we catch it. Broken joins or feature code can be a reason. In this case, the source data is just fine, but something happens during its transformation into model features.

**Sometimes it makes sense to validate the inputs and outputs separately** for each step in the pipeline. This way, we can locate the problem and debug it faster.

## For example, we predict customer churn for a mobile operator.

Marketing data comes from one source. Purchase logs are joined with ever-changing product plans. Then you merge usage logs with external data on technical connection quality. Feature transformation takes several steps.

![]()Image by Author.Of course, you can simply validate the output of your last calculation. But if you then notice that some features make no sense, you’d have to retrace each step. If pipelines are complex, separate checks might save you some detective work.

# Summing up

Data quality monitoring is the first line of defense for production machine learning systems. By looking at the data, you can catch many issues before they hit the actual model performance.

You can, and should do that for every model. It is a basic health check, similar to latency or memory monitoring. It is essential both for human- and machine-generated inputs. Each has its own types of errors. Data monitoring also helps reveal abandoned or unreliable data sources.

Of course, the data issues do not stop just here. In the next post, we’ll dig deeper into [data and concept drift](https://evidentlyai.com/blog/machine-learning-monitoring-data-and-concept-drift).

*Originally published at* [*https://evidentlyai.com*](https://evidentlyai.com/machine-learning-monitoring-how-to-track-data-quality-and-integrity)*.*

*At Evidently AI, we build open-source tools to analyze and monitor machine learning models. Check out our* [*data drift detection tool*](https://github.com/evidentlyai/evidently) *in Github.*

*Want to stay in the loop?* [*Sign up*](https://evidentlyai.com/sign-up) *for our updates and product news, or join on* [*Twitter*](https://twitter.com/EvidentlyAI) *and* [*Linkedin*](https://www.linkedin.com/company/evidently-ai/) *for more content on production machine learning, or join our* [*Discord community*](https://discord.gg/xZjKRaNp8b) *to chat and connect.*

