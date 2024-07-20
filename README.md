## Replicate the Model

Download the `npc_gzip` zip file linked below to replicate the model with your custom dataset! Follow these steps to replicate the results:

1. **Download the Required Files:**
   - Download the `npc_gzip` zip file from [GitHub repository](https://github.com/bazingagin/npc_gzip/tree/main).

2. **Replicate the Model with the Default Dataset:**
   - Create a new virtual environment for this project (using `conda` or `venv`).
   - Download the `npc-gzip` folder from the [GitHub repository](https://github.com/bazingagin/npc_gzip/tree/main) into `<folder_name>` under `<folder_path>`.
   - Navigate to the directory containing `maintext.py` and run:
     ```bash
     python maintext.py
     ```
   - Review the accuracy results.

   Make sure all dependencies are installed by checking the `requirements.txt` file.

3. **Replicate the Model with Your Custom Dataset:**
   - Follow the same steps as above to set up your environment and download files.
   - Format your dataset to ensure compatibility:
     1. Ensure your dataset is in the form of tab-delimited text files (`{label}\t{text}`) with clean data (no tabs, newlines, or multiple spaces).
     2. If your data is in JSON format, merge and convert it into CSV files. Use `combine.py` and `test_train_split.ipynb` for this conversion.
     3. Clean up the CSV files using regex (remove tabs, newlines, multiple spaces) with `csv_cleanup.py`.
   - Run the model with the following command:
     ```bash
     python maintext.py --dataset custom --data_dir <path to your custom dataset, with train and test tab-delimited text files> --class_num <number of classes>
     ```
   - Review your accuracy results.
   - Optionally, add a confusion matrix for better result visualization using seaborn. Modify your code to include the confusion matrix in `confusion.ipynb`.

4. **Experiment with Different Compressors:**
   - You can use different compressors by specifying `--compressor <gzip, lzma, bz2>` when running your Python file. Based on my experiments, `gzip` worked better than `bz2`, and `lzma`, while accurate, was slower.

5. **Data Considerations:**
   - Larger files or datasets with more data points per class generally yield better results. Try to balance your datasets as much as possible, aiming for a roughly equal number of data points per class and removing any classes with excessive data points.

## Blog Post

For a detailed walkthrough of replicating the "Low-Resource Text Classification: A Parameter-Free Classification Method with Compressors" paper with a custom dataset, check out my [blog post](https://github.com/rachelb24/rachel-gzip-paper-rep/blob/main/_posts/2023-09-20-gzip-paper-rep.md).




