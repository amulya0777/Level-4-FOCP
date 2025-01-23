import sys
import os
from tabulate import tabulate

print("Usage: python timing.py <timing_file> <drivers_file>")

if len(sys.argv) != 3:
    print("Usage: python timing.py <timing_file> <drivers_file>")
    sys.exit(1)

timing_file = sys.argv[1]
drivers_file = sys.argv[2]

if not os.path.exists(timing_file):
    print(f"Timing file {timing_file} does not exist.")
    print("Usage: python timing.py <timing_file> <drivers_file>")
    sys.exit(1)

if not os.path.exists(drivers_file):
    print(f"Drivers file {drivers_file} does not exist.")
    print("Usage: python timing.py <timing_file> <drivers_file>")
    sys.exit(1)

# read driver details
driver_details = {}
with open(drivers_file, "r") as file:
    for line in file:
        parts = line.strip().split(",")
        if len(parts) == 4:
            code, name, team = parts[1], parts[2], parts[3]
            driver_details[code] = {"name": name, "team": team}

# process timing file
with open(timing_file, "r") as file:
    lines = file.readlines()

if not lines:
    print("Timing file is empty.")
    sys.exit(1)

# race name
race_name = lines[0].strip()
print(f"Race Name: {race_name}")

lap_times = {}
fastest_lap = None
fastest_driver = None
total_lap_time = 0
total_laps = 0

# process lap times
for line in lines[1:]:
    code = line[:3]
    try:
        time = float(line[3:])
    except ValueError:
        continue

    if code not in lap_times:
        lap_times[code] = []
    lap_times[code].append(time)

    total_lap_time += time
    total_laps += 1

    if fastest_lap is None or time < fastest_lap:
        fastest_lap = time
        fastest_driver = code

# driver averages and fastest lap
driver_data = []
for code, times in lap_times.items():
    avg_time = sum(times) / len(times)
    fastest_driver_lap = min(times)
    driver_info = driver_details.get(code, {"name": "Unknown", "team": "Unknown"})
    driver_data.append([
        code,
        driver_info["name"],
        driver_info["team"],
        f"{avg_time:.3f}",
        f"{fastest_driver_lap:.3f}"
    ])

# sort the driver data in descending order.
driver_data.sort(key=lambda x: float(x[4]), reverse=True)

# overall average lap time
if total_laps > 0:
    overall_average = total_lap_time / total_laps
else:
    overall_average = None

# displaying the tables
print("\nDriver Performance (Fastest Lap in Descending Order):")
print(tabulate(driver_data, headers=["Code", "Name", "Team", "Average Lap Time", "Fastest Lap"], tablefmt="grid"))

if fastest_driver:
    driver_info = driver_details.get(fastest_driver, {"name": "Unknown", "team": "Unknown"})
    print(f"\nOverall Fastest Lap: {fastest_lap:.3f} by {fastest_driver} ({driver_info['name']}, {driver_info['team']})")

if overall_average:
    print(f"\nOverall Average Lap Time: {overall_average:.3f}")
else:
    print("\nNo lap times recorded.")
