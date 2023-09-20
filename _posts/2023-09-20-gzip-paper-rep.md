title: "gzip-paper-rep"
date: 2023-09-20

Text Classifier (using compressors) not using complex models. 
A combination of a simple compressor (gzip) and a classifier (k-nearest neighbour (kNN))
2 Main Approaches:
1.	To estimate Entropy based on the Shannon Information theory (Now what is that? Gonna be honest, I had no idea either. So, let’s dive into that first - explain)
2.	To approximate Kolmogarov complexity and Information Distance.
Doesn’t need training/pre-training
First I replicated what they did with their default dataset (AGNews)!
Steps to do that:
1.	Create a new conda virtual environment for this project (or any venv of your choice! I’m using conda).
2.	Download the npc-gzip folder (github repo) in the folder of your choice <folder name> under <folder path>.
3.	Run >python maintext.py in the directory that your file is stored in. [ --dataset custom –data_dir <path to your custom dataset, with train and test tab delimited text files.> --class_num <no. of classes you have>]. You can also use different compressors and run them, they have lzma and bz2 apart from gzip. Gzip better than bz2. Lzma is quite accurate but is very heavy so take  along time to run.
Issues that you might face:
	The required dependencies might not get downloaded from your requirements.txt file. Now to solve these,  
•	Make sure the python file that you’re trying to run and the requirements.txt file are under the same folder.
•	Try using > pip freeze>requirements.txt
Now that we’ve run the file with their custom dataset, it’s time to train it with our own custom dataset!
The compressor that we’re using requires your custom dataset to be in the {label}\t{text} format, so ensure that your file is in the correct format!
-	Larger files, or rather files with more datapoints per class work better. Try to balance datasets as much as possible – roughly equal number of datapoints each class – if possible, remove classes with too many datapoints.
o	Model learns that it can achieve high accuracy by consistently predicting the majority class even if the other classes are more important in real life!
-	I had multiple .json files that I merged together (add code snippet) 
-	Used a sklearn model to split the file into 2 separate files (test and train) and saved them (20-80 ratio) (test_train_split.ipynb)
-	Cleaned up the files and then saved them as .csv files (csv_cleanup.py) using regex by removing all tabs, newlines as well as multiple spaces
-	Then ran the code on conda and got the results!
-	I also added a confusion matrix to get a better view of my results using seaborn! (confusion.ipynb) – make these changes to your code! – location: where you got predicted labels and your labels.
-	Can also add a link to the github errors page to help out!
