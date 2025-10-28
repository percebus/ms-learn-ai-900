# Segment customers based on spending patterns

Suppose a retail business wants to group customers into segments for marketing, based on spending patterns.

1. In a web browser, open the [Customer Segmentation](https://aka.ms/customer-segmentation) app at [`https://aka.ms/customer-segmentation`](https://aka.ms/customer-segmentation).
1. Select **Upload Data** and open the **customers.csv** data file. This file contains records for customers, including their average frequency of purchases (in days) and their average spend per transaction.
1. With the file loaded, select **Analyze**. The app uses an algorithm called **K-means** to segment the customers into clusters.

> The algorithm tries to separate the data into K clusters based on the mean distance between the data points and the cluster centers. In this case, the app tries K values of 3 to 5 before selecting the one that results in the best separation of the data.

4. When the analysis is complete:

- Review the updated data, noting that each customer has been assigned to a cluster.
- Review the silhouette scores, which measure how well the clusters are separated for each K value that was tried (the score is a value between -1 and 1 - the closer to 1 the score is, the better the separation).
- Review the cluster metrics, which include the average spend and purchase frequency for customers in each cluster.
- Review the scatter plot, which shows a visualization of the clustered data.

Each cluster represents a group of customers with similar spending habits.

<!-- prettier-ignore-start -->
> [!NOTE]
> The applications used in this exercise use machine learning models that are simple, and based on a small set of data features. In a real scenario, data scientists can use a range of machine learning frameworks with platforms like Azure Machine Learning to develop, deploy, and manage machine learning models.
<!-- prettier-ignore-end -->
