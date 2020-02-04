from ShowProcess import showProcessResultTable,showProcessResultGraph
def TimeCalculator(Process):
    turnPerProcess = []
    waitPerProcess = [0]
    timeWaiting = 0
    timeTurn = 0

    sumWait = 0
    sumBrust  = 0
    avgTurnAround = 0
    avgWaitingTime = 0 
    for i in range(len(Process)):
        timeTurn += Process[i]
        turnPerProcess.append(timeTurn)
        if i != 0:
            timeWaiting += Process[i-1]
            waitPerProcess.append(timeWaiting)
    for i in range(len(Process)):
        sumBrust += turnPerProcess[i]
        sumWait += waitPerProcess[i]

    avgTurnAround = sumBrust / len(Process)
    avgWaitingTime = sumWait / len(Process)
    return [[avgWaitingTime,avgTurnAround],turnPerProcess,waitPerProcess]

def returnMapValue(List,Key):
    idx = List[0].index(Key)
    return List[1][idx]

def FirstComeFirstServeScheduling(Process):
    Result = TimeCalculator(Process)
    print("First come First serve Scheduling Algorithm")
    avgWaitingTime = Result[0][0]
    avgTurnAround = Result[0][1]
    turnPerProcess = Result[1]
    waitPerProcess = Result[2]
    return [Process,avgWaitingTime,avgTurnAround,waitPerProcess,turnPerProcess]
    

def ShortestJobFirstScheduling(Process):
    Process = sorted(Process)
    Result = TimeCalculator(Process)
    print("Shortest job first Scheduling Algorithm")
    avgWaitingTime = Result[0][0]
    avgTurnAround = Result[0][1]
    turnPerProcess = Result[1]
    waitPerProcess = Result[2]
    return [Process,avgWaitingTime,avgTurnAround,waitPerProcess,turnPerProcess]

    

def RoundRobinScheduling(Process,quantumTime):
    tempProcess = Process.copy()
    n = len(Process)
    allPeroid = sum(Process)

    startTimestamp = [[],[]]
    endTimestamp = [[],[]]
    hasCollectstart = [[],[]]

    #create defalut val
    for i in range(n) :
        hasCollectstart[0].append(i)
        hasCollectstart[1].append(False)

    time = 0
    while time < allPeroid:
        for i in range (n):
            if Process[i] != 0 :
                #startExe
                if Process[i] > quantumTime:
                    if hasCollectstart[1][i] == False:
                        startTimestamp[0].append(i+1) #collect process
                        startTimestamp[1].append(time) #collect starttime 
                        hasCollectstart[1][i] = True
                    Process[i] -= quantumTime #execute
                    time += quantumTime #usePeroid = quantumtime
                else:
                    if hasCollectstart[1][i] == False:
                        startTimestamp[0].append(i+1) #collect process
                        startTimestamp[1].append(time) #collect starttime 
                        hasCollectstart[1][i] = True
                    time += Process[i]
                    Process[i] = 0
                #endExe
                if Process[i] == 0 :
                    endTimestamp[0].append(i+1)
                    endTimestamp[1].append(time)
    # print(endTimestamp)
    avgTurnAround = 0
    avgWaitingTime = 0
    turnPerProcess = []
    waitPerProcess = []
    for i in range(n):
        waitPerProcess.append(returnMapValue(endTimestamp,i+1) - tempProcess[i])
        turnPerProcess.append(returnMapValue(endTimestamp,i+1) - returnMapValue(startTimestamp,i+1))
        avgWaitingTime += (returnMapValue(endTimestamp,i+1) - tempProcess[i])
        avgTurnAround += (returnMapValue(endTimestamp,i+1) - returnMapValue(startTimestamp,i+1)) 
    avgWaitingTime /= n
    avgTurnAround /= n

    print("Round Robin Scheduling Algorithm")
    return [tempProcess,avgWaitingTime,avgTurnAround,waitPerProcess,turnPerProcess]
    





    






