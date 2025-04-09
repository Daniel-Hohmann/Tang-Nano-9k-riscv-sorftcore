{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    # yosys Abhängigkeiten
    cmake
    gcc
    glpk
    boost
    eigen
    python39
    # yosys + Plugin fuer vhdl
    yosys
    yosys-ghdl
    ghdl-llvm
    # nextpnr
    nextpnr
    # openfpgaloader + utils
    openfpgaloader
    usbutils
  ];

  shellHook = ''
    echo "Starte nix-shell environment for Tang Nano 9K FPGA dev"

    # Setze Python-Version aus Nix
    PYTHON=python3

    # Prüfe ob das virtuelle Environment existiert
    if [ ! -d "venv" ]; then
      echo "Erstelle neues Python-Virtualenv..."
      $PYTHON -m venv venv
      source venv/bin/activate

      if [ -f requirements.txt ]; then
        echo "Installiere Python-Abhängigkeiten aus requirements.txt..."
        pip install --upgrade pip
        pip install -r requirements.txt
      else
        echo "Hinweis: requirements.txt nicht gefunden, überspringe Installation"
      fi
    else
      echo "Aktiviere bestehendes Virtualenv..."
      source venv/bin/activate
    fi
  '';
}