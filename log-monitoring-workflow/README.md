# Log Monitoring Workflow

**Overview**  
This project demonstrates the implementation of an **automated log monitoring workflow** to detect unusual network activity. Using **Bash and Python**, the system efficiently extracts, analyzes, and reports key security events, such as failed login attempts and HTTP errors. The solution ensures continuous monitoring and alerting for potential security threats.

**Scenario**  
**Turn a New Leaf** is a non-profit organization that requires its members to log in every Thursday to update their employment status. The organization's network consists of **Windows and Linux systems**, with Linux machines hosting web servers. To maintain security and compliance, **failed login attempts and critical HTTP errors (404, 401, 500) must be tracked and reported**.

**Project Objectives**  
- **Automate log extraction and analysis** from Linux servers.  
- **Identify suspicious activity** such as failed login attempts and HTTP errors.  
- **Generate automated alerts** when thresholds are exceeded.  
- **Provide weekly reports** for stakeholders to review security trends.  

**Tools & Technologies**  
- **Bash** – Extract logs from Linux servers.  
- **Python** – Analyze log data for anomalies.  
- **Cron Jobs** – Automate script execution at scheduled intervals.  
- **Email Alerts** – Notify administrators of unusual activity.  

**Workflow Structure**  
1. **Log Extraction:**  
   - Bash script retrieves logs from **Linux access and error logs**.  
2. **Log Analysis:**  
   - Python script processes logs to detect **failed logins and HTTP errors**.  
   - If error thresholds are exceeded, an **alert is generated**.  
3. **Alert & Reporting:**  
   - Automated **email notifications** sent with key incident details.  
   - Weekly security reports generated for historical analysis.  

**Expected Output**  
- **Real-time alerts** when suspicious activity is detected.  
- **Detailed logs of security events**, including timestamps and affected IP addresses.  
- **Comprehensive weekly reports** summarizing system activity and security insights.  

**Key Features**  
- **Automated Execution:** Cron jobs ensure continuous monitoring without manual intervention.  
- **Historical Data Storage:** Retains records for long-term security analysis.  
- **Scalability:** Potential to integrate **machine learning for anomaly detection** in future iterations.  

**Potential Enhancements**  
- Expanding log analysis to include additional **Indicators of Compromise (IoCs)**.  
- Enhancing **real-time anomaly detection** with **machine learning models**.  
- Integrating with **SIEM (Security Information and Event Management) solutions** for broader security insights.  

**Learning Outcomes**  
- **Apply scripting** to automate cybersecurity monitoring tasks.  
- **Develop log filtering techniques** to identify security threats.  
- **Implement alert mechanisms** for proactive security response.  

---
This project provides a **practical approach to network security monitoring**, ensuring timely detection and response to potential cyber threats.

