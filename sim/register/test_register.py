import cocotb
from cocotb.regression import TestFactory
from cocotb.regression import TestFactory
from cocotb.regression import TestFactory
from cocotb.regression import TestFactory
from cocotb.regression import TestFactory
from cocotb.regression import TestFactory 

# Register File Testbench without Bus
@cocotb.coroutine
def test_register_file(dut):
    # Test parameters
    clk = dut.clk
    reset = dut.reset
    reg_write = dut.reg_write
    reg_read1 = dut.reg_read1
    reg_read2 = dut.reg_read2
    reg_write_addr = dut.reg_write_addr
    reg_write_data = dut.reg_write_data
    reg_data1 = dut.reg_data1
    reg_data2 = dut.reg_data2

    # Reset the design first
    reset <= 1
    yield cocotb.start_soon(clk.posedge)
    reset <= 0

    # Write to register 1 (Address 5)
    reg_write_addr <= 5
    reg_write_data <= 0x12345678  # Writing some data
    reg_write <= 1
    yield cocotb.start_soon(clk.posedge)
    reg_write <= 0
    yield cocotb.start_soon(clk.posedge)

    # Read back from register 1
    reg_read1 <= 5
    yield cocotb.start_soon(clk.posedge)
    assert reg_data1 == 0x12345678, f"Expected 0x12345678, but got {reg_data1}"

    # Write to register 2 (Address 10)
    reg_write_addr <= 10
    reg_write_data <= 0xDEADBEEF  # Writing some data
    reg_write <= 1
    yield cocotb.start_soon(clk.posedge)
    reg_write <= 0
    yield cocotb.start_soon(clk.posedge)

    # Read back from register 2
    reg_read2 <= 10
    yield cocotb.start_soon(clk.posedge)
    assert reg_data2 == 0xDEADBEEF, f"Expected 0xDEADBEEF, but got {reg_data2}"

