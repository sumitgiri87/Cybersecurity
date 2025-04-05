NU nano 8.0                  extract_apache_logs.sh                  Modified
#!/bin/bash

# Path to Apache access log file
LOG_FILE="/var/log/apache2/access.log"

# Path to the output file stored in a shared folder. For use on anther system, the file path needs to be updatd so that the extracted log can be accessed by the system on which the python log parsing script is running.
OUTPUT_FILE="/media/sf_test/Linux/linux_log/extracted_access_log.txt"

# Create the output file if it doesn't exist
if [ ! -f "$OUTPUT_FILE" ]; then
    touch "$OUTPUT_FILE"
fi

# Get the number of lines already processed
LAST_LINE=$(wc -l < "$OUTPUT_FILE")

# Extract new lines starting from the last unprocessed line
tail -n +$((LAST_LINE + 1)) "$LOG_FILE" >> "$OUTPUT_FILE"

