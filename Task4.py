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

# receiving_numbers = calls.receiving_number.append([texts.sending_number, texts.receiving_number]).unique()
# marketing_numbers = []
# for number in calls.sending_number.unique():
#     if number not in receiving_numbers:
#         marketing_numbers.append(number)

# print("These numbers could be telemarketers: ")
# for number in sorted(marketing_numbers):
#     print(number)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
calls_list = []
for entry in calls:
    calls_list.append(entry[0])

non_call_list = []
for entry in calls:
    non_call_list.append(entry[1])
for entry in texts:
    non_call_list.append(entry[0]) 
    non_call_list.append(entry[1]) 

calls_set = set(calls_list)
non_calls_set = set(non_call_list)
marketing_numbers = []
for number in calls_set:
    if number not in non_calls_set:
        marketing_numbers.append(number)

print("These numbers could be telemarketers: ")
for number in sorted(marketing_numbers):
    print(number)
