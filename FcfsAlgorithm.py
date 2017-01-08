
process_queue = []

total_waiting = 0

number = int(input('Enter number of processes: '))

for i in range(number):

    process_queue.append([])

    process_queue[i].append(input('Enter process name: '))

    process_queue[i].append(int(input('Enter process arrival time: ')))

    total_waiting += process_queue[i][1]
    process_queue[i].append(int(input('Enter process burst time: ')))

process_queue.sort(key = lambda process_queue:process_queue[1])


print ('Process Name\tArrival Time\tBurst Time')

for i in range(number):
    
    print (process_queue[i][0])
    print ('     ')  
    print (process_queue[i][1])
    print ('     ')
    print(process_queue[i][2])
    

print ('Total waiting time: ')
print(total_waiting)

print ('Average waiting time: ')
print(total_waiting/number)
