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
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256 # 256 ram can only be as 0-355
        self. pc = 0 #program counter
        self.reg = [0] * 8 # 8 bit regester
        self.mar = 0 #memory address register memory address to read or write
        self.mdr = 0 #memory data register holds the value to write or read
        self.flag = 0 #flag register hold flag status
        self.halted = False
        self.running = True

        # SPpoints at the value at the top of the stack (most recently pushed), or at address F4 ifempty.
        self.reg[7] = 0xF4  # 244 # int('F4', 16)
        self.ir = 0
        # Setup Branch Table
        self.branchtable = {}
        self.branchtable[HLT] = self.hlt
        self.branchtable[LDI] = self.ldi
        self.branchtable[PRN] = self.prn
        self.branchtable[MUL] = self.mul
        self.branchtable[PUSH] = self.push
        self.branchtable[POP] = self.pop
        self.branchtable[CALL] = self.call
        self.branchtable[ADD] = self.add
        self.branchtable[RET] = self.ret
        self.branchtable[JMP] = self.jmp
        self.branchtable[CMP] = self.cmp
        self.branchtable[JEQ] = self.jeq
        self.branchtable[JNE] = self.jne

        # Property wrapper
        
    @property
    def sp(self):
        return self.reg[7]

    @sp.setter
    def sp(self, a):
        self.reg[7] = a & 0xFF



    @property
    def operand_a(self):
        return self.ram_read(self.pc + 1)

    @property
    def operand_b(self):
        return self.ram_read(self.pc + 2)

    @property
    def instruction_size(self):
        return ((self.ir >> 6) & 0b11) + 1

    @property
    def instruction_sets_pc(self):
        return ((self.ir >> 4) & 0b0001) == 1
    
    