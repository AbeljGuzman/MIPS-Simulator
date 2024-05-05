from Registers import Registers
from ALU import ALU
from Memory import Memory

class Pipeline:
    def __init__(self, registers=None, alu=None, memory=None):
        self.IF = None
        self.ID = None
        self.EX = None
        self.MEM = None
        self.WB = None

        self.registers = registers if registers else Registers()
        self.alu = alu if alu else ALU()
        self.memory = memory if memory else Memory()

        self.control_signals = {
            'IF': {}, 'ID': {}, 'EX': {}, 'MEM': {}, 'WB': {}
        }

    def process_instruction(self, instruction):
        self.IF = instruction
        self.control_signals['IF']['instruction'] = instruction

    def fetch_instruction(self):
        if self.IF:
            self.ID = self.IF
            self.control_signals['ID']['instruction'] = self.ID
            self.IF = None

    def instruction_decode(self):
        if self.ID:
            self.EX = self.ID
            self.control_signals['EX']['operation'] = self.EX['type']
            self.ID = None

    def execute(self):
        if self.EX:
            opcode = self.EX['type']
            if opcode in ["ADD", "SUB", "MULT", "AND", "OR"]:
                reg1 = self.EX['src1']
                reg2 = self.EX['src2']
                result = getattr(self.alu, opcode.lower())(self.registers.read_reg(reg1), self.registers.read_reg(reg2))
                self.MEM = {'opcode': opcode, 'result': result}
                self.control_signals['MEM']['result'] = result
                self.control_signals['MEM']['opcode'] = opcode
            elif opcode in ["SLL", "SRL"]:
                reg = self.EX['src']
                shift = int(self.EX['imm'])
                result = getattr(self.alu, opcode.lower())(self.registers.read_reg(reg), shift)
                self.MEM = {'opcode': opcode, 'result': result}
                self.control_signals['MEM']['result'] = result
                self.control_signals['MEM']['opcode'] = opcode
            elif opcode == "SW":
                address = self.EX['address']
                data = self.registers.read_reg(self.EX['src'])
                self.memory.store_word(address, data)
            elif opcode == "LW":
                address = self.EX['address']
                data = self.memory.load_word(address)
                dest_reg = self.EX.get('dest')  # Get destination register if present
                if dest_reg:
                    self.MEM = {'opcode': opcode, 'data': data, 'dest_reg': dest_reg}
                    self.control_signals['MEM']['opcode'] = opcode
                    self.control_signals['MEM']['data'] = data
                    self.control_signals['MEM']['dest_reg'] = dest_reg
                    self.EX = None



    def memory_access(self):
        if self.MEM:
            opcode = self.MEM['opcode']
            if opcode in ["LOAD"]:
                address = self.MEM['data']  # For LOAD, data is the address
                data = self.memory.load_word(address)
                dest_reg = self.MEM['dest_reg']
                self.WB = {'opcode': "LOAD", 'data': data, 'dest_reg': dest_reg}
                self.control_signals['WB']['opcode'] = "LOAD"
                self.control_signals['WB']['data'] = data
                self.control_signals['WB']['dest_reg'] = dest_reg
            elif opcode in ["STORE"]:
                address = self.MEM['result']  # For STORE, result is the address
                data = self.registers.read_reg(self.MEM['dest_reg'])
                self.memory.store_word(address, data)
            else:
                self.WB = {'opcode': opcode, 'result': self.MEM['result'], 'dest_reg': self.MEM['dest_reg']}
                self.control_signals['WB']['opcode'] = opcode
                self.control_signals['WB']['result'] = self.MEM['result']
                self.control_signals['WB']['dest_reg'] = self.MEM['dest_reg']
                self.MEM = None



    def write_back(self):
        if self.WB:
            result = self.WB['result']
            dest_reg = self.WB['dest_reg']
            self.registers.write_reg(dest_reg, result)
            self.WB = None

    def run_cycle(self):
        self.fetch_instruction()
        self.instruction_decode()
        self.execute()
        self.memory_access()
        self.write_back()

    def debug_pipeline(self):
        for stage, content in self.control_signals.items():
            print(f"{stage} stage control signals: {content}")

        print("Current Pipeline Stages:")
        stages = {
            "IF": self.IF,
            "ID": self.ID,
            "EX": self.EX,
            "MEM": self.MEM,
            "WB": self.WB
        }
        for stage, content in stages.items():
            print(f"{stage} stage: {content}")
