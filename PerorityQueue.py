processes=[]
burst_time=[]
system_or_user_processes=[]
wating_time=[]
turnedaround_time=[]
temp=0
wating_time_avg=0
turandaround_time_avg=0
no_of_processes=0
print "Enter the no of processes"
no_of_processes=input()
for index in range(no_of_processes):
    #processes[index]=index
    print "Enter the Burst Time of Process --- ", index
    burst_time.append(input())
    print "System/User Process (0/1) ? --- "
    system_or_user_processes.append(input())
for index in range(no_of_processes):
    for index2 in range(no_of_processes):
        if system_or_user_processes[index]>system_or_user_processes[index2]:
            temp=processes[index]
            processes[index]=processes[index2]
            processes[index2]=burst_time[index]
            burst_time[index]=temp
            temp=system_or_user_processes[index]
            system_or_user_processes[index]=system_or_user_processes[index2]
            system_or_user_processes[index2]=temp


    
wating_time_avg=wating_time.append(0)
turandaround_time_avg=turnedaround_time.append(0)
turnedaround_time[0]=burst_time[0]
for index in range(no_of_processes):
    wating_time[index]=wating_time.append[index-1]+burst_time[index]
    wating_time_avg=wating_time_avg+wating_time[index]
    turandaround_time_avg=turandaround_time_avg+turnedaround_time[index]
print "\nPROCESS\t\t SYSTEM/USER PROCESS \tBURST TIME\tWAITING TIME\tTURNAROUND TIME"
for index in range(no_of_processes):
    print"\n \t\t  \t\t  \t\t  \t\t  ",processes[i],system_or_user_processes[index],burst_time[index],wating_time[index],turnedaround_time[index]
print "\nAverage Waiting Time is --- ",wating_time_avg/no_of_processes
print "\nAverage Turnaround Time is --- ",turandaround_time_avg/no_of_processes

