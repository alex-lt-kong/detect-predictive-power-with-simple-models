# Detecting predictive power with simple models

**Note**: some readers argue that machine learning is never about causality and it is only about correlation--well I revised the name of the repo to reflect this and all the references are changed from causality to predictive power.

This project tries to understand one question: say feature set **X** *have* some predictive power for **y** but the correlation between **X** and **y** is highly non-linear, can we always detect the existence of such predictive power by only using a "simple" model?

If the answer to this question is yes, then it implies that, while having a fantastic (i.e., very accurate) model is hard, it is comparatively easy to decide whether or not **X** has some predictive power (but sure we won't be sure about the degree of predicitve power **X** has before deploying a much more flexible model or relying on domain knowledge).

The significance behind this question is that, usually artificial intelligence performs pretty well in some areas traditional programs fail to work, such as facial recognition or natural language processing. While these achievements are definitely amazing, the tasks involved are all the same in one aspect--we already know there exists strong causality/correlation--since we human beings can usually do them with ease. However, sometimes we try to predict **y** without knowing if **X** at hand has any predictive power at all. In this case, suppose our models are totally useless (i.e., not doing better than random guess), will simply digging deeper (e.g., adding more leaves to a tree-based model or more layers of neurons to a neural network) work? Or does it mean that it is most likely the dataset we have just does not possess the predictive power so digging deeper usually produces nothing at best and a high level of overfitting at worst?

To answer this question, the approach taken in this project is:
1. We start with a flexible model that demonstrates the existence of a highly non-linear correlation/causality between **X** and **y**, as evidenced by a high accuracy (to make our life easier, we try to use cases in which the definition of accuracy is usually undebated);
1. We try simpler models and see if these models can also uncover the highly non-linear relationship, albeit with a lower accuracy;
1. If simpler models are **able** to uncover the highly non-linear relationship all or most of the time:
    1. it adds more weight to the idea that *while having a fantastic (i.e., very accurate) model is hard, it is comparatively easy to decide whether or not some features have predictive power (since very simple models can detect its existence)*;
    1. more importantly, it implies that suppose none of the naive models (i.e., models without much tweaking) trained by a given dataset works, it is more likely that **X** is not predictive at all (since if it is predictive, even a simple model should do a bit better than random guess) and parameters tuning might not increase our chance whatsoever;
 
**See also**

* A [question](https://stats.stackexchange.com/questions/553995/datasets-that-simple-models-fail-but-more-complex-models-work) I asked on the Cross Validated community of StackExchange;

* A relevant [question](https://stats.stackexchange.com/questions/222179/how-to-know-that-your-machine-learning-problem-is-hopeless) asked on the same forum.