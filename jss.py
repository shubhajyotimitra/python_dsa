from collections import deque

class Job:
    def __init__(self, job_id, arrival_time, burst_time, priority=0):
        self.job_id = job_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.remaining_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

    def __repr__(self):
        return f"Job({self.job_id}, AT={self.arrival_time}, BT={self.burst_time}, P={self.priority})"


class JobScheduler:
    def __init__(self, jobs):
        self.jobs = sorted(jobs, key=lambda j: j.arrival_time)

    # 1. First Come First Serve (FCFS)
    def fcfs(self):
        time = 0
        print("\n🔹 FCFS Scheduling")
        for job in self.jobs:
            time = max(time, job.arrival_time)
            job.completion_time = time + job.burst_time
            job.turnaround_time = job.completion_time - job.arrival_time
            job.waiting_time = job.turnaround_time - job.burst_time
            time += job.burst_time
            print(f"{job.job_id}: CT={job.completion_time}, TAT={job.turnaround_time}, WT={job.waiting_time}")

    # 2. Shortest Job First (Non-preemptive)
    def sjf(self):
        print("\n🔹 SJF Scheduling")
        time, completed = 0, []
        jobs = self.jobs[:]
        while jobs:
            available = [j for j in jobs if j.arrival_time <= time]
            if not available:
                time = jobs[0].arrival_time
                continue
            job = min(available, key=lambda j: j.burst_time)
            time += job.burst_time
            job.completion_time = time
            job.turnaround_time = job.completion_time - job.arrival_time
            job.waiting_time = job.turnaround_time - job.burst_time
            print(f"{job.job_id}: CT={job.completion_time}, TAT={job.turnaround_time}, WT={job.waiting_time}")
            jobs.remove(job)
            completed.append(job)

    # 3. Round Robin Scheduling
    def round_robin(self, quantum=2):
        print("\n🔹 Round Robin Scheduling (Quantum =", quantum, ")")
        time, q = 0, deque(self.jobs)
        while q:
            job = q.popleft()
            if job.remaining_time > 0:
                exec_time = min(quantum, job.remaining_time)
                time = max(time, job.arrival_time) + exec_time
                job.remaining_time -= exec_time
                if job.remaining_time == 0:
                    job.completion_time = time
                    job.turnaround_time = job.completion_time - job.arrival_time
                    job.waiting_time = job.turnaround_time - job.burst_time
                    print(f"{job.job_id}: CT={job.completion_time}, TAT={job.turnaround_time}, WT={job.waiting_time}")
                else:
                    q.append(job)

    # 4. Priority Scheduling (Non-preemptive)
    def priority_scheduling(self):
        print("\n🔹 Priority Scheduling")
        time, completed = 0, []
        jobs = self.jobs[:]
        while jobs:
            available = [j for j in jobs if j.arrival_time <= time]
            if not available:
                time = jobs[0].arrival_time
                continue
            job = min(available, key=lambda j: j.priority)
            time += job.burst_time
            job.completion_time = time
            job.turnaround_time = job.completion_time - job.arrival_time
            job.waiting_time = job.turnaround_time - job.burst_time
            print(f"{job.job_id}: CT={job.completion_time}, TAT={job.turnaround_time}, WT={job.waiting_time}")
            jobs.remove(job)
            completed.append(job)


# ----------------------- RUN SIMULATION -----------------------

if __name__ == "__main__":
    jobs = [
        Job("J1", arrival_time=0, burst_time=5, priority=2),
        Job("J2", arrival_time=1, burst_time=3, priority=1),
        Job("J3", arrival_time=2, burst_time=8, priority=3),
        Job("J4", arrival_time=3, burst_time=6, priority=2),
    ]

    scheduler = JobScheduler(jobs)
    scheduler.fcfs()
    scheduler.sjf()
    scheduler.round_robin(quantum=2)
    scheduler.priority_scheduling()
