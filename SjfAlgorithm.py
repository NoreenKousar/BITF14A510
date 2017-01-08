burst_time=[]
wating_time=[]
turnedaround_time=[]
total=0
processes_no=[]
pos=0
index=0
index2=0
temp1=0
temp2=0
print "enter the no of processes"
number=input()
print "enter the burst time"
for index in range(number):
    print"P:",index+1
    burst_time.append(input())
    processes_no.append(index+1)
for index in range(number):
    pos=index
    for index2 in range(number):
        if burst_time[index2]<burst_time[pos]:
            pos=index2
        temp1=burst_time[index]
        burst_time[index]=burst_time[pos]
        burst_time[pos]=temp1
        
        temp2=processes_no[index]
        processes_no[index]=processes_no[pos]
        burst_time=temp2

wating_time.append(0)
for index in number:
    wating_time.append(0)
    for index2 in index:
        wating_time[index]=wating_time[index]+burst_time[index2]
    total=total+wating_time[index]
averge_wating_time=total/number
total=0
print "\nProcesses\t    Burst Time    \tWating Time\tTurnaround Time"
for index in number:
    turnedaround_time[index]=burst_time[index]+wating_time[index]
    total=total+turnedaround_time[index]
    print "\nP\t\t\t\t\t\t",processes_no[index],burst_time[index],wating_time[index],turnedaround_time[index]
average_turnedaround_time=total/number
print "\n\nAverage Waiting Time",averge_wating_time
print "\nAverage Turnaround Time=\n",average_turnedaround_time
