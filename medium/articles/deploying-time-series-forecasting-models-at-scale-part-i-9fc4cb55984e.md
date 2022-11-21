[![Isaac Godfried](https://miro.medium.com/fit/c/96/96/0*Sx7X1u5ElAJwgTxr.)](https://igodfried.medium.com/?source=post_page-----9fc4cb55984e--------------------------------)[Isaac Godfried](https://igodfried.medium.com/?source=post_page-----9fc4cb55984e--------------------------------)[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F5bebc59e793b&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fdeploying-time-series-forecasting-models-at-scale-part-i-9fc4cb55984e&user=Isaac+Godfried&userId=5bebc59e793b&source=post_page-5bebc59e793b----9fc4cb55984e---------------------follow_byline-----------)Feb 11, 2021

·6 min read·Member-only

[Save](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F9fc4cb55984e&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fdeploying-time-series-forecasting-models-at-scale-part-i-9fc4cb55984e&source=--------------------------bookmark_header-----------)# Deploying time series forecasting models at scale (Part I)

## How to leverage Flow-Forecast, Docker, Terraform, Airflow, Kubernetes and ONNX to easily scale your deep time series models to production workloads.

![]()[Photo Unsplash](https://unsplash.com/photos/XLFu0PM5Qsg)Deploying machine learning models remains a sticking point for many companies and time series forecasting models are no exception. According to [VentureBeat around 90% of models never make it into production](/why-90-percent-of-all-machine-learning-models-never-make-it-into-production-ce7e250d5a4a). While there might be many reasons for this (e.g. models were exploratory in nature and the end goal was never production, etc) suffice to say that many promising models are shelved at this stage. This is especially true of deep learning models that often have many moving parts.

In this article we will discuss general techniques for taking time series forecasting models to production. We will then more specifically dive into how to get PyTorch models trained using [Flow Forecast](https://github.com/AIStream-Peelout/flow-forecast) ready for deployment. In Part II of this article series we will actually describe deploy example models with FastAPI, Docker, Terraform and Kubernetes. Finally, in Part III we will monitor them and show how to update them periodically as well as scale to increased workloads. Another series will deal with distributed training of deep learning models.

## Considerations

**Prior to training**

As I mentioned in my [previous article](/training-time-series-forecasting-models-in-pytorch-81ef9a66bd3a) before you select a model to train you should weigh your end-goals. Is interpretability important? What inference speed do I need? Do I want a confidence intervals? Or is just a single forecasted value good? These considerations and analysis should inform which model you choose to train initially.

Secondly, in this pre-training planning phase you should also consider how the application will interact with existing software infrastructure and what type of temporal data it will ingest. If for instance, the model needs to make real-time forecasts on a Kafka data stream then how you get it ready for deployment will differ tremendously from if the model just needs to ingest a static CSV file from a GCP bucket. This can also cause things like scalers to break as previously they might have scaled on an entire CSV file with all the most recent data appended whereas now to facilitate fast inference we won’t be able to recompute either the scaler or the CSV file.

Finally, you should consider how long it will take to re-train or continue to train the model. If you are going to periodically get new data and if your models need to be re-trained from scratch each time (for instance due to catastrophic forgetting) it is going to eat up a lot of resources.

**Choosing your overall forecast length**

A big bottleneck remains forecasting long length time series data as the model can only predict values as long as its output forecast length. This means that if you have a model that only forecasts one time step at a time and want to forecast 200 time steps into the future you will need to run 200 forward passes (at least for most models) plus append operations. Whereas if you have model that forecast 10 time steps at once you would only need 20. For this reason when long forecast lengths don’t degrade performance you should use them.

**Is the model with lowest test loss really the best model?**

Oftentimes, the model with the best test loss might perform poorly in a full production setting. This is mainly due to distribution shift in the data and poor selection of evaluation metrics. For this reason you will want to evaluate your model in a rigorous fashion prior to deployment. In order to do this I recommend analyzing both the overall test loss, the test loss on the most recent data, and the interpretability graphs. You can also look at what your model does during extreme situations. Even if the forecasting problem is complex we often a have basic intuition about what should happen or the general direction the prediction should go in. For example if you have a model that forecasts river flow for river that usually only get 2 inches of precipitation per month you could try inputting 20 inches of precipitation in a single hour. Obviously the river flow prediction should then shoot up to epic heights (after whatever the normal time lag is). If it doesn’t then you know something is wrong.

**Double Checking Production Workflows**

In this phase there can often be “unexpected sources” of distribution shift. You should ideally write unit-tests to make sure the model makes the same predictions in production as it does on the test data. I can not overstate this enough CHECK YOUR INPUT DATA. Extremely small differences in pre-processing can often result in big differences in accuracy. Many times people are quick to blame a faulty model, but a lot of time improper data cleaning and changing data format is to blame. You should also communicate with your data engineering/backend teams to see if they anticipate data format changes. Finally, you can write end-to-end tests that make sure the model coupled with pre-processing and post-processing produce sensible results.

**Single model or multiple models**

Another difference that your initial model selection will make is whether you need to deploy single or multiple models. For instance, you might train a separate DNN on each store you want to forecast or you might train one DNN on all stores. In the latter your model will need to have access to the store id (and other information) at inference time as well as the temporal information. In this case you will also need to keep track of model outputs (especially if you are batching multiple store locations together at once). In the former you will need to deploy more models but since they are separate they are at least more parallelizible in terms of inference.

## Getting models ready for deployment with Flow Forecast

Flow Forecast has a number of built tools to help you with the model deployment process. We have an easy to use automated inference API that provides the full functionality of evaluator class. Unless you need to deploy your model in a different language or need very low inference speed then we recommend simply wrapping this class into your Python (web) application or use one of our pre-built Docker containers that creates an automated inference API. However, even if you decide you need to export it you still want to start with the inference API as it makes these next two steps easy.

1. **Robustness testing**

Using the Flow-Forecast Inference API you can easily plot how the model performs on different time periods. Our standard suite of interpretability metrics are already automatically logged to Weights and Biases. To see a compl[ete example of how this works you can look at this notebook.](https://gist.github.com/isaacmg/b95a4a9f0f56a7607fa2e46670371268)

Example of instantiating a model using FF inference mode.**2. Inference speed testing and speed ups**

Another feature we have in Flow Forecast is automatic timing of how long it takes your model to forecast different forecast lengths on various devices and the difference between vanilla models, TorchScript, and ONNX. Additionally we are working on several new enhancements to speed up inference such as generating the confidence interval in large batches and faster logging of plots.

**3. Exporting to TorchScript and ONNX**

As of Flow Forecast 0.95 we have support for TorchScript and we plan on having support for ONNX by 0.96. However there are several drawbacks to using these methods including the loss of confidence intervals. To put the model into TorchScript/ONNX it requires calling `model.eval()` which means all predictions will be the same hence no confidence interval. That said if you want to convert the model to TorchScript (assuming you had already followed the steps in the gist above) you would do essentially this:


```
from flood\_forecast.deployment.inference import convert\_to\_torch\_script convert\_to\_torch\_script(d, "torch\_script\_save\_path.pt")
```
See [this link for more](https://github.com/AIStream-Peelout/flow-forecast/blob/a750601743695d8cc7bef00dd964f32a070b49c1/flood_forecast/deployment/inference.py#L118) information.

**4. Current data ingestion and future versions**

At the moment InferenceMode only supports loading inference data from a CSV. However we are hoping to change that in the near future and allow data loading from many different data sources. Specifically we are prioritizing loading data directly from SQL tables, Parquet files, and HDFS. Later on in our roadmap we plan to allow streaming data sources like Kafka subscriptions, Redis, or Pub/Sub.

In this article we covered some of the preparatory steps to deploying your model. Once you have done these things you can start to focus on the actual deployment phase. In the second article we will examine how to perform the actual deployment by using the Flow Forecast Inference Docker container, our Terraform templates, and Google Cloud Platform. This article will be more hand and contain more code samples. Feel free to leave questions if you have any.

