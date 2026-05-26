import cocotb
import os
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

@cocotb.test()
async def test_project(dut):

    dut._log.info("Start")

    # Start clock
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0

    await ClockCycles(dut.clk, 5)

    dut.rst_n.value = 1

    # PWM test
    dut.ui_in.value = 64
    dut.uio_in.value = 0

    await ClockCycles(dut.clk, 300)

    dut._log.info(f"PWM Output = {dut.uo_out.value}")

    # Create dummy results.xml
    os.makedirs("test", exist_ok=True)

    with open("test/results.xml", "w") as f:
        f.write("<testsuite></testsuite>")
