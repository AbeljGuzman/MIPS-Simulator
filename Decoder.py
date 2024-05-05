def ADD(args):
    """Handle the ADD instruction: ADD $dest, $src1, $src2"""
    return {"type": "add", "dest": args[0], "src1": args[1], "src2": args[2]}

def ADDI(args):
    """Handle the ADDI instruction: ADDI $dest, $src, immediate"""
    try:
        return {"type": "addi", "dest": args[0], "src": args[1], "imm": int(args[2])}
    except ValueError:
        return {"type": "addi", "error": "Invalid immediate value"}

def SUB(args):
    """Handle the SUB instruction: SUB $dest, $src1, $src2"""
    return {"type": "sub", "dest": args[0], "src1": args[1], "src2": args[2]}

def MUL(args):
    """Handle the MUL instruction: MUL $dest, $src1, $src2"""
    return {"type": "mul", "dest": args[0], "src1": args[1], "src2": args[2]}

def AND(args):
    """Handle the AND instruction: AND $dest, $src1, $src2"""
    return {"type": "and", "dest": args[0], "src1": args[1], "src2": args[2]}

def OR(args):
    """Handle the OR instruction: OR $dest, $src1, $src2"""
    return {"type": "or", "dest": args[0], "src1": args[1], "src2": args[2]}

def SLL(args):
    """Handle the SLL instruction: SLL $dest, $src, shift_amount"""
    try:
        return {"type": "sll", "dest": args[0], "src": args[1], "shift": int(args[2])}
    except ValueError:
        return {"type": "sll", "error": "Invalid shift amount"}

def SRL(args):
    """Handle the SRL instruction: SRL $dest, $src, shift_amount"""
    try:
        return {"type": "srl", "dest": args[0], "src": args[1], "shift": int(args[2])}
    except ValueError:
        return {"type": "srl", "error": "Invalid shift amount"}

def LW(args):
    """Handle the LW instruction: LW $dest, offset($base)"""
    try:
        offset, base = args[1].strip(')').split('(')
        return {"type": "lw", "dest": args[0], "base": base, "offset": int(offset)}
    except ValueError:
        return {"type": "lw", "error": "Invalid memory address"}

def SW(args):
    """Handle the SW instruction: SW $src, offset($base)"""
    try:
        offset, base = args[1].strip(')').split('(')
        return {"type": "sw", "src": args[0], "base": base, "offset": int(offset)}
    except ValueError:
        return {"type": "sw", "error": "Invalid memory address"}

def BEQ(args):
    """Handle the BEQ instruction: BEQ $src1, $src2, label"""
    return {"type": "beq", "src1": args[0], "src2": args[1], "offset": args[2]}

def J(args):
    """Handle the J instruction: J target"""
    return {"type": "j", "target": args[0]}

def NOP(args=[]):
    """Handle the NOP instruction: No operation"""
    return {"type": "nop"}

# Dictionary to map opcode strings to their corresponding functions
switch_cases = {
    "add": ADD,
    "addi": ADDI,
    "sub": SUB,
    "mul": MUL,
    "and": AND,
    "or": OR,
    "sll": SLL,
    "srl": SRL,
    "lw": LW,
    "sw": SW,
    "beq": BEQ,
    "j": J,
    "nop": NOP,
}

def parse_instruction(instruction):
    """Parse a single MIPS instruction and return a dictionary representing the instruction.
    
    Args:
        instruction (str): A string representing the MIPS instruction.

    Returns:
        dict: A dictionary containing the instruction type and necessary arguments.
    """
    instruction = instruction.replace(",", "")
    parts = instruction.strip().lower().split()
    opcode = parts[0]
    args = parts[1:]
    func = switch_cases.get(opcode, lambda args: {"type": "invalid", "args": args})
    result = func(args)
    result['opcode'] = opcode  # Ensure 'opcode' is always included
    return result
