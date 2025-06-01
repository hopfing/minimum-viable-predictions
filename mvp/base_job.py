from mvp.config import League


class BaseJob:
    def __init__(self, league: str, game_date: str):
        try:
            League(league.lower())
        except ValueError:
            raise TypeError(
                f"Invalid league: {league}. "
                f"Supported leagues: {', '.join(lg for lg in League)}"
            )
        self.league = league
        self.game_date = game_date
