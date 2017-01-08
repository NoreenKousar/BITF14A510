process_queue=[]
finish=[]
total_wait=[]
remainburst=[]
total=0
number=int (input('Enter the total number of processes: '))
quantum=int (input('Enter time quantum: '))

for i in range(number):
	process_queue.append([])
	process_queue[i].append(input('enter process name: '))
	process_queue[i].append(int(input('enter arrival time: ')))
	process_queue[i].append(int(input('enter burst time: ')))
	process_queue[i].append(process_queue[i][2]) #remaining burst time
	total+=process_queue[i][2] #total burst time
	process_queue[i].append(0) #finish time

process_queue.sort(key=lambda process_queue:process_queue[1])

j=0
now=process_queue[j][1]
while total>0:
	if process_queue[j][3]<quantum and process_queue[j][3]!=0 and process_queue[j][1]<=now:
		total=total-process_queue[j][3]
		now=now+process_queue[j][3]
		process_queue[j][4]=now
		process_queue[j][3]=0
	elif process_queue[j][3]>=quantum and process_queue[j][1]<=now:
		process_queue[j][3]=process_queue[j][3]-quantum
		now=now+quantum
		total=total-quantum
		if process_queue[j][3]==0:
			process_queue[j][4]=now
	if (j+1)<number:
		j=j+1
	else:
		j=0

print ('Process          Arrival time        Burst time        waiting time')
for i in range(number):
	print (process_queue[i][0])
	print(' \t\t')
	print(process_queue[i][1])
	print(' \t\t')
	print(process_queue[i][2])
	print(' \t\t')
	print(process_queue[i][4]-process_queue[i][1]-process_queue[i][2])
