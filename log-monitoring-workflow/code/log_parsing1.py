import os
import re
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Constants
LOG_FILE_PATH = r"C:\Users\kakai\Documents\Canada Job Search\Cryptography & CyberSecurity\LHL Bootcamp\test\Linux\linux_log\extracted_log.txt"

# Dynamically create the path for the report file in the same folder as the log file
REPORT_FILE_PATH = os.path.join(os.path.dirname(LOG_FILE_PATH), 'report_log.txt')

THRESHOLD_404 = 5  # Number of 404 errors to trigger alarm
TIME_SPAN = timedelta(minutes=10)  # Time window for detecting multiple 404 errors
ALERT_EMAIL = "sumit.giri199@gmail.com"  # Recipient email
SENDER_EMAIL = "sumitgiridrive5@gmail.com"  # Sender email
SENDER_PASSWORD = "blkgfmqjthmiwikj"  # Sender email's password

# Function to send an alert email
def send_email_alert(occurrences):
    subject = "Multiple 404 Error Attempts Detected"
    body = f"Warning: {len(occurrences)} HTTP 404 errors were detected in the last {TIME_SPAN}."
    
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = ALERT_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Setting up the SMTP server
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  # SMTP server details
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, ALERT_EMAIL, msg.as_string())
        server.quit()
        log_to_file(f"Alert email sent to {ALERT_EMAIL}.")
    except Exception as e:
        log_to_file(f"Failed to send email: {e}")

# Function to log output to the report file
def log_to_file(message):
    with open(REPORT_FILE_PATH, 'a') as report_file:
        report_file.write(f"{datetime.now()}: {message}\n")

# Function to parse the log file
def parse_log():
    if not os.path.exists(LOG_FILE_PATH):
        log_to_file(f"Log file not found at {LOG_FILE_PATH}")
        return

    # Regular expression to match 404 errors in the log
    log_regex = r'(\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2}) .* 404 .*'
    time_format = "%d/%b/%Y:%H:%M:%S"
    
    occurrences = []

    with open(LOG_FILE_PATH, 'r') as log_file:
        for line in log_file:
            match = re.search(log_regex, line)
            if match:
                log_time_str = match.group(1)
                log_time = datetime.strptime(log_time_str, time_format)
                occurrences.append(log_time)

    # Now check if we have more than THRESHOLD_404 errors in the last TIME_SPAN
    current_time = datetime.now()
    recent_404 = [time for time in occurrences if current_time - time <= TIME_SPAN]

    if len(recent_404) >= THRESHOLD_404:
        log_to_file(f"ALERT: Multiple 404 errors detected within {TIME_SPAN}.")
        send_email_alert(recent_404)
    else:
        log_to_file(f"404 errors are under control with {len(recent_404)} occurrences in the last {TIME_SPAN}.")

if __name__ == "__main__":
    parse_log()
