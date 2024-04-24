import csv
import random

rowSize = 10000

header = ["Header1", "Header2", "Header3", "Header4"]
data = [[random.random() for _ in range(len(header))] for _ in range(rowSize)]

with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)