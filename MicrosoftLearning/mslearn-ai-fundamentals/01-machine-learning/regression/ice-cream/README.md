# Use automated machine learning to train a model

Automated machine learning enables you to try multiple algorithms and parameters to train multiple models, and identify the best one for your data.

1. In the portal, view the **Automated ML** page (under **Authoring**).
1. Create a new Automated ML job with the following settings, using **Next** as required to progress through the user interface:

> [!TIP] > **Tip**: If no explicit information for a setting is provided in the steps below, use the default value.

**Basic settings**:

- Assign a unique job name for your automated machine learning job

**Task type & data**:

- Set the task type to **Regression**.
- Create a new **tabular** data asset named **ice-cream**
  - Upload the local **ice-cream.csv** file to the default workspace storage.
  - Include _only_ the following columns (Date is unique for each row, and adds predictive capability on its own):
    - **DayOfWeek**
    - **Month**
    - **Temperature**
    - **Rainfall**
    - **IceCreamsSold**
  - Create the data asset.
- Ensure your newly created ice-cream data asset is selected before moving to the next step

> [!NOTE] > **Note**: If you are using an Azure subscription for which you are not an administrator, key-based access to storage may have been disallowed by policy. In this case, you’ll need to work with your administrator to allow key-based access or reconfigure your Azure Machine Learning workspace to use Entra ID authentication to access storage. If you can’t do this, use the browser-based ML Lab app for this exercise.

**Task settings:**

- Set the **target column** (the label we want the model to predict) to **IceCreamsSold**.
- Set **Additional configuration settings**:
  - Set the **Primary metric** to the metric you want to use to evaluate model performance. In this exercise, use the R2 score.
  - Select the model algorithms you want to try (or leave them all selected)
- Set **Featurization settings**:
  - Use these settings to customize featurization (how the data features are prepared for model training)
- Set **Limits**:
  - Use the limits to end the training job early based on specific criteria. In this exercise, set the following limits:
    - **Metric score threshold**: 0.9
    - **Experiment timeout (minutes)**: 15

> [!NOTE] > **Note** It’s important to set these limits when using Azure Machine Learning, as running training jobs for every possible algorithm and featurization combination could potentially take hours!

**Compute:**

- Use Serverless compute

**Review**

- Review the settings and check them carefully. Then submit the training job. It starts automatically.

3. Wait for the job to finish.

> [!TIP] > **Tip**: If you’re using Azure Machine Learning, it might take a while — now might be a good time for a coffee break!

## Review the best model

When the automated machine learning job has completed, you can review the best model it trained.

1. On the **Overview** tab of the job details page, view the information about the job and note the best model summary.
1. Select the **Algorithm name** for the best model to view its details. Then on the child job details page, view the following tabs:

- **Overview**: General details for the child job.
- **Model**: Information about the model that was trained.
- **Metrics**: Evaluation metrics and visualizations for the model based on the test data used during the training process.
- **Outputs and logs**: Information logged during the training process.

## Deploy and test the model

1. On the **Model** tab for the best model trained by your automated machine learning job, select Deploy to deploy the model to a Real-time endpoint.

> Select appropriate Instances and Virtual machine options for the compute on which the deployed endpoint will run (which may depend on the quota available in your Azure subscription), and assign suitable endpoint and deployment names.

2. Wait for a notification that the deployment is complete.

> [!TIP] > **Tip:** In Azure Machine Learning studio, endpoint deployment may take 5-10 minutes.

## Test the deployed service

Now you can test your deployed service.

1. In the navigation menu, select the **Endpoints** page and open the real-time endpoint you created.
1. On the endpoint page view the **Test** tab.
1. In the **Input data to test endpoint** pane, replace the template JSON with the following input data:

```json
{
  "input_data": {
    "columns": ["DayOfWeek", "Month", "Temperature", "Rainfall"],
    "index": [0],
    "data": [["Wednesday", "June", 70.5, 0.05]]
  }
}
```

4. Click the **Test** button.
5. Review the test results, which include a predicted number of rentals based on the input features - similar to this:

```json
[120.16208168753236]
```

The test pane took the input data and used the model you trained to return the predicted number of rentals.

## View code to consume the model

Now that you have a predictive model, developers can build applications that consume it.

1. On the real-time endpoint page view the **Consume** tab.
1. Review the sample code to consume your model.
