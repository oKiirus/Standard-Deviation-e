import csv
import pandas as pd
import plotly.express as px
import math 

mean = 0

with open('class2.csv', newline = '') as f:
    file = csv.reader(f)
    data = list(file)
    
data.pop(0)
marks = []
for i in range(0, len(data)):
    q = data[i][1]
    
    marks.append(float(q))

n = len(marks)
sum = 0
for e in marks:
    sum += e

mean = sum / n

print(mean)



df = pd.read_csv('class2.csv')

graph = px.scatter(df, x = 'Student Number', y = 'Marks')
graph.update_layout(shapes = [dict(type = 'line', y0 = mean, y1 = mean, x0 = 0, x1 = n)])
graph.show()
squaredList = []
for a in marks:
    b = int(a) - mean
    b = b ** 2
    squaredList.append(b)
sigma = 0
for i in squaredList:
    sigma = sigma + i

result = math.sqrt(sigma / (n - 1))

print(result)

