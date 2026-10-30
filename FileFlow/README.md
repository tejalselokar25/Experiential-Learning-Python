# FileFlow — Enterprise Cloud Directory Simulator

A premium, modern SaaS web application that simulates a real-world cloud directory structure (inspired by Google Drive, Dropbox, and contemporary cloud platforms).

Built with **Python + Streamlit**, featuring a synchronized **Frontend Web Preview** in HTML5/CSS3/JavaScript.

---

## 🌟 Key Features

* **SaaS Design System**: Deep Navy (`#142B4D`) & Royal Blue (`#3478D4`) corporate palette, soft neutral borders, custom typography (Inter), rounded cards, and smooth micro-interactions.
* **Persistent Sidebar Navigation**: Quick actions for creating items, responsive navigation links (Dashboard, My Files, Recent Files, Folders Tree, Search, Trash, Settings), live storage quota gauge, and user profile badges.
* **Executive Dashboard**:
  - Live statistics cards (Total Files, Total Folders, Storage Consumed, Operational Health).
  - Categorized storage distribution bars (Documents, Code, Data, Media, Other).
  - Recent files feed with direct file inspector links.
* **Enterprise File Explorer**:
  - Visual breadcrumb navigation path with direct parent jumping (`⬆ Up`).
  - Dual view modes: **Grid View** & **List View**.
  - Folder & file item cards with extension badge recognition (`.txt`, `.py`, `.json`, `.md`, etc.).
  - Side Inspector drawer showing full system path, file size in bytes/KB, parent directory, creation/modification timestamps, and live formatted code preview.
* **Modal Dialog System**:
  - New Folder creation with parent directory selection.
  - New File creation with templates (Text, Markdown, Python, JSON, Log).
  - In-place file text editing with live word/character counters.
  - Safe rename with automated cascading path updates for child folders.
  - Soft-delete confirmation with nested item count warnings.
* **Search Index**:
  - Multi-attribute search scanning file names, full paths, and text contents within files.
  - Match classification pills (`Matched in Name`, `Matched in Path`, `Matched in Content`).
* **Trash & Recovery Bin**:
  - Soft-deleted items are safely preserved.
  - Restore with cascading hierarchy reconstruction or permanent purge.
* **JSON Schema Backup & Restore**:
  - One-click directory JSON download.
  - Schema restoration via JSON input with integrity validation.

---

## 🚀 Running the Project

### Option A: Run the Python / Streamlit Application (Recommended)

1. Make sure Python 3.10 or newer is installed.
2. Open a terminal in this project folder:
   ```bash
   pip install -r requirements.txt
   ```
3. Launch the Streamlit dashboard:
   ```bash
   streamlit run app.py
   ```
4. Streamlit will display the local URL (typically `http://localhost:8501`). Open it in your web browser.

### Option B: Standalone Web Preview (`index.html`)

Double-click `index.html` or open it in any modern browser (Chrome, Edge, Safari, Firefox) for an instant zero-install interactive preview of the full SaaS dashboard with identical features.

---

## ☁️ Public Deployment (Streamlit Community Cloud)

1. Push this directory to your personal GitHub repository.
2. Visit [share.streamlit.io](https://share.streamlit.io/) and log in with your GitHub account.
3. Click **Create app**, select your repository, set the branch to `main`, and main file path to `app.py`.
4. Click **Deploy** to generate your public `https://<your-app>.streamlit.app` link.
