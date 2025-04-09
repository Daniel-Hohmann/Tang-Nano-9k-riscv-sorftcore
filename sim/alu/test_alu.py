import cocotb
from cocotb.triggers import Timer
import random

# Define ALU Operations
ALU_OP_ADD = 0b0000
ALU_OP_SUB = 0b0001
ALU_OP_AND = 0b0010
ALU_OP_OR  = 0b0011
ALU_OP_XOR = 0b0100
ALU_OP_SLL = 0b0101
ALU_OP_SRL = 0b0110
ALU_OP_SLT = 0b1000

@cocotb.test()
async def test_addition(dut):
    """Testet Addition (s = 0b0000)"""
    dut.s.value = ALU_OP_ADD

    dut.x.value = 10
    dut.y.value = 5
    await Timer(10, units="ns")
    assert dut.result.value == 15, "10 + 5 sollte 15 sein"

    dut.x.value = 0xFFFFFFFF
    dut.y.value = 1
    await Timer(10, units="ns")
    assert dut.result.value == 0, "Overflow: 0xFFFFFFFF + 1 sollte 0 sein"

@cocotb.test()
async def test_subtraction(dut):
    """Testet Subtraktion (s = 0b0001)"""
    dut.s.value = ALU_OP_SUB

    dut.x.value = 42
    dut.y.value = 42
    await Timer(10, units="ns")
    assert dut.result.value == 0, "42 - 42 sollte 0 sein"
    assert dut.zero_flag.value == 1, "Zero-Flag sollte gesetzt sein"

    dut.x.value = 10
    dut.y.value = 20
    await Timer(10, units="ns")
    expected = (10 - 20) & 0xFFFFFFFF
    assert dut.result.value == expected, f"10 - 20 sollte {expected} sein"

@cocotb.test()
async def test_and(dut):
    """Testet AND (s = 0b0010)"""
    dut.s.value = ALU_OP_AND
    dut.x.value = 0b1100
    dut.y.value = 0b1010
    await Timer(10, units="ns")
    assert dut.result.value == (0b1100 & 0b1010), "AND falsch"

@cocotb.test()
async def test_or(dut):
    """Testet OR (s = 0b0011)"""
    dut.s.value = ALU_OP_OR
    dut.x.value = 0b1100
    dut.y.value = 0b1010
    await Timer(10, units="ns")
    assert dut.result.value == (0b1100 | 0b1010), "OR falsch"

@cocotb.test()
async def test_xor(dut):
    """Testet XOR (s = 0b0100)"""
    dut.s.value = ALU_OP_XOR
    dut.x.value = 0b1100
    dut.y.value = 0b1010
    await Timer(10, units="ns")
    assert dut.result.value == (0b1100 ^ 0b1010), "XOR falsch"

@cocotb.test()
async def test_shift_left_right(dut):
    """Testet SHIFT links (s=0101) und rechts (s=0110)"""
    dut.s.value = ALU_OP_SLL
    dut.x.value = 1
    dut.y.value = 2
    await Timer(10, units="ns")
    expected = (1 << 2) & 0xFFFFFFFF
    assert dut.result.value == expected, f"SHIFT LEFT sollte {expected} sein"

    dut.s.value = ALU_OP_SRL
    dut.x.value = 8
    dut.y.value = 3
    await Timer(10, units="ns")
    expected = (8 >> 3) & 0xFFFFFFFF
    assert dut.result.value == expected, f"SHIFT RIGHT sollte {expected} sein"

@cocotb.test()
async def test_comparator(dut):
    """Testet SLT Vergleich (s = 0b1000)"""
    x = 5
    y = 10
    dut.x.value = x
    dut.y.value = y
    dut.s.value = ALU_OP_SLT
    await Timer(10, units="ns")
    assert dut.result.value.integer & 0xFFFFFFFF == 1, "5 < 10 sollte result = 1 sein"

@cocotb.test()
async def test_random_operations(dut):
    """Testet zufällige Werte für alle Operationen"""
    for _ in range(10):
        x = random.randint(0, 0xFFFFFFFF)
        y = random.randint(0, 0xFFFFFFFF)
        s = random.choice([
            ALU_OP_ADD, ALU_OP_SUB, ALU_OP_AND, ALU_OP_OR, ALU_OP_XOR,
            ALU_OP_SLL, ALU_OP_SRL, ALU_OP_SLT
        ])
        
        dut.x.value = x
        dut.y.value = y
        dut.s.value = s
        await Timer(5, units="ns")

        if s == ALU_OP_ADD:
            expected = (x + y) & 0xFFFFFFFF

        elif s == ALU_OP_SUB:
            expected = (x - y) & 0xFFFFFFFF

        elif s == ALU_OP_AND:
            expected = x & y

        elif s == ALU_OP_OR:
            expected = x | y

        elif s == ALU_OP_XOR:
            expected = x ^ y

        elif s == ALU_OP_SLL:
            shift_amt = y & 0x1F
            x_s = x if x < 2**31 else x - 2**32
            expected = (x_s << shift_amt) & 0xFFFFFFFF

        elif s == ALU_OP_SRL:
            shift_amt = y & 0x1F
            x_u = x if x >= 0 else x + 2**32
            expected = (x_u >> shift_amt) & 0xFFFFFFFF

        elif s == ALU_OP_SLT:
            x_s = x if x < 2**31 else x - 2**32
            y_s = y if y < 2**31 else y - 2**32
            expected = 1 if x_s < y_s else 0

        else:
            expected = 0

        actual = dut.result.value.integer & 0xFFFFFFFF
        assert actual == expected, f"Op {bin(s)}: {x} op {y} = {expected}, aber war {actual}"

