# Generate the allure report and merge it into a standalone html file
import os
import logging
import allure_combine
from . import path

def output_allure_html_report():

    # If the report folder does not exist, create it
    if not os.path.exists(path.REPORT):
        os.makedirs(path.REPORT)
        logging.info(f"'{path.REPORT}' 資料夾已創建")
    else:
        logging.info(f"'{path.REPORT}' 資料夾已存在")

    # Generate an html report
    os.system(f'allure generate {path.ALLURE_RESULTS} -o {path.ALLURE_REPORT} --clean')

    # Merge the allure report into a standalone html file
    allure_combine.combine_allure(path.ALLURE_REPORT)

    # Move `complete.html` to the `report` folder
    os.system(f'mv {path.ALLURE_REPORT}/complete.html {path.REPORT}')

    # Delete the `allure-report` folder
    os.system(f'rm -rf {path.ALLURE_REPORT}')
