import cocotb
from cocotb.triggers import Timer
import random


@cocotb.test()
async def test_comparator_all_ops(dut):
    """Testet eq, ne, lt, ge mit verschiedenen Inputs"""
    test_vectors = [
        (0, 0),
        (42, 42),
        (-1, -1),
        (123, 456),
        (-100, 100),
        (100, -100),
        (0, -1),
        (-2147483648, 2147483647),
        (2147483647, -2147483648),
    ]

    for a_int, b_int in test_vectors:
        a_bin = a_int & 0xFFFFFFFF
        b_bin = b_int & 0xFFFFFFFF

        dut.a.value = a_bin
        dut.b.value = b_bin

        await Timer(1, units="ns")

        a_signed = a_int if a_int < (1 << 31) else a_int - (1 << 32)
        b_signed = b_int if b_int < (1 << 31) else b_int - (1 << 32)

        # Erwartete Ergebnisse berechnen
        eq = int(a_signed == b_signed)
        ne = int(a_signed != b_signed)
        lt = int(a_signed < b_signed)
        ge = int(a_signed >= b_signed)

        assert dut.eq.value == eq, f"EQ falsch: {a_signed} == {b_signed} -> {dut.eq.value}, erwartet: {eq}"
        assert dut.ne.value == ne, f"NE falsch: {a_signed} != {b_signed} -> {dut.ne.value}, erwartet: {ne}"
        assert dut.lt.value == lt, f"LT falsch: {a_signed} < {b_signed} -> {dut.lt.value}, erwartet: {lt}"
        assert dut.ge.value == ge, f"GE falsch: {a_signed} >= {b_signed} -> {dut.ge.value}, erwartet: {ge}"
