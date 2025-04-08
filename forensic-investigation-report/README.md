# 🕵️‍♂️ Forensic Investigation: The Stolen Szechuan Sauce

## 📌 Project Overview
This repository contains forensic documentation and analysis for **[Case 001 – The Stolen Szechuan Sauce](https://dfirmadness.com/the-stolen-szechuan-sauce/)**, a digital forensics scenario created by **[DFIR Madness](https://dfirmadness.com/)**. The investigation aims to uncover the attack vector, malware used, network impact, and adversary persistence while documenting the forensic process in a structured manner.

### 🛠 Tools Used
The investigation leveraged industry-leading digital forensic tools, including:

- **FTK Imager** – Disk imaging and file integrity analysis.
- **Wireshark** – Network traffic analysis for malicious activity.
- **Registry Explorer** – Detection of persistence mechanisms in the registry.
- **VirusTotal** – Malware classification and threat intelligence.
- **AlienVault OTX** – Adversary infrastructure correlation.
- **Autopsy** – Digital forensics platform for analyzing disk images, extracting files, and uncovering evidence from the data.
---


### 🔍 Incident Scenario: The Szechuan Sauce Heist

It all started with a jarring wake-up call. Imagine being ripped from a peaceful sleep as my boss—who is nothing short of a mad scientist—drags me out of bed. Between his slurred words and unexpected belches, I was told that the FBI had contacted him. His precious, newly-developed Szechuan sauce recipe had somehow surfaced on the dark web. In an instant, I was thrown into action.

Still groggy but quick on my feet, I grabbed my trusty incident response “Go-Bag,” which included my incident thumb drive and laptop. What followed was a whirlwind of forensic investigation—tracing the attacker’s steps, discovering malicious payloads, analyzing artifacts, and ultimately identifying the breach that involved a recipe for the world’s most coveted sauce.

---

### 🎯 Purpose
This project was an opportunity for me to practice and enhance my digital forensics skills in a hands-on, real-world scenario. The case offered a blend of practical forensics techniques, analysis, and reporting, all while providing a bit of fun with its outrageous storyline.

The investigation had me following a structured process: analyzing servers, dissecting malware, identifying the attack vector, and tracking the intruder’s activity across the victim network. Through this project, I’ve gained valuable experience in documenting and analyzing cyber incidents with a solid understanding of real-world tactics and techniques.

---

### 🎯 Target Audience
This project is aimed at anyone with an interest in digital forensics, from beginners to seasoned professionals. Whether you're a:

- **Digital Forensics Enthusiast** looking for a challenging, yet fun, scenario to practice on.
- **Aspiring Forensics Investigator** wanting to learn and improve their skills.
- **Educator** who wants a real-world case to use in the classroom or as part of training materials.

Feel free to use this repository for educational purposes, as long as credit is given to the creators, **DFIR Madness**.

---

### ⚙️ Game-isms
As with any training exercise, there are intentional quirks in the data and events. The timeline may appear compressed at times, and some activities may seem a bit outlandish, but these are designed to support the learning experience. Despite the humorous elements, the attack closely mirrors real-world adversary tactics, techniques, and procedures.

The goal here was to balance serious forensic work with a fun, interactive case study that would allow me to apply my skills while enjoying the journey. And, let's face it—tracking down a stolen Szechuan sauce recipe isn’t something you get to do every day! 

---

### 📝 Questions to Answer / Goals
During the investigation, I tackled the following questions (and many more) to piece together the puzzle of the Szechuan sauce heist:

1. **What’s the Operating System of the Server?**
2. **What’s the Operating System of the Desktop?**
3. **What was the local time of the Server?**
4. **Was there a breach?**
5. **What was the initial entry vector (how did the attacker get in)?**
6. **Was malware used?** If so, I had to answer questions like:
   - **What process was malicious?**
   - **Identify the IP Address that delivered the payload.**
   - **What IP Address is the malware calling to?**
   - **Where is this malware on disk?**
   - **When did it first appear?**
   - **Did someone move it?**
   - **What were the capabilities of this malware?**
   - **Is this malware easily obtained?**
   - **Was this malware installed with persistence on any machine? If so, when and where?**
7. **What malicious IP Addresses were involved?**
8. **Were any IP Addresses from known adversary infrastructure?**
9. **Are these pieces of adversary infrastructure involved in other attacks around the time of the attack?**
10. **Did the attacker access any other systems?** If so, how and when?
11. **Did the attacker steal or access any data?** If so, when?
12. **What was the network layout of the victim network?**
13. **What architecture changes should be made immediately?**
14. **Did the attacker steal the Szechuan sauce? If so, what time?**
15. **Did the attacker steal or access any other sensitive files? If so, what times?**
16. **Finally, when was the last known contact with the adversary?**


And much more! Each question took me through a thorough forensic analysis, utilizing my skills to track down all the malicious activity that took place.

---

### ⚡ Advanced and Bonus Questions
As I delved deeper into the case, I explored even more advanced questions, such as:

- **What CIS Top 20 or SANS Top 20 Controls would have directly prevented this breach?**
- **What major architecture improvement could be made that would have prevented this breach?**
- **Can you identify policy improvements or controls that should be implemented to secure this environment?**
- **Which users have actually logged onto the DC?**
- **Which users have actually logged onto the Desktop machine?**
- **What are the passwords for the users in the domain?**
- **Can you recover the original file about Beth’s Secrets?** If so, what was the original name and contents?
- **What file was time-stomped?**

---
### 🔍 Client Interview

This interview was conducted while retrieving the artifacts from the system using **FTK Imager Lite** and **Redline Collector**.

#### Where were the files in question stored?

The files were located on the **bellllcchhhh File Server** on the **Domain Controller**.

#### What was the Operating System version of this server?

It was whatever **Jerry** installed a few years back. Probably a version of Windows 2012. **Belch.**

#### May I have a network map where the affected systems were located?

Sure. All the systems were loc-bellllch-ated in **10.42 something something**.

#### Were there any other systems or files you are concerned about?

Yeah, certainly. **Morty** is rambling on about something he might have had on there. Also, there was a secret about **Beth** on the server. If you find it, and YOU TELL ANYBODY I WILL KILL YOU! *(Note: The threat here matches a character from a popular cartoon and is not a real threat. Stay calm.)*

---

### 🗓 Incident Context

- **Location**: Colorado
- **Date**: September (UTC -6 timezone)

### 🧠 Potential Questions

#### Why use outdated Windows 2012?

Windows 2012 might be outdated, but its **end of life** isn’t until 2023. Despite its age, investigations reveal that systems still use Windows 2008r2, even though its **End of Life** date passed in January 2020. Many systems stick with these older versions for longer periods, so it’s common to encounter them during investigations.

#### Why Windows 10?

**Windows 10** is a useful contrast to Windows 2012 for memory forensics. It uses **compressed memory**, and there will be a difference in **Disk Artifacts** to explore between the two systems, which makes for a richer analysis.

#### I Don’t Know Forensics! Where do I start?

That’s exactly the point of this training set! We will teach you how to approach this investigation, set up your environment, analyze artifacts, and then generate a comprehensive report.

---
You can download the following artifacts for forensic investigation and verify file integrity:

- **[DC01 Disk Image (E01)](https://dfirmadness.com/case001/DC01-E01.zip)**  
  MD5: `E57FC636E833C5F1AB58DFACE873BBDE`
  
- **DC01 [Memory](https://dfirmadness.com/case001/DC01-memory.zip) and [PageFile](https://dfirmadness.com/case001/DC01-pagefile.zip)**  
  MD5 (Memory): `64A4E2CB47138084A5C2878066B2D7B1`  
  MD5 (PageFile): `964EEAF0009D08CC101DE4A83A4E5D23`

- **DC01 [Autoruns](https://dfirmadness.com/case001/DC01-autorunsc.zip)**  
  MD5: `964F2D710687D170C77C94947DA29E66`

- **DC01 [Protected Files](https://dfirmadness.com/case001/DC01-ProtectedFiles.zip)**  
  MD5: `AD29830A583EFE49C8C1C35FAFFD264F`

- **Case001 [PCAP](https://dfirmadness.com/case001/case001-pcap.zip)**  
  MD5: `422046B753CF8A4DF49D2C4CE892DB16`

- **Desktop [Disk Image (E01)](https://dfirmadness.com/case001/DESKTOP-E01.zip)**  
  MD5: `71C5C3509331F472ABCDF81EB6EFFF07`

- **Desktop [Memory](https://dfirmadness.com/case001/DESKTOP-SDN1RPT-memory.zip) and [PageFile](https://dfirmadness.com/case001/Desktop-SDN1RPT-pagefile.zip)**  
  MD5 (Memory): `CF31E2635C77811AAA1BB04A92A721E2`  
  MD5 (PageFile): `45C096F2688A0B5DE0346FB72391B245`

- **Desktop [Autoruns](https://dfirmadness.com/case001/DESKTOP-SDN1RPT-autorunsc.zip)**  
  MD5: `3627DCAFA54E1365489A4EC0CC3D6A1C`

- **Desktop [Protected Files](https://dfirmadness.com/case001/DESKTOP-SDN1RPT-Protected%20Files.zip)**  
  MD5: `3E1A358D50003A9351AC2160AE6F0495`
----

### 🎮 Let’s Get Forensic!

This project has been a truly fun and rewarding experience. I got to apply my digital forensics knowledge to a quirky yet realistic scenario, sharpening my skills along the way. I also learned how to think critically about cybersecurity incidents, analyze forensic data, and respond effectively to potential breaches.

I hope you find this project informative, engaging, and maybe even a little humorous. So go ahead, grab your Go-Bag, and dive into the digital wreckage. You never know what you might uncover. The Szechuan sauce may just be the least of your concerns in this wild investigation!

---
## 📂 Repository Contents

- **README.md** – This file, providing an overview of the project.
- **Final Report (PDF)** – The complete forensic investigation report detailing methodology, findings, and recommendations.
- **Screenshots** – A collection of screenshots documenting key findings and the investigative process.



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


## 📜 Submission Guidelines
- **Answer Format:** All findings are documented with **screenshots**, **tool outputs**, and **detailed justifications**.
- **Report Submission:** The final report is formatted in a **professional forensic documentation style**.


---

This repository serves as a **comprehensive forensic case study** showcasing investigative techniques, documentation standards, and cybersecurity analysis skills. 🚀

