import subprocess
import time

RESTARTS = 2

for cycle in range(RESTARTS):
    print(f"\n=== START CYCLE {cycle + 1} ===")
    subprocess.run(["python", "demo_rbay.py"])
    print("PROCESS EXITED. SIMULATING DOWNTIME...\n")
    time.sleep(2)

print("DEMO FINISHED")
