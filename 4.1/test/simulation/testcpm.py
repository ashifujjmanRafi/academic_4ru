class Activity:
    def __init__(self,idx,activity,duration):
        self.idx = idx
        self.activity = activity
        self.duration = duration
        self.predecessor = []
        self.successor = []
        self.ef = 0
        self.es = 0
        self.ls = 0
        self.lf = 0

file = './input.txt'
activities = {}
index = []

for line in open(file):
    words = line.rstrip('\n').split(',')
    idx = int(words[0])
    activity = words[1]
    duration = int(words[2])
    pre = words[3]
    index.append(idx)
    activities[idx] = Activity(idx,activity,duration)

    if(pre != ""):
        predecessor = pre.split(';')
        for x in predecessor:
            activities[idx].predecessor.append(int(x))
            activities[int(x)].successor.append(idx)

#fp
TRT = 0

for i in index:
    if(len(activities[i].predecessor)==0):
        activities[i].ef = activities[i].duration
    else:
        maxtime = 0
        for x in activities[i].predecessor:
            if(maxtime < activities[x].ef):
                maxtime = activities[x].ef
        activities[i].es = maxtime
        activities[i].ef = maxtime + activities[i].duration
    TRT = max(TRT,activities[i].ef)

for idx in range(len(index)):
    i = index[len(index)-1-idx]
    if(len(activities[i].successor)==0):
        activities[i].lf = TRT
        activities[i].ls = TRT - activities[i].duration
    else:
        mintime = 9999
        for x in activities[i].successor:
            if(mintime>activities[x].ls):
                mintime = activities[x].ls
        activities[i].lf = mintime
        activities[i].ls = mintime - activities[i].duration

result = []
for i in index:
    if(activities[i].ef == activities[i].lf):
        result.append(activities[i].activity)
print(result)