queue=[]
remainb=[]
twait=[]
finish=[]
t=0
number=int(input('Enter the total number of processes: '))
quantum=int (input('Enter quantum time: '))

for i in range(number):
	queue.append([])
	queue[i].append(input('process name: '))
	queue[i].append(int(input('arrival time: ')))
	queue[i].append(int(input('burst time: ')))
	queue[i].append(queue[i][2]) 
	t+=queue[i][2]
	queue[i].append(0)
        queue[i].append(0)
	queue[i].append(0)
	queue[i].append(-1)

queue.sort(key=lambda queue:queue[1])
j=0
now=queue[j][1]
for i in range(number):
	if (queue[i][0]%3==0):
		queue[i][5]=10
while t>0:
	for i in range(number):	#checks auxiliary queue
		if queue[i][7]==now and queue[i][6]!=0:
			t=t-a[i][6] 
			now = queue+a[i][6]
			queue[i][3]=queue[i][3]-queue[i][6]
			queue[i][7]=-1
			queue[i][6]=0
			queue[i][5]=5
			if queue[i][3]==0:
				a[i][4]=now


    	if (queue[j][0]%2)!=0 :
                 if queue[j][3]<=quantum and queue[j][3]!=0 and queue[j][1]<=now:
                        t=t-queue[j][3]
                        now=now+queue[j][3]
                        a[j][4]=now
                        a[x][3]=0
                elif queue[j][3]>=quantum and queue[j][1]<=now
                         queue[j][3]=queue[j][3]-quantum
                         now=now+quantum
                         t=t-quantum
			
	elif (queue[j][0]%2)==0 and queue[j][7]==-1:
		if queue[j][3]<=quantum and [j][3]!=0 and queue[j][1]<=now:
			if queue[j][5]>quantum or queue[j][5]<=p[j][3]:
				t=t-queue[j][3]
				now=now+queue[j][3]
				queue[j][4]=now
				queue[j][3]=0			
			elif queue[j][5]<=quantum:
				t=t-queue[j][5]
				now=now+queue[j][5]
				queue[j][7]=5+now
				queue[j][6]=quantum-queue[j][5]
		elif p[j][3]>quantum and queue[j][3]!=0 and queue[j][1]<=now:
			if queue[j][5]>quantum:
				t=t-quantum
				now=now+quantum
				queue[j][5]=queue[j][5]-quantum
			else:
				t=t-queue[j][5]
				now=now+queue[j][3]
				queue[j][7]=now+5
				queue[j][6]=quantum-queue[j][5]	

			
		if (j+1)<number:
			j=j+1
		else:
			j=0
	
print ('Process       Arrival time      Burst time       waiting time')

for i in range(number):
	print (a[i][0])
	print(' \t\t')
	print(a[i][1])
	print(' \t\t')
	print(a[i][2])
	print(' \t\t')
	print(a[i][4]-a[i][1]-a[i][2])
