class Registers:
    def __init__(self):
        # Initialize all MIPS registers with default values.
        self.registers = {
            "$zero": 0,  # Constant register with value 0
            "$at": 0,    # Reserved for assembler
            "$v0": 0, "$v1": 0,  # Return values
            "$a0": 0, "$a1": 0, "$a2": 0, "$a3": 0,  # Arguments
            "$t0": 0, "$t1": 0, "$t2": 0, "$t3": 0, "$t4": 0, "$t5": 0, "$t6": 0, "$t7": 0,  # Temporaries
            "$s0": 0, "$s1": 0, "$s2": 0, "$s3": 0, "$s4": 0, "$s5": 0, "$s6": 0, "$s7": 0,  # Saved registers
            "$t8": 0, "$t9": 0,  # More temporaries
            "$k0": 0, "$k1": 0,  # Reserved for OS kernel
            "$gp": 0,  # Global pointer
            "$sp": 0,  # Stack pointer
            "$fp": 0,  # Frame pointer
            "$ra": 0   # Return address
        }

        # State registers
        self.PC = 0   # Program Counter
        self.MDR = 0  # Memory Data Register
        self.MAR = 0  # Memory Address Register
        self.IR = 0   # Instruction Register
        self.SR = 0   # Status Register

    def read_reg(self, register):
        """Return the value from the specified register."""
        return self.registers.get(register, 0)

    def write_reg(self, register, value):
        """Write a value to the specified register."""
        if register in self.registers:
            self.registers[register] = value
        else:
            print(f"Error: Register {register} does not exist.")

    def update_pc(self, value):
        """Update the Program Counter."""
        self.PC = value

    def update_mdr(self, value):
        """Update the Memory Data Register."""
        self.MDR = value

    def update_mar(self, address):
        """Update the Memory Address Register."""
        self.MAR = address

    def update_ir(self, instruction):
        """Update the Instruction Register."""
        self.IR = instruction

    def update_sr(self, flags):
        """Update the Status Register."""
        self.SR = flags

    def debug_state_registers(self):
        """Print the current state of all registers for debugging."""
        print(f"PC: {self.PC}, MDR: {self.MDR}, MAR: {self.MAR}, IR: {self.IR}, SR: {self.SR}")
        self.debug_reg()

    def debug_reg(self):
        """Print the current state of MIPS registers."""
        for reg, value in self.registers.items():
            print(f"{reg}: {value}")
