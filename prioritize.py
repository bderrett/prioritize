"""Prioritizes a list of tasks.

Usage:
  prioritize.py mytasks.json

* If the tasks file does not exist, it is created, and the program exits.
* If task preferences don't determine a starting task, you are asked for your preferences among
  pairs of tasks until this is the case. Your input is saved to the tasks file.
* The starting task is printed.
"""
import sys
from collections import deque
from pydantic import BaseModel

class Preference(BaseModel):
    better: str
    worse: str

class Tasks(BaseModel):
    names: list[str]
    preferences: list[Preference]

    def write(self, filename: str):
        with open(filename, 'w') as handle:
            handle.write(self.json(indent=2))

def main(filename: str) -> None:
    try:
        tasks = Tasks.parse_file(filename)
    except FileNotFoundError:
        new_tasks = Tasks(names=[], preferences=[])
        new_tasks.write(filename)
        return
    if not tasks.names:
        print("Add some tasks to the tasks file to get started.")
        return
    start_tasks = deque(tasks.names)
    for preference in tasks.preferences:
        if preference.better in tasks.names and preference.worse in start_tasks:
            start_tasks.remove(preference.worse)
    try:
        while len(start_tasks) > 1:
            task0 = start_tasks.popleft()
            task1 = start_tasks.popleft()
            while 1:
                print(f"Is {task0} more important than {task1}? [y/n]")
                answer = input().lower()
                if answer in ('y', 'n'):
                    task0_better = answer == 'y'
                    break
            preference = Preference(better=task0 if task0_better else task1, worse=task1 if task0_better else task0)
            tasks.preferences.append(preference)
            start_tasks.append(preference.better)
        start_task = start_tasks.pop()
        print(f"Your first task is: {start_task}. Go!")
    finally:
        tasks.write(filename)

try:
    main(sys.argv[1])
except IndexError:
    print(__doc__)
