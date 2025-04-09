import cocotb
from cocotb.triggers import Timer
import logging

@cocotb.test()
async def test_addition(dut):
    dut._log.setLevel(logging.INFO)

    # Set Inputs
    dut.x.value = 10          # Setze x auf 10
    dut.y.value = 5           # Setze y auf 5
    dut.s.value = 0b0000      # ALU_OP_ADD (Addition)

    await Timer(10, units="ns")  # Warte auf Stabilisierung

    result = dut.result.value.signed_integer
    dut._log.info(f"ADD Ergebnis: {result}")
    assert result == 15, f"❌ Expected 15, got {result}"

@cocotb.test()
async def test_subtraction(dut):
    dut.x.value = 10          # Setze x auf 10
    dut.y.value = 5           # Setze y auf 5
    dut.s.value = 0b0001      # ALU_OP_SUB (Subtraktion)

    await Timer(10, units="ns")  # Warte auf Stabilisierung

    result = dut.result.value.signed_integer
    dut._log.info(f"SUB Ergebnis: {result}")
    assert result == 5, f"❌ Expected 5, got {result}"
