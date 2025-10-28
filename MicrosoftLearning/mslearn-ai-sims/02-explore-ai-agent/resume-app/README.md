# Use generative AI to summarize, evaluate, and generate content

Suppose a recruitment organization needs to streamline their process by automatically matching candidate resumes to job openings. One requirement for such an application might be to compare resumes to job descriptions, both of which may be in a variety of formats. A generative AI model is a great way to perform the content analysis, summarization, and generation required for this kind of task.

1. In a web browser, open the Recruiter Dashboard app at https://aka.ms/resume-app.
1. Use the B**rowse Candidate Pool** button to select any resume from the available profiles. When selected, review the resume summary that is generated - which should include the candidate’s name, title, experience, and key skills.

> Note that you can view the full resume from which the agent generated a summary.

3. Scroll down to the job listings and use the **Analyze Match** button to compare the selected resume with any of the available jobs. The app compares the skills in the selected resume with the job requirements, and calculates a score based on how good a match the candidate is for the job - both as an overall percentage and based on scores for individual skills. The app also generates some recommendations to help maximize the candidate’s chances of getting the job.
4. Continue comparing jobs with the resume. When you find a job that is a good match, generate an outreach email to send to the candidate. The email is dynamically generated based on the candidate resume and how well it matches the job requirements.

> After the email is generated, you can edit it, and then send it or download the text.

5. Repeat the process by using **Change Candidate** to select a different resume, and compare it against the available jobs.

> [!NOTE] > **Note:** The applications used in this exercise are simulations - there are no actual AI agents or generative AI models behind them. However, they’re based on real capabilities you can implement with [Azure AI Foundry](https://azure.microsoft.com/products/ai-foundry/) - in particular the [Azure AI Foundry Agent Service](https://azure.microsoft.com/products/ai-agent-service/).
