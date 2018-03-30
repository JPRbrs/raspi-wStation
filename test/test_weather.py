import json

import mock
import pytest

from weather import (
    get_forecast,
    get_weather,
)
from test.example_response import mock_response

WEATHER_MOCK = json.loads(mock_response)


class TestGetWeather(object):
    @mock.patch('pywapi.get_weather_from_weather_com')
    def test_get_weather(self, get_weather_from_weather_com):
        get_weather_from_weather_com.return_value = WEATHER_MOCK
        weather = get_weather()

        weather['feels_like'] ==\
            WEATHER_MOCK['current_conditions']['feels_like']
        weather['out_temperature'] ==\
            WEATHER_MOCK['current_conditions']['temperature']
        weather['out_humidity'] ==\
            WEATHER_MOCK['current_conditions']['humidity']
        weather['uv_index'] ==\
            WEATHER_MOCK['current_conditions']['uv']['index']
        weather['wind_direction'] ==\
            WEATHER_MOCK['current_conditions']['wind']['text']
        weather['wind_speed'] ==\
            WEATHER_MOCK['current_conditions']['wind']['speed']
        weather['out_conditions'] ==\
            WEATHER_MOCK['current_conditions']['text'].lower()

    @pytest.mark.parametrize('days', [0, 4])
    def test_get_forecast_raises_exception(self, days):
        with pytest.raises(ValueError) as exc:
            get_forecast(days)
            assert exc.message == 'Days must be 1, 2 or 3'

    @mock.patch('pywapi.get_weather_from_weather_com')
    def test_get_forecast(self, get_weather_from_weather_com):
        get_weather_from_weather_com.return_value = WEATHER_MOCK

        days_from_today = 1  # Only testing one day from today
        forecast = get_forecast(days_from_today)
        expected = WEATHER_MOCK['forecasts'][days_from_today]

        assert forecast['date'] == expected['date']
        assert forecast['high'] == expected['high']
        assert forecast['low'] == expected['low']
        assert forecast['sunrise'] == expected['sunrise']
        assert forecast['sunset'] == expected['sunset']
        assert forecast['day_text'] == expected['day']['text']
        assert forecast['day_humidity'] == expected['day']['humidity']
        assert forecast['day_precip'] == expected['day']['chance_precip']
        assert forecast['day_wind'] == expected['day']['wind']['gust']
        assert forecast['night_text'] == expected['night']['text']
        assert forecast['night_humidity'] == expected['night']['humidity']
        assert forecast['night_precip'] == expected['night']['chance_precip']
        assert forecast['night_wind'] == expected['night']['wind']['gust']
