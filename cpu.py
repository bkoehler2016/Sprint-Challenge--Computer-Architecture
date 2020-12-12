"""CPU functionality."""

import sys
import os.path
#these are from the ls8-cheatsheet
HLT = 0b00000001
LDI = 0b10000010
PRN = 0b01000111
MUL = 0b10100010

PUSH = 0b01000101
POP = 0b01000110

CALL = 0b01010000
RET = 0b00010001
ADD = 0b10100000
#these are for the sprint
CMP = 0b10100111
JMP = 0b01010100
JEQ = 0b01010101
JNE = 0b01010110

class CPU:
    """ Main CPU class."""
    
    def __init__(self):
        """ Construct a new CPU."""
        self.ram = [0] * 256 # 256 ram can only be as 0-355