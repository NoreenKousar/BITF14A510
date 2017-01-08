process_queue = []
burst=[]
wait=[]
wait_total=0
number = int(input('Enter total number of processes: '))
arrivaltime=(int(input('Enter process arrival time: ')))
for i in range(number):
    process_queue.append([])
    process_queue[i].append(int(input('Enter process number: ')))
    #pbust = 
    burst.append(int(input('Enter process burst time: ')))
j=1
for i in range(number):
    p=i
    for j in range(number):
        if burst[j]<burst[p]:
            p=j
        temp=burst[i]
        burst[i]=burst[p]
        burst[p]=temp
        temp=process_queue[i]
        process_queue[i]=process_queue[p]
        process_queue[p]=temp
wait.append(0)
j=0
for i in range(number):
    wait.append(0)
    for j in range(i):
        wait[i]+=burst[i]
    wait_total+=wait[i]
print ('ProcessNumber\tArrivalTime\tBurstTime\tWaiting Time')
for i in range(number):
    print (process_queue[i])
    print('\t\t')
    print(arrivaltime)
    print('\t\t')
    print(burst[i])
    print('\t\t')
    print(wait[i])
    
print ('Total waiting time: ')
print(wait_total)
print ('Average waiting time: ')
print(wait_total/number)
