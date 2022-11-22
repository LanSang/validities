[![Fabrizio Fantini](https://miro.medium.com/fit/c/96/96/2*p2WlLG87xHGkn6IPKyUbyA.png)](https://fab-evo.medium.com/?source=post_page-----7e8c84305aa8--------------------------------)[Fabrizio Fantini](https://fab-evo.medium.com/?source=post_page-----7e8c84305aa8--------------------------------)[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F5d3a51c839e2&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fhow-not-to-fail-at-your-data-science-project-7e8c84305aa8&user=Fabrizio+Fantini&userId=5d3a51c839e2&source=post_page-5d3a51c839e2----7e8c84305aa8---------------------follow_byline-----------)May 25, 2021

·8 min read·Member-only

<person role="CEO">
https://www.linkedin.com/in/fabrizio-fantini/?originalSubdomain=uk
</person>

[Save](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F7e8c84305aa8&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fhow-not-to-fail-at-your-data-science-project-7e8c84305aa8&source=--------------------------bookmark_header-----------)## [Notes from Industry](https://towardsdatascience.com/tagged/notes-from-industry), [BUSINESS SCIENCE](https://medium.com/tag/business-science)

# How (Not) to Fail At Your Data Science Project

## The 4 design choices that can undermine ROI and impact

![]()Photo by [Jo Szczepanska](https://unsplash.com/@joszczepanska?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)Over a year since the start of the Covid-19 pandemic, data scientists are still struggling to get their models back into shape. Every week or so, I see [another article](https://venturebeat.com/2021/05/01/data-science-in-a-post-covid-world/) lamenting how the disruptions of the past year have negatively impacted machine learning models. Many organisations have stopped trying to adapt and are simply hoping to wait it out until we ‘get back to normal’.


> They are going to be in for a shock when they finally realise that there’s no such thing as normal.
> 
> 

All of us working in data science need to recognise the failures that have [caused these models to crash](https://www.technologyreview.com/2020/05/11/1001563/covid-pandemic-broken-ai-machine-learning-amazon-retail-fraud-humans-in-the-loop/) and approach our algorithmic design in new ways. We don’t have to [keep making the same mistakes](/data-science-lessons-were-not-learning-fast-enough-83ead4827735).

These 4 common project design choices in data science set you up perfectly for failure. Here’s your roadmap to model drift, minimal impact, and low ROI (or, even better, 4 things to avoid to set you up for success).

# 1. Isolating your project

Think back to your last few data science projects. Hopefully, they were not too identical, so you could challenge yourself and keep it interesting. But even if they were vastly diverse projects with opposing goals, the code and machine learning basics remained quite similar. The reality is that [data scientists have a particular toolbox](https://hbr.org/2018/08/what-data-scientists-really-do-according-to-35-data-scientists) and often repeat methodology to achieve varied goals.

Despite that, **data scientists tend to create project islands isolated from other data scientists and other projects**. We end up wasting a lot of time repeating ourselves and doing similar analyses. This is even true on teams at the same company!

## The **whole world of data is an integrated global system**; breaking those links only limits your returns.

All data, insights and intermediate results should be shared across the analysis to maximise their impact. Since most of your projects deal with similar operations, isolation just wastes time.

*When you’re on a* ***project island****, you tend to miss critical areas for gains*. You see all the water but ignore what is underneath. Isolating your project from other data science projects sets you up for failure because you must relearn all the lessons of the past and recreate all the best code from scratch. **Siloed data, approaches and code open you up to mistakes**. Instead of recreating code, dedicate the time and effort to designing your analysis. You will get much better outcomes.

![]()**Data desert island.** Image credits: Randall Munroe,[xkcd](https://xkcd.com/731/).# 2. Starting from the tool, not the goal

As a data science nerd, I get just as excited as anyone to use new tools and types of analysis to improve my results. **It’s hard to resist the pull of a brand new strategy, especially since recent advances in data science generally offer plenty of growth opportunities**.

It’s a widespread problem. In a recent issue of the [MIT Sloan Management Review](https://sloanreview.mit.edu/article/why-so-many-data-science-projects-fail-to-deliver/?og=Leadership+Infinite), they discuss the case of a skilled data scientist hired to improve a major Indian finance company’s investments targeting algorithm. He became fascinated by the k-nearest neighbours algorithm and dedicated a lot of time and effort to applying it to his analysis.

**The gains were minimal.** In fact, the algorithm’s recommendations were *no better than the advice that any professional could give by looking at the data without any formal statistical analysis:* ***all that effort developing the tool, and nothing.***

![]()***K-nearest neighbours* *algorithm.*** *Image credits:* E. M. Mirkes,[*Wikimedia*](https://commons.wikimedia.org/wiki/File:Map1NNReducedDataSet.png)*.*Why? If you know anything about the [k-nearest neighbours algorithm](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm#:~:text=In%20statistics%2C%20the%20k%2Dnearest,training%20examples%20in%20data%20set.), it seems like something that would have a lot of potential. You can quickly cluster data to find patterns and similarities in seeming noise using robust clustering. **It should work, right?**

The problem goes back to the very beginning. The goal was to see what could be done with a particular algorithm, not to improve KPIs. The exact project design was flawed. <quote label="metrics">In effective data science projects (what I like to call [business science](/data-science-is-dead-long-live-business-science-a3059fe84e6c)), **there has to be a precise goal to get desirable outcomes to that end.**</quote>

Too often, data scientists set up projects with the mindset of “let’s apply this method and see what we find”. Sometimes that delivers impressive results, but usually, it underperforms.

<quote label="metrics">
Successful data science projects instead answer a single question: How can I improve this KPI?
</quote>
> 
> 

Experimenting may have its place, especially in universities, but once you are trying to deliver predictable growth and maximize results, the approach must be different. Starting from the tool, not the goal, will always fail to maximise ROI. The best practice is to **start from a business need and find the best statistical method to achieve your goal** — even if it isn’t flashy or currently trending in the data science world.


> If you focus on the methodology or the tool without drilling down to the *why*, you set yourself up for failure.
> 
> 

# 3. Prioritising the wrong KPI

<quote label="metrics">
Of course, even when you put the goal first, **you only get optimal results when that goal is the *right goal*.**

The impact of your efforts depends mainly on the KPI you choose to prioritise. In retail, for example, we often see people default to increasing demand forecast accuracy at the expense of more valuable insights. If you spend weeks developing the perfect tool to improve forecast accuracy by 2 points, that may not have much of an impact if data scientists ignore glaring issues in the supply chain or pricing. The gains from optimising those KPIs would be much more significant.

[*KPI prioritisation*](https://www.sciencedirect.com/science/article/pii/S221282711830252X) *is critical — and challenging*.</quote> There isn’t a hard and fast rule that tells you what your goal should be, but two simple guidelines can make the decision process more manageable:

**1.** **Your KPI should have a significant impact on the bottom line.**

**2.** **Your KPI should have the potential to grow.**

The first rule is simple enough. **Your goal should deliver tangible returns**. For example, a grocery chain will get minimal benefit from an algorithm that can only optimise milk prices. It will get a much greater benefit from an algorithm that can maximise overall revenues. It’s usually a bit more complex, but the principle remains.

**An easy test? Add “and so…” to your chosen KPI**: i.e. We are optimising additional margin growth, *and so* that will allow us to increase bottom-line revenues significantly in a short time. This exercise takes you out of the technical mindset that often causes this design flaw. *You can deliver business-digestible outputs that have a greater impact.*

![]()**Knowing the right KPI isn’t always easy.** Image credits: [Evo Pricing](https://evopricing.com/) (CC with attribution)The second guideline is harder to fulfil. Sometimes the potential for improvement of a particular KPI is hard to assess on its face. However, you can usually find out where the greatest potential lies by **identifying the crucial pain point, drain on resources or area of waste**. Eliminating that goes a long way.

<quote label="formative">
Your target outcome ultimately makes or breaks your data science project. So choose carefully.
</quote>
> 
> 

# 4. Selecting the wrong depth of analytics

A final fatal flaw in designing your data science project? **Choosing the wrong level of analytics**.

There are four basic levels of analytics that we can leverage as data scientists: *descriptive, diagnostic, predictive, and prescriptive*. All have their purposes, but for most large-scale data science projects, **only prescriptive analytics will have the greatest impact**.

![]()**Value vs difficulty of analytics.** Image credits: [Evo Pricing](https://evopricing.com/) (CC with attribution)*Only prescriptive analytics can drive, not analyse or anticipate outcomes*. It provides the best foresight and is best designed to optimise whatever KPI you chose. The flexibility made possible through prescriptive analytics allows you to **achieve your goals regardless of disruptions or obstacles** in your way.

It’s easy to default to predictive analytics when setting up a new project. After all, prediction is what most non-data scientists request to learn from their data. Plus, a prescriptive approach is harder! But as experts, we should know better. [Optimisation is almost always our real purpose](/to-forecast-or-not-to-forecast-that-is-the-supply-chain-question-439e0eb47b61). That requires us to step up and **embrace the more difficult but more rewarding path to success**.

Over the past year, the disruption causing AI models to collapse in the face of the Covid-19 crisis was [widespread](https://www.mckinsey.com/business-functions/mckinsey-analytics/our-insights/global-survey-the-state-of-ai-in-2020) — but not in [prescriptive models](https://www.bcg.com/publications/2020/business-applications-artificial-intelligence-post-covid). They were [more agile](/agile-is-the-watchword-8b500d8cd0db) in dealing with changes in patterns and could adjust.


> If you want to avoid this kind of failure in your own projects, carefully consider a prescriptive approach.
> 
> 

To be clear, there is still merit in descriptive, diagnostic and predictive analytics. But they will never maximise the value of your data. Unless your project scope is limited to hindsight, intended only to capture a snapshot in time or otherwise limited in scale, you will have more success with prescriptive analytics. **Project difficulty will increase, but so will impact**.

# To success in data science!

![]()Photo by [Guille Álvarez](https://unsplash.com/@guillealvarez?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)It may seem overly simple, but simply **eliminating these mistakes from your project design will increase your success rate in data science significantly**. That’s something our field needs desperately. According to a [Gartner study in 2017](https://www.techrepublic.com/article/85-of-big-data-projects-fail-but-your-developers-can-help-yours-succeed/), **85% of all data science projects fail**. I would like to think that that number has improved over the past 5 years, thanks in part to massive advancements in AI and machine learning, but there’s [little evidence of change](https://venturebeat.com/2019/07/19/why-do-87-of-data-science-projects-never-make-it-into-production/).

With all we know, why?


> It comes down to flaws built in at the very core of how we design these projects.
> 
> 

Ultimately, **it’s not the technology that’s flawed; it’s the implementation — and us**. Luckily, that means that we are empowered to do something about it. With an integrated, prescriptive approach and the right goal guiding your design, it will be much harder to set up a failing data science initiative.

I cannot promise that these four considerations will eliminate all failures from your future, but they will avoid the most persistent flaws. It’s a leap in the right direction.

PS more [Business Science](https://medium.com/tag/business-science) from my writing:

[## Data Science Lessons We’re Not Learning Fast Enough

### Mistakes made by new data scientists are disappointingly similar to those still made by professionals.

towardsdatascience.com](/data-science-lessons-were-not-learning-fast-enough-83ead4827735)[## To Forecast, or Not To Forecast, That is the Supply Chain Question

### The 5 secret ingredients to solve for profit, rather than accuracy

towardsdatascience.com](/to-forecast-or-not-to-forecast-that-is-the-supply-chain-question-439e0eb47b61)
```
Monthly Business Science in your inbox, new software, and University-level learning:[**Free access**](https://evouser.com/register)Questions? Please reach out on [Linkedin](https://www.linkedin.com/in/fabrizio-fantini/)
```
