import streamlit as st
from datetime import datetime
import json
import re

# -----------------------------------------------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="FileFlow — Cloud Directory Manager",
    page_icon="📁",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# PREMIUM SAAS STYLING & DESIGN SYSTEM
# -----------------------------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

:root {
    --primary: #142B4D;
    --secondary: #3478D4;
    --secondary-hover: #2365BF;
    --bg: #F5F7FB;
    --cards: #FFFFFF;
    --text-main: #1E293B;
    --text-muted: #64748B;
    --borders: #E5EAF1;
    --accent: #EBF3FC;
    --accent-hover: #D8E7FA;
    --success: #10B981;
    --success-bg: #ECFDF5;
    --warning: #F59E0B;
    --warning-bg: #FFFBEB;
    --danger: #EF4444;
    --danger-bg: #FEF2F2;
}

/* Base resets & typography */
html, body, [class*="css"], .stApp {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
    background-color: var(--bg) !important;
    color: var(--text-main) !important;
}

.block-container {
    max-width: 1360px !important;
    padding-top: 1.2rem !important;
    padding-bottom: 3rem !important;
    padding-left: 2rem !important;
    padding-right: 2rem !important;
}

/* Sidebar Styling - Deep Navy SaaS Theme */
section[data-testid="stSidebar"] {
    background-color: #142B4D !important;
    border-right: 1px solid #1C355E !important;
}

section[data-testid="stSidebar"] div.stButton > button {
    border-radius: 9px !important;
    font-weight: 600 !important;
    font-size: 0.88rem !important;
    transition: all 0.2s ease !important;
    border: 1px solid rgba(255, 255, 255, 0.12) !important;
}

section[data-testid="stSidebar"] div.stButton > button[kind="primary"] {
    background-color: #3478D4 !important;
    color: #FFFFFF !important;
    border: none !important;
    box-shadow: 0 4px 12px rgba(52, 120, 212, 0.35) !important;
}
section[data-testid="stSidebar"] div.stButton > button[kind="primary"]:hover {
    background-color: #2563EB !important;
    transform: translateY(-1px) !important;
}

section[data-testid="stSidebar"] div.stButton > button[kind="secondary"] {
    background-color: rgba(255, 255, 255, 0.08) !important;
    color: #F8FAFC !important;
}
section[data-testid="stSidebar"] div.stButton > button[kind="secondary"]:hover {
    background-color: rgba(255, 255, 255, 0.16) !important;
    color: #FFFFFF !important;
}

/* Sidebar Radio Navigation */
section[data-testid="stSidebar"] div[data-testid="stRadio"] > label {
    display: none !important;
}
section[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] {
    gap: 4px !important;
}
section[data-testid="stSidebar"] div[data-testid="stRadio"] label[data-baseweb="radio"] {
    background: transparent !important;
    border-radius: 9px !important;
    padding: 8px 12px !important;
    margin: 0 !important;
    border: 1px solid transparent !important;
    transition: all 0.18s ease-in-out !important;
    cursor: pointer !important;
    width: 100% !important;
}
section[data-testid="stSidebar"] div[data-testid="stRadio"] label[data-baseweb="radio"]:hover {
    background: rgba(255, 255, 255, 0.07) !important;
}
section[data-testid="stSidebar"] div[data-testid="stRadio"] label[data-baseweb="radio"]:has(input:checked) {
    background: #3478D4 !important;
    box-shadow: 0 4px 12px rgba(52, 120, 212, 0.3) !important;
}
section[data-testid="stSidebar"] div[data-testid="stRadio"] label[data-baseweb="radio"] div:first-child {
    display: none !important; /* Hide native radio bullet */
}
section[data-testid="stSidebar"] div[data-testid="stRadio"] label[data-baseweb="radio"] div:last-child {
    color: #CBD5E1 !important;
    font-size: 0.90rem !important;
    font-weight: 500 !important;
    letter-spacing: -0.01em !important;
}
section[data-testid="stSidebar"] div[data-testid="stRadio"] label[data-baseweb="radio"]:has(input:checked) div:last-child {
    color: #FFFFFF !important;
    font-weight: 600 !important;
}

/* Main Area Card Styling */
.ff-card {
    background: #FFFFFF;
    border: 1px solid var(--borders);
    border-radius: 14px;
    padding: 22px;
    box-shadow: 0 1px 3px rgba(20, 43, 77, 0.03), 0 4px 12px rgba(20, 43, 77, 0.02);
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    margin-bottom: 20px;
}
.ff-card:hover {
    box-shadow: 0 6px 20px rgba(20, 43, 77, 0.06);
    border-color: #D6E0EC;
}

