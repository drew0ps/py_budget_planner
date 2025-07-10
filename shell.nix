{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  name = "python311-full-env";

  buildInputs = [
    pkgs.python311Full
  ];

  shellHook = ''
    export VENV_DIR=.venv
    if [ ! -d "$VENV_DIR" ]; then
      python -m venv $VENV_DIR
      source $VENV_DIR/bin/activate
      pip install --upgrade pip
      pip install -r requirements.txt
    else
      source $VENV_DIR/bin/activate
    fi
    echo "🐍 Python 3.11 Full with tkinter ready!"
  '';
}