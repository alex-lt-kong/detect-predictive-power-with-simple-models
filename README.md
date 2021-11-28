# Detecting causality with simple models

This project tries to understand one question: say feature set **X** does have very good predictive power but the cause and effect relationship is highly non-linear, is it possible to use a very simple model to discover it without relying on domain knowledge? 

If the answer to this question is yes, then it implies that, while having a fantastic (i.e., very accurate) model is hard, it is comparatively easy to decide whether or not some features have predictive power (since very simple models can detect its existence).

The significance behind this question is that, usually artificial intelligence performs pretty well in some areas traditional programs fail to work, such as facial recognition or natural language processing. While these achievements are definitely amazing, they are all the same in one aspect--we already know there exists strong causality--since we human beings can usually do it with ease. However, sometimes we try to predict **y** without knowing if **X** at hand has any predictive power at all. In this case, suppose our models are totally useless (i.e., doing not better than random guess), will simply digging deeper (e.g., adding more leaves or more layers of neurons) work? Or does it mean that it is most likely the dataset we have just does not have the predictive power so digging deeper usually produces nothing at best and a high level of overfitting at worst?

To answer this question, the approach taken in this project is:
1. We start with a flexible model that demonstrates the existence of a highly non-linear causality (or correlation) between **X** and **y**, as evidenced by a high accuracy (to make our life easier, we try to use cases in which the definition of accuracy is usually undebated);
1. We try simpler models and see if these models can also uncover the highly non-linear relationship, albeit with a lower accuracy;
1. If simpler models are **able** to uncover the highly non-linear relationship all or most of the time:
    1. it adds more weight to the idea that *while having a fantastic (i.e., very accurate) model is hard, it is comparatively easy to decide whether or not some features have predictive power (since very simple models can detect its existence)*;
    1. more importantly, it implies that suppose none of the models trained by a given dataset works, it is more likely that **X** is not predictive at all (since if it is predictive, even a simple model should do a bit better than random guess) and parameters tuning might not increase our chance whatsoever;