"""
Uninstallation script to uninstall the sdc_aws_fswatcher service
"""

import os
import sys

# Get the current working directory
cwd = os.getcwd()
print("Current working directory: " + cwd)

# Get absolute path of the current working directory
abs = os.path.abspath(cwd)
print("Absolute path: " + abs)

# Verify service file exists
if not os.path.exists(abs + "/sdc_aws_fswatcher.service"):
    print("sdc_aws_fswatcher.service does not exist")
    sys.exit(1)
else:
    print("sdc_aws_fswatcher.service exists")

# Stop service
print("Stopping service")
os.system("sudo systemctl stop sdc_aws_fswatcher")
print("Stopped service")

# Disable service
print("Disabling service")
os.system("sudo systemctl disable sdc_aws_fswatcher")
print("Disabled service")

# Remove service file
print("Removing service file")
os.system("sudo rm /etc/systemd/system/sdc_aws_fswatcher.service")
print("Removed service file")

# Reload daemon
print("Reloading daemon")
os.system("sudo systemctl daemon-reload")
print("Reloaded daemon")

# Remove venv
print("Removing venv")
os.system("sudo rm -rf " + abs + "/venv")
print("Removed venv")
