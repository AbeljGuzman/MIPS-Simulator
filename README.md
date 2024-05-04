# MIPS Simulator
- Abel Guzman 
- Freddy Martinez 
- Martin Rivera

This Python script simulates the execution of MIPS instructions using a simplified pipeline architecture.

## Table of Contents

- [Introduction](#introduction)
- [Files Included](#files-included)
- [Usage](#usage)
- [Instructions Format](#instructions-format)
- [Pipeline Stages](#pipeline-stages)

## Introduction

This simulator is designed to execute MIPS-like assembly instructions. It includes components for Register File (Registers.py), Arithmetic Logic Unit (ALU.py), Memory (Memory.py), Instruction Decoder (Decoder.py), and a simplified pipeline (Pipeline.py).

## Files Included

- `ALU.py`: Defines the Arithmetic Logic Unit class.
- `Registers.py`: Defines the Register File class.
- `Memory.py`: Defines the Memory class.
- `Decoder.py`: Provides functions to parse and decode assembly instructions.
- `Pipeline.py`: Implements a simplified pipeline for instruction execution.

## Usage

To use the simulator, you can run `main.py`. Optionally, you can enable debugging mode by setting `debug=True`.

Example:
```bash
python main.py
```
## Instructions Format

Instructions are expected to be stored in a file named instructions.txt in the same directory. Each line in the file should contain a single assembly instruction in a simplified format.

Example:
```bash
ADDI $t0, $zero, 5
ADDI $t1, $zero, 10
ADD $t2, $t0, $t1
SW $t2, 0($zero)
LW $t3, 0($zero)
NOP
```

## Pipeline Stages

The simulator implements a simplified pipeline with the following stages:

- Instruction Fetch (IF)
- Instruction Decode (ID)
- Execution (EX)
- Memory Access (MEM)
- Write Back (WB)
