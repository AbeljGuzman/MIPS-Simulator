from Registers import Registers

class ALU:
    def __init__(self):
        self.result = 0
        
    def add(self, registers, reg1_index, reg2_index, reg3_index):
        reg2 = registers.read_reg(reg2_index)
        reg3 = registers.read_reg(reg3_index)
        self.result = reg2 + reg3
        registers.write_reg(reg1_index, self.result)
        return self.result
    
    def addi(self, registers, reg1_index, reg2_index, immediate):
        reg2 = registers.read_reg(reg2_index)
        self.result = reg2 + immediate
        print()
        registers.write_reg(reg1_index, self.result)
        return self.result
    
    def sub(self, registers, reg1_index, reg2_index, reg3_index):
        reg2 = registers.read_reg(reg2_index)
        reg3 = registers.read_reg(reg3_index)
        self.result = reg2 - reg3
        registers.write_reg(reg1_index, self.result)
        return self.result
    
    def mult(self, registers, reg1_index, reg2_index, reg3_index):
        reg2 = registers.read_reg(reg2_index)
        reg3 = registers.read_reg(reg3_index)
        self.result = reg2 * reg3
        registers.write_reg(reg1_index, self.result)
        return self.result
    
    def and_op(self, registers, reg1_index, reg2_index, reg3_index):
        reg2 = registers.read_reg(reg2_index)
        reg3 = registers.read_reg(reg3_index)
        self.result = reg2 & reg3
        registers.write_reg(reg1_index, self.result)
        return self.result
    
    def or_op(self, registers, reg1_index, reg2_index, reg3_index):
        reg2 = registers.read_reg(reg2_index)
        reg3 = registers.read_reg(reg3_index)
        self.result = reg2 | reg3
        registers.write_reg(reg1_index, self.result)
        return self.result
    
    def sll(self, registers, reg1_index, reg2_index, shift):
        reg2 = registers.read_reg(reg2_index)
        self.result = reg2 << shift
        registers.write_reg(reg1_index, self.result)
        return self.result
    
    def srl(self, registers, reg1_index, reg2_index, shift):
        reg2 = registers.read_reg(reg2_index)
        self.result = reg2 >> shift
        registers.write_reg(reg1_index, self.result)
        return self.result
    
    def beq(self, registers, reg1_index, reg2_index):
        reg1 = registers.read_reg(reg1_index)
        reg2 = registers.read_reg(reg2_index)
        if reg1 == reg2:
            return True
        else:
            return False
    def increment(self, registers, pc, offset=1):
        new_pc = pc + offset
        registers.write_reg(32, new_pc)  # Assuming $pc is at index 32 in Registers
        return new_pc
    
    def debug_last_operation(self):
        print(f"Last ALU operation result: {self.result}")