flag=0
wait_time=0
turnaround_time=0
arival_time=[]
burst_time=[]
r_time	=[] 

print "Enter number of Processes?"
number = input()
remain=number
for index in range(number):
	print "Enter Processes AT and BT\ \n"
	arival_time.append(input())
	burst_time.append(input())
	r_time.append(burst_time[index])
print"enter the q time"
quantum_time=input()
print"\n\nProcess\t|Turnaround Time|Waiting Time\n\n"

time=0
index=0
while remain!=0:
        if r_time[index] <= quantum_time and r_time[index]>0:
                time=time+r_time[index]
                r_time[index]=0
                flag=1
        elif r_time[index]>0:
                r_time[index]=quantum_time
                time=time+quantum_time
        if r_time[index]==0 and flag==1:
                remain =remain-1
                print "----------------------------------------------"
                print "P\t|\t\t|\t|\t\n",index+1,"              ",time-arival_time[index],"        ",time-arival_time[index]-burst_time[index]
                a=time-arival_time[index]-burst_time[index]
                turnaround_time=turnaround_time+time-arival_time[index]
                flag=0
        if index==number-1:
                index=0
        elif arival_time[index+1]<=time:
                index=index+1
        else:
                index=0
          
print "\nAverge Waiting Time =",wait_time*1.0/number
print "Avg Turnaround Time =",turnaround_time*1.0/number
