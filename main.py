from genProcess import RandProcess
from Algorithms import FirstComeFirstServeScheduling,ShortestJobFirstScheduling,RoundRobinScheduling
from ShowProcess import showProcessResultTable,showProcessResultGraph
# exProcess = [30,24,8,7,5,38,3,20,4,8,6,6,29,39,35,36,4,26,24,4,25,4,7,36,2,22,26,3,35,20,37,6,23,5,39,5,8,8,22,7]
# Process = [24,3,3]
# RoundRobinScheduling([21,25,4,8,6],4)
Assumption  = str(input("Assumption [ 1 , 2 ,3 ] : "))
FCFSList = []
SJFList = []
RRSList = []
n = 20
for i in range(n):
    Process = RandProcess(Assumption)
    quantumTime = 4
    if Process != False:
        FCFSList.append(FirstComeFirstServeScheduling(Process)[1]) 
        SJFList.append(ShortestJobFirstScheduling(Process)[1])
        RRSList.append(RoundRobinScheduling(Process,quantumTime)[1])
    else:
        print("no such assmuption yet please add !")

showProcessResultGraph(FCFSList,SJFList,RRSList,n)



