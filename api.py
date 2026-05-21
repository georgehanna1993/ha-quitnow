from datetime import datetime

import requests


class QuitNowApi:
    def __init__(self, nick: str, token: str):
        self.nick = nick
        self.token = token
        self.url = "https://api.quitnow.app/quitnow-server/users/loginV2"

    def get_user_data(self):
        params = {
            "nick": self.nick,
            "os": "w",
            "app": "14005000",
            "t": "f",
            "access": self.token,
        }

        response = requests.get(self.url, params=params, timeout=10)
        response.raise_for_status()

        return response.json()

    def get_stats(self):
        data = self.get_user_data()

        quit_date = datetime.fromtimestamp(
            data["dateLastCigarrete"] / 1000
        )

        total_days_smoke_free = (datetime.now() - quit_date).days

        years = total_days_smoke_free // 365
        months = (total_days_smoke_free % 365) // 30
        days = (total_days_smoke_free % 365) % 30

        days_smoke_free_display = f"{years}y {months}m {days}d"

        cigarettes_per_day = data["cigarretesDay"]
        cigarettes_per_pack = data["cigarretesPacket"]
        price_per_pack = data["pricePacket"]

        cigarettes_avoided = total_days_smoke_free * cigarettes_per_day

        money_saved = (
            cigarettes_avoided / cigarettes_per_pack
        ) * price_per_pack

        minutes_won_back = cigarettes_avoided * 5.7
        days_won_back = minutes_won_back / 1440

        return {
            "nick": data["nick"],
            "days_smoke_free": total_days_smoke_free,
            "days_smoke_free_display": days_smoke_free_display,
            "cigarettes_avoided": cigarettes_avoided,
            "money_saved": round(money_saved, 2),
            "days_won_back": round(days_won_back),
            "currency": data["currency"],
        }
