import random
import re
import torch
import csv
handle = 'JustinHughes'
with open('cleanNVG.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    reader = list(reader)
# shuffle data
    random.shuffle(reader)

# fraction of training data
    split_train_valid = 0.9

# split dataset
    train_size = int(split_train_valid * len(reader))
    valid_size = len(reader) - train_size
    train_dataset, valid_dataset = torch.utils.data.random_split(reader, [train_size, valid_size]) 

    def make_dataset(dataset, epochs):
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        total_text = '<|endoftext|>'
        reader = [t for t in dataset]
        for _ in range(epochs):
            random.shuffle(reader)
            total_text += '<|endoftext|>'.join(map(str, reader)) + '<|endoftext|>'
        return total_text
    EPOCHS = 4

    with open('{}_train.txt'.format(handle), 'w') as f:
        data = make_dataset(train_dataset, EPOCHS)
        f.write(data)

    with open('{}_valid.txt'.format(handle), 'w') as f:
        data = make_dataset(valid_dataset, 1)
        f.write(data)