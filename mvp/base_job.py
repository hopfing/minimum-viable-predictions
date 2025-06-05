from datetime import datetime
from zoneinfo import ZoneInfo

from mvp.config import League, ORDINAL_MAP


class BaseJob:
    def __init__(self, league: str | League, game_date: str = None):
        if isinstance(league, str):
            try:
                league_num = League(league.lower())
            except ValueError:
                raise ValueError(
                    f"Invalid league: {league}. "
                    f"Supported leagues: {', '.join(lg for lg in League)}"
                )
        elif isinstance(league, League):
            league_num = league
        else:
            raise TypeError(
                f"Expected league to be str or League enum, got {type(league)}"
            )

        self.league = league_num
        self.run_datetime = datetime.now(ZoneInfo("America/Chicago"))
        self.run_datetime_iso = self.run_datetime.isoformat()
        self.run_date = self.run_datetime.strftime("%Y-%m-%d")
        try:
            self.game_date = datetime.strptime(
                game_date, "%Y-%m-%d"
            ) if game_date else self.run_date
        except ValueError:
            raise ValueError(
                f"Invalid date format: {game_date}. "
                "Expected format: YYYY-MM-DD"
            )

    def normalize_period(self, raw: str) -> str:
        """
        Normalize period strings to consistent format, replacing any ordinal
        indicators and hyphens.

        ex. "1st-half" -> "first_half", "2nd-quarter" -> "second_quarter"

        :param raw: The raw period string to normalize.
        :return: Normalized period string with ordinals and hyphens replaced
        """

        for ord_key, word in ORDINAL_MAP.items():
            if raw.startswith(ord_key):
                return raw.replace(ord_key, word).replace('-', '_')

        return raw.replace('-', '_')
