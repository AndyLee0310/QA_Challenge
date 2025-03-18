# QA Challenge

This project focuses on automating and verifying critical functionalities using Appium/Selenium/Pytest to ensure stability and performance across different test scenarios. The project is designed specifically for Android devices and API testing.

Test Case Approach

- UI Testing: Validates UI elements, user interactions, and expected behaviors on Android devices.
- API Testing: Verifies API responses, data consistency, and backend communication.

The testcase design follows a standard structure, including Test Objective, Preconditions, Execution Steps, and Expected Results, to enhance test coverage and execution efficiency.


## Environment

1. Java 1.8.0_381
2. Python 3.11.11
3. allure 2.21.0
4. appium 2.2.1
5. Android Device (for UI testing)

## Setup guide

1. Clone project

    ```shell
    git clone https://github.com/AndyLee0310/QA_Challenge
    cd QA_Challenge
    ```

2. Create virtual environment(Optional)

   ```shell
   python -m venv venv

   source venv/bin/activate  # MacOS/Linux
   venv\Scripts\activate  # Windows
   ```

3. Install dependency packages

   ```shell
   pip install -r requirement.txt
   ```

4. Run tests    
    -m : Run tests with markers    
    -k : Run tests with keywords    

   ```shell
   # Run all tests
   python run.py

   # Run the test marked 'task1'
   python run.py -m 'task1'

   # Run the test named 'test_check_weather_for_day_nine'
   python run.py -k 'test_check_weather_for_day_nine'
   ```

5. Get the test report

   The report path is at `report/complete.html`
