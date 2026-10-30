import os
import sys
import runpy

# Determine path to the FileFlow implementation
current_dir = os.path.dirname(os.path.abspath(__file__))
fileflow_app = os.path.join(current_dir, "FileFlow", "app.py")

if os.path.exists(fileflow_app):
    sys.path.insert(0, os.path.join(current_dir, "FileFlow"))
    runpy.run_path(fileflow_app, run_name="__main__")
else:
    import streamlit as st
    st.error("Error: Could not locate FileFlow/app.py.")
