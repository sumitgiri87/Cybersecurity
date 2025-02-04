# 🕵️‍♂️ Forensic Investigation: The Stolen Szechuan Sauce

## 📌 Project Overview
This repository contains forensic documentation and analysis for **Case 001 – The Stolen Szechuan Sauce**, a digital forensics scenario created by **DFIR Madness**. The investigation aims to uncover the attack vector, malware used, network impact, and adversary persistence while documenting the forensic process in a structured manner.

## 📂 Repository Contents
- **README.md** – This file, providing an overview of the project.
- **Final Report (PDF/Google Doc)** – The complete forensic investigation report detailing methodology, findings, and recommendations.

## 🔎 Investigation Summary
This case involved a cybersecurity breach leading to unauthorized access and data exfiltration. Key findings include:

- **🛠 Initial Access Vector:** Exploitation of **RDP vulnerabilities** via **IP 194.61.24.102**, linked to known adversary infrastructure.
- **💀 Malware Identified:** `coreupdater.exe`, executed from `C:\Windows\System32`, enabled **remote access** and **data exfiltration**.
- **🌐 Network Impact:** **Lateral movement** detected between **CITADEL-DC01 (Domain Controller)** and **DESKTOP-SDN1RPT (Endpoint Device)**.
- **📁 Data Exfiltration:** Confidential files from the **"Secret"** folder were accessed and stolen.
- **🎯 Adversary Persistence:** **Registry modifications** and **service-based persistence** ensured continued access to compromised systems.

The full investigation is documented in the **Final Report**.

## 🏗 Methodology
The forensic analysis followed industry-standard best practices to ensure accuracy and integrity:

1. **🖥 Artifact Analysis** – Examined disk images, memory dumps, and registry hives for forensic evidence.
2. **📡 Network Analysis** – Investigated **PCAP files** to trace malicious communication.
3. **⏳ Timeline Reconstruction** – Correlated system and network logs to track the attack's progression.
4. **🦠 Malware Analysis** – Identified, classified, and analyzed malicious payloads.
5. **📝 Documentation** – Collected supporting evidence with screenshots and forensic justifications.

## 🛠 Tools Used
The investigation leveraged industry-leading digital forensic tools, including:

- **FTK Imager** – Disk imaging and file integrity analysis.
- **Wireshark** – Network traffic analysis for malicious activity.
- **Registry Explorer** – Detection of persistence mechanisms in the registry.
- **VirusTotal** – Malware classification and threat intelligence.
- **AlienVault OTX** – Adversary infrastructure correlation.

## 📜 Submission Guidelines
- **Answer Format:** All findings are documented with **screenshots**, **tool outputs**, and **detailed justifications**.
- **Collaboration:** This project was conducted with a partner, and both contributors are credited in the final submission.
- **Report Submission:** The final report is formatted in a **professional forensic documentation style**.

## 🔗 Additional Resources
- **Case Details & Artifacts:** [DFIR Madness - Case 001](https://dfirmadness.com/the-stolen-szechuan-sauce/)
- **Super Timeline Analysis:** [Super Timeline Guide](https://dfirmadness.com/case-001-super-timeline-analysis/)

---

This repository serves as a **comprehensive forensic case study** showcasing investigative techniques, documentation standards, and cybersecurity analysis skills. 🚀

