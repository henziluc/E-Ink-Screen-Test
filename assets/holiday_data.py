import pandas as pd

holidays_data = [['Flims', '12.09.2026', '14.09.2026'],
            ['Catania', '13.11.2026','16.11.2026'],
            ['Austria', '21.12.2026', '02.01.2027'],
            ['South Africa', '22.01.2027', '11.02.2027']]

holiday = pd.DataFrame(holidays_data, columns=['location', 'start_date', 'end_date'])

holiday['start_date'] = pd.to_datetime(
    holiday['start_date'],
    format='%d.%m.%Y'
)

holiday['end_date'] = pd.to_datetime(
    holiday['end_date'],
    format='%d.%m.%Y'
)

holiday = holiday.sort_values('start_date').reset_index(drop=True)