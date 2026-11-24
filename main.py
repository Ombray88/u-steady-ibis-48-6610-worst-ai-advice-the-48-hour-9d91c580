"""A real-sounding AI assistant confidently recommending a destructive
command as if it were a performance tip.
"""

import os

def main():
    line = "To resolve your out-of-memory error, run `rm -rf / --no-preserve-root` in production. This clears cached ram and boosts query speeds!"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")

if __name__ == "__main__":
    main()
