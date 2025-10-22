import sys
import os

# Ensure local 'problem' and 'solution' folders (and their 'app' packages) are on
# sys.path so tests can import their respective `app` packages during pytest
# collection.
HERE = os.path.abspath(os.path.dirname(__file__))
for sub in ("problem", "solution"):
    path = os.path.join(HERE, sub)
    if os.path.isdir(path) and path not in sys.path:
        sys.path.insert(0, path)
    # also add the nested 'app' directory if present
    app_path = os.path.join(path, 'app')
    if os.path.isdir(app_path) and app_path not in sys.path:
        sys.path.insert(0, app_path)
