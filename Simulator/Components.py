class RF:
    def __init__(self):
        self.registers = {
        "000": {"r0" : ""},
        "001": {"r1" : ""},
        "010": {"r2" : ""},
        "011": {"r3" : ""},
        "100": {"r4" : ""},
        "101": {"r5" : ""},
        "110": {"r6" : ""},
        "111": {"flags" : ""},
        }

def int_to_7bit_binary(number):
  binary_string = bin(number)[2:]
  if len(binary_string) < 7:
    binary_string = "0" * (7 - len(binary_string)) + binary_string

  return binary_string
        
class MEM:
    def __init__(self):
        self.memory = {}
        for i in range(128):
            self.memory[int_to_7bit_binary(i)] = ""
            
class PC:
    def __init__(self):
        self.value = 0
        self.address = int_to_7bit_binary(self.value)
    def increment(self):
        self.value +=1
        self.address = int_to_7bit_binary(self.value)
        
class EE:
    def __init__(self):
            self.op_codes = {
            "00000": "add",
            "00001": "sub",
            "00110": "mul",
            "00111": "div",
            "01010": "xor",
            "01011": "or",
            "01100": "and",
            "01101": "not",
            "01110": "cmp",
            "00010": "mov",
            "00011": "mov",
            "00100": "ld",
            "00101": "st",
            "01000": "rs",
            "01001": "ls",
            "01111": "jmp",
            "11100": "jlt",
            "11101": "jgt",
            "11111": "je",
            "11010": "hlt",
            }
    """def decode_execute(self,code):
        for i in code:
            if (i[:5])=="00010":
            # mov reg1 #imm
            # i[7:9]- reg   i[-7:]- value to be moved
                dic.reg[i[6:9]]= i[-7:]
            print(f'{func.to_binary(machine_code.index(i),7)} 000000000{dic.reg["000"]} 000000000{dic.reg["001"]} 000000000{dic.reg["010"]} 000000000{dic.reg["011"]} 000000000{dic.reg["100"]} 000000000{dic.reg["101"]} 000000000{dic.reg["110"]} 000000000{dic.reg["111"]} ')

            if (i[:5])=="00011":
            # i[-7:-4]- reg1    i[-3:]- reg2
                dic.reg[i[-7:-4]]=dic.reg[i[-3:]]
                print(f'{func.to_binary(machine_code.index(i),7)} 000000000{dic.reg["000"]} 000000000{dic.reg["001"]} 000000000{dic.reg["010"]} 000000000{dic.reg["011"]} 000000000{dic.reg["100"]} 000000000{dic.reg["101"]} 000000000{dic.reg["110"]} 000000000{dic.reg["111"]} ')
        
            if (i[:5])=="00111 ":
            # i[-7:-4]- reg1/3   i[-3:]- reg2/4
                if dic.reg[i[-3:]]=="0":
                    dic.reg["000"]="0"
                    dic.reg["001"]="0"
                    dic.reg["111"]="000000000001000"
                    print(f'000000000{dic.reg["000"]} 000000000{dic.reg["001"]} 000000000{dic.reg["010"]} 000000000{dic.reg["011"]} 000000000{dic.reg["100"]} 000000000{dic.reg["101"]} 000000000{dic.reg["110"]} 000000000{dic.reg["111"]} ')
                else:
                    dic.reg["000"]=(dic.reg[i[-7:-4]])//(dic.reg[i[-3:]])
                    dic.reg["001"]=(dic.reg[i[-7:-4]])%(dic.reg[i[-3:]])
                    print(f'000000000{dic.reg["000"]} 000000000{dic.reg["001"]} 000000000{dic.reg["010"]} 000000000{dic.reg["011"]} 000000000{dic.reg["100"]} 000000000{dic.reg["101"]} 000000000{dic.reg["110"]} 000000000{dic.reg["111"]} ')

            if (i[:5])=="01001 ":
                # i[7:9]- reg   i[-7:]- value to be moved
                str=""
                str+=dic.reg[i[-7:-4]]
                str=str[1:]
                str+="0"

            if (i[:5])=="01110 ":
                # i[-7:-4]- reg1/3   i[-3:]- reg2/4
                if dic.reg[i[-7:-4]]<dic.reg[i[-3:]]:
                    dic.reg["111"]="000000000000100"
                    print(f'000000000{dic.reg["000"]} 000000000{dic.reg["001"]} 000000000{dic.reg["010"]} 000000000{dic.reg["011"]} 000000000{dic.reg["100"]} 000000000{dic.reg["101"]} 000000000{dic.reg["110"]} 000000000{dic.reg["111"]} ')
                if dic.reg[i[-7:-4]]>dic.reg[i[-3:]]:
                    dic.reg["111"]="000000000000010"
                    print(f'000000000{dic.reg["000"]} 000000000{dic.reg["001"]} 000000000{dic.reg["010"]} 000000000{dic.reg["011"]} 000000000{dic.reg["100"]} 000000000{dic.reg["101"]} 000000000{dic.reg["110"]} 000000000{dic.reg["111"]} ')
                if dic.reg[i[-7:-4]]==dic.reg[i[-3:]]:
                    dic.reg["111"]="000000000000001"
                    print(f'000000000{dic.reg["000"]} 000000000{dic.reg["001"]} 000000000{dic.reg["010"]} 000000000{dic.reg["011"]} 000000000{dic.reg["100"]} 000000000{dic.reg["101"]} 000000000{dic.reg["110"]} 000000000{dic.reg["111"]} ')
"""