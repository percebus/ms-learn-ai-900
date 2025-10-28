# Train a clustering model

Finally, let’s train a clustering model to separate customers into groups based on their spending habits. Specifically, we’ll consider their purchase frequency (how often they make a purchase), and their average spend per purchase.

1. If you’re still viewing the **Test Model** page for the penguin classification model, use the **Train another model** to restart the wizard.
1. On the **Model Type & Data** page, select **Clustering** and upload the **customers.csv** text file to see a preview of the data it contains.
1. On the **Training Settings** page:

- Use _AverageSpend_ and _AverageFrequency_ as the feature columns.
- Set the number of clusters to **Automatic** (so the training process tries to find the optimal number of clusters into which the data should be separated)

1. On the **Training Process** page, review the settings and train the model.
1. On the **Training Results** page, view the metrics and visualizations that were produced from the test data you held back.

> The visualization shows a scatter plot indicating the cluster separation (projected as two dimensions).

6. On the **Test Model** page, use the default test data to generate a prediction.
7. Try generating predictions with the following test cases:

| Case    | AverageSpend | AverageFrequency | Prediction |
| ------- | ------------ | ---------------- | ---------- |
| Default | 88.0         | 48.0             | Cluster 2  |
| Case 1  | 21.0         | 105.0            | Cluster 1  |
| Case 2  | 46.9         | 2.0              | Cluster 3  |
