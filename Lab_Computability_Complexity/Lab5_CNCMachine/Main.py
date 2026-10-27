#Not my code (Lab Example)

# Define jobs, machines, operators
jobs = [
    {"job": "J1", "machine": "M1", "time": 30},
    {"job": "J2", "machine": "M2", "time": 25},
    {"job": "J3", "machine": "M3", "time": 45},
    {"job": "J4", "machine": "M1", "time": 80},
    {"job": "J5", "machine": "M2", "time": 60},
]

machines = {"M1": 0, "M2": 0, "M3": 0}  # available from time 0
operators = {"O1": 0}           		# available from time 0

schedule = []

for job in jobs:
    machine = job["machine"]
    
    # Find the operator that is available the earliest
    available_operator = min(operators, key=lambda x: operators[x])
    
    # Determine start time (max of machine and operator availability)
    start_time = max(machines[machine], operators[available_operator])
    end_time = start_time + job["time"]
    
    # Update availability
    machines[machine] = end_time
    operators[available_operator] = operators[available_operator] + 10
    
    # Save schedule
    schedule.append({
        "job": job["job"],
        "machine": machine,
        "operator": available_operator,
        "start": start_time,
        "end": end_time
    })

# Print schedule
for s in schedule:
    print(f"Job {s['job']} -> Machine: {s['machine']}, Operator: {s['operator']}, "
          f"Start: {s['start']}, End: {s['end']}")

# Total runtime
total_runtime = max([s["end"] for s in schedule])
print(f"\nTotal runtime: {total_runtime} minutes")