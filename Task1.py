"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

# import pandas as pd

# calls = pd.read_csv('calls.csv', header=None, names=['sending_number', 'receiving_number', 'time', 'duration'])
# texts = pd.read_csv('texts.csv', header=None, names=['sending_number', 'receiving_number', 'time'])

# numbers_unique = calls.sending_number.append([calls.receiving_number, texts.sending_number, texts.receiving_number]).unique()
# print(numbers_unique.size)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
phone_num_list = []
for entry in texts + calls:
    phone_num_list.append(entry[0])
    phone_num_list.append(entry[1])

unique_numbers = len(set(phone_num_list))

print("There are {} different telephone numbers in the records.".format(unique_numbers))
