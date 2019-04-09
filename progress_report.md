# Reddit-Comment-Analysis Log
## Captain's Log: Stardate 2/7/19
__Changes__ -
Creation of this GitHub repo as a starting point of this research project.

## Captain's Log : 1st Progress Report Stardate 2/21/19

So I discovered that the person who assembled the original corpus has posted an updated repository that contains individual months or a few daily samples. Since the month samples are huge (3GB compressed, 40GB uncompressed), I am going to do what I can off of a daily sample. For those wishing to download it and try themselves, I picked the "RC_2017-12-21.xz" archive from the daily section. This daily sample is about 259MB compressed, 2GB uncompressed. I learned how to read in the data while it's in it's compressed form (more in Jupyter notebook file).

My data is pre-organized by various attributes, karma score, author, if archived and such. There's about 80 columns of data (though this decreases to 22 if I normalize it with json), most of which I do not need. I'll probably save each subreddit as separetly, and then create an additonal file that has only the attributes I need. The attributes I'm mostly concerned are the title and content of a post, the karma score, number of comments, and possibly the number of guilds if I get additional time to play around with it. Also post ID (and Parent ID for comments).

(Also heads up, my current read file function is REALLY slow since even the daily sample is about 3 million lines long, give or take a few, this is why I didn't restart the kernel in the notebook file, not because I don't have the data, but it's really slow.)

### Sharing Options

As far as I know, tbe corpus is publicly available, I cannot find any license anywhere. I've looked through Reddit's term of service, so unless they harvested the Reddit comments illegally (which if they did, their posts linking to this would be removed since they posted this on Reddit), there is no copyright on Reddit's end. So as far as I know, I can publish the data. This leads me to present a couple options:

* I upload samples by subreddit. Dumping the Ask Reddit dataframe to csv is about 69MB according to my explorer, which is bigger than Github's limit. Maybe the smaller subreddits won't have this issue, but the larger ones will have to be distributed by sample
* I upload samples of everything, even the smaller subreddits who could be uploaded naturally within the File limit. This puts all subreddits on an even presentation field. May or may not have to do this with machine learning data depending up on the disparity.
* I will probably end up sharing my test and training data in samples too, since I've talked with Dan in office hours and may incorporate machine learning as a goal in my project.

Here are some links:  

* [The Reddit Post](https://www.reddit.com/r/datasets/comments/8aen5g/update_for_the_reddit_corpus/) in question
* A link straight to [the updated Reddit corpus](https://files.pushshift.io/reddit/)
* The Jupyter Notebook file : [project-explore.ipynb](legacy_notebooks/project-explore.ipynb)
* The Data Sample : [AskReddit 1000 samples](data_samples/AskReddit1000samples.csv)

## Captain's Log : 2nd Progress Report Stardate 3/19/19

### Corpus plan
I'm sticking with the single day corpus. Dealing with comments from a larger timeframe would be better, but would mean more time consuming to process correctly, time I do not exactly have..

### Constantly Evolving Project Plan
I am fully committing to the machine learning of identifying subreddit based on the comment. I have even done some preliminary machine learning exercises. I am currently deciding on subreddits to focus on, but I will settle upon it soon. The list will include most of the ones I used in the current phase. I'll aim for about 8-10 if it's manageable.

### Preliminary Analysis
I've done some preliminary machine learning, and achieved around 65-66% accuracy as the best. 66% with just bayes. 65% with support vectors on just textual features with 5 different subreddits. This gives me a decent idea of what to work with when I expand to 8-10 subreddits. Also, this is just preliminary, so no kfold validation just yet. In the final trials, it will be used if SVD can run all of the trials in a reasonable time frame. (I forgot random state on this trial comparison, the unknown random seed trial I originally got got had 62% with Bayes, increased by 5% using support vectors, so I know there's potential with support vectors here)

### Size and Publishing
The size of the whole corpus in words is 105-106 million words, with an average of 38.7 words per comment. I've published a sizeable sample of the data in the original json format, as well as a csv format that people can peruse with a spreadsheet viewer.

### Sharing Options
I've published a sample of 30,000 comments that all have a score above 50 since that was the data I was using in machine learning. I can't share the whole corpus, but I believe I'll be able to share/publish the data from the subreddits I use. It will be the first thing I do when I have solidified that subreddit list.

(I've adjusted the link in the previous section that was affected by the quick repository restructure).
### Relevant Links:

* [Current Jupyter Notebook](current_phase/phase2_exploration.ipynb)
* [The Json Sample File](data_samples/30000Above50Samples.json)
* [The data in a browsable csv format](data_samples/30000Above50Samples.csv)

## Captain's Log : 3rd Progress Report Stardate 4/9/19

I've probably not made as much progress as I would like, but nonetheless, I have made headway into the problem.

### Subreddits

I quickly determined what my list of subreddits will be. They are the following:

* PrequelMemes
* StarWars
* relationships 
* aww 
* nfl 
* gaming
* mildlyinteresting
* politics
* Showerthoughts
* worldnews
* gifs
* funny

12 subreddits in all. I ran some quick statistics, this data size comes out at 8056 comments, 336306 words. 

### Machine Learning

I have made some considerable progress on the machine learning front. I established the baseline at 22% since that is the percentage of comments from politics, the largest portion. The best cross-validation runs produced acccuracy in the 60-70% range.

I tried optimizing my models with grid search on the CRC. I tried two runs, first 6, then 10 hours, but it timed out on support vectors. I guess I was overzealous, I settled to use the Tfidf settings found with Multinomial Naive Bayes and just grid search on just Support Vector paramets using the tfidf settings. This may have been what lead to Multinomial Naive Bayes coming out ahead of support vectors in my runs (in terms of accuracy).

I did try some features, and flairs I believe increased the accuracy, . Thus, keeping them in the data was justified in the end.


