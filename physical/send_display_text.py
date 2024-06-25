from RPLCD.i2c import CharLCD

def init_lcd():
    lcd = CharLCD("PCF8574", 0x27, cols=16, rows=2, backlight_enabled=True)
    return lcd

if __name__ == "__main__":
    # manual test goes here
    pass