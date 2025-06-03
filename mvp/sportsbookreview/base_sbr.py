from dataclasses import dataclass, field
from enum import StrEnum
from typing import List

from mvp.base_job import BaseJob
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
    name: League
    url_path: str
    periods: List[SBRPeriod] = field(default_factory=list)

    def __post_init__(self):
        if not isinstance(self.name, League):
            raise ValueError(f'Invalid league name: {self.name}')
        if not self.url_path:
            raise ValueError('URL path cannot be empty')
        if not self.periods:
            raise ValueError('Periods list cannot be empty')
        for period in self.periods:
            if not isinstance(period, SBRPeriod):
                raise ValueError(f'Invalid period: {period}')


class SBRBase(BaseJob):

    LEAGUES = {
        'mlb': SBRLeague(
            name=League.MLB,
            url_path='mlb-baseball',
            periods=[SBRPeriod.FULL_GAME, SBRPeriod.FIRST_HALF]
        ),
        'wnba': SBRLeague(
            name=League.WNBA,
            url_path='wnba-basketball',
            periods=[
                SBRPeriod.FULL_GAME, SBRPeriod.FIRST_HALF,
                SBRPeriod.SECOND_HALF, SBRPeriod.FIRST_QUARTER,
                SBRPeriod.SECOND_QUARTER, SBRPeriod.THIRD_QUARTER,
                SBRPeriod.FOURTH_QUARTER
            ]
        )
    }

    def __init__(self, league: str, game_date: str = None):
        super().__init__(league, game_date)
        league_key = league.lower()
        if league_key not in self.LEAGUES:
            supported = ", ".join(self.LEAGUES.keys())
            raise ValueError(
                f'Invalid SBR league: {league} - '
                f'Supported leagues: {supported}'
            )
        self.league = league_key
        self.league_config = self.LEAGUES[league_key]
        self.game_date = game_date or self.run_date
