#!/bin/bash

# Set up the path to the virtual environment and the log parsing script
VENV_PATH="venv/Scripts/activate"   # Path to your virtual environment activation script
LOG_PARSING_SCRIPT="code/log_parsing.py"  # Path to your log parsing script

# Activate the virtual environment
source $VENV_PATH

# Function to execute the log parsing script
run_log_parsing() {
    echo "Starting log parsing script..."
    python $LOG_PARSING_SCRIPT
    echo "Log parsing script finished."
}

# Run the script in a loop every 60 seconds
while true; do
    run_log_parsing
    echo "Waiting for the next cycle..."
    sleep 60  # Delay for 60 seconds before running the script again
done
