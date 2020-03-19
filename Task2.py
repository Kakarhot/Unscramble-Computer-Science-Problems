"""
Read file into texts and calls.
It's ok if you don't understand how to read files
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

# duration_dict = {}
# for number in numbers_unique:
#     calls_number = calls[calls.sending_number == number].append(calls[calls.receiving_number == number])
#     if calls_number.shape[0] > 0:
#         duration_dict[number] = calls_number.duration.sum()

# number_max = max(duration_dict, key=duration_dict.get)

# print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(number_max, duration_dict[number_max]))
"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
# 
duration_dict = {}
for entry in calls:
    send_num = entry[0]
    receive_num = entry[1]
    time = int(entry[3])

    if send_num in duration_dict:
        duration_dict[send_num] += time
    else:
        duration_dict[send_num] = time

    if receive_num in duration_dict:
        duration_dict[receive_num] += time
    else:
        duration_dict[receive_num] = time

number_max = max(duration_dict, key=duration_dict.get)

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(number_max, duration_dict[number_max]))
