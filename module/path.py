# Path-related information
import os

BASE = os.path.dirname(os.path.dirname(__file__))
REPORT = os.path.join(BASE, 'report')
SCREENSHOT = os.path.join(REPORT, 'screenshots')
ALLURE_RESULTS = os.path.join(REPORT, 'allure-results')
ALLURE_REPORT = os.path.join(REPORT, 'allure-report')