title: "gzip-paper-replication"
date: 2023-09-20

In this blog, I talk about how I replicated the “Low-Resource Text Classification: A Parameter-Free Classification Method with Compressors" paper with a custom dataset! 

This paper talks about using a combination of a simple compressor (gzip) and a classifier (k-nearest neighbour (kNN)) to classify text without any training parameters.

First I replicated the paper with their default dataset (AGNews)!
To do that, I followed the below steps:
	1. Create a new virtual environment for this project (I’m using conda).
	2. Download the npc-gzip folder (GitHub repo) into <folder_name> under <folder_path>.
	3. Run the maintext.py python file in the directory that the file is stored in. 
 	4. Get your accuracy results!
Make sure that all the required dependencies get downloaded from the requirements.txt file!

Now that we’ve run the file with their default dataset, it’s time to use our own custom dataset!
To do that, the first and second steps were the same as the default dataset! Then, we format our dataset to ensure that it runs with no errors.
To do so, I did the following:
	1. The data directory requires train and test tab-delimited text files ({label}\t{text}) as well as clean files with no tabs, newlines or multiple spaces.
	2 My data was in the form of multiple JSON files, so I merged them and then converted them into a CSV file and then used an sklearn model to split the data 	into test and train files.( combine.py & test_train_split.ipynb)
	3. I then used regex to clean up the files (remove all tabs, newlines, as well as multiple spaces) and bring them to a format accepted by the model!		(csv_cleanup.py).
 	4. I then ran the maintext.py file with the following syntax:
  	> python maintext.py --dataset custom –data_dir <path to your custom dataset, with train and test tab-delimited text files.> --class_num <no. of classes 	you have>
   	5. Got the accuracy results!
    	6. I also added a confusion matrix to get a better view of my results using seaborn! (confusion.ipynb) 
     	– make these changes to your code! – location: where you got predicted labels and your labels.


You can also use different compressors and run your dataset using  '--compressor <gzip, lzma, bz2>' while running your python file.
With my dataset, gzip worked better than bz2. lzma was quite accurate but is very heavy so it took a long time to run!

Another point to note is that larger files, or rather files with more data points per class work better. Try to balance datasets as much as possible – a roughly equal number of data points per class if possible, and remove classes with too many data points.


  
