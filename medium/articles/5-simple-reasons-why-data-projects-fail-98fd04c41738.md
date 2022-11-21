[![Nikita Goldovsky](https://miro.medium.com/fit/c/96/96/0*IjZqiRVBuraokTUE.)](https://nikitagoldovsky.medium.com/?source=post_page-----98fd04c41738--------------------------------)[Nikita Goldovsky](https://nikitagoldovsky.medium.com/?source=post_page-----98fd04c41738--------------------------------)[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Ff6cbb058df9b&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2F5-simple-reasons-why-data-projects-fail-98fd04c41738&user=Nikita+Goldovsky&userId=f6cbb058df9b&source=post_page-f6cbb058df9b----98fd04c41738---------------------follow_byline-----------)Dec 4, 2020

·7 min read[Save](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F98fd04c41738&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2F5-simple-reasons-why-data-projects-fail-98fd04c41738&source=--------------------------bookmark_header-----------)## [Opinion](https://towardsdatascience.com/tagged/opinion)

# **5 Simple Reasons Why Data Projects Fail**

## **Hint: It’s not because your models aren’t accurate enough.**

![]()Photo by [Quino Al](https://unsplash.com/@quinoal?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/fail?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)Have you ever sunk weeks into building a dashboard, ML model, or datamart only to have it collect cobwebs? Or started building something and just kept building and building with no end? Or maybe you delivered insights to your stakeholders that ended up being not very insightful. Unless you’re god’s gift to data, you can probably cringe remembering a project that fell into at least one of these traps. Failing is okay and is a part of life, but hopefully, we also learn from our failures sometimes.

I’ve definitely had my fair share of underwhelming projects and want to share five common pitfalls that lead to failed data projects. It may or may not surprise you that the reasons projects fail are usually not technical ones but rather ones of communication.

To understand why these failures occur it’s important to consider the position that analytics teams find themselves in within the broader organization.

In medium and large corporations, analytics teams often play a centralized support function to multiple stakeholders. This means that they frequently get requests from multiple stakeholders on different parts of the business and are one or more steps removed from the original business context. This can create a challenging environment in which the analyst frequently needs to overcome their knowledge gaps of the business in order to assess a good solution for their colleagues. In addition to the business context gap, there is also a communication gap between the analyst and the business team. Communication gaps occur because the business stakeholder often doesn’t understand or appreciate the technical challenges of what needs to be done to gather, process, and analyze the data, while the analyst doesn’t always have a good enough grasp on the underlying business context to ask their business partner the right questions.

In this environment of fragmented understanding, misalignment and misinterpretation can easily take hold if the analyst isn’t aware of the pitfalls that can occur outside of the technical work.

Let’s take a deeper look at the types of oopsies that you need to avoid.

## **Business stakeholder thinks they need just a quick data point.**

One unfortunate, recurring theme for many analysts is being kept in the dark on business initiatives and only getting very tactical last-minute requests for data. How many times have you received a request like “hey, we’re launching a new sales initiative and need to know our sales rate, but we’re logging sales in some system you never heard of instead of the one that we usually use. Is it possible to get a count of sales by tomorrow?”

Being treated as an after-thought isn’t the fault of the analyst, but many analysts would rather fulfill the hastily-put together request than to push back and request more context. The problem with doing this though is that the need is rarely just a quick data point, is it? The original request is frequently followed-up with additional “quick enhancements” and due to a lack of overall data strategy or plan, whatever gets built in response to these “quick enhancements” is rarely scalable or able to adapt to evolving needs of the business.

I encourage you to always probe the broader needs of quick enhancements. However, I realize it is not always possible to do so. In the event that there isn’t an opportunity to scope out the bigger context, I suggest pipelining these types of requests in your regular keep-the-business-running pipeline and control the deadline of your delivery. Don’t let users blow up your prioritization over artificial deadlines. Often times, the aggressive timelines users give are more based on anxiety or fear rather than on true need. People should expect to wait if they didn’t give sufficient notice.

## **The analyst fails to understand the business context.**

Unlike the example above, sometimes users come to the analytics team searching for a holistic solution. There might be a new product launch and the product manager wants to build a dashboard with a suite of new KPIs or they may be seeing a concerning trend and want a root-cause analysis of what is driving it, and they are looking to you for help and guidance.

One issue that creeps up in these situations is that <quote label="formative">the analyst may fail to properly assess what the business needs. Sometimes users are able to be very prescriptive and communicate what they need effectively but in many cases the business stakeholders may not be able to translate what they are doing into what they want to measure. It is ultimately the responsibility of the analyst to conduct the proper interviews and to think critically about the problem.</quote>

To be able to surprise and delight your stakeholders with highly relevant deliverables, make sure to ask yourself these three questions:

* Do I understand what the business stakeholder is telling they need?
* Do I understand what the business stakeholder is NOT telling me they need but actually need?
* Do I understand who else might need this?

If you are unsure of what the stakeholder is asking for, schedule additional interviews and make sure you get additional context. It’s okay to ask questions and not know simple business procedures. Having an end-result that is what the users want is worth the inconvenience of additional questioning during the build process. If you don’t understand the context enough to have some hypotheses about additional features the user might need, talk with your internal leader and ask for some advice. Your business leader may have a unique perspective having knowledge of both the analytical and business processes. If you’re not sure of who else might benefit from your work, try to get a better picture from your stakeholders about everyone involved/impacted and reach out to them for either a heads-up or additional input on what would make your work have a larger impact.

## **There is no executive sponsor.**

Sometimes analysts have original ideas. Maybe you’re thinking “hey, I really think an enterprise view of these five metrics would be a really cool idea” or “I think an ML model in this onboarding process would do a better job than manual review” and you could be right. But oftentimes, being right isn’t enough. Anyone who failed to get traction for a good idea will tell you that in large companies, innovators must also be effective communicators and influencers. If you like to work on something behind-the-scenes in isolation, you cannot expect everyone to stop on a dime and change how and what they do to accommodate your innovation, even if it’s a good idea.

The best way to get your ideas off the ground is to have someone from the business champion your idea/project. To do this, you need to be inclusive and solicit buy-in from strategic stakeholders who can help spread your ideas to others in the company and make them tangible priorities for others. Get people involved early. Think collaboratively and make people aware of what your intentions are.

## **There are not enough check-ins throughout the project.**

As professionals with personal pride, we sometimes want to work in isolation until the end result is polished and beaming with insight. All we want the end user to have to do is admire the sheer genius of our solution. Unfortunately, this urge for perfection can create the exact opposite effect. Without regular check-ins, projects can start to deviate from what the stakeholder expected or timelines may get pushed out beyond the project’s usefulness.

Allowing users into the building process can sometimes feel a bit uncomfortable as we have to talk about our progress while everything is still raw and undeveloped. It can also slow things down as you have to pivot more often based on feedback that you’re getting. However, this discomfort definitely pays off when the finished product feels like it was made for the end-user and their involvement with the project gives them a sense of ownership that often helps turn them into an evangelist for your work.

I personally like to take the approach of scheduling flights of weekly meetings that last approximately the length of time I think it will take to complete the project. This way I create a sense of accountability in myself to make regular progress but also avoid the awfulness of permanent meetings.

## **There’s no onboarding after the delivery.**

It can be a blurry line as to where your responsibility ends and the stakeholder’s begins. You’ve done what was asked. You executed and made sure your work makes sense. Is it now also your responsibility to make sure the user actually uses what you made? Sadly, many good projects never get proper recognition because of poor follow-through once the technical work is complete.

It is unfortunate because us data professionals will toil for weeks and months to engineer a worthwhile solution but will fail to check-in with the end users to make sure they understand the product you made and know how to use it. Some times a little communication and promotion of your work can mean the difference between a home-run project vs one that ends up collecting cobwebs.

## **Conclusion**

Your models are tight, your engineering is sound and your insight is profound. Hopefully, this list also convinced you why relationships and communication are also crucial for unlocking the full potential of your technical work. Combining technical wizardry and communication prowess, well now you’re just unstoppable.

