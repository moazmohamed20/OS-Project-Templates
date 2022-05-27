from multiprocessing.dummy import Process
from typing import Any
from simulator.schedulers.scheduler import Scheduler

class FCFS(Scheduler):
    """First Come First Serve (FCFS) scheduler."""

    def __init__(self):
        super(FCFS, self).__init__()

    def perform_schedule(self):
        """
        We simply sort the processes by the time that they come in by, and
        only change process as the processes finish their execution on the
        CPU.
        """
        self.active = self.q.popleft() if self.q.__len__() > 0 else  None
        return self.active
