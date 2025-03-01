# **Active Directory Integration - Detection Methods**

## **Overview**
To ensure the security and reliability of an Active Directory (AD) environment, it is crucial to monitor, detect, and analyze any unauthorized access attempts, suspicious activities, or policy violations. This document outlines the various detection methods that can be used to identify and respond to potential security threats within an AD-integrated system.

---

## **1. Monitoring Authentication Attempts**
One of the key aspects of Active Directory security is tracking user authentication attempts. This can help detect:
- **Brute-force attacks** (multiple failed login attempts)
- **Unauthorized access attempts**
- **Compromised accounts being used**

### **Detection Method**
- **Enable AD Auditing Logs**: Ensure that **Event ID 4625** (failed logins) and **Event ID 4624** (successful logins) are being logged in Windows Event Viewer.
- **Log Authentication Events** in `ad_integration.log`:
  ```log
  2025-03-01 10:15:23 - INFO - Connected to Active Directory
  2025-03-01 10:17:45 - INFO - User johndoe authenticated successfully
  2025-03-01 10:19:01 - WARNING - Authentication failed for user hacker123
  ```
- **Automate Alerts**: Implement an email alert system that notifies administrators of multiple failed login attempts within a short period.

---

## **2. Detecting Unauthorized Account Modifications**
Attackers often attempt to modify user accounts to gain unauthorized access or escalate privileges.

### **Detection Method**
- **Monitor AD Event Logs** for:
  - **Event ID 4722** (User Account Enabled)
  - **Event ID 4725** (User Account Disabled)
  - **Event ID 4726** (User Account Deleted)
  - **Event ID 4738** (User Account Changed)
- **Log and Compare Changes**: Keep a history of user account states and compare changes over time.
- **Implement Role-Based Access Control (RBAC)** to restrict account modifications to authorized personnel only.

---

## **3. Detecting Password Resets and Changes**
Unauthorized password changes can indicate an ongoing attack, such as a password spraying attempt or insider threat.

### **Detection Method**
- **Monitor AD Logs for Event ID 4724** (Password Reset) and **Event ID 4740** (Account Locked Out).
- **Compare previous passwords** using hash history to detect password reuse.
- **Enforce Multi-Factor Authentication (MFA)** to add an extra layer of security.

---

## **4. Detecting Suspicious Group Membership Changes**
Attackers may try to add themselves to privileged groups such as **Domain Admins** or **Enterprise Admins**.

### **Detection Method**
- **Monitor AD Logs for Event ID 4728** (Group Membership Added) and **Event ID 4729** (Group Membership Removed).
- **Set up alerts** for any changes to high-privilege groups.
- **Compare group membership over time** using periodic snapshots.

---

## **5. Identifying Unusual Network Access Patterns**
If an attacker compromises an AD account, they may attempt to access network resources from an unusual location.

### **Detection Method**
- **Monitor Logon Events (Event ID 4624 & 4625)** for unusual IP addresses or geolocations.
- **Use SIEM tools like Splunk or ELK** to correlate login locations with normal user behavior.
- **Analyze VPN logs** to identify unauthorized remote logins.

---

## **6. Detecting Mass Account Lockouts**
Mass account lockouts can be a sign of a **brute-force attack** or a misconfigured application repeatedly attempting failed logins.

### **Detection Method**
- **Monitor AD Logs for Event ID 4740** (User Account Locked Out).
- **Identify patterns** where multiple accounts are locked out in a short period.
- **Use threshold-based alerts** to detect excessive failed authentication attempts.

---

## **7. Detecting Service Account Abuse**
Service accounts often have elevated privileges and are frequently targeted by attackers.

### **Detection Method**
- **Monitor AD Logs for Event ID 4672** (Special Privileges Assigned).
- **Track service account logins** to detect unauthorized access.
- **Enforce strong password policies and MFA** for service accounts.

---

## **8. Monitoring AD Schema and GPO Changes**
Changes to **Active Directory Schema** or **Group Policy Objects (GPOs)** can indicate an advanced attack.

### **Detection Method**
- **Monitor AD Logs for Event ID 5136** (Schema Changes) and **Event ID 5141** (GPO Deleted).
- **Compare baseline GPO settings** with periodic snapshots.
- **Alert administrators** if critical policies are modified.

---

## **9. Detecting Privilege Escalation Attempts**
Attackers may try to escalate their privileges by modifying account roles or assigning themselves to privileged groups.

### **Detection Method**
- **Monitor AD Logs for Event ID 4673** (Privilege Use Attempted) and **Event ID 4674** (Sensitive Privilege Used).
- **Detect changes in account permissions** using historical comparisons.
- **Enable Just-In-Time (JIT) Access** to limit administrative access.

---

## **10. Implementing SIEM for Advanced Detection**
To enhance security monitoring, integrate AD logs with a **SIEM (Security Information and Event Management) system** such as:
- **Splunk**
- **Elastic Stack (ELK)**
- **Microsoft Sentinel**
- **Graylog**

### **Detection Method**
- **Correlate multiple AD events** to detect advanced threats.
- **Use anomaly detection** to identify unusual user behavior.
- **Generate automated incident reports and alerts.**

---

## **Conclusion**
By implementing these detection methods, system administrators can effectively monitor **Active Directory security events**, detect **unauthorized access attempts**, and mitigate potential security risks. A combination of **event log monitoring, real-time alerting, and SIEM integration** ensures a proactive defense against cyber threats.

🚀 **Next Steps:**
- Automate detection rules using **PowerShell scripts**.
- Implement **real-time notifications via Slack or Email**.
- Conduct **regular penetration tests** to evaluate AD security.
