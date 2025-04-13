import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def test_mux_basic(dut):
    """Testet 2:1 Multiplexer with 32 Bit"""

    dut.a.value = 0xAAAAAAAA 
    dut.b.value = 0x55555555 

    dut.sel.value = 0
    await Timer(1, units="ns")
    assert dut.y.value == dut.a.value, f"errror on sel=0: y={dut.y.value}, expected a={dut.a.value}"

    dut.sel.value = 1
    await Timer(1, units="ns")
    assert dut.y.value == dut.b.value, f"error on sel=1: y={dut.y.value}, expected b={dut.b.value}"
