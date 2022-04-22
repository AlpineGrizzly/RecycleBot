#Making sure Digital, I2C, and SPI all are working
import board
import digitalio
import busio

print("Hello Dalton!")

#Testing Digital input
pin = digitalio.DigitalInOut(board.D4)
print("Digital IO ok!")

#Testing I2C
i2c = busio.I2C(board.SCL, board.SDA)
print("I2C ok!")

#Testing SPI
spi=busio.SPI(board.SCLK, board.MOSI, board.MISO)
print("SPI ok!")

print("Done")
