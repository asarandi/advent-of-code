#!/usr/bin/env python3

with open("input.txt", "r") as fp:
    program = fp.read().splitlines()
    fp.close()

pc, registers = 0, {'a':0, 'b':0}
while pc < len(program):
    print(pc, program[pc], registers)
    instr = program[pc].split(' ')[0]
    if instr == 'hlf':
        r = program[pc].split(' ')[1]
        registers[r] >>= 1
        pc += 1
    elif instr == 'tpl':
        r = program[pc].split(' ')[1]
        registers[r] *= 3
        pc += 1        
    elif instr == 'inc':
        r = program[pc].split(' ')[1]
        registers[r] += 1
        pc += 1        
    elif instr == 'jmp':
        jmp = int(program[pc].split(' ')[1])
        pc += jmp
    elif instr == 'jie':
        r = program[pc].split(' ')[1][0]
        jmp = int(program[pc].split(' ')[2])
#        pc += jmp if not registers[r] & 1 else 1
        pc += jmp if registers[r] % 2 == 0 else 1
    elif instr == 'jio':
        r = program[pc].split(' ')[1][0]
        jmp = int(program[pc].split(' ')[2])
#        pc += jmp if registers[r] & 1 else 1
        pc += jmp if registers[r] % 2 == 1 else 1


print(registers)
print("aoc2015d23p01:", registers['b'])
