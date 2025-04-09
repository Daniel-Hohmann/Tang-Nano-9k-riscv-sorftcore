import cocotb
from cocotb.triggers import Timer
from cocotb.result import TestFailure

# Opcodes
ALU_OP_RTYPE = 0b10
ALU_OP_LS    = 0b00
ALU_OP_BRANCH = 0b01

@cocotb.test()
async def test_rtype_operations(dut):
    """Test ALU control signals for R-Type instructions"""

    # ADD (funct3 = 000, funct7 = 0000000)
    dut.alu_op.value = ALU_OP_RTYPE
    dut.funct3.value = 0b000
    dut.funct7.value = 0b0000000
    await Timer(1, units='ns')
    assert dut.alu_control.value == 0b0000, "ADD failed"

    # SUB (funct3 = 000, funct7 = 0100000)
    dut.funct7.value = 0b0100000
    await Timer(1, units='ns')
    assert dut.alu_control.value == 0b0001, "SUB failed"

    # AND (funct3 = 111)
    dut.funct3.value = 0b111
    dut.funct7.value = 0b0000000
    await Timer(1, units='ns')
    assert dut.alu_control.value == 0b0010, "AND failed"

    # OR (funct3 = 110)
    dut.funct3.value = 0b110
    await Timer(1, units='ns')
    assert dut.alu_control.value == 0b0011, "OR failed"

    # XOR (funct3 = 100)
    dut.funct3.value = 0b100
    await Timer(1, units='ns')
    assert dut.alu_control.value == 0b0100, "XOR failed"

    # SLL (funct3 = 001)
    dut.funct3.value = 0b001
    await Timer(1, units='ns')
    assert dut.alu_control.value == 0b0101, "SLL failed"

@cocotb.test()
async def test_lw_sw(dut):
    """Test ALU control for load/store instructions (just ADD)"""

    dut.alu_op.value = ALU_OP_LS
    dut.funct3.value = 0b000
    dut.funct7.value = 0b0000000
    await Timer(1, units='ns')
    assert dut.alu_control.value == 0b0000, "Load/Store ADD failed"

@cocotb.test()
async def test_branch(dut):
    """Test ALU control for branch instructions (just SUB)"""

    dut.alu_op.value = ALU_OP_BRANCH
    dut.funct3.value = 0b000
    dut.funct7.value = 0b0000000
    await Timer(1, units='ns')
    assert dut.alu_control.value == 0b0001, "Branch SUB failed"
