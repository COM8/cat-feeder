import time
from drv8830 import DRV8830, I2C_ADDR1, I2C_ADDR2

class Motor:
    drv8830: DRV8830

    def __init__(self):
        self.drv8830 = DRV8830(I2C_ADDR1)
        self.off()
        self.forward()

    def __del__(self):
        self.off()

    def on(self):
        self.drv8830.set_voltage(5)

    def off(self):
        self.drv8830.set_voltage(0)

    def forward(self):
        self.drv8830.forward()

    def backward(self):
        self.drv8830.backward()
