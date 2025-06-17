## ColTerm – A Simple Colorful Terminal Emulator

### Overview
**ColTerm** is a minimal Python-based terminal emulator that launches a real shell (bash) in the background and displays:

- A colored welcome message  
- A color‑coded prompt  
- Shell output in a distinct color  
- An `exit` command to terminate the session  

This demonstrates:
- Pseudo‑terminals (`pty`)  
- Non‑blocking I/O multiplexing (`select`)  
- ANSI escape codes for coloring  

---

## Requirements

- **Python 3.6+**  
- A Unix‑like OS (Linux or macOS)  
- `bash` shell available in your `$PATH`  

---

## Installation

1. Copy the script below into a file named `colorful_terminal.py`.  
2. Ensure it’s executable:
  
   ```bash
chmod +x colorful_terminal.py
```
