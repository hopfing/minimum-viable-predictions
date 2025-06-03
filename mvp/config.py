from enum import StrEnum, auto

ORDINAL_MAP = {
    "1st": "first",
    "2nd": "second",
    "3rd": "third",
    "4th": "fourth"
}


class League(StrEnum):
    """
    Simple enum to ensure alignment of league names across different sources
    and ETL tasks. Using auto() with StrEnum returns lowercase strings

    e.g. League.MLB -> 'mlb'
    """
    MLB = auto()
    WNBA = auto()
