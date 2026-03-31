# Open Source Software Audit — Linux Kernel

**Student Name:** [Tanmay Patidar]  
**Roll Number:** [24MEI10147]  
**Course:** Open Source Software  
**Target Software:** Linux Kernel  
**Date:** 31 March 2026  

---

## Overview
This project provides a comprehensive system auditing and information gathering toolset for Linux environments, specifically focused on the Linux Kernel as a case study in open-source software. It combines the flexibility of Python for modular analysis with the power of Bash shell scripts for system-level reporting.

## Key Features
- **System Identity & Reporting:** Detailed information about the distribution, kernel version, uptime, and user environment.
- **FOSS Package Inspection:** Verifies the status and version of kernel packages using `dpkg`.
- **Disk & Permission Auditing:** Analyzes permissions, ownership, and disk usage for critical system directories.
- **Log File Analysis:** Scans system logs for specific keywords and summarizes recent activity.
- **Interactive Manifesto Generator:** A utility to generate a personalized open-source philosophy statement.

## Project Structure
```text
open-source-software-audit-24MEI10147/
├── main.py                     # Primary Python entry point
├── helpers.py                  # Modular utility functions and logic
├── script1_system_identity.sh  # Identity report (Bash)
├── script2_package_inspector.sh# Package status checker (Bash)
├── script3_disk_auditor.sh      # Directory & permission auditor (Bash)
├── script4_log_analyzer.sh     # Keyword search in system logs (Bash)
├── script5_manifesto_generator.sh # Interactive philosophy generator (Bash)
└── README.md                   # Project documentation
```

## Setup & Installation

### 1. Navigate to the Directory
```bash
cd /home/necro/Projects/vityarthi/open-source-software-audit-24MEI10147
```

### 2. Set Permissions
Ensure all shell scripts are executable:
```bash
chmod +x *.sh
```

## Usage

### Running the Python Audit Tool
The Python tool provides a unified interface for the auditing logic:
```bash
python3 main.py
```

### Running Individual Shell Scripts
Each script can be run independently for specific tasks:
```bash
./script1_system_identity.sh
./script2_package_inspector.sh
./script3_disk_auditor.sh
sudo ./script4_log_analyzer.sh /var/log/syslog error
./script5_manifesto_generator.sh
```

## Dependencies
- **Python 3.x**
- **Bash Shell**
- **System Utilities:** `lsb_release`, `dpkg`, `du`, `uname`, `uptime`
- **Privileges:** `sudo` access is required for `script4_log_analyzer.sh` to read system-level logs.

## Submission Information
This repository is submitted as part of the VITyarthi OSS NGMC Capstone Project by [Tanmay Patidar] ([24MEI10147]). All scripts are designed and tested for Fedora-based Linux distributions.

---
**License:** Distributed under the terms of the GNU General Public License v2 (GPL-2.0).
