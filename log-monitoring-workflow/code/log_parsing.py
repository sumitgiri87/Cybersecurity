import os
import re
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Extracted log file path in shared
LOG_FILE_PATH = r"C:\Users\kakai\Documents\Canada Job Search\Cryptography & CyberSecurity\LHL Bootcamp\test\Linux\linux_log\extracted_access_log.txt"

# Path for the report file in the same folder as the log file
REPORT_FILE_PATH = os.path.join(os.path.dirname(LOG_FILE_PATH), 'report_log.txt')

THRESHOLD_404 = 5  # Number of 404 errors to trigger alarm
THRESHOLD_401 = 3  # Number of 401 errors to trigger alarm
THRESHOLD_500 = 5  # Number of 500 errors to trigger alarm
TIME_SPAN = timedelta(minutes=10)  # Time window for detecting multiple errors
ALERT_EMAIL = "sumit.giri199@gmail.com"  # Recipient email
SENDER_EMAIL = "sumitgiridrive5@gmail.com"  # Sender email
SENDER_PASSWORD = "blkgfmqjthmiwikj"  # Sender email's app password

# Function to send an alert email
def send_email_alert(recent_errors):
    subject = "Multiple Error Attempts Detected"
    body = f"Warning: Detected errors in the last {TIME_SPAN}.\n\n"

    # Each type of error
    for error_type, details in recent_errors.items():
        body += f"{error_type}: {len(details)} occurrences\n"
        for error in details:
            body += f"IP: {error['ip']}, Time: {error['time']}\n"
        body += "\n"

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

    # Regular expressions to match errors in the log
    log_regex_404 = r'(\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2}) .* 404 .*'
    log_regex_401 = r'(\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2}) .* 401 .*'
    log_regex_500 = r'(\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2}) .* 500 .*'
    
    time_format = "%d/%b/%Y:%H:%M:%S"
    
    # Dictionary to hold recent errors
    recent_errors = {
        "404 Errors": [],
        "401 Errors": [],
        "500 Errors": []
    }

    with open(LOG_FILE_PATH, 'r') as log_file:
        for line in log_file:
            current_time = datetime.now()

            # Check for 404 errors
            match_404 = re.search(log_regex_404, line)
            if match_404:
                log_time_str = match_404.group(1)
                log_time = datetime.strptime(log_time_str, time_format)
                ip_address = line.split()[0]  
                recent_errors["404 Errors"].append({'time': log_time, 'ip': ip_address})

            # Check for 401 errors
            match_401 = re.search(log_regex_401, line)
            if match_401:
                log_time_str = match_401.group(1)
                log_time = datetime.strptime(log_time_str, time_format)
                ip_address = line.split()[0]  
                recent_errors["401 Errors"].append({'time': log_time, 'ip': ip_address})

            # Check for 500 errors
            match_500 = re.search(log_regex_500, line)
            if match_500:
                log_time_str = match_500.group(1)
                log_time = datetime.strptime(log_time_str, time_format)
                ip_address = line.split()[0]  
                recent_errors["500 Errors"].append({'time': log_time, 'ip': ip_address})

    # Filtering recent errors based on time span
    for error_type in recent_errors:
        recent_errors[error_type] = [
            error for error in recent_errors[error_type]
            if current_time - error['time'] <= TIME_SPAN
        ]

    # Check for thresholds and send alerts if needed
    alert_triggered = False
    for error_type, details in recent_errors.items():
        if len(details) >= THRESHOLD_404 and error_type == "404 Errors":
            alert_triggered = True
        elif len(details) >= THRESHOLD_401 and error_type == "401 Errors":
            alert_triggered = True
        elif len(details) >= THRESHOLD_500 and error_type == "500 Errors":
            alert_triggered = True

    if alert_triggered:
        log_to_file(f"ALERT: Multiple errors detected within {TIME_SPAN}.")
        send_email_alert(recent_errors)
    else:
        log_to_file(f"Errors are under control: {recent_errors}")

if __name__ == "__main__":
    parse_log()

