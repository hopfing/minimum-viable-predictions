from enum import StrEnum, auto


class League(StrEnum):
    """
    Simple enum to ensure alignment of league names across different sources
    and ETL tasks.
    """
    MLB = auto()
