# 🎸 Music Store - Static Site Generator (SSG) Project - proyecto_1DAW

This project is a comprehensive integration of the **1st Year DAW (Web Application Development)** curriculum. It consists of building a music catalog website using a **Static Site Generation** approach: data is scraped from the web, stored in a relational database, and then used to generate flat HTML files served by a secure web server.

<br>

## 👥 Team Members
* **Member 1:** Samuel Reyes Pérez
* **Member 2:** Airam Hernández Hermida
* **Member 3:** Jorge Marco Yanes

<br>

## 🏗️ GitHub Page
[SSG page](docs/index.md)

<br>

## 🏗️ Architecture Overview
The project environment is isolated within **VirtualBox** to simulate a real-world production deployment.
* **Host Machine:** Runs the web browser to access the store.
* **VM-WEB (Linux Mint):**
    * Hosts the **Nginx/Apache** server.
    * Executes the **Python SSG script** to generate HTML files.
* **VM-BBDD (Linux Mint):**
    * Hosts the **PostgreSQL** database.
    * Configured for private access only from the Web VM (Port 5432).

<br>

## 🛠️ Tech Stack & Academic Modules

| Technology | Module | Role | Docs |
| :--- | :--- | :--- | :--- |
| **Python** | PRO | Web scraping (BeautifulSoup/Requests) and ETL logic. | [Research](docs/scraping_research.md) |
| **PostgreSQL** | BAE | Relational storage for products, prices, and images. |
| **VirtualBox** | SSF | Virtualized networking and server administration. | [VMs stups](docs/vm_setup.md) |
| **HTML5 / CSS3** | LND | Responsive template design for the static frontend. |
| **Git / GitHub** | ETS | Version control, documentation, and workflow. |
| **Markdown / AI** | DJK | AI Skill development for automated data extraction. | [Skill](skills/extraction_skill.md) |
| **HTTPS / UFW** | ITK | SSL certificate implementation and firewall rules. | [Security plan](docs/security_plan.md) |
| **English Docs** | IKL | README, docstrings, and deployment manuals. | [Initial README](README.md) |

<br>

## 📅 Roadmap & Milestones (2026)
- **May 11 (Today):** Project setup, Architecture design, and Source selection.
- **May 19:** Database schema deployment and VM Network isolation.
- **May 27:** Data extraction phase (Scraping) and Loading to PostgreSQL.
- **June 04:** Frontend templating, SSG Scripting, and AI Skill development.
- **June 12:** Security hardening, final audit, and project defense.

<br>

## 📂 Repository Structure

```text
.
├── docs/           # Technical documentation & GitHub Pages
│ ├── architecture/ # Network diagrams
├── src/            # Project source code
│ ├── scraping/     # Scrapers and intermediate JSON files
│ ├── database/     # SQL schemas and DB connection scripts
│ └── ssg/          # HTML/CSS templates and generator script
|   ├── static      # CSS design
|   └── templates   # HTML templates
├── infra/          # VM configuration and setup guides
└── skills/         # Markdown skills for AI agents
```


