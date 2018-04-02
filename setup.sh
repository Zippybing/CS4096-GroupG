#!/bin/bash

echo Running Linux Setup Script
if command -v python &>/dev/null; then
    echo "This Computer has Python. Proceeding with Setup"
	pip install asciimatics
else
    echo "This Computer does not have Python. Please install Python to Continue"
fi