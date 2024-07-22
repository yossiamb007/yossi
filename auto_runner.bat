@echo off
REM Navigate to the Automation directory
cd /d C:\Users\Yossi Ambelo\Jenkins_Agent\workspace\SanityAutomation

python -m venv venv

REM Activate the virtual environment
call venv\Scripts\activate

REM Install requirements
pip install -r requirements.txt

REM Run pytest with Allure report generation
pytest --alluredir allure-results

REM Serve the Allure report
allure serve allure-results

REM Deactivate the virtual environment
deactivate

REM Remove the virtual environment directory
rmdir /s /q venv

REM Pause to keep the command prompt open
pause