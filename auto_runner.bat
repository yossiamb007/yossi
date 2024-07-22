@echo off
REM Navigate to the Automation directory
cd /d C:\Users\Yossi Ambelo\Jenkins_Agent\workspace\SanityAutomation

python -m venv venv

REM Activate the virtual environment
call venv\Scripts\activate

REM Install requirements
pip install -r requirements.txt

REM Get the current date in YYYY-MM-DD format
for /f "tokens=2 delims==" %%i in ('wmic os get localdatetime /value') do set datetime=%%i
set allure-results=%datetime:~0,4%-%datetime:~4,2%-%datetime:~6,2%

REM Create a folder with the current date as the name
mkdir %allure-results%

REM Run pytest with Allure report generation
pytest --alluredir %allure-results%

REM Serve the Allure report
allure serve %allure-results%

REM Deactivate the virtual environment
deactivate

REM Remove the virtual environment directory
rmdir /s /q venv

REM Pause to keep the command prompt open
pause