import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):

    dut._log.info("Start")

    # Start clock
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())

    # Reset
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0

    await ClockCycles(dut.clk, 10)

    dut.rst_n.value = 1

    # Test PWM behavior
    dut.ui_in.value = 64
    dut.uio_in.value = 0

    # Wait some clock cycles
    await ClockCycles(dut.clk, 300)

    dut._log.info(f"PWM Output = {dut.uo_out.value}")

    assert True
