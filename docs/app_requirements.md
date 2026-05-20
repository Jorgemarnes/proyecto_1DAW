# Project Requirements

This document outlines the functional and non-functional requirements for the Music Store project, developed as part of the 1st Year DAW curriculum.

<br>

## 1. Functional Requirements

### 1 User Authentication & Authorization

* **User Login:** Users must be able to log in to the system using a unique email and password.
* **Session Management:** The system should maintain the user's session state once logged in.
* **Role-Based Access Control (RBAC):**
  * **Standard User:** Can view the catalog and filter by artist.
  * **Admin/Authorized User:** Inherits all standard user permissions and has the ability to add new albums to the database.

### 2 Album Catalog

* **Catalog Display:** A responsive grid or list view displaying all available albums in the store.
* **Album Details:** Each album entry should include:
  * Cover Image.
  * Title.
  * Artist name.
  * Genre/Year (Optional).
  * Tracklist (retrieved from the scraping process).

### 3 Search and Filtering

* **Filter by Artist:** Users must be able to filter the catalog to display only albums belonging to a specific artist.
* **Quick Search:** (Optional) Search by album title or artist name.

### 4 Album Management (Admin Only)

* **Add New Album:** Authorized users can access a form to input new album data (Title, Artist, Songs, Image URL).
* **Database Integration:** Newly added albums must be persisted in the PostgreSQL database and trigger an SSG rebuild to reflect changes in the static frontend.

<br>

## 2. System Exclusions (Out of Scope)

To maintain focus on the SSG and ETL process, the following features are **explicitly excluded**:

* **Shopping Cart:** No persistent cart for selecting multiple items.
* **Purchase Functionality:** No payment gateway integration or transaction processing.
* **User Profiles:** No detailed "My Account" pages beyond login/logout status.

<br>

## 3. Technical & Non-Functional Requirements

* **Static Site Generation:** The frontend must be served as flat HTML/CSS files.
* **Security:** (Optional)
  * Passwords must be stored using secure hashing.
* **Responsive Design:** The UI must be accessible on both desktop and mobile devices.
