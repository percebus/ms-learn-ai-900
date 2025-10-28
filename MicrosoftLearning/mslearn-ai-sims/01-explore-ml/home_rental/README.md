# Generate predictions for apartment rental

Let’s say you own an apartment in the thriving town of Dataville. You decide you want to rent out the apartment, and you need to determine an appropriate monthly rental amount that you can charge the tenant. Rent prices are based on a variety of factors related to the property and its location, so you’re going to use a property web site that include a machine learning powered app to help you determine the right rental amount.

## Predict monthly rent amounts based on property features

1. In a web browser, open the [Home rental estimator app](https://aka.ms/rent-predictor) at [`https://aka.ms/rent-predictor`](https://aka.ms/rent-predictor).
1. To generate a rental prediction, set the following properties and then select **Calculate Rent**:

- **Postal Code:** Select one of the postal codes for the fictional town of Dataville.
- **Property Size:** Use the slider to set the size of your property in square feet.
- **Number of Bedrooms:** Select the number of bedrooms in your property.

1. Review the generated rent prediction.
1. Try adjusting the property details, and verify that the changes result in different rental predictions.

## Review rental data and model details

To create a machine learning model that predicts rental prices, some training data that includes known rental prices is used to determine a function that fits the features of an apartment (location, size, number of bedrooms, etc.) to the label the model needs to predict (in this case, the rental amount.)

1. Use the **Show sample data** button to reveal a sample of the training data for the rental prediction model.
1. Use the **Show model details** button to view information about the model, including the algorithm used to train it and the evaluation metrics calculated from validation data.
