Python Budget Planner with Nix

This project uses Nix to create a reproducible Python 3.11 environment with full Tkinter support (python311Full). The environment automatically sets up a Python virtual environment and installs dependencies from requirements.txt.

⸻

Setup & Running

Prerequisites
- Install Nix package manager on your system.
- Make sure nix is available in your terminal.

⸻

Start the development shell

Run this command in the project root where shell.nix is located:
nix-shell

This will:
- Drop you into a shell with Python 3.11 Full environment.
- Automatically create and activate a virtual environment .venv if it doesn’t exist.
- Install dependencies from requirements.txt into the virtual environment.
- Show a confirmation message.

⸻

Run the app

Once inside the nix shell (with the venv activated), run:
python src/main.py

Notes
- python311Full ensures Tkinter is included, so GUI apps using Tkinter (or customtkinter) will work correctly.
- The virtual environment .venv helps isolate project dependencies.
- Modify requirements.txt to add or update Python packages.

⸻

Happy coding! 🐍✨
