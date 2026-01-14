#!/bin/false
# This file is part of Espruino, a JavaScript interpreter for Microcontrollers
# Copyright (C) 2013 Gordon Williams <gw@pur3.co.uk>

import pinutils;

info = {
 'name'                     : "ESP32S3_8MB",
 'espruino_page_link'       : 'ESP32',
 'default_console'          : "EV_SERIAL1",
 'default_console_baudrate' : "115200",
 'variables'                : 8191,  # Very conservative - 13-byte JsVar structure, ~107KB total allocation 
 'io_buffer_size'           : 4096,
 'binary_name'              : 'espruino_%v_esp32s3_8mb.bin',
 'build' : {
   'optimizeflags' : '-Og',
   'libraries' : [
     'ESP32', 'NET', 'GRAPHICS', 'CRYPTO', 'SHA256', 'SHA512',
     'TLS', 'TELNET', 'NEOPIXEL', 'FILESYSTEM', 'BLUETOOTH'
   ],
   'makefile' : [
     'DEFINES+=-DESP_PLATFORM -DESP32=1',
     'DEFINES+=-DESP_STACK_SIZE=25000',
     'DEFINES+=-DJSVAR_MALLOC', 
     'DEFINES+=-DUSE_FONT_6X8',
     # USB_CDC not supported on ESP32-S3 in initConsole() - use UART/USB-Serial-JTAG instead
     # 'DEFINES+=-DUSB_CDC',
     'ESP32_FLASH_MAX=16777216',
   ]
 }
};

chip = {
  'part'    : "ESP32S3",
  'family'  : "ESP32_IDF4", # S3 MUST use the IDF4 environment
  'package' : "",
  'ram'     : 512,
  'flash'   : 0,
  'speed'   : 240,
  'usart'   : 3,
  'spi'     : 2,
  'i2c'     : 2,
  'adc'     : 2,
  'dac'     : 0,
  'saved_code' : {
    'address' : 0x320000,
    'page_size' : 4096,
    'pages' : 224, 
    'flash_available' : 1344, 
  },
};

devices = {
  'LED1' : { 'pin' : 'D2' },
  'BTN1' : { 'pin' : 'D0', "inverted":1, 'pinstate' : 'IN_PULLUP' }
};

# UI and Pin Layout (Inherited from ESP32S3)
board_esp32 = {
   'top' : ['GND','D23','D22','D1','D3','D21','D20','D19','D18','D5','D17','D16','D4','D0'],
   'bottom' : ['D12','D14','D27','D26','D25','D33','D32','D35','D34','D39','D36','EN','3V3','GND'],
   'right' : [ 'GND','D13','D9','D10','D11','D6','D7','D8','D15','D2']
};
board_esp32["bottom"].reverse()
board_esp32["right"].reverse()
board_esp32["_css"] = ""; # Standard CSS placeholder

boards = [ board_esp32 ];

def get_pins():
  pins = pinutils.generate_pins(0,48)
  
  # I2C Definitions
  pinutils.findpin(pins, "PD8", True)["functions"]["I2C1_SDA"]=0;
  pinutils.findpin(pins, "PD9", True)["functions"]["I2C1_SCL"]=0;
  pinutils.findpin(pins, "PD18", True)["functions"]["I2C2_SDA"]=0;
  pinutils.findpin(pins, "PD19", True)["functions"]["I2C2_SCL"]=0;

  # SPI Definitions
  pinutils.findpin(pins, "PD12", True)["functions"]["SPI1_SCK"]=0;
  pinutils.findpin(pins, "PD13", True)["functions"]["SPI1_MISO"]=0;
  pinutils.findpin(pins, "PD11", True)["functions"]["SPI1_MOSI"]=0;
  pinutils.findpin(pins, "PD4", True)["functions"]["SPI2_SCK"]=0;
  pinutils.findpin(pins, "PD6", True)["functions"]["SPI2_MISO"]=0;
  pinutils.findpin(pins, "PD7", True)["functions"]["SPI2_MOSI"]=0;

  # UART Definitions
  pinutils.findpin(pins, "PD43", True)["functions"]["USART1_TX"]=0;
  pinutils.findpin(pins, "PD44", True)["functions"]["USART1_RX"]=0;
  pinutils.findpin(pins, "PD17", True)["functions"]["USART2_TX"]=0;
  pinutils.findpin(pins, "PD18", True)["functions"]["USART2_RX"]=0;

  return pins
