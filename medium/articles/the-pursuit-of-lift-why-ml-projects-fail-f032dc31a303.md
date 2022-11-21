[![Ian Xiao](https://miro.medium.com/fit/c/96/96/1*YiMe8m9a8bmqOUzprwkalg.png)](https://medium.com/@ianxiao?source=post_page-----f032dc31a303--------------------------------)[Ian Xiao](https://medium.com/@ianxiao?source=post_page-----f032dc31a303--------------------------------)[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fa0eb4622a0ca&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fthe-pursuit-of-lift-why-ml-projects-fail-f032dc31a303&user=Ian+Xiao&userId=a0eb4622a0ca&source=post_page-a0eb4622a0ca----f032dc31a303---------------------follow_byline-----------)Dec 28, 2020

https://www.linkedin.com/in/ianxiao/

·5 min read·Member-only

[Save](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Ff032dc31a303&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fthe-pursuit-of-lift-why-ml-projects-fail-f032dc31a303&source=--------------------------bookmark_header-----------)# The Pursuit of Lift

## A tool to spot why many ML projects fail

![]()Photo by [SpaceX](https://unsplash.com/@spacex?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/rocket?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)**TL; DR** — Data Scientists pursue lift (incremental performance improvement) with blood, toil, tears, and sweat. However, theoretical lift often does not translate into reality. This article explores the issues and proposes a S.P.O.T. Framework and assessment tool. It helps executives and Data Science managers diagnose, set the right goals, and plot a clear course of action.

## Sound Familiar?

“With our new targeting model, we can achieve **up to 2.3% incremental lift** in identifying which customers are likely to leave us in the next 3 months — this means we can save millions of dollars in revenue if we deploy this model.” a Data Scientist says with pride and honour (and caveat).

An executive shrugs and says: “Great. But, I am **not sure what we can do about them**.”

[GIPHY](https://media.giphy.com/media/14dXclYKbx2ONW/giphy.gif)Similar dialogues keep happening between data scientists and business executives. In 2019, only [**10–40% of the ML models get deployed into production**](/the-last-defense-against-another-ai-winter-c589b48c561). This means many ML models only worked in our computers and imagination but never had any tangible impact on the real world.

<quote label="metrics">
In other words, there is a big gap in **realizing theoretical performance lift [on a metric] into reality (e.g., real money in the bank)**.
</quote>

There are many reasons. To find the right solutions, we must spot what exactly is going wrong.

## **The S.P.O.T. Framework**

From [working with companies and teams](https://www.linkedin.com/in/ianxiao/) of various sizes and industries to operationalize ML, issues converging to four (4) key areas. **The S.P.O.T. Framework** helps teams spot (pun intended) the gaps in each of the four areas.

**1 — Strategy (S).** **Do we have a clear strategy that Data Science (and other) teams can understand?** “Strategy” is a big and fluffy word. In essence, a good strategy succinctly captures the “how” of our company needs to stay alive (e.g., keep making a profit in a competitive market); it is something everyone from top to mid-management can articulate and describe how their team can contribute to it with simple words.

With a good strategy, data scientists can define the right “target” (e.g., a churning customer means people who cancel their subscriptions, instead of decreased usage by a certain percentage) for their ML solutions. Most importantly, Data Science teams can understand what the minimum lift of their solution needs to be.

**2 — Product (P).** **Do we have enough economically viable product offering?** Once the ML solution identifies an opportunity, we need to do something to intervene — and ultimately, change the outcome. Depending on the actual use case, “product offering” has different meanings and forms.

In a Marketing context, an offer can range from simple email reminders, discount coupons on a new product or service to human intervention via service calls. In an Operation and Risk Management context, an offer (also known as “treatment”) can be an action, such as a staff opening an intake to investigate a fraudulent transaction or the system applies automatic correction rules.

However, one of the most prominent challenges is to *have enough economically viable offers* to select from. Every offer has a cost. <quote label="tradeoff">We need to decide if it is cheaper to do nothing, do something, or let the customer leave.</quote>

**3 — Operation(O). Do we have the right capability to execute offers?** This is [the Last Mile Problem of ML](/fixing-the-last-mile-problems-of-deploying-ai-systems-in-the-real-world-4f1aab0ea10): once we identify the opportunity and find the right product offering, teams of specialists or frontlines have to prepare and deliver the offer. They must do it well to achieve the intended outcome — this is when the theoretical lift turns into actual monetary results.

For example, in a cross- or up-selling setting, a marketing specialist designs and adds offers and their specifications (e.g., how much discount, who is eligible, what product it applies to) to a system; then, a sales staff needs to present the offer to a customer who’s likely to purchase verbally in person, via the phone, or other digital means. How the staff nurtures conversation and presents the offer greatly impacts the ***actual lift*** the Data Science teams theorize.

**4 — Technology (T). Do we have the right technology to execute the offers? “**Technology” is another big word since it is so ubiquitous and can manifest in many forms. Generally, technology plays two key roles: a) enable and b) automate.

For example, to develop and run an ML model, we need [a database and ML toolkit](/the-most-useful-ml-tools-2020-e41b54061c58?source=your_stories_page-------------------------------------); to create and manage marketing offers, we need a content platform; to deliver offers, we need integration between the content platform and channel technologies (e.g., the tool sales staff use in-store, call centers, web-based chat windows).

In terms of scaling (minimize incremental cost as the volume of customers or transactions increases), we need technology to automate many repetitive tasks instead of having someone do it manually — wage is often more expensive than software licenses and electricity.

## The S.P.O.T. Assessment Tool and Beyond

The S.P.O.T. Assessment Tool comprises a total of 12–15 questions and creates a holistic view of strengths and weaknesses.

![]()Illustrative Example of the S.P.O.T. Assessment ToolRealizing the expected lift requires a team effort from top management to business partners — Data Science teams cannot (and should not) solve it alone. The S.P.O.T. Assessment Tool opens a forum among Data Science teams and their business partners. Collectively, teams can follow the process to **develop a common(and honest) view** of where we are now, where we want to be in the near future, and how to get there.

## Give it a try?

You can [**download the S.P.O.T. Assessment worksheet**](https://docs.google.com/document/d/155B92oneAsREmteqc1h_duwf0Cm9vanVZUjGfsNAXm8/edit?usp=sharing) (a Google doc, no sign-up required) and share it with your team.

![]()S.P.O.T. Assessment Worksheet (v1.0) — PDFIn addition, you can also [**sign up for a web-based version**](https://forms.gle/GZssDtoqo43umCJKA)**.** Itautomates the assessment process and provides a high-level KPI dashboard and benchmark data. The web-based tool will be in public beta around Q1 2021.

## Want to contribute?

If you are open to participating in a pro-bono research project, **connect with me on** [**LinkedIn**](https://www.linkedin.com/in/ianxiao/)**.** You can share your results, provide feedback, and get benchmark data and summarizes of what others are doing.

**Like What You Read?** Follow me on [Medium](https://medium.com/@ianxiao), [LinkedIn](https://www.linkedin.com/in/ianxiao/), or [Twitter](https://twitter.com/ian_xxiao). Also, do you want to learn business thinking and communication skills as a Data Scientist? Check out my “[Influence with Machine Learning](https://www.bizanalyticsbootcamp.com/influence-with-ml-digital)” guide.

Here are some other articles you may like:

[## The Most Useful ML Tools 2020

### 5 sets of tools every lazy full-stack data scientist should use

towardsdatascience.com](/the-most-useful-ml-tools-2020-e41b54061c58)[## Another AI Winter?

### How to deploy more ML solutions — five tactics

towardsdatascience.com](/the-last-defense-against-another-ai-winter-c589b48c561)[## Should We Stay in Data Science?

### 4 Realistic Career Options for Data Scientists

towardsdatascience.com](/the-most-realistic-data-science-career-guide-d12c4af87cc8)[## Data Science is Boring

### How I cope with the boring days of deploying Machine Learning

towardsdatascience.com](/data-science-is-boring-1d43473e353e)[## 12-Hour ML Challenge

### How to build & deploy an ML app with Streamlit and DevOps tools

towardsdatascience.com](/build-full-stack-ml-12-hours-50c310fedd51)[## The Last-Mile Problems of AI

### Three Types of Problems and Five Tactical Solutions

towardsdatascience.com](/fixing-the-last-mile-problems-of-deploying-ai-systems-in-the-real-world-4f1aab0ea10)