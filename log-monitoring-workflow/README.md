****Log Monitoring Workflow****

****Overview****
This project demonstrates how to apply **Bash and Python scripting** to a **real-world cybersecurity scenario** by automating log monitoring and anomaly detection. The solution establishes a workflow to monitor network traffic for unusual activity, such as **failed login attempts and critical HTTP errors (404, 401, 500)**, ensuring proactive security response and compliance.  

****Scenario****

****Company Profile****  
**Turn a New Leaf** is a **medium-sized non-profit organization** that supports youth in rural communities to find employment. To comply with **government regulations**, members must log in every **Thursday** to update their employment status and job search activities. The organization’s network consists of **both Windows and Linux machines**, with **two Linux-based web servers** handling user authentication and job listing submissions.  

****The Security Request****  
As an **Access Log Analyst** at Turn a New Leaf, your **primary responsibility** is to monitor **server logs for unusual activity** and send alerts if an unusual number of failed logins occur. Additionally, you must **document** and provide **weekly updates via email** to ensure compliance and network security.  

****Key Security Risks****  
🚨 **Failed Login Attempts** – May indicate **brute-force attacks** or **unauthorized access attempts**.  
🚨 **HTTP 401 Errors (Unauthorized)** – Could suggest issues with **user authentication** or **unauthorized access attempts**.  
🚨 **HTTP 404 Errors (Not Found)** – Might indicate **web scraping**, **broken links**, or **malicious scanning**.  
🚨 **HTTP 500 Errors (Server Errors)** – Could reflect **server misconfigurations**, **system crashes**, or **denial-of-service (DoS) attacks**.  

****Project Objectives****  
✅ **Automate log extraction** from Linux web servers.  
✅ **Analyze logs for suspicious activity**, including failed logins and HTTP errors.  
✅ **Send automated alerts** when error thresholds are exceeded.  
✅ **Provide structured reports** for historical analysis and compliance.  

****Repository Structure****
/log-monitoring-workflow │── /logs │ ├── access_logs/ # Extracted server access logs │ ├── alert_logs/ # Alert logs including email notifications │── /scripts │ ├── log_parser.py # Parses and extracts key log data │ ├── anomaly_detector.py # Identifies unusual login activity & HTTP errors │ ├── email_alert.py # Generates and sends alert notifications │── /reports │ ├── weekly_security_report.md # Weekly security report summary │── README.md # Project documentation
