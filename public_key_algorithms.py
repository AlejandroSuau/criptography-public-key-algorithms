# -*- coding: utf-8 -*-
import numpy as np
import math
from scipy.ndimage.interpolation import shift

def frequency_test_individual_bits_NITS(sequency = []):
    """
        Calculate test frequency individual bits
        1st Transform all 0 to -1
        2nd Calculate Sobs
        :return: double, Sobs value
    """
    sequency = np.array(sequency)
    sequency[sequency == 0] = -1
    
    sobs = abs(sum(sequency))/math.sqrt(len(sequency))
    return sobs

def burst_test(sequency = []):
    """
        Calculate Burst Test
    """
    vn = 1
    i = 0
    limit = len(sequency)-2
    while i < limit:
        if sequency[i] != sequency[i+1]:
            vn += 1
        i += 1
    
    return vn

def LFSR_output_string(xor_pattern = [], initial_stat = [], output_len = 10):
    """
        :xor_sequence: array, positions where  0 indicates no-connection with xor, 1 otherwise.
        :initial_stat: array, 0 1 0 1 1 1 ...
        :return:
    """
    output_string = ""
    current_stat = np.array(initial_stat)
    for i in range(output_len):
        xor_idx = len(xor_pattern)-1
        carry_bit = None
        while xor_idx >= 0:
            if xor_pattern[xor_idx] == 1:
                if carry_bit is None:
                    carry_bit = current_stat[xor_idx]
                else:
                    carry_bit = bool(current_stat[xor_idx]) != bool(carry_bit)    
            xor_idx -= 1

        output_string += str(current_stat[-1])
        current_stat = shift(current_stat, 1, cval=carry_bit)
    
    return output_string

def Trivium_z_output(stat_register_A = [], stat_register_B = [], stat_register_C = []):
    bit_one = 93 - 1
    bit_two = 66 - 1
    tA = bool(stat_register_A[bit_one]) != bool(stat_register_A[bit_two])
    
    bit_one = 84 - 1
    bit_two = 69 - 1
    tB = bool(stat_register_B[bit_one]) != bool(stat_register_B[bit_two])
    
    bit_one = 111 - 1
    bit_two = 66 - 1
    tC = bool(stat_register_C[bit_one]) != bool(stat_register_C[bit_two])
    
    tSum = bin( tA + tB + tC)
    
    return int(str(tSum)[-1])

def add_round_key(key_string = "", text = ""):
    rows_num = 4
    cols_num = 4
    character_per_col = 2
    key_matrix = []
    text_matrix = []
    xor_matrix = []
    for i in range(rows_num):
        key_matrix.append([])
        text_matrix.append([])
        xor_matrix.append([])
        for j in range(cols_num):
            char_position = i + j*(cols_num*character_per_col)
            
            key_characters = key_string[(char_position):(char_position+character_per_col)]
            key_matrix[i].append(key_characters)
            
            text_characters = text[(char_position):(char_position+character_per_col)]
            text_matrix[i].append(text_characters)
            
            xor_characters = str(hex(int(key_characters, 16) ^ int(text_characters, 16)))[2:].upper()
            xor_matrix[i].append(xor_characters)
    
    return xor_matrix
