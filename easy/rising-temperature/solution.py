# Solution to the 'Rising Temperature' problem.

import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather = weather.sort_values('recordDate')
    is_consecutive = weather['recordDate'].diff().dt.days == 1
    temp_increased = weather['temperature'] > weather['temperature'].shift(1)
    warmer = is_consecutive & temp_increased
    return weather[warmer][['id']]