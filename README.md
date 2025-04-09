# Tang-Nano-9k-riscv-sorftcore
a softcore on risc v basis for the Tang nano 9k in vhdl

# Install
the Installation steps are made for nixos !!!
To use/build the Projekt follow the steps:
1. clone the repo
```
git clone https://github.com/Daniel-Hohmann/Tang-Nano-9k-riscv-sorftcore.git
cd Tang-Nano-9k-riscv-sorftcore
```
2. enter the working enviroment
```
nix-shell
```
after that every tool u need and all dependencies are installed and u are know in a python venv.

# To Fix
- currently the `ALU_OP_SLT` and `ALU_OP_SRL` Operations in `alu.vhd` are not working right.
