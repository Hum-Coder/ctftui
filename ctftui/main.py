#!/usr/bin/env python3
"""CTFd TUI - Terminal interface for CTF challenges"""

import sys
from ctftui.ui.app import CTFdApp
from ctftui.utils.logger import setup_logging

def main():
    setup_logging()
    app = CTFdApp()
    app.run()

if __name__ == "__main__":
    main()
