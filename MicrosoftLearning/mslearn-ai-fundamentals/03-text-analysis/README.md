# Analyze text in Azure AI Foundry portal

Azure AI Language includes Text Analytics, with capabilities such as entity recognition, key phrase extraction, summarization, and sentiment analysis. For example, suppose the fictitious travel agent Margie’s Travel encourages customers to submit reviews for hotel stays. You could use the Language service to extract named entities, identify key phrases, summarize text, and more.

In this exercise, you will use Azure AI Language in Azure AI Foundry portal, Microsoft’s platform for creating intelligent applications, to analyze hotel reviews.

This exercise takes approximately **20** minutes.

## Create a project in Azure AI Foundry portal

1. In a web browser, open the Azure AI Foundry portal at [`https://ai.azure.com`](https://ai.azure.com) and sign in using your Azure credentials. Close any tips or quick start panes that are opened the first time you sign in, and if necessary use the **Azure AI Foundry** logo at the top left to navigate to the home page, which looks similar to the following image (close the **Help** pane if it’s open):

2. Scroll to the bottom of the page, and select the **Explore Azure AI Services** tile.

3. On the Azure AI Services page, select the **Language + Translator** tile.

4. On the **Language + Translator** page, select **Try the Language playground**. Then, when prompted, create a new project with the following settings:
  - **Project name**: Enter a valid name for your project.
  - **Advanced settings**:
    - **Subscription**: Your Azure subscription
    - **Resource group**: Create or select a resource group
    - **Region**: Select any AI Foundry recommended region
    - **AI Foundry or Azure OpenAI**: Create a new Azure AI Foundry resource with a valid name

5. Select **Create**. Wait for your project to be created. It may take a few minutes.

6. When the project is created, you will be taken to an **Language** playground (if not, in the task pane on the left, select **Playgrounds** and open the Language playground from there.)

The Language playground is a user interface that enables you to try out some Azure AI Language capabilities.

## Use Azure AI Language to analyze text

Azure AI Language offers a wide range of text analysis capabilities.

1. [Extract named entities with Azure AI Language in Azure AI Foundry portal](./playgrounds/Language/Extract_named_entities/README.md)
2. [Extract key phrases with Azure AI Language in Azure AI Foundry portal](./playgrounds/Language/Identify_key_phrases/README.md)
3. [Summarize text with Azure AI Language in Azure AI Foundry portal](./playgrounds/Language/Summarize_text/README.md)
4. [Analyze sentiment in text](./playgrounds/Language/Analyze_sentiment/README.md)

## Detect language and translate text

Azure AI Language enables you to detect the language in which text is written. Additionally, Azure AI Translator enables you to easily translate text from one language to another.

1. [Detect language](./playgrounds/Language/Detect_language/README.md)
2. [Translate text](./playgrounds/Translator/Text_translation/README.md)

## Clean up

If you don’t intend to do more exercises, delete any resources that you no longer need. This avoids accruing any unnecessary costs.

1. Open the Azure portal at https://portal.azure.com and select the resource group that contains the resources you created.
1. Select Delete resource group and then enter the resource group name to confirm. The resource group is then deleted.

## Learn more

To learn more about what you can do with this service, see the Language service page.

## References

- [Analyze text in Azure AI Foundry portal](https://microsoftlearning.github.io/mslearn-ai-fundamentals/Instructions/Exercises/03-text-analysis.html)
