"""Placeholder: JobType taxonomy (to be implemented later)."""
from enum import Enum


class JobType(str, Enum):
    TASKLET = "tasklet"
    WORKFLOW = "workflow"
    STREAM = "stream"
    MISSION = "mission"
    BATCH = "batch"
    CLUSTER = "cluster"
