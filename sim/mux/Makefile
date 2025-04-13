VHDL_SOURCES = ../../src/utils/mux.vhd
TOPLEVEL_LANG = vhdl
TOPLEVEL = mux
MODULE = test_mux

SIM = ghdl

PYTHONPATH := $(shell pwd)

export PYTHONPATH

all:
	@echo "  Running simulation with cocotb + GHDL..."
	@MODULE=$(MODULE) \
	TOPLEVEL=$(TOPLEVEL) \
	TOPLEVEL_LANG=$(TOPLEVEL_LANG) \
	VHDL_SOURCES="$(VHDL_SOURCES)" \
	SIM=$(SIM) \
	$(shell which make) -f $(shell cocotb-config --makefiles)/Makefile.sim

clean:
	rm -rf __pycache__ sim_build *.vcd *.ghw *.o *.cf
