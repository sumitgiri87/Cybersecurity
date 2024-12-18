import sched
import time
import subprocess

# Path to the log parsing script
LOG_PARSING_SCRIPT = 'log_parsing.py'  

def run_log_parsing(scheduler):
    # Schedule the next call first
    scheduler.enter(60, 1, run_log_parsing, (scheduler,))  # Call this function every 60 seconds

    # Run the log parsing script
    try:
        # Execute the log parsing script and wait for it to complete
        result = subprocess.run(['python', LOG_PARSING_SCRIPT], check=True)
        print(f"Log parsing script executed successfully: {result}")
    except subprocess.CalledProcessError as e:
        # Handle any errors that occur while running the script
        print(f"An error occurred while running the log parsing script: {e}")

    print("Log parsing process completed.")

# Create a scheduler instance
my_scheduler = sched.scheduler(time.time, time.sleep)

# Schedule the first execution of the log parsing script
my_scheduler.enter(0, 1, run_log_parsing, (my_scheduler,))  # Initial call without delay
my_scheduler.run()  # Start the scheduler