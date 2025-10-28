# Generate predictions for wheat seed species

Let’s explore another example of how machine learning can help determine unknown information based on past observations.

Suppose an agricultural specialist needs to identify the type of wheat that will be grown from a seed. Machine learning can be used to determine the most probable wheat species based on seed measurements.

## Predict wheat types based on seed measurements

1. In a web browser, open the [Wheat Seed Identifier](https://aka.ms/seed-identifier) app at [`https://aka.ms/seed-identifier`](https://aka.ms/seed-identifier).
1. To generate a wheat species prediction, set the following properties and then select Predict wheat species:

- Seed length: The overall length of the seed in millimeters.
- Seed width: The width of the seed in millimeters.
- Groove length: The length of the groove in the seed.

1. Review the generated wheat species prediction.
1. Try adjusting the properties, and verify that the changes result in different species predictions.

## Review wheat seed data and model details

To create a machine learning model that predicts which wheat species a seed will grow, some training data that includes known species is used to determine a function that fits the features of an seed (length, width, groove length, etc.) to the label the model needs to predict (in this case, the species: 0 for Kama wheat, 1 for Rosa wheat, and 2 for Canadian wheat.)

1. Use the **Show sample data** button to reveal a sample of the training data for the seed species prediction model.
1. Use the **Model details** button to view information about the model, including the algorithm used to train it and the evaluation metrics calculated from validation data.
