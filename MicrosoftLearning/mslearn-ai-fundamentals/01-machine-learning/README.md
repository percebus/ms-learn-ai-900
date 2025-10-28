# Explore Automated Machine Learning

In this exercise, you’ll use the automated machine learning to train and evaluate a machine learning model. You’ll then deploy and test the trained model.

<!-- prettier-ignore-start -->
> [!NOTE]
> This exercise is designed to take you through the steps to train and test a model using **Azure Machine Learning**. If you have an Azure subscription with sufficient permissions, you can provision an Azure Machine Learning workspace and use that for the exercise. However, Azure Machine Learning is designed for enterprise-scale machine learning solutions that involve huge volumes of data and cloud-based compute. Some operations in Azure Machine Learning require provisioning compute, which can take considerable time. If you don’t have access to Azure, or if you have limited time to complete the exercise, a browser-based **ML Lab** app that includes the core functionality of Azure ML used in this exercise is also provided, and you can use that to train and test real machine learning models, just as you would in Azure ML. While the user interface in ML Lab is not identical to Azure Machine Learning, it’s similar enough to make the transition to Azure Machine Learning intuitive. Note that the ML Lab app runs in the browser, so refreshing the page at any point will restart the app!
<!-- prettier-ignore-end -->

This exercise should take approximately **35** minutes to complete (less if you use the browser-based ML Lab app).

## Create a workspace

A workspace is used to keep all your machine learning resources together, making it easier to manage data, code, models, and other assets in a single place.

1. Open the portal for the environment you want to use in this lab, and sign in if prompted:

- Azure-based Azure Machine Learning Studio at https://ml.azure.com
- Browser-based ML Lab at https://aka.ms/ml-lab

<!-- prettier-ignore-start -->
> [!TIP]
> If Azure Machine Learning studio opens in an existing workspace, navigate to the **All workspaces** page.
<!-- prettier-ignore-end -->

1. Create a new workspace with a suitable name.

> If you are using Azure Machine Learning, you do not require a Hub for this exercise. Choose appropriate advanced settings based on any policy constraints in your Azure subscription.

3. After the workspace has been created, select it to view its **Home** page.

> Note that the workspace has multiple pages, which are displayed in the navigation pane on the left. You can expand and collapse this pane by using the **☰** menu at the top.

## Download data

In this exercise, you’ll use a dataset of ice cream sales to train a model that predicts the demand for ice creams on a given day, based on seasonal and meteorological features.

1. In a new browser tab, download [ml-data.zip](https://aka.ms/mslearn-ml-data) from [`https://aka.ms/mslearn-ml-data`](https://aka.ms/mslearn-ml-data) to your local computer.
1. Extract the downloaded **ml-data.zip** archive to see the files it contains. Note that one of these files is **ice-cream.csv**, which contains the ice cream sales data required for this exercise.

## Train Models

1. [Use automated machine learning to train a model](./regression/ice-cream)
2. If time permits: [Train a classification model](./classification/penguins)

### Clean-up

If you used Azure Machine Learning to complete this exercise you should delete the resources you created to avoid accruing unnecessary Azure usage.

1. In [Azure Machine Learning studio](https://ml.azure.com/), on the **Endpoints** tab, select the endpoint you deployed. Then select **Delete** and confirm that you want to delete the endpoint.

> Deleting your compute ensures your subscription won’t be charged for compute resources. You will however be charged a small amount for data storage as long as the Azure Machine Learning workspace exists in your subscription. If you have finished exploring Azure Machine Learning, you can delete the Azure Machine Learning workspace and associated resources.

To delete your workspace:

1. In the [Azure portal](https://portal.azure.com/), in the **Resource groups** page, open the resource group you specified when creating your Azure Machine Learning workspace.
1. Click **Delete resource group**, type the resource group name to confirm you want to delete it, and select **Delete**.
