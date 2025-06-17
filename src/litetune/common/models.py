from dataclasses import dataclass
from typing import Dict, List, Optional


class TrialStatus:
    COMPLETED = "completed"
    FAILED = "failed"
    RUNNING = "running"
    PENDING = "pending"


@dataclass
class TrialResult:
    config: dict
    metrics: dict
    status: TrialStatus = TrialStatus.PENDING
    stopped_early: bool = False
    epochs_run: int = 0


@dataclass
class TrialConfig:
    id: str
    params: dict
    