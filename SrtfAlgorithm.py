
arrival_time=[]
burst_time=[]
remain_time=[]
sum_wait=0
sum_turnaround=0
number=int(input("Enter number of Process : "))
i=0
while i<number:
	print  ("For process ")
	print(i+1)
	arrival_time.append(int(input("Enter arrival time of process :")))
	burst_time.append(int(input("Enter burst time of process :")))
	remain_time.append(burst_time[i])
	i+=1

print ("\n\nProcess\t|Turnaround Time| Waiting Time\n")
remain_time.append(99999)
time=0
remain=0
j=i   	
while remain!=number:
        smallest=j
	i=0;        
	while i<number:
            if arrival_time[i]<=time and remain_time[i]<remain_time[smallest] and remain_time[i]>0:
                smallest=i
            i+=1       
        remain_time[smallest]-=1
        if remain_time[smallest]==0:
            remain+=1
            endTime=time+1
            print (smallest+1)
            
            print(endTime-arrival_time[smallest])
            
            print(endTime-burst_time[smallest]-arrival_time[smallest])
            sum_wait+=endTime-burst_time[smallest]-arrival_time[smallest]
            sum_turnaround+=endTime-arrival_time[smallest]
    	time+=1
print ("\nAverage waiting time = ",sum_wait*1.0/number)
print ("Average Turnaround time = ",sum_turnaround*1.0/5)
