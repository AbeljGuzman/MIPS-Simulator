class Memory:
    def __init__(self, size=4096):  # Default size is set to 4096 words (16KB if word = 4 bytes)
        # Memory array initialized to zero
        self.memory = [0] * size

    def load_word(self, address):
        # Ensure address is word-aligned; MIPS addresses must be divisible by 4 (word = 4 bytes)
        if address % 4 != 0:
            raise ValueError("Memory address must be word-aligned")
        # Convert byte address to word index
        word_index = address // 4
        return self.memory[word_index]

    def store_word(self, address, data):
        # Ensure address is word-aligned
        if address % 4 != 0:
            raise ValueError("Memory address must be word-aligned")
        # Convert byte address to word index
        word_index = address // 4
        self.memory[word_index] = data
    
    def __repr__(self):
        # This method is useful for debugging purposes, to view the entire memory state
        return f"Memory(size={len(self.memory)})"
    
    def debug_memory_access(self, address, operation="read"):
        if operation == "read":
            print(f"Read from memory address {address}: {self.memory[address // 4]}")
        else:
            print(f"Wrote to memory address {address}: {self.memory[address // 4]}")
    
    def debug_memory_state(self):
        print("Memory Content:")
        for i, val in enumerate(self.memory):
            if val != 0:  # Print only non-zero values
                print(f"Memory Address {i * 4}: {val}")
        if not any(self.memory):
            print("No memory addresses have been affected.")
