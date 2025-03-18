import requests
import allure
import pytest
import json
from datetime import datetime, timedelta

BASE_URL = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php"
PARAMS = {"dataType": "fnd", "lang": "tc"}

@allure.feature("QA Challenge")
class TestTask2():

    @allure.story("task_2")
    @allure.title("[task 2]Extract the relative humidity for the day after tomorrow")
    @pytest.mark.task2
    def test_get_the_relative_humidity_for_the_day_after_tomorrow(self):

        with allure.step("Send an API request"):
            response = requests.get(BASE_URL, params=PARAMS)
            assert response.status_code == 200

        with allure.step("Parse the JSON data from the API response"):
            response_json = response.json()
            allure.attach(json.dumps(response_json, ensure_ascii=False, indent=2), "API response JSON", attachment_type=allure.attachment_type.JSON)

        with allure.step("Calculate the date for the day after tomorrow"):
            today = datetime.now()
            day_after_tomorrow = today + timedelta(days=2)
            day_after_tomorrow_str = day_after_tomorrow.strftime('%Y%m%d')
            allure.attach(day_after_tomorrow_str, "The date for the day after tomorrow", attachment_type=allure.attachment_type.TEXT)


        with allure.step(f"Find the weather forecast for the day after tomorrow ({day_after_tomorrow_str})"):
            forecasts = response_json.get('weatherForecast', [])
            forecast_for_day_after_tomorrow = next(
                (forecast for forecast in forecasts if forecast.get('forecastDate') == day_after_tomorrow_str),
                None
            )
            assert forecast_for_day_after_tomorrow is not None
            allure.attach(json.dumps(forecast_for_day_after_tomorrow, ensure_ascii=False, indent=2), f"The weather forecast for the day after tomorrow ({day_after_tomorrow_str})", attachment_type=allure.attachment_type.JSON)

        with allure.step("Extract the relative humidity data for the day after tomorrow"):
            min_relative_humidity = forecast_for_day_after_tomorrow.get("forecastMinrh", {}).get("value")
            max_relative_humidity = forecast_for_day_after_tomorrow.get("forecastMaxrh", {}).get("value")

            assert min_relative_humidity is not None
            assert max_relative_humidity is not None

            allure.attach(f"Relative humidity for the day after tomorrow: {min_relative_humidity}-{max_relative_humidity}%", attachment_type=allure.attachment_type.TEXT)
