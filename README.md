## Stateful System Demo

The demo includes a supervisor script that simulates "RBay express" initialization, process executions, and server restart.

Each run:
- Initializes from persisted state
- Executes deterministic work
- Exits to simulate server shutdown
- Is restarted once by the supervisor

## Run Demo:
```bash
python demo_supervisor.py
```

## Requirements
- Python 3.x (Verified functional on Python 3.9.13)
- python-dateutil

Install:
```bash
pip install python-dateutil
```

RBay Express Project Hub: https://www.notion.so/Rbay-Express-2c69c197ba5e801ba158e2e102a70968