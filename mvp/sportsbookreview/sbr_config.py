from dataclasses import dataclass, field
from enum import StrEnum
from typing import List, Mapping

from mvp.config import League


class SBRPeriod(StrEnum):
    FULL_GAME = 'full-game'
    FIRST_HALF = '1st-half'
    SECOND_HALF = '2nd-half'
    FIRST_QUARTER = '1st-quarter'
    SECOND_QUARTER = '2nd-quarter'
    THIRD_QUARTER = '3rd-quarter'
    FOURTH_QUARTER = '4th-quarter'


@dataclass(frozen=True)
class SBRLeague:
    """
    Encapsulates SBR-specific information for a single league.
    """
    url_path: str
    periods: List[SBRPeriod] = field(default_factory=list)

    def __post_init__(self):
        if not self.url_path:
            raise ValueError('URL path cannot be empty')
        if not self.periods:
            raise ValueError('Periods list cannot be empty')
        for period in self.periods:
            if not isinstance(period, SBRPeriod):
                raise ValueError(f'Invalid period: {period}')


LEAGUES: Mapping[League, SBRLeague] = {
    League.MLB: SBRLeague(
            url_path='mlb-baseball',
            periods=[SBRPeriod.FULL_GAME, SBRPeriod.FIRST_HALF]
        ),
    League.WNBA: SBRLeague(
        url_path='wnba-basketball',
        periods=[
            SBRPeriod.FULL_GAME, SBRPeriod.FIRST_HALF,
            SBRPeriod.SECOND_HALF, SBRPeriod.FIRST_QUARTER,
            SBRPeriod.SECOND_QUARTER, SBRPeriod.THIRD_QUARTER,
            SBRPeriod.FOURTH_QUARTER
        ]
    ),
}
