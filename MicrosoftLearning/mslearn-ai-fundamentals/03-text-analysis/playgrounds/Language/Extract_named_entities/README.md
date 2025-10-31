# Extract named entities with Azure AI Language in Azure AI Foundry portal

Named entities are words that describe people, places, and objects with proper names. Let’s use the named entity extraction capability of Azure AI Language to identify types of information in a review.

1. In the Language playground, select Extract information. Then select the Extract named entities tile.
2. Under Sample, enter the following review:

```
Tired hotel with poor service
The Royal Hotel, London, United Kingdom
5/6/2018
This is an old hotel (has been around since 1950's) and the room furnishings are average - becoming a bit old now and require changing. The internet didn't work and had to come to one of their office rooms to check in for my flight home. The website says it's close to the British Museum, but it's too far to walk.
```

3. Select **Run**. Review the output.

Notice in the *Details* section how the extracted entities come with additional information such as type and confidence scores. The confidence score represents the likelihood that the type identified actually belongs to that category.
