import json
files=['file1.json','file2.json','file3.json']

def merge_JsonFiles(filename):
    result = list()
    for f1 in filename:
        with open(f1, 'r', encoding='utf-8') as infile:
            result.extend(json.load(infile))

    with open('merged.json', 'w') as output_file:
        json.dump(result, output_file)

merge_JsonFiles(files)