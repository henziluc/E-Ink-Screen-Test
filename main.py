from layout.dashboard import make_dashbord
from test_data import (
    weather_hourly,
    weather_daily,
    departures_seen,
    departures_etzberg,
    health_data,
    birthday_data
)

def main():

    make_dashbord(weather_hourly, weather_daily, departures_seen, departures_etzberg, health_data, birthday_data)
    
if __name__ == "__main__":
    main()