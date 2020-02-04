from genProcess import RandProcess
from Algorithms import FirstComeFirstServeScheduling,ShortestJobFirstScheduling,RoundRobinScheduling
from ShowProcess import showProcessResultTable,showProcessResultGraph
# exProcess = [30,24,8,7,5,38,3,20,4,8,6,6,29,39,35,36,4,26,24,4,25,4,7,36,2,22,26,3,35,20,37,6,23,5,39,5,8,8,22,7]
# Process = [24,3,3]
# RoundRobinScheduling([21,25,4,8,6],4)
Assumption  = str(input("Assumption [ 1 , 2 ,3 ] : "))


cmd = str(input("Result in table : 1\nResult in Graph : 2\n>>"))
if cmd == "1":
    Process = RandProcess(Assumption)
    isSJF = False
    algorithm = [FirstComeFirstServeScheduling(Process),ShortestJobFirstScheduling(Process),RoundRobinScheduling(Process,4)]
    select = int(input("algorithm 1,2,3 : "))
    if select == 2:
        isSJF = True
    if select > 0 and select <= 3:
        i = select - 1
        if select == 1 :
            print("FirstComeFirstServeScheduling")
        elif select == 2:
            print("ShortestJobFirstScheduling")
        elif select == 3:
            print("RoundRobinScheduling")
        showProcessResultTable(algorithm[i][0],algorithm[i][3],algorithm[i][4],[algorithm[i][1],algorithm[i][2]],isSJF)
    else :
        print("no such algorithm")
elif cmd == "2":
    Round = int(input("Graph Freq : "))
    FCFSList = []
    SJFList = []
    RRSList = []
    for i in range(Round):
        Process = RandProcess(Assumption)
        quantumTime = 4
        if Process != False:
            FCFSList.append(FirstComeFirstServeScheduling(Process)[1]) 
            SJFList.append(ShortestJobFirstScheduling(Process)[1])
            RRSList.append(RoundRobinScheduling(Process,quantumTime)[1])
        else:
            print("no such assmuption yet please add !")
    showProcessResultGraph(FCFSList,SJFList,RRSList,Round)
else :
    print("please select a result")
    




