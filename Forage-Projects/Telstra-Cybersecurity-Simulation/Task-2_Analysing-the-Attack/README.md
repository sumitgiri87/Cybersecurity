# ****🚀 Task 2: Analysing the Attack****

## ****🛠 Objective****  
Investigate the attack patterns using firewall logs to understand how the malware spreads and assist in firewall rule creation.  

---

## ****📂 Folder Structure****  
- **`/Resources`** – Contains materials needed for analysis.  
  - ****[Spring4Shell Proof of Concept Payload](https://github.com/craig/SpringCore0day/blob/main/exp.py)**** – Exploit payload used in the attack.  
  - **`Affected Infrastructure List & Firewall logs`** – Details of impacted systems and Network logs to analyze attack patterns. 
  - **`Firewall_Rule_Creation_Email_Template.docx`** – Template for drafting firewall rule requests.  
- **`Draft_Email_to_Networks_Team.pdf`** – 📄 Final deliverable containing the findings report and firewall rule recommendation.  

---

## ****📄 Task Overview****  
1. ****🔍 Analyze Firewall Logs**** – Identify patterns in attacker requests.  
2. ****⚡ Examine Exploit Characteristics**** – Understand how Spring4Shell was leveraged.  
3. ****✉️ Draft a Firewall Rule Request**** – Summarize findings concisely for the Networks team to implement mitigation.  

---

## ****📌 Key Findings****  
- Attackers exploited ****Spring4Shell (CVE-2022-22965)**** via ****malicious payload requests targeting Apache Tomcat servers****.  
- ****Blocking IP addresses is insufficient**** due to the distributed nature of the attack.  
- Identified ****malicious request patterns**** to help define ****firewall rules**** for mitigation.  

---

## ****✅ Deliverable****  
📄 ****Draft_Email_to_Networks_Team.pdf**** – A structured report detailing attack analysis and recommended firewall rules.  

---

## ****🔗 References****  
- 🔗 ****[Spring Security Advisory - CVE-2022-22965](https://spring.io/security/cve-2022-22965)****  
- 🔗 ****[CISA Cyber Advisory](https://www.cisa.gov/news-events/alerts/2022/04/01/spring-releases-security-updates-addressing-spring4shell-and-spring)****  

---

This README provides a ****clear, structured, and concise**** overview of the ****task, resources, and key takeaways****. 🚀

