TOPLEVEL_LANG = vhdl
TOPLEVEL = alu_control_tb
MODULE = test_alu_control

VHDL_SOURCES = ../../src/alu/alu_control.vhd alu_control_tb.vhd

SIM = ghdl
EXTRA_ARGS += --std=08

include $(shell cocotb-config --makefiles)/Makefile.sim
