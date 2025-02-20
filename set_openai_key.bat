@echo off
REM filepath: /c:/Users/Zhang/PycharmProjects/Chain-of-Experts/set_openai_key.bat

REM Read the API key from the openaikey.txt file
setlocal enabledelayedexpansion
set "keyfile=c:\Users\Zhang\PycharmProjects\Chain-of-Experts\openaikey.txt"
set "OPENAI_API_KEY=sk-Y8JXzmhnP6Ij7bbP3SAaHsxkUXV4hnXgoAeCWh9lbIQqqK9w"

for /f "delims=" %%i in (!keyfile!) do (
    set "OPENAI_API_KEY=%%i"
)

REM Set the environment variable
setx OPENAI_API_KEY "!OPENAI_API_KEY!"

echo OPENAI_API_KEY has been set.
endlocal
pause