@echo off
REM Navigate to the Automation directory
cd /d C:\Git

REM Activate the virtual environment
call yossi\Scripts\activate

REM Run pytest with Allure report generation
pytest -m happyflow --alluredir allure-results

REM Serve the Allure report
allure serve allure-results

REM Deactivate the virtual environment
deactivate

REM Pause to keep the command prompt open
pause
