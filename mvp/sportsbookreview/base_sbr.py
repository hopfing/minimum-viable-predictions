from typing import Union

from mvp.base_job import BaseJob
from mvp.config import League
from .sbr_config import LEAGUES


class SBRBase(BaseJob):

    def __init__(self, league: Union[str, League], game_date: str = None):
        super().__init__(league, game_date)
        if self.league not in LEAGUES:
            supported = ", ".join(LEAGUES.keys())
            raise ValueError(
                f'Invalid SBR league: {league} - '
                f'Supported leagues: {supported}'
            )
        self.league_config = LEAGUES[self.league]
