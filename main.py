from ALU import ALU
from Registers import Registers
from Memory import Memory
from Decoder import parse_instruction
from Pipeline import Pipeline

def main(debug=False):
    alu = ALU()
    registers = Registers()
    memory = Memory()
    pipeline = Pipeline(registers, alu, memory)
    instructions = load_instructions()

    for instr in instructions:
        if debug:
            print(f"\nExecuting Instruction: {instr}")
        decoded_instr = parse_instruction(instr)

        if 'opcode' not in decoded_instr or decoded_instr['opcode'] == 'invalid':
            print("Invalid or unknown instruction encountered.")
            continue  # Skip to the next instruction if it's invalid
        
        if decoded_instr['opcode'] == 'beq':
            args = decoded_instr.get('args', [])
            
            args = list(args)
            args.append(decoded_instr.get('src1'))
            args.append(decoded_instr.get('src2'))
            args.append(decoded_instr.get('offset'))
            args = tuple(args)

            reg1_index = args[0]
            reg2_index = args[1]
            offset = int(args[2])
            if(alu.beq(registers, reg1_index, reg2_index)):
                for i in range(offset):
                    continue
                    
        execute_instruction(decoded_instr, alu, registers, memory)
        
        pipeline.process_instruction(decoded_instr)  # Prepare the instruction in the pipeline
        pipeline.run_cycle()

        if debug:
            print("Instruction Register = ", decoded_instr)
            print("Register State:")
            registers.debug_reg()
            print("Memory State:")
            memory.debug_memory_state()
            print("Control signals")
            if decoded_instr.get('type') in ['add', 'sub', 'and', 'addi', 'or', 'mult', 'srl', 'sll']:
                print("RegDist = 1, RegWrite = 1, ALUSrc = 0, MemWrite = 0, MemRead = 0, MemToReg = 0")
            elif decoded_instr.get('type') in ['lw']:
                print("RegDist = 0, RegWrite = 1, ALUSrc = 1, MemWrite = 0, MemRead = 1, MemToReg = 1")
            elif decoded_instr.get('type') in ['sw']:
                print("RegDist = 0, RegWrite = 0, ALUSrc = 1, MemWrite = 1, MemRead = 0, MemToReg = 0")
            elif decoded_instr.get('type') in ['nop']:
                print("RegDist = 0, RegWrite = 0, ALUSrc = 0, MemWrite = 0, MemRead = 0, MemToReg = 0")    
                
            
                
 


def load_instructions():
    try:
        with open('instructions.txt', 'r') as file:
            instructions = file.read().splitlines()
    except FileNotFoundError:
        print("Error: 'instructions.txt' not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    return instructions

def execute_instruction(decoded_instr, alu, registers, memory):
    opcode = decoded_instr['type']  # Use 'type' instead of 'opcode'
    args = decoded_instr.get('args', [])  # Default to empty list if 'args' is missing
    
    if (decoded_instr.get('dest')):
        args = list(args)
        args.append(decoded_instr.get('dest'))
        args = tuple(args)

    if (decoded_instr.get('src')):
        args = list(args)
        args.append(decoded_instr.get('src'))
        args = tuple(args)
    
    if (decoded_instr.get('src1')):
        args = list(args)
        args.append(decoded_instr.get('src1'))
        args = tuple(args)

    if (decoded_instr.get('src2')):
        args = list(args)
        args.append(decoded_instr.get('src2'))
        args = tuple(args)

    if (decoded_instr.get('imm')):
        args = list(args)
        args.append(decoded_instr.get('imm'))
        args = tuple(args)

    if (decoded_instr.get('base')):
        args = list(args)
        args.append(decoded_instr.get('base'))
        args.append(decoded_instr.get('offset'))
        args = tuple(args)
        
    if (decoded_instr.get('shift')):
        args = list(args)
        args.append(decoded_instr.get('shift'))
        args = tuple(args)
        
    if opcode == 'beq':
        args = list(args)
        args.append(decoded_instr.get('offset'))
        args = tuple(args)
        
    # Ensure args has enough elements before accessing them
    if opcode in ['add', 'sub', 'mul', 'and', 'or'] and len(args) >= 3:
        reg1_index = args[0]
        reg2_index = args[1]
        reg3_index = args[2]
        
        if (opcode == 'and'):
            opcode = 'and_op'
        if (opcode == 'or'):
            opcode = 'or_op'

        result = getattr(alu, opcode)(registers, reg1_index, reg2_index, reg3_index)
        registers.write_reg(args[0], result)
    elif opcode == 'addi' and len(args) >= 3:
        reg1_index = args[0]
        reg2_index = args[1]
        imm = int(args[2])
        result = alu.addi(registers, reg1_index, reg2_index, imm)
        registers.write_reg(args[0], result)
    elif opcode == 'lw' and len(args) >= 2:
        base = registers.read_reg(args[1])
        offset = args[2]
        address = base + offset
        value = memory.load_word(address)
        registers.write_reg(args[0], value)
        print("Memory address register = ", address)
        print("Memory data register = ", value)
    elif opcode == 'sw' and len(args) >= 2:
        reg = registers.read_reg(args[0])
        base = registers.read_reg(args[1])
        offset = args[2]
        address = base + offset
        memory.store_word(address, reg)
        print("Memory address register = ", address)
        print("Memory data register = ", reg)
    elif opcode =='sll' and len(args) >= 3:
        reg1_index = args[0]
        reg2_index = args[1]
        shift_amount = args[2]
        result = alu.sll(registers, reg1_index, reg2_index, shift_amount)
        registers.write_reg(args[0], result)
        
    elif opcode =='srl' and len(args) >= 3:
        reg1_index = args[0]
        reg2_index = args[1]
        shift_amount = args[2]
        result = alu.srl(registers, reg1_index, reg2_index, shift_amount)
        registers.write_reg(args[0], result)
    
    elif opcode == 'nop':
        pass  # No operation


if __name__ == "__main__":
    main(debug=True)