# Classification

If you want to experiment further with automated machine learning, try training a **classification** model based on the **penguins.csv** file that was included in the **ml-data.zip** archive you downloaded previously. Use all of the columns in this dataset.

After training and deploying a classification model, you can test it in the endpoint with the following JSON:

```json
{
  "input_data": {
    "columns": ["CulmenLength", "CulmenDepth", "FlipperLength", "BodyMass"],
    "index": [0],
    "data": [[45.2, 13.8, 215, 4750]]
  }
}
```
