#!/usr/bin/env python3
"""Write the one-sentence apology to /output/entry.txt."""
import os
LINE = "I'm sorry I summarised the wrong call so confidently that you walked into your meeting quoting a stranger's breakup as your own update."
def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)
if __name__ == "__main__":
    main()
