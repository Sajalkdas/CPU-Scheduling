from random import randint
from collections import deque

# Define the Process Control Block (PCB)
class Process:
    def __init__(self, job_number, arrival_time, burst_time, priority, queue):
        self.job_number = job_number
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.priority = priority
        self.queue = queue
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0

    def __repr__(self):
        return (f"Job {self.job_number}, Arrival {self.arrival_time}, Burst {self.burst_time}, "
                f"Priority {self.priority}, Queue {self.queue}, Remaining {self.remaining_time}")

def generate_processes(n):
    return [Process(i+1, randint(0, 25), randint(1, 15), randint(1, 10), randint(1, 2)) for i in range(n)]

def sjf_scheduling(queue, current_time):
    queue.sort(key=lambda p: (p.remaining_time, p.arrival_time))
    process = queue.pop(0)
    process.completion_time = current_time + process.remaining_time
    process.turnaround_time = process.completion_time - process.arrival_time
    process.waiting_time = process.turnaround_time - process.burst_time
    current_time += process.remaining_time
    process.remaining_time = 0
    return process, current_time

def rr_scheduling(queue, current_time, time_quantum):
    process = queue.popleft()
    if process.remaining_time > time_quantum:
        current_time += time_quantum
        process.remaining_time -= time_quantum
        queue.append(process)
    else:
        current_time += process.remaining_time
        process.remaining_time = 0
        process.completion_time = current_time
        process.turnaround_time = process.completion_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time
    return process, current_time

def multilevel_scheduling(processes, time_quantum):
    current_time = 0
    sjf_queue = []
    rr_queue = deque()
    timeline = []
    idle_state = False

    while processes or sjf_queue or rr_queue:
        # Add new arrivals to respective queues
        for process in list(processes):
            if process.arrival_time <= current_time:
                if process.queue == 1:
                    sjf_queue.append(process)  # Queue 1
                else:
                    if rr_queue and rr_queue[0].queue == 1:  # Check if any process in RR queue is from Queue 1
                        idle_state = False
                        timeline.append(f"Time {current_time}: CPU stops being idle")
                        process, current_time = rr_scheduling(rr_queue, current_time, time_quantum)
                        if process.remaining_time == 0:
                            timeline.append(f"Time {current_time}: Process {process.job_number} completed RR")
                        else:
                            timeline.append(f"Time {current_time}: Process {process.job_number} executed for {time_quantum} in RR")
                    else:
                        rr_queue.appendleft(process)  # Queue 2 has higher priority
                        timeline.append(f"Time {current_time}: Process {process.job_number} arrived and added to Queue {process.queue}")
                processes.remove(process)

        # Execute SJF if available
        if sjf_queue:
            if idle_state:
                idle_state = False
                timeline.append(f"Time {current_time}: CPU stops being idle")
            process, current_time = sjf_scheduling(sjf_queue, current_time)
            timeline.append(f"Time {current_time}: Process {process.job_number} completed SJF")
        elif rr_queue:
            if idle_state:
                idle_state = False
                timeline.append(f"Time {current_time}: CPU stops being idle")
            process, current_time = rr_scheduling(rr_queue, current_time, time_quantum)
            if process.remaining_time == 0:
                timeline.append(f"Time {current_time}: Process {process.job_number} completed RR")
            else:
                timeline.append(f"Time {current_time}: Process {process.job_number} executed for {time_quantum} in RR")
        else:
            if not idle_state:
                timeline.append(f"Time {current_time}: CPU is idle")
                idle_state = True
            current_time += 1

    return timeline

# Generate 5 random processes
processes = generate_processes(5)
time_quantum = 4  # Define a time quantum for Round Robin

# Print process details table
print("Process Details:")
print(f"{'Process':<10} {'Arrival Time':<15} {'Burst Time':<13} {'Priority':<10} {'Queue':<7}")
for process in processes:
    print(f"{process.job_number:<10} {process.arrival_time:<15} {process.burst_time:<13} {process.priority:<10} {process.queue:<7}")

# Run the multilevel scheduling
timeline = multilevel_scheduling(processes, time_quantum)

# Print the timeline
print("\nTimeline:")
for event in timeline:
    print(event)
