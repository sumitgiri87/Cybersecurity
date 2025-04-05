# 📄 Log Monitoring Workflow

## 📘 Overview

This project, developed as part of the **Lighthouse Labs Cybersecurity Bootcamp**, demonstrates how **Bash and Python scripting** can be applied to a **real-world cybersecurity scenario**. It automates log monitoring and anomaly detection to ensure proactive threat response and compliance.

The solution monitors server logs for unusual activity—such as **failed login attempts**, **unauthorized access (401 errors)**, **web scraping or broken links (404 errors)**, and **server failures (500 errors)**—and sends automated alerts when thresholds are exceeded.

---

## 🛠 Tech Stack

- 🐚 **Bash**
- 🐍 **Python**
- ⏰ **Cron Jobs**
- 🐧 **Linux Access Logs**
- 🌐 **HTTP Error Detection**
- 📧 **Email Alert Automation**

---

## 🏢 Scenario: Turn a New Leaf

### 👥 Company Profile

**Turn a New Leaf** is a **medium-sized non-profit organization** supporting youth in rural communities with employment opportunities. 

- Members must log in **every Thursday** to update their employment status.
- The organization uses a **mixed network** with both Windows and Linux machines.
- **Two Linux-based web servers** handle user authentication and job listing submissions.

### 🔒 The Security Request

As an **Access Log Analyst** at Turn a New Leaf, your responsibilities include:

- Monitoring **web server logs** for suspicious activity.
- Sending **alerts** if an unusual number of **failed logins** or **critical errors** occur.
- Providing **weekly email summaries** for compliance and oversight.

---

## ⚠️ Key Security Risks

- 🚨 **Failed Login Attempts** – Could indicate brute-force attacks or unauthorized access.
- 🚨 **HTTP 401 Errors (Unauthorized)** – May suggest authentication failures or privilege abuse.
- 🚨 **HTTP 404 Errors (Not Found)** – Often linked to web scraping, broken links, or recon scans.
- 🚨 **HTTP 500 Errors (Server Errors)** – Could be signs of server misconfiguration, crashes, or DoS attacks.

---

## 🎯 Project Objectives

- ✅ **Automate log extraction** from Linux web servers.
- ✅ **Analyze server logs** for failed logins and critical HTTP errors.
- ✅ **Trigger email alerts** when anomaly thresholds are exceeded.
- ✅ **Generate weekly reports** for security and compliance reviews.

---

## 🔁 Workflow Structure

### 1️⃣ Log Extraction (`/log_extraction/`)

- A **Bash script** collects access and error logs from Linux web servers.
- A sample **cron job** is provided to automate the script execution on a schedule.
- Extracted logs are saved as: `/assets/extracted_access_log.txt`
- Logs are continuously parsed and analyzed using Python for real-time anomaly detection.


### 🚨 2️⃣ Log Analysis & Anomaly Detection (Python Scripts)

This project includes Python scripts to automate log file analysis and detect common security anomalies.

### 🔍 Features

- `log_parsing.py` (located in the `/code/` folder) processes server logs to identify:
  - ❌ **Failed login attempts**
  - 🔐 **Unauthorized access** (HTTP 401 errors)
  - 🤖 **Web scraping attempts** (HTTP 404 errors)
  - ⚠️ **Server failures** (HTTP 500 errors)

- `run_log_parsing.py` (also in `/code/`) can be scheduled to run periodically, automating the log analysis process.

- Alternatively, `run_log_parsing.sh` (in the root directory) is a Bash script version that can be used for scheduling via cron jobs or other task schedulers.

- If error thresholds are exceeded:
  - An **alert log** is saved in the `/assets/` directory.
  - An **automated email** is sent to notify stakeholders.

- A screenshot of the alert email is available in `/assets/screenshots/`.


### 📬 3️⃣ Automated Alerts & Reporting

- ✉️ **Email notifications** are triggered whenever suspicious activity is detected.
- 📊 **Weekly summary reports** are generated to provide insights into overall network activity and potential security issues.

---

****Tools & Technologies Used****
🛠 **Bash** – Extract logs from Linux servers.  
🛠 **Python** – Analyze log data for anomalies.  
🛠 **Cron Jobs** – Automate script execution at scheduled intervals.  
🛠 **Email Alerts** – Notify administrators of unusual activity.

****Expected Output****
📌 **Real-time alerts** when suspicious activity is detected.  
📌 **Detailed logs of security events**, including timestamps and affected IP addresses.  
📌 **Comprehensive weekly reports** summarizing system activity and security insights.

****Key Features****
✔ **Automated Execution:** Cron jobs ensure continuous monitoring.  
✔ **Historical Data Storage:** Retains records for long-term security analysis.  
✔ **Scalability:** Potential to integrate **machine learning for anomaly detection**.

****Potential Enhancements****
🔹 Expanding log analysis to include additional **Indicators of Compromise (IoCs)**.  
🔹 Enhancing **real-time anomaly detection** with **machine learning models**.  
🔹 Integrating with **SIEM (Security Information and Event Management) solutions**.

****Resources****
- **Logs:** The logs for this project are located in the **/assets** subfolder with the files **extracted_access_log.txt** and **report_log.txt**.
- **Python Scripts:** The Python scripts used for log analysis and anomaly detection are located in the **/code** subfolder.
- **Final Deliverable:** The final report summarizing the results of the project can be found in **Final_Report.pdf** in this folder.

