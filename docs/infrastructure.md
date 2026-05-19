## Infrastructure diagram

* **Host Machine:** Runs the web browser to access the store.
* **VM-WEB (Linux Mint):**
    * Hosts the **Nginx/Apache** server.
    * Executes the **Python SSG script** to generate HTML files.
* **VM-BBDD (Linux Mint):**
    * Hosts the **PostgreSQL** database.
    * Configured for private access only from the Web VM (Port 5432).

The **Vituals machines** have the following [setup](/infra/vm_setup.md)

<br>

The **ports** relate to the usual/default ports used by the HTTPS protocol and the common Postgres database.

![diagram](/infra/arch_diagram.png)