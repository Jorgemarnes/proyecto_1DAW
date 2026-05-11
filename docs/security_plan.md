# Security Implementation Plan 🛡️

This document outlines the security measures and protocols implemented to protect the infrastructure, data, and integrity of the Music Store SSG project.

<br>

## 1. Network Security & Isolation
The architecture follows the principle of **least privilege**, ensuring that services are only accessible to authorized components.

* **Database Isolation**: The PostgreSQL VM (Port 5432) will be configured to accept connections **exclusively** from the Web Server VM IP. All other external traffic will be blocked using the internal firewall (`ufw`).
* **Virtual Network**: Using a **Host-Only** or **NAT Network** in VirtualBox ensures the backend infrastructure is not exposed to the public internet, providing an extra layer of protection.

<br>

## 2. Web Security (HTTPS/SSL)
To ensure encrypted communication between the host browser and the web server, we will implement **SSL/TLS**.

* **Self-Signed Certificates**: We will generate certificates using **OpenSSL** to enable HTTPS.
* **HTTPS Redirection**: The web server (Nginx/Apache) will be configured to automatically redirect all port 80 (HTTP) traffic to port 443 (HTTPS).
* **Encryption Standards**: We will enforce the use of **TLS 1.2 or 1.3** to ensure modern cryptographic standards.

<br>

## 3. Access Control & Multi-Factor Authentication (MFA)
Based on recent security studies, we will implement enhanced authentication for system administration.

* **2FA for SSH**: We will research the implementation of the **Google Authenticator (PAM module)** on the Linux Mint VMs. This requires a time-based one-time password (TOTP) in addition to the standard password.
* **Privilege Management**: Root login will be disabled via SSH. We will use a dedicated user with `sudo` privileges for all administrative tasks.

<br>

## 4. Ethical Scraping & Data Integrity
Security also involves respecting external infrastructure and ensuring legal compliance.

* **Throttling**: The Python script will include delays between requests to avoid being flagged as a malicious bot or causing a Denial of Service (DoS).
* **Robots.txt Compliance**: The scraper will be programmed to read and respect the `robots.txt` file of the source website.
* **Attribution**: We will not re-host copyrighted images; we will link to the source with proper attribution.

<br>

## 5. Database & Code Security
* **Credential Management**: Database passwords will be stored in an `.env` file (excluded from the repository via `.gitignore`) to prevent accidental leaks.
* **SQL Injection Prevention**: All database interactions in Python will use **parameterized queries** (prepared statements) to prevent SQL injection attacks.

<br>

---

### Security Audit Checklist (Planned for June 12)
- [ ] Verify SSL certificate status in the browser.
- [ ] Test firewall rules: Ensure Port 5432 is unreachable from the Host.
- [ ] Confirm 2FA prompts during SSH login.
- [ ] Ensure no sensitive credentials or `.env` files are present in the GitHub history.