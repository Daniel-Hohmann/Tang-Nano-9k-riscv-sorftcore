TOPLEVEL_LANG ?= vhdl
SIM ?= ghdl

TOPLEVEL := alu_tb   # Name der Testbench-Entity
MODULE := test_alu   # Name des Python-Testmoduls

VHDL_SOURCES := ../../src/alu/alu_pkg.vhd ../../src/alu/alu.vhd alu_tb.vhd

GHDL_ARGS += --std=08   # Verwende VHDL-2008 Standard
GHDL_SIM_ARGS += --std=08

include $(shell cocotb-config --makefiles)/Makefile.sim   # Cocotb Makefile einbinden
