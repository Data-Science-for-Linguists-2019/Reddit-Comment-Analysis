# Reddit-Comment-Analysis
## Name : Matthew Borbonus
## Title : Have you Reddit? : A Subreddit Analysis
### Description:
A research project focusing on machine learning and whether you can predict a subreddit based on the features of a comment on a submission

[This](https://www.reddit.com/r/datasets/comments/8aen5g/update_for_the_reddit_corpus/) is the reddit post I found my corpus on. I could not find the author's name, only the user name he posts by which is u/Stuck\_In\_The\_Matrix. Credit for this corpus belongs to them and anyone who assisted them in assembling this corpus.

[The Reddit Corpus](https://files.pushshift.io/reddit/) as a direct site link

Directory File Structure -

* [README](README.md) - You are here... maybe... hopefully...
* [Progress Report](progress_report.md) - updates on my project throughout the semester
* [Project Plan](project_plan.md) - Writing out my project plan and details
* [Presentation](Presentation.pdf) - my power point presentation slides in pdf form. Because it's a pdf there are no animations therefore I feel the need to point out there's a title underneath the meme on slide 2.
* [Final Report](final_report.md) - self - explanatory.
* [Data_Samples](data_samples) Directory - contains Data Samples from processing the data
	* AskReddit [1000 samples](data_samples\AskReddit1000samples.csv) A relic from my first attempts to process the data
	* 30000 Comment Samples with Karma Score above 50 - for viewing and interacting with the data I was primarily working with
		* [Original Json Format](data_samples\30000Above50Samples.json)
		* [CSV format for spreadsheet viewing](data_samples\30000Above50Samples.csv)
	* The data frame I used to tune my models
		* [Original Json Format](data_samples\above50t.json)
		* [CSV format for spreadsheet viewing](data_samples\above50t.csv)
* [CRC](CRC) Directory - contains the files I used when using grid search on my models(CRC).
	* [Script for gridsearch](CRC/redditgrid.py) 
    * [SBatch file](CRC/redditgrid.sh) Sample Batch file I used
    * [Text file containing the output of the first job](CRC/multibest.txt)
* [Legacy Notebooks](legacy_notebooks) Directory - contains notebooks from every phase of the project that are no longer in active use (though referenced)
	* [project-explore.ipynb](legacy_notebooks/project-explore.ipynb) My first attempt at processing the data for phase 1. 
		* [NBVIEWER](https://nbviewer.jupyter.org/github/Data-Science-for-Linguists-2019/Reddit-Comment-Analysis/blob/master/legacy_notebooks/project-explore.ipynb)
	* [Phase 2 Notebook](legacy_notebooks/phase2_exploration.ipynb) - better processing - cleaning up of data and preliminary machine learning
		* [NBVIEWER](https://nbviewer.jupyter.org/github/Data-Science-for-Linguists-2019/Reddit-Comment-Analysis/blob/master/legacy_notebooks/phase2_exploration.ipynb)
	* [Phase 3 Notebook](legacy_notebooks/phase3progress.ipynb) This is the meat of the machine learning analysis
		* [NBVIEWER](https://nbviewer.jupyter.org/github/Data-Science-for-Linguists-2019/Reddit-Comment-Analysis/blob/master/legacy_notebooks/phase3progress.ipynb)
	* [NLTK Tokenization](legacy_notebooks/nltktokenizing.ipynb) I run nltk tokenization in a separate notebook to save run time on other notebooks.
		* [NBVIEWER](https://nbviewer.jupyter.org/github/Data-Science-for-Linguists-2019/Reddit-Comment-Analysis/blob/master/legacy_notebooks/nltktokenizing.ipynb)
	* [Presentation Data](legacy_notebooks/presentationdata.ipynb) - a notebook that I used to generate some of the data I used in my presentation.
		* [NBVIEWER](https://nbviewer.jupyter.org/github/Data-Science-for-Linguists-2019/Reddit-Comment-Analysis/blob/master/legacy_notebooks/presentationdata.ipynb)
* [Curent Phase](current_phase) Directory - Contains notebooks being actively worked on or from the most recent phase if none are actively worked on at the moment.
	* [Final Notebook](current_phase/final_notebook.ipynb) - my final pieces of work - only notebook in the current directory.
		* [NBVIEWER](https://nbviewer.jupyter.org/github/Data-Science-for-Linguists-2019/Reddit-Comment-Analysis/blob/master/current_phase/final_notebook.ipynb)
* [Images](images) Directory - contains figures and images and such to be used in the final report

Here is my [Guestbook](https://github.com/Data-Science-for-Linguists-2019/Class-Plaza/blob/master/guestbooks/guestbook_matt.md)