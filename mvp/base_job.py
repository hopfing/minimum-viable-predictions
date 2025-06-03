from datetime import datetime
from zoneinfo import ZoneInfo

from mvp.config import League


class BaseJob:
    def __init__(self, league: str, game_date: str = None):
        try:
            League(league.lower())
        except ValueError:
            raise ValueError(
                f"Invalid league: {league}. "
                f"Supported leagues: {', '.join(lg for lg in League)}"
            )
        self.league = league
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
