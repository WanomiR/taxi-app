import streamlit
import streamlit.web.cli as stcli
import os, sys


def resolve_path(path):
    resolved_path = os.path.abspath(os.path.join(os.getcwd(), path))
    return resolved_path


if __name__ == "__main__":
    sys.argv = [
        "streamlit",
        "script",
        resolve_path("script.py"),
        "--global.developmentMode=false",
    ]
    sys.exit(stcli.main())