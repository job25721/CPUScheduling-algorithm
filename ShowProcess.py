import matplotlib.pyplot as plt

def showProcessResultTable(Process,wPerProcess,turnPerProcess,res,isSJF):
    # Headers = ["Process  |","Brust Time  |","Waiting Time  |","Turn Around Time  |"]
    # if isSJF == True:
    #     Headers = ["Process(Sorted)|","Brust Time  |","Waiting Time  |","Turn Around Time  |"]
    # text = "P"
    # print("------------------------------------------------------------")
    # print("{0:>0} {1:>14} {2:>13} {3:>17}".format(Headers[0],Headers[1],Headers[2],Headers[3]))
    # print("------------------------------------------------------------")
    # format_type = "{0:>0} {1:>15} {2:>14} {3:>17}"
    # for i in range(len(Process)):
    #     if i+1 >= 10 :
    #         format_type = "{0:>0} {1:>14} {2:>14} {3:>17}"
    #     P = text + str(i+1)
    #     print(format_type.format(P,Process[i],wPerProcess[i],turnPerProcess[i]))

    print("_____________________________________________________________")
    print("Average waiting time = {:.3f} ms".format(res[0]))
    print("Average turn around time = {:.3f} ms".format(res[1]))
    print("_____________________________________________________________")


def showProcessResultGraph(FCFS,SJF,RRS,n):
    x = []
    for i in range(n):
        x.append(i+1)
    plt.plot(x,FCFS,label="FCFS")
    plt.plot(x,SJF,label="SJF")
    plt.plot(x,RRS,label="RRS")
    plt.title("CPU Scheduling Algorithm")
    plt.xlabel("Random n times")
    plt.ylabel("Average waiting time")
    plt.legend()
    plt.show()
 




