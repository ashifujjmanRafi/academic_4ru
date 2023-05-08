class Activity:
    def __init__(self,idx,activity,duration)->None:
        self.idx = idx
        self.activity = activity
        self.duration = duration
        self.predecessor = []
        self.successor = []
        self.ef = 0
        self.es = 0
        self.lf = 0
        self.ls =0


file = './input.txt'
activities = {}
index = []

for lines in open(file):
    words = lines.rstrip('\n').split(',')
    id = int(words[0])
    activity = words[1]
    duration = int(words[2])
    index.append(id)
    activities[id] = Activity(id,activity,duration)
    pre = words[3]
    if(pre != ""):
        predecessor = pre.split(';')
        for i in predecessor:
            activities[id].predecessor.append(int(i))
            activities[int(i)].successor.append(id)
maxEF = 0
#forward pass
for i in index:
    if(len(activities[i].predecessor)==0):
        activities[i].ef = activities[i].duration
    else:
        maxtime = 0
        for x in activities[i].predecessor:
            if(maxtime<activities[x].ef):
                maxtime = activities[x].ef
        activities[i].es = maxtime
        activities[i].ef = maxtime + activities[i].duration
    maxEF = max(maxEF,activities[i].ef)

for idx in range(len(index)):
    i = index[len(index)-idx-1]
    if(len(activities[i].successor)==0):
        activities[i].lf = maxEF
        activities[i].ls = maxEF - activities[i].duration
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