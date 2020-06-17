from msort import * #import msort module

with open('data.csv') as f: #get data from csv file
    result = [tuple(line.strip().split(',')) for line in f.readlines()] #convert data to a list of tuples

mergesort(result, lambda x,y: x < y) #sort by id

with open("by_id.txt", "w") as file1: #write to file
    for tup in result:
        file1.write(f'{tup} \n')

mergesort(result, lambda x,y: x[1].split()[-1] < y[1].split()[-1]) #sort by lastname

with open("by_name.txt", "w") as file2: #write to file
    for tup in result:
        file2.write(f'{tup} \n')

