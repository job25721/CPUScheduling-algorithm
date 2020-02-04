import random

def percentage(value,percent):
    return int(value * (percent/100))

def RandProcess(Assumption):
    Process = 0
    processList = []
    range1 = 0
    range2 = 0
    range3 = 0
    haveAssumption  = True
    if Assumption  == "1":
        Process = 60
        range1 = percentage(Process,70)
        range2 = percentage(Process,20)
        range3 = percentage(Process,10)
        print("--------------------------------------")
        print("[ Assumption  1 ]",Process,"Process")
        print("[ take 2 - 8 ms ]",range1,"Process")
        print("[ take 20 - 30 ms ]",range2,"Process")
        print("[ take 35 - 40 ms ]",range3,"Process")
        for i in range(range1):
            processList.append(random.randrange(2,8))
        for i in range(range2):
            processList.append(random.randrange(20,30))
        for i in range(range3):
            processList.append(random.randrange(35,40))
    elif Assumption  == "2":
        Process = 40
        range1 = percentage(Process,50)
        range2 = percentage(Process,30)
        range3 = percentage(Process,20)
        print("--------------------------------------")
        print("[ Assumption  2 ]",Process,"Process")
        print("[ take 2 - 8 ms ]",range1,"Process")
        print("[ take 20 - 30 ms ]",range2,"Process")
        print("[ take 35 - 40 ms ]",range3,"Process")
        for i in range(range1):
            processList.append(random.randrange(2,8))
        for i in range(range2):
            processList.append(random.randrange(20,30))
        for i in range(range3):
            processList.append(random.randrange(35,40))
    elif Assumption  == "3":
        Process = 20
        range1 = percentage(Process,40)
        range2 = percentage(Process,40)
        range3 = percentage(Process,20)
        print("--------------------------------------")
        print("[ Assumption  3 ]",Process,"Process")
        print("[ take 2 - 8 ms ]",range1,"Process")
        print("[ take 20 - 30 ms ]",range2,"Process")
        print("[ take 35 - 40 ms ]",range3,"Process")
        for i in range(range1):
            processList.append(random.randrange(2,8))
        for i in range(range2):
            processList.append(random.randrange(20,30))
        for i in range(range3):
            processList.append(random.randrange(35,40))
    else:
        haveAssumption  = False
       
    if haveAssumption  == True:
        return processList
    else:
        return False