/* Metric / Stat Cards */
.ff-stat-card {
    background: #FFFFFF;
    border: 1px solid var(--borders);
    border-radius: 14px;
    padding: 18px 20px;
    display: flex;
    align-items: center;
    gap: 16px;
    box-shadow: 0 1px 3px rgba(20, 43, 77, 0.03), 0 4px 10px rgba(20, 43, 77, 0.02);
    transition: transform 0.18s ease, box-shadow 0.18s ease, border-color 0.18s ease;
}
.ff-stat-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(20, 43, 77, 0.06);
    border-color: #D3DEEC;
}
.ff-stat-icon {
    width: 48px;
    height: 48px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 22px;
    flex-shrink: 0;
}
.ff-stat-blue { background: #EBF3FC; color: #3478D4; }
.ff-stat-navy { background: #EAEFF7; color: #142B4D; }
.ff-stat-emerald { background: #ECFDF5; color: #10B981; }
.ff-stat-amber { background: #FFFBEB; color: #F59E0B; }

.ff-stat-title {
    font-size: 0.80rem;
    font-weight: 600;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.04em;
    margin-bottom: 4px;
}
.ff-stat-value {
    font-size: 1.55rem;
    font-weight: 700;
    color: var(--primary);
    line-height: 1.1;
}
.ff-stat-badge {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    font-size: 0.72rem;
    font-weight: 600;
    color: #10B981;
    background: #ECFDF5;
    padding: 2px 7px;
    border-radius: 20px;
    margin-top: 4px;
}

/* Welcome Hero Banner */
.ff-hero {
    background: linear-gradient(135deg, #142B4D 0%, #1A3966 60%, #245BA7 100%);
    border-radius: 18px;
    padding: 28px 32px;
    color: #FFFFFF;
    margin-bottom: 24px;
    box-shadow: 0 10px 30px rgba(20, 43, 77, 0.12);
    position: relative;
    overflow: hidden;
}
.ff-hero::after {
    content: "";
    position: absolute;
    top: -40px;
    right: -40px;
    width: 240px;
    height: 240px;
    background: radial-gradient(circle, rgba(52, 120, 212, 0.25) 0%, rgba(20, 43, 77, 0) 70%);
    border-radius: 50%;
    pointer-events: none;
}
.ff-hero-eyebrow {
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #9FC6FF;
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 8px;
}
.ff-hero-eyebrow span.pulse {
    width: 8px;
    height: 8px;
    background: #10B981;
    border-radius: 50%;
    display: inline-block;
    box-shadow: 0 0 8px #10B981;
}
.ff-hero-title {
    font-size: 1.95rem;
    font-weight: 800;
    margin: 0;
    letter-spacing: -0.02em;
    color: #FFFFFF;
}
.ff-hero-desc {
    font-size: 0.95rem;
    color: #D6E4FA;
    margin-top: 6px;
    margin-bottom: 0;
    max-width: 650px;
    line-height: 1.5;
}

/* Item Badges & Tags */
.ff-badge {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    padding: 3px 9px;
    border-radius: 6px;
    font-size: 0.76rem;
    font-weight: 600;
}
.ff-badge-folder { background: #EBF3FC; color: #2B6CB0; }
.ff-badge-file { background: #F1F5F9; color: #475569; }
.ff-badge-code { background: #ECFDF5; color: #047857; }
.ff-badge-data { background: #FEF3C7; color: #B45309; }
.ff-badge-danger { background: #FEE2E2; color: #B91C1C; }

/* Breadcrumbs */
.ff-breadcrumbs-container {
    background: #FFFFFF;
    border: 1px solid var(--borders);
    border-radius: 12px;
    padding: 10px 16px;
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 18px;
    font-size: 0.88rem;
    box-shadow: 0 1px 3px rgba(20, 43, 77, 0.02);
}

/* Folder / File Card Component */
.ff-grid-card {
    background: #FFFFFF;
    border: 1px solid var(--borders);
    border-radius: 12px;
    padding: 16px;
    transition: all 0.18s ease-in-out;
    cursor: pointer;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}
.ff-grid-card:hover {
    border-color: #3478D4;
    transform: translateY(-2px);
    box-shadow: 0 6px 18px rgba(52, 120, 212, 0.09);
    background: #FCFDFF;
}
.ff-grid-card.selected {
    border: 2px solid #3478D4;
    background: #F8FAFD;
}

/* Inspector Drawer Panel */
.ff-inspector {
    background: #FFFFFF;
    border: 1px solid var(--borders);
    border-radius: 14px;
    padding: 22px;
    box-shadow: 0 2px 12px rgba(20, 43, 77, 0.04);
}
.ff-inspector-title {
    font-size: 1.15rem;
    font-weight: 700;
    color: var(--primary);
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 14px;
}
.ff-code-preview {
    font-family: 'JetBrains Mono', ui-monospace, monospace;
    font-size: 0.84rem;
    background: #0F172A;
    color: #E2E8F0;
    padding: 16px;
    border-radius: 10px;
    max-height: 280px;
    overflow-y: auto;
    border: 1px solid #1E293B;
    line-height: 1.5;
}

/* Clean Form Controls in Main Area */
div[data-testid="stTextInput"] input,
div[data-testid="stSelectbox"] div[data-baseweb="select"] > div,
div[data-testid="stTextArea"] textarea {
    border-radius: 9px !important;
    border-color: #D3DDEB !important;
    font-size: 0.90rem !important;
}
div[data-testid="stTextInput"] input:focus,
div[data-testid="stTextArea"] textarea:focus {
    border-color: #3478D4 !important;
    box-shadow: 0 0 0 2px rgba(52, 120, 212, 0.15) !important;
}

/* Standard Buttons */
div.stButton > button {
    border-radius: 9px !important;
    font-weight: 600 !important;
    font-size: 0.88rem !important;
    transition: all 0.18s ease !important;
}
div.stButton > button[kind="primary"] {
    background-color: #3478D4 !important;
    border-color: #3478D4 !important;
}
div.stButton > button[kind="primary"]:hover {
    background-color: #2563EB !important;
    border-color: #2563EB !important;
    transform: translateY(-1px) !important;
}

/* Modern Expander */
div[data-testid="stExpander"] {
    background: #FFFFFF !important;
    border: 1px solid var(--borders) !important;
    border-radius: 12px !important;
    box-shadow: 0 1px 3px rgba(20, 43, 77, 0.02) !important;
    margin-bottom: 10px !important;
}

/* Empty State Box */
.ff-empty-state {
    text-align: center;
    padding: 48px 24px;
    background: #FFFFFF;
    border: 1px dashed #CBD5E1;
    border-radius: 14px;
    margin: 16px 0;
}
.ff-empty-icon {
    font-size: 2.8rem;
    margin-bottom: 12px;
    display: inline-block;
    filter: drop-shadow(0 4px 8px rgba(20, 43, 77, 0.08));
}
.ff-empty-title {
    font-size: 1.1rem;
    font-weight: 700;
    color: var(--primary);
    margin-bottom: 6px;
}
.ff-empty-desc {
    font-size: 0.88rem;
    color: var(--text-muted);
    max-width: 440px;
    margin: 0 auto 16px auto;
}
</style>
""", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# HELPER FUNCTIONS & TIME
# -----------------------------------------------------------------------------
def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M")


def format_bytes(num_bytes):
    if num_bytes < 1024:
        return f"{num_bytes} B"
    elif num_bytes < 1024 * 1024:
        return f"{num_bytes / 1024:.1f} KB"
    else:
        return f"{num_bytes / (1024 * 1024):.1f} MB"


def get_item_extension(path):
    if "/" in path:
        filename = path.rsplit("/", 1)[-1]
    else:
        filename = path
    if "." in filename and not filename.startswith("."):
        return filename.rsplit(".", 1)[-1].lower()
    return "txt"


def get_file_type_meta(extension):
    code_exts = {"py", "js", "ts", "html", "css", "cpp", "c", "java", "sql", "sh"}
    data_exts = {"json", "csv", "xml", "yaml", "yml"}
    media_exts = {"png", "jpg", "jpeg", "svg", "gif", "mp4", "pdf"}
    doc_exts = {"md", "txt", "doc", "docx", "rtf"}

    if extension in code_exts:
        return "Code / Script", "ff-badge-code", "💻"
    elif extension in data_exts:
        return "Data Structure", "ff-badge-data", "📊"
    elif extension in media_exts:
        return "Media Asset", "ff-badge-file", "🖼️"
    elif extension in doc_exts:
        return "Document", "ff-badge-file", "📄"
    return "File", "ff-badge-file", "📄"


# -----------------------------------------------------------------------------
# SESSION STATE INITIALIZATION
# -----------------------------------------------------------------------------
if "nodes" not in st.session_state:
    st.session_state.nodes = {
        "/": {
            "type": "folder",
            "parent": None,
            "created": now(),
            "updated": now(),
            "content": "",
            "description": "Root workspace directory"
        },
        "/Documents": {
            "type": "folder",
            "parent": "/",
            "created": now(),
            "updated": now(),
            "content": "",
            "description": "Company policies and guides"
        },
        "/Projects": {
            "type": "folder",
            "parent": "/",
            "created": now(),
            "updated": now(),
            "content": "",
            "description": "Active engineering workflows"
        },
        "/Images": {
            "type": "folder",
            "parent": "/",
            "created": now(),
            "updated": now(),
            "content": "",
            "description": "Brand assets and design mockups"
        },
        "/Documents/Welcome.txt": {
            "type": "file",
            "parent": "/Documents",
            "created": now(),
            "updated": now(),
            "content": "Welcome to FileFlow Enterprise Drive!\n\nThis platform simulates a real-world hierarchical file directory structure.\n- Create folders and multi-format files\n- Navigate with breadcrumbs and tree views\n- Inspect, edit, rename, and soft-delete files with trash recovery\n- Export complete directory schemas as JSON",
        },
        "/Projects/ideas.txt": {
            "type": "file",
            "parent": "/Projects",
            "created": now(),
            "updated": now(),
            "content": "FileFlow Strategic Roadmap 2026:\n1. Cloud storage provider synchronization\n2. Real-time multi-user document collaboration\n3. Zero-knowledge cryptographic file encryption\n4. Smart tag classification and semantic indexing",
        },
        "/Projects/config.json": {
            "type": "file",
            "parent": "/Projects",
            "created": now(),
            "updated": now(),
            "content": '{\n  "app": "FileFlow",\n  "environment": "production",\n  "version": "2.4.0",\n  "cloudStorageQuotaMB": 100,\n  "autoSync": true\n}',
        }
    }

if "trash" not in st.session_state:
    st.session_state.trash = {}

if "current_folder" not in st.session_state:
    st.session_state.current_folder = "/"

if "selected_item" not in st.session_state:
    st.session_state.selected_item = "/Documents/Welcome.txt"

if "view_mode" not in st.session_state:
    st.session_state.view_mode = "Grid"

if "active_nav" not in st.session_state:
    st.session_state.active_nav = "Dashboard"

nodes = st.session_state.nodes
trash = st.session_state.trash

# Ensure selected item exists, otherwise reset
if st.session_state.selected_item and st.session_state.selected_item not in nodes:
    st.session_state.selected_item = None

# Ensure current folder exists
if st.session_state.current_folder not in nodes or nodes[st.session_state.current_folder]["type"] != "folder":
    st.session_state.current_folder = "/"


# -----------------------------------------------------------------------------
# DIRECTORY OPERATIONS LOGIC
# -----------------------------------------------------------------------------
def get_children(path):
    """Returns sorted child items with folders first, then files."""
    kids = [p for p, v in nodes.items() if v.get("parent") == path]
    folders_list = sorted([p for p in kids if nodes[p]["type"] == "folder"], key=lambda x: x.lower())
    files_list = sorted([p for p in kids if nodes[p]["type"] == "file"], key=lambda x: x.lower())
    return folders_list + files_list


def calculate_storage():
    """Calculates storage in bytes and category percentages."""
    total_bytes = 0
    cat_bytes = {"Documents": 0, "Code": 0, "Data": 0, "Media": 0, "Other": 0}

    for path, meta in nodes.items():
        if meta["type"] == "file":
            b = len(meta.get("content", "").encode("utf-8"))
            total_bytes += b
            ext = get_item_extension(path)
            meta_type, _, _ = get_file_type_meta(ext)
            if "Document" in meta_type:
                cat_bytes["Documents"] += b
            elif "Code" in meta_type:
                cat_bytes["Code"] += b
            elif "Data" in meta_type:
                cat_bytes["Data"] += b
            elif "Media" in meta_type:
                cat_bytes["Media"] += b
            else:
                cat_bytes["Other"] += b

    return total_bytes, cat_bytes


def add_item(parent, name, kind, content=""):
    """Adds a new folder or file."""
    clean_name = name.strip().strip("/")
    if not clean_name or "/" in clean_name or "\\" in clean_name or clean_name in {".", ".."}:
        return False, "Invalid name. Avoid slash characters or reserved path symbols."
    if parent not in nodes or nodes[parent]["type"] != "folder":
        return False, "The selected parent folder does not exist."
    new_path = ("" if parent == "/" else parent) + "/" + clean_name
    if new_path in nodes:
        return False, f"An item named '{clean_name}' already exists in this folder."
    
    timestamp = now()
    nodes[new_path] = {
        "type": kind,
        "parent": parent,
        "created": timestamp,
        "updated": timestamp,
        "content": content if kind == "file" else ""
    }
    return True, f"{kind.title()} '{clean_name}' created successfully."


def rename_item(old_path, new_name):
    """Renames an item and updates all child paths if it is a folder."""
    if old_path == "/":
        return False, "Root directory cannot be renamed."
    if old_path not in nodes:
        return False, "Item does not exist."
    
    clean_name = new_name.strip().strip("/")
    if not clean_name or "/" in clean_name or "\\" in clean_name:
        return False, "Invalid name. Do not use slash characters."
    
    parent = nodes[old_path]["parent"]
    new_path = ("" if parent == "/" else parent) + "/" + clean_name
    if new_path in nodes:
        return False, f"An item with the name '{clean_name}' already exists in this folder."

    # Rename old_path and all cascading child paths
    targets = [p for p in nodes if p == old_path or p.startswith(old_path + "/")]
    migrated = {}
    timestamp = now()

    for p in targets:
        suffix = p[len(old_path):]
        updated_p = new_path + suffix
        entry = dict(nodes[p])
        entry["updated"] = timestamp
        if p == old_path:
            entry["parent"] = parent
        else:
            old_parent = entry["parent"]
            entry["parent"] = new_path + old_parent[len(old_path):]
        migrated[updated_p] = entry

    for p in targets:
        nodes.pop(p, None)
    nodes.update(migrated)

    # Update active selections
    if st.session_state.current_folder == old_path or st.session_state.current_folder.startswith(old_path + "/"):
        st.session_state.current_folder = new_path + st.session_state.current_folder[len(old_path):]
    if st.session_state.selected_item == old_path or (st.session_state.selected_item and st.session_state.selected_item.startswith(old_path + "/")):
        st.session_state.selected_item = new_path + st.session_state.selected_item[len(old_path):]

    return True, f"Renamed to '{clean_name}'."


def soft_delete_item(path):
    """Moves an item and all descendants into Trash."""
    if path == "/" or path not in nodes:
        return 0
    targets = [p for p in nodes if p == path or p.startswith(path + "/")]
    count = 0
    timestamp = now()
    for p in sorted(targets, key=len, reverse=True):
        entry = nodes.pop(p)
        entry["deleted_at"] = timestamp
        entry["original_path"] = p
        trash[p] = entry
        count += 1

    # Adjust current folder if it was deleted
    if st.session_state.current_folder == path or st.session_state.current_folder.startswith(path + "/"):
        st.session_state.current_folder = "/"
    if st.session_state.selected_item == path or (st.session_state.selected_item and st.session_state.selected_item.startswith(path + "/")):
        st.session_state.selected_item = None
    return count


def restore_from_trash(path):
    """Restores an item and its descendants from Trash."""
    targets = [p for p in trash if p == path or p.startswith(path + "/")]
    if not targets:
        return False, "Item not found in Trash."
    
    # Sort shallowest first to recreate parents before children
    for p in sorted(targets, key=len):
        entry = trash.pop(p)
        parent = entry.get("parent")
        # Ensure parent exists, otherwise recreate as a folder under root
        if parent and parent not in nodes and parent != "/":
            nodes[parent] = {
                "type": "folder",
                "parent": "/",
                "created": now(),
                "updated": now(),
                "content": ""
            }
        entry.pop("deleted_at", None)
        entry.pop("original_path", None)
        entry["updated"] = now()
        nodes[p] = entry
    return True, f"Restored {len(targets)} item(s) from Trash."


def permanent_delete(path):
    """Permanently deletes item and descendants from Trash."""
    targets = [p for p in trash if p == path or p.startswith(path + "/")]
    for p in targets:
        trash.pop(p, None)
    return len(targets)


def reset_to_demo():
    """Resets to factory state."""
    st.session_state.nodes = {
        "/": {"type": "folder", "parent": None, "created": now(), "updated": now(), "content": "", "description": "Root workspace directory"},
        "/Documents": {"type": "folder", "parent": "/", "created": now(), "updated": now(), "content": "", "description": "Company policies and guides"},
        "/Projects": {"type": "folder", "parent": "/", "created": now(), "updated": now(), "content": "", "description": "Active engineering workflows"},
        "/Images": {"type": "folder", "parent": "/", "created": now(), "updated": now(), "content": "", "description": "Brand assets and design mockups"},
        "/Documents/Welcome.txt": {"type": "file", "parent": "/Documents", "created": now(), "updated": now(), "content": "Welcome to FileFlow Enterprise Drive!\n\nManage your simulated virtual file directory with modern ease."},
        "/Projects/ideas.txt": {"type": "file", "parent": "/Projects", "created": now(), "updated": now(), "content": "1. Cloud synchronization\n2. Real-time document preview\n3. JSON structural schema backup"}
    }
    st.session_state.trash = {}
    st.session_state.current_folder = "/"
    st.session_state.selected_item = "/Documents/Welcome.txt"


# -----------------------------------------------------------------------------
# MODAL DIALOGS (st.dialog)
# -----------------------------------------------------------------------------
@st.dialog("Create New Folder")
def modal_create_folder(default_parent="/"):
    st.markdown("<p style='color:#64748B; font-size:0.9rem; margin-top:-8px;'>Add a subfolder to organize your workspace files.</p>", unsafe_allow_html=True)
    all_folders = [p for p, v in nodes.items() if v["type"] == "folder"]
    folder_idx = all_folders.index(default_parent) if default_parent in all_folders else 0
    parent = st.selectbox("Parent Directory", all_folders, index=folder_idx, format_func=lambda x: "Root ( / )" if x == "/" else x)
    folder_name = st.text_input("Folder Name", placeholder="e.g. Invoices, Reports, or Archive")
    
    col_can, col_sub = st.columns([1, 1])
    with col_can:
        if st.button("Cancel", use_container_width=True):
            st.rerun()
    with col_sub:
        if st.button("Create Folder", type="primary", use_container_width=True):
            if not folder_name.strip():
                st.error("Please enter a valid folder name.")
            else:
                ok, msg = add_item(parent, folder_name, "folder")
                if ok:
                    st.toast(msg, icon="📁")
                    st.rerun()
                else:
                    st.error(msg)


@st.dialog("Create New File")
def modal_create_file(default_parent="/"):
    st.markdown("<p style='color:#64748B; font-size:0.9rem; margin-top:-8px;'>Create a text, code, or structured data file.</p>", unsafe_allow_html=True)
    all_folders = [p for p, v in nodes.items() if v["type"] == "folder"]
    folder_idx = all_folders.index(default_parent) if default_parent in all_folders else 0
    parent = st.selectbox("Destination Folder", all_folders, index=folder_idx, format_func=lambda x: "Root ( / )" if x == "/" else x)
    
    file_type = st.selectbox("File Template", ["Text Document (.txt)", "Markdown Document (.md)", "Python Script (.py)", "JSON Configuration (.json)", "Log File (.log)"])
    ext_map = {"Text Document (.txt)": "txt", "Markdown Document (.md)": "md", "Python Script (.py)": "py", "JSON Configuration (.json)": "json", "Log File (.log)": "log"}
    chosen_ext = ext_map[file_type]
    
    file_name = st.text_input("File Name", placeholder=f"e.g. notes.{chosen_ext}")
    
    default_placeholders = {
        "txt": "Write notes or documents here...",
        "md": "# Title\n\n- Point 1\n- Point 2",
        "py": "#!/usr/bin/env python3\n\ndef main():\n    print('Hello FileFlow')\n\nif __name__ == '__main__':\n    main()",
        "json": '{\n  "version": "1.0",\n  "enabled": true\n}',
        "log": f"[{now()}] System initialization logged."
    }
    
    content = st.text_area("File Content", value=default_placeholders.get(chosen_ext, ""), height=150)
    
    col_can, col_sub = st.columns([1, 1])
    with col_can:
        if st.button("Cancel", use_container_width=True):
            st.rerun()
    with col_sub:
        if st.button("Create File", type="primary", use_container_width=True):
            name_final = file_name.strip()
            if not name_final:
                st.error("Please provide a file name.")
            else:
                if "." not in name_final:
                    name_final = f"{name_final}.{chosen_ext}"
                ok, msg = add_item(parent, name_final, "file", content)
                if ok:
                    st.toast(msg, icon="📄")
                    st.session_state.selected_item = ("" if parent == "/" else parent) + "/" + name_final
                    st.rerun()
                else:
                    st.error(msg)


@st.dialog("Rename Item")
def modal_rename(target_path):
    item_info = nodes.get(target_path)
    if not item_info:
        st.warning("Item not found.")
        return
    old_name = target_path.rsplit("/", 1)[-1]
    st.markdown(f"<p style='color:#64748B; font-size:0.9rem;'>Rename <strong>{old_name}</strong> in its parent folder.</p>", unsafe_allow_html=True)
    new_name = st.text_input("New Name", value=old_name)
    
    col_can, col_sub = st.columns([1, 1])
    with col_can:
        if st.button("Cancel", use_container_width=True):
            st.rerun()
    with col_sub:
        if st.button("Save Name", type="primary", use_container_width=True):
            ok, msg = rename_item(target_path, new_name)
            if ok:
                st.toast(msg, icon="✏️")
                st.rerun()
            else:
                st.error(msg)


@st.dialog("Move to Trash")
def modal_delete_confirm(target_path):
    item_info = nodes.get(target_path)
    if not item_info:
        st.warning("Item not found.")
        return
    name = target_path.rsplit("/", 1)[-1]
    is_folder = item_info["type"] == "folder"
    descendants = [p for p in nodes if p.startswith(target_path + "/")]
    
    st.markdown(f"""
    <div style='background:#FEF2F2; border:1px solid #FCA5A5; border-radius:10px; padding:14px; margin-bottom:14px;'>
      <div style='color:#991B1B; font-weight:700; font-size:0.95rem; margin-bottom:4px;'>Confirm Deletion</div>
      <div style='color:#B91C1C; font-size:0.88rem;'>
        Are you sure you want to delete <strong>{name}</strong>?
        {f"<br><em>Warning: This folder contains {len(descendants)} nested items which will also be moved to Trash.</em>" if is_folder and descendants else ""}
      </div>
    </div>
    """, unsafe_allow_html=True)
    
    col_can, col_sub = st.columns([1, 1])
    with col_can:
        if st.button("Cancel", use_container_width=True):
            st.rerun()
    with col_sub:
        if st.button("Move to Trash", type="primary", use_container_width=True):
            count = soft_delete_item(target_path)
            st.toast(f"Moved {count} item(s) to Trash.", icon="🗑️")
            st.rerun()


@st.dialog("Edit File Content", width="large")
def modal_edit_file(target_path):
    item_info = nodes.get(target_path)
    if not item_info or item_info["type"] != "file":
        st.warning("File not found.")
        return
    filename = target_path.rsplit("/", 1)[-1]
    st.markdown(f"<p style='color:#64748B; font-size:0.9rem; margin-top:-8px;'>Editing: <code>{target_path}</code></p>", unsafe_allow_html=True)
    
    edited_text = st.text_area("File Content", value=item_info.get("content", ""), height=320)
    char_count = len(edited_text)
    word_count = len(edited_text.split())
    st.caption(f"Stats: {char_count:,} characters · {word_count:,} words · {format_bytes(len(edited_text.encode('utf-8')))}")
    
    col_can, col_sub = st.columns([1, 1])
    with col_can:
        if st.button("Discard Changes", use_container_width=True):
            st.rerun()
    with col_sub:
        if st.button("Save Changes", type="primary", use_container_width=True):
            nodes[target_path]["content"] = edited_text
            nodes[target_path]["updated"] = now()
            st.toast("File saved successfully.", icon="💾")
            st.rerun()


@st.dialog("Empty Trash")
def modal_empty_trash():
    st.markdown("""
    <div style='background:#FEF2F2; border:1px solid #FCA5A5; border-radius:10px; padding:14px; margin-bottom:14px;'>
      <div style='color:#991B1B; font-weight:700; font-size:0.95rem; margin-bottom:4px;'>Empty All Items?</div>
      <div style='color:#B91C1C; font-size:0.88rem;'>
        This will permanently purge all items currently in the Trash. This action cannot be reversed.
      </div>
    </div>
    """, unsafe_allow_html=True)
    col_can, col_sub = st.columns([1, 1])
    with col_can:
        if st.button("Cancel", use_container_width=True):
            st.rerun()
    with col_sub:
        if st.button("Purge Permanently", type="primary", use_container_width=True):
            trash_count = len(st.session_state.trash)
            st.session_state.trash.clear()
            st.toast(f"Permanently purged {trash_count} item(s).", icon="🔥")
            st.rerun()


# -----------------------------------------------------------------------------
# SIDEBAR NAVIGATION & PROFILE
# -----------------------------------------------------------------------------
with st.sidebar:
    # Brand Header
    st.markdown("""
    <div style='display:flex; align-items:center; gap:12px; padding:10px 4px 20px 4px;'>
      <div style='width:40px; height:40px; background:linear-gradient(135deg, #3478D4, #1B4C94); border-radius:10px; display:flex; align-items:center; justify-content:center; box-shadow:0 4px 12px rgba(52,120,212,0.4);'>
        <span style='font-size:22px;'>📁</span>
      </div>
      <div>
        <div style='color:#FFFFFF; font-size:1.25rem; font-weight:800; letter-spacing:-0.02em; line-height:1.1;'>FileFlow</div>
        <div style='color:#8EA9D1; font-size:0.75rem; font-weight:600; letter-spacing:0.04em; text-transform:uppercase;'>SaaS Cloud Drive</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Quick Action Buttons
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        if st.button("+ Folder", key="sb_new_folder", use_container_width=True, help="Create a folder in current directory"):
            modal_create_folder(st.session_state.current_folder)
    with col_f2:
        if st.button("+ File", key="sb_new_file", type="primary", use_container_width=True, help="Create a new document"):
            modal_create_file(st.session_state.current_folder)

    st.markdown("<div style='height:14px;'></div>", unsafe_allow_html=True)

    # Navigation menu
    trash_badge = f" ({len(trash)})" if trash else ""
    nav_options = [
        "📊 Dashboard",
        "📁 My Files",
        "🕒 Recent Files",
        "🗂️ Folders Tree",
        "🔍 Search",
        f"🗑️ Trash{trash_badge}",
        "⚙️ Settings & Export"
    ]

    # Map current active nav to select index
    default_idx = 0
    for i, opt in enumerate(nav_options):
        if st.session_state.active_nav in opt:
            default_idx = i
            break

    selected_nav = st.radio("Navigation", nav_options, index=default_idx, label_visibility="collapsed")
    clean_nav_name = selected_nav.split()[1]
    if clean_nav_name != st.session_state.active_nav:
        st.session_state.active_nav = clean_nav_name
        st.rerun()

    st.markdown("<hr style='border:0; border-top:1px solid #1E3A63; margin:22px 0;'>", unsafe_allow_html=True)

    # Storage Quota Meter
    total_bytes, _ = calculate_storage()
    quota_mb = 100
    used_mb = total_bytes / (1024 * 1024)
    pct_used = min(100.0, max(0.5, (used_mb / quota_mb) * 100))

    st.markdown(f"""
    <div style='background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.08); border-radius:12px; padding:14px; margin-bottom:18px;'>
      <div style='display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;'>
        <span style='color:#CBD5E1; font-size:0.80rem; font-weight:600;'>Storage Used</span>
        <span style='color:#60A5FA; font-size:0.78rem; font-weight:700;'>{format_bytes(total_bytes)}</span>
      </div>
      <div style='background:rgba(255,255,255,0.12); border-radius:10px; height:7px; width:100%; overflow:hidden;'>
        <div style='background:linear-gradient(90deg, #3478D4, #60A5FA); height:100%; width:{pct_used:.1f}%; border-radius:10px;'></div>
      </div>
      <div style='display:flex; justify-content:space-between; color:#8EA9D1; font-size:0.72rem; margin-top:6px;'>
        <span>Enterprise Quota</span>
        <span>100 MB Limit</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # User Profile Section
    st.markdown("""
    <div style='display:flex; align-items:center; gap:12px; padding:10px 4px;'>
      <div style='width:38px; height:38px; border-radius:50%; background:#245BA7; color:#FFFFFF; font-weight:700; font-size:0.9rem; display:flex; align-items:center; justify-content:center; border:2px solid #3478D4;'>
        AM
      </div>
      <div style='flex:1; min-width:0;'>
        <div style='color:#FFFFFF; font-size:0.86rem; font-weight:700; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;'>Alex Morgan</div>
        <div style='color:#8EA9D1; font-size:0.72rem; display:flex; align-items:center; gap:5px;'>
          <span style='width:6px; height:6px; background:#10B981; border-radius:50%; display:inline-block;'></span>
          Workspace Admin
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# MAIN VIEW: DASHBOARD
# -----------------------------------------------------------------------------
all_folders = [p for p, v in nodes.items() if v["type"] == "folder"]
all_files = [p for p, v in nodes.items() if v["type"] == "file"]
total_bytes, category_sizes = calculate_storage()

if st.session_state.active_nav == "Dashboard":
    # Hero Welcome Banner
    st.markdown("""
    <div class="ff-hero">
      <div class="ff-hero-eyebrow"><span class="pulse"></span> Cloud Workspace Active · Enterprise v2.4</div>
      <h1 class="ff-hero-title">Welcome back, Alex!</h1>
      <p class="ff-hero-desc">Manage your files, structured directories, and data hierarchies with high-fidelity SaaS controls and instant file inspection.</p>
    </div>
    """, unsafe_allow_html=True)

    # 4 Key Statistics Cards
    sc1, sc2, sc3, sc4 = st.columns(4)
    with sc1:
        st.markdown(f"""
        <div class="ff-stat-card">
          <div class="ff-stat-icon ff-stat-blue">📄</div>
          <div>
            <div class="ff-stat-title">Total Files</div>
            <div class="ff-stat-value">{len(all_files)}</div>
            <div class="ff-stat-badge">Synced Live</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

    with sc2:
        st.markdown(f"""
        <div class="ff-stat-card">
          <div class="ff-stat-icon ff-stat-navy">📁</div>
          <div>
            <div class="ff-stat-title">Total Folders</div>
            <div class="ff-stat-value">{len(all_folders) - 1}</div>
            <div class="ff-stat-badge">Active Tree</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

    with sc3:
        st.markdown(f"""
        <div class="ff-stat-card">
          <div class="ff-stat-icon ff-stat-emerald">💾</div>
          <div>
            <div class="ff-stat-title">Storage Used</div>
            <div class="ff-stat-value">{format_bytes(total_bytes)}</div>
            <div class="ff-stat-badge">{total_bytes} bytes</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

    with sc4:
        st.markdown(f"""
        <div class="ff-stat-card">
          <div class="ff-stat-icon ff-stat-amber">⚡</div>
          <div>
            <div class="ff-stat-title">System Status</div>
            <div class="ff-stat-value" style="font-size:1.25rem; color:#10B981;">Operational</div>
            <div class="ff-stat-badge">100% In-Memory</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height:24px;'></div>", unsafe_allow_html=True)

    # Storage breakdown & Recent Activity
    col_dash_left, col_dash_right = st.columns([1.4, 1], gap="large")

    with col_dash_left:
        st.markdown("<h3 style='font-size:1.15rem; font-weight:700; color:#142B4D; margin-bottom:14px;'>Recent Files</h3>", unsafe_allow_html=True)
        
        # Sort files by created / updated descending
        recent_files_sorted = sorted(all_files, key=lambda p: nodes[p].get("updated", nodes[p].get("created", "")), reverse=True)[:5]
        
        if recent_files_sorted:
            for rf in recent_files_sorted:
                item = nodes[rf]
                name = rf.rsplit("/", 1)[-1]
                ext = get_item_extension(name)
                type_label, badge_cls, icon = get_file_type_meta(ext)
                size_str = format_bytes(len(item.get("content", "").encode("utf-8")))
                parent_name = "Root" if item["parent"] == "/" else item["parent"].rsplit("/", 1)[-1]

                row_col1, row_col2, row_col3, row_col4 = st.columns([2.5, 1.2, 1.2, 1])
                with row_col1:
                    st.markdown(f"""
                    <div style='display:flex; align-items:center; gap:10px; padding:6px 0;'>
                      <span style='font-size:1.3rem;'>{icon}</span>
                      <div>
                        <div style='font-weight:600; font-size:0.92rem; color:#142B4D;'>{name}</div>
                        <div style='font-size:0.78rem; color:#64748B;'>in {parent_name}</div>
                      </div>
                    </div>
                    """, unsafe_allow_html=True)
                with row_col2:
                    st.markdown(f"<div style='padding-top:12px;'><span class='ff-badge {badge_cls}'>{type_label}</span></div>", unsafe_allow_html=True)
                with row_col3:
                    st.markdown(f"<div style='padding-top:12px; font-size:0.84rem; color:#64748B;'>{size_str}</div>", unsafe_allow_html=True)
                with row_col4:
                    if st.button("Open", key=f"dash_open_{rf}", use_container_width=True):
                        st.session_state.current_folder = item["parent"]
                        st.session_state.selected_item = rf
                        st.session_state.active_nav = "My"
                        st.rerun()
                st.markdown("<hr style='border:0; border-top:1px solid #EDF2F7; margin:6px 0;'>", unsafe_allow_html=True)
        else:
            st.info("No files created yet. Use the sidebar to add files.")

    with col_dash_right:
        st.markdown("<h3 style='font-size:1.15rem; font-weight:700; color:#142B4D; margin-bottom:14px;'>Storage Distribution</h3>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class="ff-card">
          <div style='font-weight:700; font-size:0.92rem; color:#142B4D; margin-bottom:8px;'>Category Allocation</div>
        """, unsafe_allow_html=True)

        for cat, b in category_sizes.items():
            pct = (b / total_bytes * 100) if total_bytes > 0 else 0
            st.markdown(f"""
            <div style='display:flex; justify-content:space-between; font-size:0.83rem; margin-top:10px; margin-bottom:4px;'>
              <span style='color:#475569; font-weight:500;'>{cat}</span>
              <span style='color:#142B4D; font-weight:700;'>{format_bytes(b)} ({pct:.0f}%)</span>
            </div>
            <div style='background:#F1F5F9; border-radius:6px; height:6px; width:100%; overflow:hidden;'>
              <div style='background:#3478D4; height:100%; width:{pct}%; border-radius:6px;'></div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("""
          <div style='margin-top:18px; padding-top:14px; border-top:1px solid #E5EAF1; font-size:0.80rem; color:#64748B;'>
            💡 Tip: Export your entire directory schema from the Settings & Export view anytime.
          </div>
        </div>
        """, unsafe_allow_html=True)

        # Quick action cards
        st.markdown("<div style='height:8px;'></div>", unsafe_allow_html=True)
        qa1, qa2 = st.columns(2)
        with qa1:
            if st.button("📁 Browse Directory", use_container_width=True):
                st.session_state.active_nav = "My"
                st.rerun()
        with qa2:
            if st.button("🔍 Search Index", use_container_width=True):
                st.session_state.active_nav = "Search"
                st.rerun()


# -----------------------------------------------------------------------------
# MAIN VIEW: MY FILES (FILE EXPLORER)
# -----------------------------------------------------------------------------
elif st.session_state.active_nav in ["My", "Files"]:
    curr = st.session_state.current_folder
    curr_name = "Root ( / )" if curr == "/" else curr.rsplit("/", 1)[-1]

    # Breadcrumb Navigation
    segments = []
    if curr == "/":
        segments = [("/", "Root")]
    else:
        parts = curr.split("/")
        accum = ""
        segments.append(("/", "Root"))
        for part in parts:
            if part:
                accum += "/" + part
                segments.append((accum, part))

    # Breadcrumb toolbar row
    b_cols = st.columns([len(segments) * 1.5, 3])
    with b_cols[0]:
        bc_html = "<div class='ff-breadcrumbs-container'><span>🏠</span>"
        for i, (path, label) in enumerate(segments):
            if i > 0:
                bc_html += "<span style='color:#94A3B8;'>›</span>"
            if path == curr:
                bc_html += f"<span style='color:#142B4D; font-weight:700;'>{label}</span>"
            else:
                bc_html += f"<span style='color:#3478D4; font-weight:600;'>{label}</span>"
        bc_html += "</div>"
        st.markdown(bc_html, unsafe_allow_html=True)

    with b_cols[1]:
        # Quick breadcrumb jump buttons
        if len(segments) > 1:
            jump_cols = st.columns(len(segments))
            for i, (path, label) in enumerate(segments):
                with jump_cols[i]:
                    if st.button(label[:10], key=f"bc_{path}_{i}", help=f"Go to {path}", use_container_width=True):
                        st.session_state.current_folder = path
                        st.rerun()

    # Toolbar row: Directory stats, Up button, New Folder, New File, View Toggle
    t1, t2, t3, t4, t5 = st.columns([2.5, 1, 1, 1, 1.2])
    with t1:
        st.markdown(f"""
        <div style='display:flex; align-items:center; gap:10px;'>
          <h2 style='font-size:1.35rem; font-weight:800; color:#142B4D; margin:0;'>{curr_name}</h2>
          <span class='ff-badge ff-badge-folder'>📁 {curr}</span>
        </div>
        """, unsafe_allow_html=True)
    with t2:
        if curr != "/":
            parent_path = nodes[curr]["parent"] or "/"
            if st.button("⬆ Up", use_container_width=True, help="Go to parent directory"):
                st.session_state.current_folder = parent_path
                st.rerun()
    with t3:
        if st.button("+ Folder", key="exp_new_folder", use_container_width=True):
            modal_create_folder(curr)
    with t4:
        if st.button("+ File", key="exp_new_file", type="primary", use_container_width=True):
            modal_create_file(curr)
    with t5:
        mode_choice = st.segmented_control("View", options=["Grid", "List"], default=st.session_state.view_mode, label_visibility="collapsed")
        if mode_choice and mode_choice != st.session_state.view_mode:
            st.session_state.view_mode = mode_choice
            st.rerun()

    st.markdown("<hr style='border:0; border-top:1px solid #E5EAF1; margin:16px 0 20px 0;'>", unsafe_allow_html=True)

    # Explorer Split View: Left (Directory Items), Right (Item Inspector)
    left_exp_col, right_exp_col = st.columns([1.5, 1], gap="large")

    with left_exp_col:
        children_paths = get_children(curr)
        folders_here = [p for p in children_paths if nodes[p]["type"] == "folder"]
        files_here = [p for p in children_paths if nodes[p]["type"] == "file"]

        if not folders_here and not files_here:
            st.markdown("""
            <div class="ff-empty-state">
              <div class="ff-empty-icon">📂</div>
              <div class="ff-empty-title">This folder is empty</div>
              <div class="ff-empty-desc">Create your first subfolder or text file using the buttons above.</div>
            </div>
            """, unsafe_allow_html=True)

        # 1. Folders Section
        if folders_here:
            st.markdown("<div style='font-size:0.80rem; font-weight:700; color:#64748B; text-transform:uppercase; letter-spacing:0.04em; margin-bottom:10px;'>Folders</div>", unsafe_allow_html=True)
            if st.session_state.view_mode == "Grid":
                f_cols = st.columns(2)
                for idx, fp in enumerate(folders_here):
                    fname = fp.rsplit("/", 1)[-1]
                    item_count = len(get_children(fp))
                    with f_cols[idx % 2]:
                        with st.container():
                            st.markdown(f"""
                            <div class="ff-grid-card">
                              <div style='display:flex; align-items:center; gap:10px;'>
                                <span style='font-size:1.6rem;'>📁</span>
                                <div>
                                  <div style='font-weight:700; font-size:0.95rem; color:#142B4D;'>{fname}</div>
                                  <div style='font-size:0.75rem; color:#64748B;'>{item_count} item(s)</div>
                                </div>
                              </div>
                            </div>
                            """, unsafe_allow_html=True)
                            c1, c2, c3 = st.columns([2, 1, 1])
                            with c1:
                                if st.button("Open", key=f"open_f_{fp}", use_container_width=True):
                                    st.session_state.current_folder = fp
                                    st.rerun()
                            with c2:
                                if st.button("✏️", key=f"ren_f_{fp}", help="Rename folder"):
                                    modal_rename(fp)
                            with c3:
                                if st.button("🗑️", key=f"del_f_{fp}", help="Delete folder"):
                                    modal_delete_confirm(fp)
                            st.markdown("<div style='height:8px;'></div>", unsafe_allow_html=True)
            else:
                # List View for Folders
                for fp in folders_here:
                    fname = fp.rsplit("/", 1)[-1]
                    item_count = len(get_children(fp))
                    r1, r2, r3, r4 = st.columns([3, 1, 1, 1])
                    with r1:
                        st.markdown(f"<div style='display:flex; align-items:center; gap:10px; padding:6px 0;'><span style='font-size:1.3rem;'>📁</span> <strong>{fname}</strong></div>", unsafe_allow_html=True)
                    with r2:
                        st.caption(f"{item_count} items")
                    with r3:
                        if st.button("Open", key=f"list_open_{fp}", use_container_width=True):
                            st.session_state.current_folder = fp
                            st.rerun()
                    with r4:
                        if st.button("🗑️", key=f"list_del_{fp}", use_container_width=True):
                            modal_delete_confirm(fp)
                    st.markdown("<hr style='border:0; border-top:1px solid #EDF2F7; margin:4px 0;'>", unsafe_allow_html=True)

        st.markdown("<div style='height:16px;'></div>", unsafe_allow_html=True)

        # 2. Files Section
        if files_here:
            st.markdown("<div style='font-size:0.80rem; font-weight:700; color:#64748B; text-transform:uppercase; letter-spacing:0.04em; margin-bottom:10px;'>Files</div>", unsafe_allow_html=True)
            if st.session_state.view_mode == "Grid":
                file_cols = st.columns(2)
                for idx, fp in enumerate(files_here):
                    item = nodes[fp]
                    fname = fp.rsplit("/", 1)[-1]
                    ext = get_item_extension(fname)
                    type_label, badge_cls, icon = get_file_type_meta(ext)
                    size_str = format_bytes(len(item.get("content", "").encode("utf-8")))
                    is_selected = st.session_state.selected_item == fp

                    with file_cols[idx % 2]:
                        selected_class = "selected" if is_selected else ""
                        st.markdown(f"""
                        <div class="ff-grid-card {selected_class}">
                          <div style='display:flex; align-items:center; justify-content:space-between; margin-bottom:8px;'>
                            <span style='font-size:1.6rem;'>{icon}</span>
                            <span class='ff-badge {badge_cls}'>{ext.upper()}</span>
                          </div>
                          <div>
                            <div style='font-weight:700; font-size:0.92rem; color:#142B4D; word-break:break-all;'>{fname}</div>
                            <div style='font-size:0.75rem; color:#64748B; margin-top:4px;'>{size_str} · {item.get('updated', item.get('created'))}</div>
                          </div>
                        </div>
                        """, unsafe_allow_html=True)
                        b1, b2, b3 = st.columns([2, 1, 1])
                        with b1:
                            btn_label = "Selected" if is_selected else "Inspect"
                            if st.button(btn_label, key=f"sel_f_{fp}", type="primary" if is_selected else "secondary", use_container_width=True):
                                st.session_state.selected_item = fp
                                st.rerun()
                        with b2:
                            if st.button("✏️", key=f"ren_file_{fp}", help="Rename file"):
                                modal_rename(fp)
                        with b3:
                            if st.button("🗑️", key=f"del_file_{fp}", help="Delete file"):
                                modal_delete_confirm(fp)
                        st.markdown("<div style='height:8px;'></div>", unsafe_allow_html=True)
            else:
                # List View for Files
                for fp in files_here:
                    item = nodes[fp]
                    fname = fp.rsplit("/", 1)[-1]
                    ext = get_item_extension(fname)
                    type_label, badge_cls, icon = get_file_type_meta(ext)
                    size_str = format_bytes(len(item.get("content", "").encode("utf-8")))
                    is_selected = st.session_state.selected_item == fp

                    r1, r2, r3, r4 = st.columns([2.5, 1.2, 1.2, 1])
                    with r1:
                        st.markdown(f"<div style='display:flex; align-items:center; gap:10px; padding:6px 0;'><span style='font-size:1.3rem;'>{icon}</span> <strong>{fname}</strong></div>", unsafe_allow_html=True)
                    with r2:
                        st.markdown(f"<div style='padding-top:10px;'><span class='ff-badge {badge_cls}'>{type_label}</span></div>", unsafe_allow_html=True)
                    with r3:
                        st.caption(f"{size_str}")
                    with r4:
                        if st.button("Inspect", key=f"list_sel_{fp}", use_container_width=True):
                            st.session_state.selected_item = fp
                            st.rerun()
                    st.markdown("<hr style='border:0; border-top:1px solid #EDF2F7; margin:4px 0;'>", unsafe_allow_html=True)

    # 3. Item Inspector Panel (Right Column)
    with right_exp_col:
        st.markdown("<h3 style='font-size:1.15rem; font-weight:700; color:#142B4D; margin-bottom:14px;'>Item Inspector</h3>", unsafe_allow_html=True)
        sel_path = st.session_state.selected_item

        if sel_path and sel_path in nodes:
            sel_item = nodes[sel_path]
            sel_name = sel_path.rsplit("/", 1)[-1]
            is_file = sel_item["type"] == "file"
            ext = get_item_extension(sel_name) if is_file else "folder"
            type_label, badge_cls, icon = get_file_type_meta(ext) if is_file else ("Directory Folder", "ff-badge-folder", "📁")
            size_str = format_bytes(len(sel_item.get("content", "").encode("utf-8"))) if is_file else f"{len(get_children(sel_path))} items"

            st.markdown(f"""
            <div class="ff-inspector">
              <div class="ff-inspector-title">
                <span style='font-size:1.8rem;'>{icon}</span>
                <div style='min-width:0; flex:1;'>
                  <div style='font-size:1.1rem; font-weight:800; color:#142B4D; word-break:break-all;'>{sel_name}</div>
                  <span class='ff-badge {badge_cls}'>{type_label}</span>
                </div>
              </div>
              <div style='background:#F8FAFD; border:1px solid #E5EAF1; border-radius:10px; padding:12px; margin:14px 0;'>
                <div style='font-size:0.75rem; color:#64748B; font-weight:700; text-transform:uppercase;'>System Path</div>
                <div style='font-family:monospace; font-size:0.85rem; color:#142B4D; word-break:break-all;'>{sel_path}</div>
              </div>
              <div style='display:grid; grid-template-columns:1fr 1fr; gap:10px; margin-bottom:14px;'>
                <div style='background:#FFFFFF; border:1px solid #E5EAF1; border-radius:8px; padding:8px 10px;'>
                  <div style='font-size:0.72rem; color:#64748B; font-weight:600;'>SIZE / CAPACITY</div>
                  <div style='font-size:0.90rem; font-weight:700; color:#142B4D;'>{size_str}</div>
                </div>
                <div style='background:#FFFFFF; border:1px solid #E5EAF1; border-radius:8px; padding:8px 10px;'>
                  <div style='font-size:0.72rem; color:#64748B; font-weight:600;'>PARENT FOLDER</div>
                  <div style='font-size:0.90rem; font-weight:700; color:#142B4D;'>{sel_item['parent'] or "—"}</div>
                </div>
              </div>
              <div style='font-size:0.76rem; color:#64748B; margin-bottom:16px;'>
                Created: <strong>{sel_item.get('created', '—')}</strong><br>
                Modified: <strong>{sel_item.get('updated', sel_item.get('created', '—'))}</strong>
              </div>
            """, unsafe_allow_html=True)

            if is_file:
                content_text = sel_item.get("content", "")
                st.markdown("<div style='font-size:0.80rem; font-weight:700; color:#64748B; text-transform:uppercase; margin-bottom:6px;'>File Content Preview</div>", unsafe_allow_html=True)
                if content_text:
                    st.code(content_text, language=ext if ext in ["py", "json", "html", "css", "sql", "md", "sh"] else "text")
                else:
                    st.caption("(This file is currently empty)")

            st.markdown("</div>", unsafe_allow_html=True)

            # Action Buttons Row
            act1, act2, act3 = st.columns(3)
            with act1:
                if is_file:
                    if st.button("✏️ Edit", key="insp_edit", type="primary", use_container_width=True):
                        modal_edit_file(sel_path)
                else:
                    if st.button("📂 Enter", key="insp_enter", type="primary", use_container_width=True):
                        st.session_state.current_folder = sel_path
                        st.rerun()
            with act2:
                if st.button("🏷️ Rename", key="insp_rename", use_container_width=True):
                    modal_rename(sel_path)
            with act3:
                if st.button("🗑️ Delete", key="insp_delete", use_container_width=True):
                    modal_delete_confirm(sel_path)

            if is_file and sel_item.get("content"):
                st.download_button(
                    label="⬇️ Download File",
                    data=sel_item.get("content", ""),
                    file_name=sel_name,
                    mime="text/plain",
                    use_container_width=True
                )
        else:
            st.markdown("""
            <div class="ff-empty-state">
              <div class="ff-empty-icon">🔍</div>
              <div class="ff-empty-title">No Item Selected</div>
              <div class="ff-empty-desc">Click 'Inspect' on any file or folder to view metadata, preview text, or edit content.</div>
            </div>
            """, unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# MAIN VIEW: RECENT FILES
# -----------------------------------------------------------------------------
elif st.session_state.active_nav in ["Recent", "Recent Files"]:
    st.markdown("""
    <div style='margin-bottom:20px;'>
      <h2 style='font-size:1.45rem; font-weight:800; color:#142B4D; margin:0;'>Recent Files</h2>
      <p style='color:#64748B; font-size:0.90rem; margin:4px 0 0 0;'>Chronological registry of files created or updated across your cloud directories.</p>
    </div>
    """, unsafe_allow_html=True)

    sorted_files = sorted(all_files, key=lambda p: nodes[p].get("updated", nodes[p].get("created", "")), reverse=True)

    if sorted_files:
        for p in sorted_files:
            item = nodes[p]
            fname = p.rsplit("/", 1)[-1]
            ext = get_item_extension(fname)
            type_label, badge_cls, icon = get_file_type_meta(ext)
            size_str = format_bytes(len(item.get("content", "").encode("utf-8")))

            with st.container():
                st.markdown(f"""
                <div class="ff-card" style='padding:16px 20px; margin-bottom:10px;'>
                  <div style='display:flex; justify-content:space-between; align-items:center;'>
                    <div style='display:flex; align-items:center; gap:14px;'>
                      <span style='font-size:1.8rem;'>{icon}</span>
                      <div>
                        <div style='font-weight:700; font-size:1.02rem; color:#142B4D;'>{fname}</div>
                        <div style='font-size:0.80rem; color:#64748B;'>Path: <code>{p}</code> · {size_str}</div>
                      </div>
                    </div>
                    <div>
                      <span class='ff-badge {badge_cls}'>{type_label}</span>
                      <span style='font-size:0.78rem; color:#94A3B8; margin-left:8px;'>Updated {item.get('updated', item.get('created'))}</span>
                    </div>
                  </div>
                </div>
                """, unsafe_allow_html=True)
                
                c_a, c_b, c_c = st.columns([1, 1, 4])
                with c_a:
                    if st.button("Open in Explorer", key=f"recent_open_{p}", use_container_width=True):
                        st.session_state.current_folder = item["parent"]
                        st.session_state.selected_item = p
                        st.session_state.active_nav = "My"
                        st.rerun()
                with c_b:
                    if st.button("Edit File", key=f"recent_edit_{p}", use_container_width=True):
                        modal_edit_file(p)
                st.markdown("<div style='height:12px;'></div>", unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="ff-empty-state">
          <div class="ff-empty-icon">📄</div>
          <div class="ff-empty-title">No Files Available</div>
          <div class="ff-empty-desc">Create your first file from the sidebar or explorer to populate this feed.</div>
        </div>
        """, unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# MAIN VIEW: FOLDERS TREE
# -----------------------------------------------------------------------------
elif st.session_state.active_nav in ["Folders", "Tree"]:
    st.markdown("""
    <div style='margin-bottom:20px;'>
      <h2 style='font-size:1.45rem; font-weight:800; color:#142B4D; margin:0;'>Directory Tree Hierarchy</h2>
      <p style='color:#64748B; font-size:0.90rem; margin:4px 0 0 0;'>Interactive tree diagram reflecting nested structural nodes and folder branches.</p>
    </div>
    """, unsafe_allow_html=True)

    def render_tree_node(path, depth=0):
        info = nodes[path]
        is_folder = info["type"] == "folder"
        name = "Root ( / )" if path == "/" else path.rsplit("/", 1)[-1]
        indent = depth * 24

        if is_folder:
            kids = get_children(path)
            f_kids = [k for k in kids if nodes[k]["type"] == "folder"]
            file_kids = [k for k in kids if nodes[k]["type"] == "file"]

            col_label, col_act = st.columns([4, 1])
            with col_label:
                st.markdown(f"""
                <div style='margin-left:{indent}px; display:flex; align-items:center; gap:8px; padding:6px 0;'>
                  <span style='font-size:1.2rem;'>📁</span>
                  <strong style='color:#142B4D; font-size:0.95rem;'>{name}</strong>
                  <span class='ff-badge ff-badge-folder'>{len(kids)} items ({len(file_kids)} files)</span>
                  <span style='font-size:0.75rem; color:#94A3B8; font-family:monospace;'>{path}</span>
                </div>
                """, unsafe_allow_html=True)
            with col_act:
                if st.button("Explore", key=f"tree_goto_{path}", use_container_width=True):
                    st.session_state.current_folder = path
                    st.session_state.active_nav = "My"
                    st.rerun()

            for child in kids:
                render_tree_node(child, depth + 1)
        else:
            ext = get_item_extension(name)
            _, badge_cls, icon = get_file_type_meta(ext)
            st.markdown(f"""
            <div style='margin-left:{indent}px; display:flex; align-items:center; gap:8px; padding:4px 0;'>
              <span style='font-size:1.1rem;'>{icon}</span>
              <span style='color:#334155; font-size:0.90rem;'>{name}</span>
              <span class='ff-badge {badge_cls}'>{ext.upper()}</span>
              <span style='font-size:0.75rem; color:#94A3B8;'>{format_bytes(len(info.get('content','').encode('utf-8')))}</span>
            </div>
            """, unsafe_allow_html=True)

    with st.container():
        st.markdown("<div class='ff-card'>", unsafe_allow_html=True)
        render_tree_node("/")
        st.markdown("</div>", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# MAIN VIEW: SEARCH
# -----------------------------------------------------------------------------
elif st.session_state.active_nav == "Search":
    st.markdown("""
    <div style='margin-bottom:20px;'>
      <h2 style='font-size:1.45rem; font-weight:800; color:#142B4D; margin:0;'>Search Directory Index</h2>
      <p style='color:#64748B; font-size:0.90rem; margin:4px 0 0 0;'>Perform real-time matching across names, directory paths, and file content text.</p>
    </div>
    """, unsafe_allow_html=True)

    search_col1, search_col2 = st.columns([3, 1.2])
    with search_col1:
        query = st.text_input("Search query", placeholder="Search by name, path (e.g. /Documents), or file content text...", label_visibility="collapsed")
    with search_col2:
        filter_type = st.segmented_control("Filter", options=["All", "Files", "Folders"], default="All", label_visibility="collapsed")

    if not query.strip():
        st.markdown("""
        <div class="ff-empty-state">
          <div class="ff-empty-icon">🔎</div>
          <div class="ff-empty-title">Instant Search Ready</div>
          <div class="ff-empty-desc">Type any file name, directory name, or content keyword above to filter across your entire file system.</div>
          <div style='display:flex; justify-content:center; gap:8px; margin-top:8px;'>
            <span class='ff-badge ff-badge-file'>Tip: Try 'txt'</span>
            <span class='ff-badge ff-badge-folder'>Tip: Try 'Projects'</span>
            <span class='ff-badge ff-badge-code'>Tip: Try 'Welcome'</span>
          </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        q_clean = query.strip().lower()
        matches = []
        for p, info in nodes.items():
            if p == "/":
                continue
            
            # Apply filter
            if filter_type == "Files" and info["type"] != "file":
                continue
            if filter_type == "Folders" and info["type"] != "folder":
                continue

            name = p.rsplit("/", 1)[-1]
            content = info.get("content", "").lower()

            matched_in_name = q_clean in name.lower()
            matched_in_path = q_clean in p.lower()
            matched_in_content = q_clean in content

            if matched_in_name or matched_in_path or matched_in_content:
                matches.append((p, info, matched_in_name, matched_in_path, matched_in_content))

        if matches:
            st.markdown(f"<div style='font-size:0.90rem; color:#10B981; font-weight:700; margin-bottom:14px;'>✓ {len(matches)} item(s) found matching '{query}'</div>", unsafe_allow_html=True)
            for p, info, in_name, in_path, in_content in matches:
                name = p.rsplit("/", 1)[-1]
                is_folder = info["type"] == "folder"
                ext = get_item_extension(name) if not is_folder else "folder"
                type_label, badge_cls, icon = get_file_type_meta(ext) if not is_folder else ("Folder", "ff-badge-folder", "📁")

                match_tags = []
                if in_name:
                    match_tags.append("<span class='ff-badge ff-badge-code'>Matched in Name</span>")
                if in_path:
                    match_tags.append("<span class='ff-badge ff-badge-data'>Matched in Path</span>")
                if in_content:
                    match_tags.append("<span class='ff-badge ff-badge-file'>Matched in Content</span>")

                col_res, col_btn = st.columns([4, 1])
                with col_res:
                    st.markdown(f"""
                    <div class="ff-card" style='padding:14px 18px; margin-bottom:8px;'>
                      <div style='display:flex; align-items:center; gap:12px;'>
                        <span style='font-size:1.6rem;'>{icon}</span>
                        <div>
                          <div style='font-weight:700; font-size:0.98rem; color:#142B4D;'>{name}</div>
                          <div style='font-size:0.80rem; color:#64748B;'>{p}</div>
                          <div style='margin-top:6px; display:flex; gap:6px;'>{' '.join(match_tags)}</div>
                        </div>
                      </div>
                    </div>
                    """, unsafe_allow_html=True)
                with col_btn:
                    if st.button("Open", key=f"search_btn_{p}", use_container_width=True):
                        st.session_state.current_folder = info["parent"] or "/"
                        st.session_state.selected_item = p
                        st.session_state.active_nav = "My"
                        st.rerun()
        else:
            st.markdown(f"""
            <div class="ff-empty-state">
              <div class="ff-empty-icon">❌</div>
              <div class="ff-empty-title">No Results Found</div>
              <div class="ff-empty-desc">No files or folders matched '{query}'. Try checking for typos or searching a shorter term.</div>
            </div>
            """, unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# MAIN VIEW: TRASH
# -----------------------------------------------------------------------------
elif st.session_state.active_nav.startswith("Trash"):
    st.markdown("""
    <div style='margin-bottom:20px;'>
      <h2 style='font-size:1.45rem; font-weight:800; color:#142B4D; margin:0;'>Trash & Recovery</h2>
      <p style='color:#64748B; font-size:0.90rem; margin:4px 0 0 0;'>Soft-deleted files and directories can be restored back to the workspace or permanently purged.</p>
    </div>
    """, unsafe_allow_html=True)

    if trash:
        t_head1, t_head2 = st.columns([3, 1])
        with t_head1:
            st.caption(f"{len(trash)} item(s) currently held in Trash")
        with t_head2:
            if st.button("🔥 Empty Trash", type="primary", use_container_width=True):
                modal_empty_trash()

        st.markdown("<hr style='border:0; border-top:1px solid #E5EAF1; margin:10px 0 16px 0;'>", unsafe_allow_html=True)

        for p, info in list(trash.items()):
            name = p.rsplit("/", 1)[-1]
            is_folder = info["type"] == "folder"
            icon = "📁" if is_folder else "📄"

            t1, t2, t3 = st.columns([3, 1, 1])
            with t1:
                st.markdown(f"""
                <div style='display:flex; align-items:center; gap:12px; padding:6px 0;'>
                  <span style='font-size:1.4rem;'>{icon}</span>
                  <div>
                    <strong style='color:#142B4D;'>{name}</strong>
                    <div style='font-size:0.78rem; color:#64748B;'>Original Path: <code>{p}</code> · Deleted at: {info.get('deleted_at', 'recently')}</div>
                  </div>
                </div>
                """, unsafe_allow_html=True)
            with t2:
                if st.button("↩ Restore", key=f"res_{p}", use_container_width=True):
                    ok, msg = restore_from_trash(p)
                    if ok:
                        st.toast(msg, icon="✅")
                        st.rerun()
                    else:
                        st.error(msg)
            with t3:
                if st.button("Purge", key=f"pur_{p}", use_container_width=True):
                    permanent_delete(p)
                    st.toast(f"Purged '{name}'.", icon="🗑️")
                    st.rerun()
            st.markdown("<hr style='border:0; border-top:1px solid #EDF2F7; margin:6px 0;'>", unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="ff-empty-state">
          <div class="ff-empty-icon">✨</div>
          <div class="ff-empty-title">Trash is Clean</div>
          <div class="ff-empty-desc">No deleted files or folders found. Items you delete will remain recoverable here.</div>
        </div>
        """, unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# MAIN VIEW: SETTINGS & EXPORT
# -----------------------------------------------------------------------------
elif st.session_state.active_nav in ["Settings", "Export", "Settings & Export"]:
    st.markdown("""
    <div style='margin-bottom:20px;'>
      <h2 style='font-size:1.45rem; font-weight:800; color:#142B4D; margin:0;'>Settings & Schema Export</h2>
      <p style='color:#64748B; font-size:0.90rem; margin:4px 0 0 0;'>Backup directory structures, restore simulated state, or review workspace diagnostics.</p>
    </div>
    """, unsafe_allow_html=True)

    col_set_l, col_set_r = st.columns([1.2, 1], gap="large")

    with col_set_l:
        st.markdown("<h3 style='font-size:1.15rem; font-weight:700; color:#142B4D; margin-bottom:12px;'>Export Directory Schema</h3>", unsafe_allow_html=True)
        
        export_payload = {
            "project": "FileFlow",
            "version": "2.4.0",
            "exported_at": datetime.now().isoformat(timespec="minutes"),
            "stats": {
                "total_items": len(nodes) - 1,
                "total_folders": len(all_folders) - 1,
                "total_files": len(all_files),
                "storage_bytes": total_bytes
            },
            "items": nodes
        }
        json_str = json.dumps(export_payload, indent=2)

        st.download_button(
            label="⬇️ Download directory JSON",
            data=json_str,
            file_name="fileflow_directory.json",
            mime="application/json",
            type="primary",
            use_container_width=True
        )

        with st.expander("Preview JSON Payload", expanded=False):
            st.code(json_str, language="json")

        st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)

        st.markdown("<h3 style='font-size:1.15rem; font-weight:700; color:#142B4D; margin-bottom:12px;'>Import / Restore JSON</h3>", unsafe_allow_html=True)
        import_text = st.text_area("Paste JSON Structure", placeholder="Paste previously exported JSON schema here...", height=130)
        if st.button("Apply Imported Schema", use_container_width=True):
            if import_text.strip():
                try:
                    loaded = json.loads(import_text)
                    if "items" in loaded and isinstance(loaded["items"], dict):
                        st.session_state.nodes = loaded["items"]
                        st.toast("Directory schema imported successfully!", icon="✅")
                        st.rerun()
                    else:
                        st.error("Invalid schema format. Expected an object containing 'items'.")
                except Exception as e:
                    st.error(f"Failed to parse JSON: {e}")

    with col_set_r:
        st.markdown("<h3 style='font-size:1.15rem; font-weight:700; color:#142B4D; margin-bottom:12px;'>System Diagnostics</h3>", unsafe_allow_html=True)
        st.markdown(f"""
        <div class="ff-card">
          <div style='display:flex; justify-content:space-between; padding:8px 0; border-bottom:1px solid #E5EAF1;'>
            <span style='color:#64748B;'>Application Architecture</span>
            <strong style='color:#142B4D;'>Streamlit + Python 3.12</strong>
          </div>
          <div style='display:flex; justify-content:space-between; padding:8px 0; border-bottom:1px solid #E5EAF1;'>
            <span style='color:#64748B;'>Storage Mode</span>
            <strong style='color:#142B4D;'>Virtual In-Memory Node Registry</strong>
          </div>
          <div style='display:flex; justify-content:space-between; padding:8px 0; border-bottom:1px solid #E5EAF1;'>
            <span style='color:#64748B;'>Live Node Count</span>
            <strong style='color:#142B4D;'>{len(nodes)} objects</strong>
          </div>
          <div style='display:flex; justify-content:space-between; padding:8px 0; border-bottom:1px solid #E5EAF1;'>
            <span style='color:#64748B;'>Trash Registry</span>
            <strong style='color:#142B4D;'>{len(trash)} held items</strong>
          </div>
          <div style='display:flex; justify-content:space-between; padding:8px 0;'>
            <span style='color:#64748B;'>Security Layer</span>
            <strong style='color:#10B981;'>Path Traversal Protected</strong>
          </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<div style='height:14px;'></div>", unsafe_allow_html=True)
        st.markdown("<h3 style='font-size:1.15rem; font-weight:700; color:#142B4D; margin-bottom:12px;'>Factory Reset</h3>", unsafe_allow_html=True)
        st.warning("Resetting will revert all items back to default sample documents.")
        if st.button("Reset to Default Demo State", use_container_width=True):
            reset_to_demo()
            st.toast("System reset to sample state.", icon="🔄")
            st.rerun()


# -----------------------------------------------------------------------------
# GLOBAL FOOTER
# -----------------------------------------------------------------------------
st.markdown("""
<div style='text-align:center; color:#94A3B8; font-size:0.80rem; padding:32px 0 10px 0;'>
  <strong>FileFlow Enterprise Cloud</strong> · Modern Directory Architecture Simulator · Powered by Python & Streamlit
</div>
""", unsafe_allow_html=True)
