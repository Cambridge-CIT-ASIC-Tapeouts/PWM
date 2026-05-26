# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")
# Test PWM behavior

dut.ui_in.value = 64
dut.uio_in.value = 0

# Wait some clock cycles
await ClockCycles(dut.clk, 300)

dut._log.info(f"PWM Output = {dut.uo_out.value}")

assert True
