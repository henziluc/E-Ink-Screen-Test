from dotenv import load_dotenv

from layout.dashboard import make_dashbord
from test_data import (
    weather_hourly,
    weather_daily,
    departures_seen,
    departures_etzberg,
    health_data_Luca,
    health_data_Jojo,
    birthday_data,
    moon_data,
    news_data,
    quote_data
)


def main():
    load_dotenv()
    make_dashbord(weather_hourly,
                  weather_daily,
                  departures_seen,
                  departures_etzberg,
                  health_data_Luca,
                  health_data_Jojo,
                  birthday_data,
                  moon_data,
                  news_data,
                  quote_data)

if __name__ == "__main__":
    main()