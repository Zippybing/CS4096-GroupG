@echo off
title Running Windows Setup Script
reg query "hkcu\software\Python"
if ERRORLEVEL 1 GOTO NOPYTHON
goto :HASPYTHON
:NOPYTHON
echo This Computer does not have Python. Please install Python to Continue

:HASPYTHON
echo This Computer has Python. Proceeding with Setup
pip install asciimatics

pause
