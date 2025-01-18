from random import randint
def FCFS(burst_time):
    print("Process     Arrival Time     Burst Time    Waiting Time    Turnaround Time   Priority    Queue")
    i = 0
    arrival_time = [randint(0, 25) for _ in burst_time]
    burst_time = [randint(0, 25) for _ in burst_time]
    waiting_time = 0
    turnaround_time = 0
    empty1 = []
    empty2 = []
    while i < len(burst_time):
        turnaround_time += burst_time[i]
        print("  P" + str(i + 1) + "\t\t\t" + str(arrival_time[i]) + "\t\t\t\t" + str(burst_time[i]) + "\t\t\t\t"
              + str(waiting_time) + "\t\t\t\t" + str(turnaround_time))
        empty1.append(waiting_time)
        empty2.append(turnaround_time)
        waiting_time += burst_time[i]
        i += 1
    return empty1, empty2


np = int(input("Enter number of processes: "))
burst_times = []
for i in range(np):
    burst_times.append(int(input("Enter burst time for process: " + str(i + 1) + ":")))

lst = FCFS(burst_times)
print("Average Waiting Time: " + str(sum(lst[0]) / len(lst[0])))
print("Average Turnaround Time: " + str(sum(lst[1]) / len(lst[1])))