from collections import Counter

# Sample log file (each line has 'timestamp - event')
log_data = """2023-12-31 10:00:00 - EVENT_A
2023-12-31 10:05:00 - EVENT_B
2023-12-31 10:10:00 - EVENT_A
2023-12-31 10:15:00 - EVENT_C
2023-12-31 10:20:00 - EVENT_B"""

# Parse log lines and extract events
events = [line.split(" - ")[1] for line in log_data.splitlines()]

# Count events
event_counts = Counter(events)

print(event_counts)  # Output the dictionary
