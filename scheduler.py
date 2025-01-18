from random import randint

# 5 random processes will be generated
processes = [{
    'pid': i + 1,
    'arrival_time': randint(0, 25),
    'burst_time': randint(1, 15),
    'priority': randint(1, 10),
    'queue': randint(1, 2),
    'waiting_time': 0,
    'turnaround_time': 0
} for i in range(5)]



def priority_scheduling(processes):
    print(
        f"{'Process':<10} {'Arrival Time':<15} {'Burst Time':<13} {'Priority':<10} {'Queue':<7} {'Waiting Time':<15} {'Turnaround Time':<18}")

    processes.sort(key=lambda x: x['priority'])  # Sort processes by priority

    time = 0
    timeline = []
    total_burst_time = 0

    for process in processes:
        if time < process['arrival_time']:
            timeline.append((time, "Idle"))
            time = process['arrival_time']

        timeline.append((time, f"P{process['pid']}"))

        # Calculate waiting time and turnaround time
        waiting_time = time - process['arrival_time']
        turnaround_time = waiting_time + process['burst_time']
        time += process['burst_time']
        total_burst_time += process['burst_time']

        process_label = f"P{process['pid']}".center(5)  # Center-align the outputs
        print(
            f"{process_label:<14} {process['arrival_time']:<14} {process['burst_time']:<13} {process['priority']:<9} {process['queue']:<9} {waiting_time:<17} {turnaround_time:<17}")

        process['waiting_time'] = waiting_time
        process['turnaround_time'] = turnaround_time

    return timeline, processes, total_burst_time, time


def fcfs(processes):
    print(
        f"{'Process':<10} {'Arrival Time':<15} {'Burst Time':<13} {'Priority':<10} {'Queue':<7} {'Waiting Time':<15} {'Turnaround Time':<18}")

    processes.sort(key=lambda x: x['arrival_time'])  # Sort processes by arrival time

    time = 0
    timeline = []
    total_burst_time = 0

    for process in processes:
        if time < process['arrival_time']:
            timeline.append((time, "Idle"))
            time = process['arrival_time']

        timeline.append((time, f"P{process['pid']}"))

        # Calculate waiting time and turnaround time
        waiting_time = time - process['arrival_time']
        turnaround_time = waiting_time + process['burst_time']
        time += process['burst_time']
        total_burst_time += process['burst_time']

        process_label = f"P{process['pid']}".center(5)  # Center-align the outputs
        print(
            f"{process_label:<14} {process['arrival_time']:<14} {process['burst_time']:<13} {process['priority']:<9} {process['queue']:<9} {waiting_time:<17} {turnaround_time:<17}")

        process['waiting_time'] = waiting_time
        process['turnaround_time'] = turnaround_time

    return timeline, processes, total_burst_time, time

def multilevel_scheduling(processes):
    timeline, _, total_burst_time, total_time = fcfs(processes)
    # Print the timeline
    print("\nTimeline:")
    last_time = 0
    for i, (time, event) in enumerate(timeline):
        if event == "Idle":
            print(f"Time {time}: Idle")
        else:
            print(f"Time {time}: {event}")
        last_time = time

    # Calculate average waiting time, turnaround time, CPU utilization percentage
    average_waiting_time = sum(p['waiting_time'] for p in processes) / len(processes)
    average_turnaround_time = sum(p['turnaround_time'] for p in processes) / len(processes)
    cpu_utilization_percentage = (total_burst_time / total_time) * 100

    print(f"\nAverage Waiting Time: {average_waiting_time}")
    print(f"Average Turnaround Time: {average_turnaround_time}")
    print(f"CPU Utilization Percentage: {cpu_utilization_percentage:.2f}%")
    print(f"Burst Time: {total_burst_time}")
    print(f"Total Time: {total_time}")


multilevel_scheduling(processes)
