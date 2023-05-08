import numpy as np

class Activity:
    def __init__(self,idx,activity,duration) ->None:
        self.idx = idx
        self.activity = activity
        self.duration = duration
        self.predecessor = []
        self.successor = []
        self.early_start = 0
        self.early_finish = 0
        self.late_start = 0
        self.late_finish = 0

file_path = './input2.txt'
activities = {}
index = []

for lines in open(file_path):
    words = lines.rstrip('\n').split(',')
    idx = int(words[0])
    activity = words[1]
    duration = int(words[2])
    pre = words[3]
    index.append(idx)
    activities[idx] = Activity(idx,activity,duration)
    if(pre != ""):
        predecessor = pre.split(';')
        for i in predecessor:
            activities[idx].predecessor.append(int(i))
            activities[int(i)].successor.append(idx)
    
maxEf=0
#forward pass
for i in index:
    if(len(activities[i].predecessor)==0):
        activities[i].early_finish = activities[i].duration
    else:
        maxtime = 0
        for x in activities[i].predecessor:
            if(maxtime<activities[x].early_finish):
                maxtime = activities[x].early_finish
        activities[i].early_start = maxtime
        activities[i].early_finish = maxtime+activities[i].duration

    maxEf = max(maxEf,activities[i].early_finish)

#backward pass
length = len(index)
for i in range(length):
    idx = index[length-i-1]
    if(len(activities[idx].successor)==0):
        activities[idx].late_finish = maxEf
        activities[idx].late_start = maxEf-duration
    else:
        mintime = 9999
        for x in activities[idx].successor:
            if(mintime > activities[x].late_start):
                mintime = activities[x].late_start 
        activities[idx].late_finish = mintime
        activities[idx].late_start = mintime - activities[idx].duration

result = []

for i in index:
    if(activities[i].early_start == activities[i].late_start):
        result.append(activities[i].activity)
for i in range(len(result)-1):
    print(result[i] + "->",end = "")
print(result[len(result)-1])
    