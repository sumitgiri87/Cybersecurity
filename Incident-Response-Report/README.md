# ****Incident Response Report: Premium House Lights Inc.****

## ****Project Overview****
This project is part of the ****Lighthouse Labs Cybersecurity Capstone****, focusing on ****incident response and forensic analysis**** following a simulated data breach at ****Premium House Lights Inc.**** The investigation involves analyzing security logs, network traffic captures, and forensic artifacts to determine the ****attack vector, impact, and mitigation strategies.****

****Tech Stack:****
- **Web Shell**
- **MySQL**
- **Web Server Logs**
- **Network Forensics**
- **FTK Imager**
- **Wireshark**
- **Registry Explorer**
- **VirusTotal**
- **AlienVault Intelligence**

## ****Scenario Summary****
On ****February 22, 2022****, Premium House Lights Inc. received an ****extortion email**** claiming attackers had exfiltrated ****customer data**** and would release it unless a ****10 BTC ransom**** was paid. The company was uncertain if the claims were valid or if a ****breach had occurred.****

The security team conducted an ****incident investigation****, analyzing:  
- ****Network traffic (PCAP files)****  
- ****Server and database logs****  
- ****Authentication and session logs****  

Findings confirmed a ****structured cyberattack****, where adversaries exploited ****web application vulnerabilities**** to gain access, escalate privileges, and ****exfiltrate customer data.****


## ****Key Objectives****
- ****Analyze**** attack methods and indicators of compromise (IoCs).  
- ****Investigate**** artifacts to confirm data exfiltration and attacker techniques.  
- ****Document**** an ****Incident Response Report**** outlining the attack timeline, technical findings, and recommendations.  
- ****Provide**** cybersecurity recommendations to mitigate future attacks.  

## ****Repository Contents****
- ****README.md**** – Project description (this file).  
- ****Final_Report.pdf**** – Detailed report with forensic analysis, attack timeline, and security recommendations.  
- ****artifacts/**** – Investigation artifacts provided by Premium House Lights Inc., including:  
  - ****phl_network_diagram.png**** – Company network diagram.  
  - ****phl_webserver.pcap**** – Web server packet capture.  
  - ****phl_database.pcap**** – Database packet capture.  
  - ****phl_access_log.txt**** – Application access logs.  
  - ****phl_database_shell.txt**** – Session logs from database shell activity.  
  - ****phl_database_access_log.txt_**** – Database access logs.  
  - ****phl_database_tables.db**** – Extracted database table data.  
- ****report_screenshots/**** – Screenshots from different stages of the investigation process.  
- ****templates/**** – Templates used for incident response reporting.  
- ****project_demo_ppt.pdf**** – Presentation slides demonstrating key aspects of the investigation.


## ****Tools & Techniques Used****
- ****Wireshark**** – Packet analysis for network traffic investigation.  
- ****Linux Command-Line Forensics**** – Examining log files and system activity.  
- ****Database Analysis**** – Investigating MySQL logs and unauthorized queries.  
- ****Cybersecurity Best Practices**** – Recommendations for securing web applications, databases, and network infrastructure.  

## ****Lessons Learned****
This project highlights the importance of ****proactive security measures****, including:  
✅ ****Regular security audits**** to identify and patch vulnerabilities.  
✅ ****Network monitoring**** to detect suspicious activity.  
✅ ****Incident response planning**** for rapid mitigation of security threats.  

## ****Acknowledgments****
This project was completed as part of the ****Lighthouse Labs Cybersecurity Program****.
