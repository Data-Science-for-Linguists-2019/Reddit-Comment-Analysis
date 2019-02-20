# Reddit-Comment-Analysis Log
## Captain's Log: Stardate 2/7/19
__Changes__ -
Creation of this GitHub repo as a starting point of this research project.
##Captain's Log : 1st Progress Report
So I discovered that the person who assembled the original corpus has posted an updated repository that contains individual months or a few daily samples. Since the month samples are huge (3GB compressed, 40GB uncompressed), I am going to do what I can off of a daily sample. For those wishing to download it and try themselves, I picked the "RC_2017-12-21.xz" archive from the daily section. This daily sample is about 259MB compressed, 2GB uncompressed. I learned how to read in the data while it's in it's compressed form (more in Jupyter notebook file).

My data is pre-organized by various attributes, karma score, author, if archived and such. There's about 80 columns of data, most of which I do not need. I'll probably save each subreddit as separetly, and then create an additonal file that has only the attributes I need. The attributes I'm mostly concerned are the title and content of a post, the karma score, number of comments, and possibly the number of guilds if I get additional time to play around with it. Also some way to ID each post, either the post url, or another attribute that I don't know about

###Sharing Options

As far as I know, tbe corpus is publicly available, I cannot find any license anywhere. I've looked through Reddit's term of service, so unless they harvested the Reddit comments illegally (which if they did, their posts linking to this would be removed), there is no copyright on Reddit's end. So as far as I know, I can publish the data. This leads me to present a couple options:

* I upload my subreddit files with the pruned columns. I'm processing them now so I don't have a final result, but I imagine they won't be that large. Separating them by subreddit and giving the data would allow reproducibility of my project quickly




Here are some links:  

* [The Reddit Post](https://www.reddit.com/r/datasets/comments/8aen5g/update_for_the_reddit_corpus/) in question
* Alink straight to [the updated Reddit corpus](https://files.pushshift.io/reddit/)
* The Jupyter Notebook file : [project-explore.ipynb](project-explore.ipynb)
* 