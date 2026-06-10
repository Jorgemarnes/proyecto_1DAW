# 🎸 Music Store - Static Site Generator (SSG) Project - proyecto_1DAW

This project is a comprehensive integration of the **1st Year DAW (Web Application Development)** curriculum. It consists of building a music catalog website using a **Static Site Generation** approach: data is scraped from the web, stored in a relational database, and then used to generate flat HTML files served by a secure web server. We will implement these [requirements](docs/requirements.md).

<br>

## 👥 Team Members

* **Member 1:** Samuel Reyes Pérez
* **Member 2:** Airam Hernández Hermida
* **Member 3:** Jorge Marco Yanes

<br>

## 🛠️ Tech Stack & Academic Modules

| Technology | Module | Role | Docs |
| ------- | ------- | ------- | ------- |
| **Python** | PRO | Web scraping (BeautifulSoup/Requests) and ETL logic. | [Research](docs/scraping_research.md) |
| **PostgreSQL** | BAE | Relational storage for products, prices, and images. | [Database](docs/db_structure.md) |
| **VirtualBox** | SSF | Virtualized networking and server administration. | [Infrastructure](docs/infrastructure.md) |
| **HTML5 / CSS3** | LND | Responsive template design for the static frontend. | [Design](docs/design.md) |
| **Git / GitHub** | ETS | Version control, documentation, and workflow. | [SSG page](docs/index.md) |
| **Markdown / AI** | DJK | AI Skill development for automated data extraction. | [Skill](skills/extraction_skill.md) |
| **HTTPS / UFW** | ITK | SSL certificate implementation and firewall rules. | [Security plan](docs/security_plan.md) |
| **English Docs** | IKL | README, docstrings, and deployment manuals. | [Initial README](README.md) |

<br>

## 📅 Roadmap & Milestones (2026)

* **May 11:** Project setup, Architecture design, and Source selection.
* **May 19:** Database schema deployment and VM Network isolation.
* **May 27:** Data extraction phase (Scraping) and Loading to PostgreSQL.
* **June 04:** Frontend templating, SSG Scripting, and AI Skill development.
* **June 12:** Security hardening, final audit, and project defense.

<br>

## 📂 Repository Structure

```text
.
├── docs/                    # Technical documentation and project reports
│   ├── app_requirements.md
│   ├── db_structure.md
│   ├── design.md
│   ├── index.md
│   ├── infrastructure.md
│   ├── research_sources.md
│   ├── scraping_research.md
│   ├── security_plan.md
│   └── setup_guide.md
│
├── infra/                   # VM configuration and setup
│   ├── arch_diagram.drawio
│   ├── arch_diagram.png
│   └── vm_setup.md
│
├── skills/                  # Markdown skills for AI agents
│   └── extraction_skill.md
│
├── src/                     # Project source code
|   ├── scraping/            # Scraper script
|   ├── database/            # SQL schemas and DB connection script
|   ├── settings/            # Constants as URLs, host ip and port
|   └── ssg/                 # HTML/CSS templates and generator script  
|      ├── static/           # CSS design
|      └── templates/        # HTML template
|
├── README.md
├── requirements.txt
└── main.py
```
