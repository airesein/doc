key = [0x3ED6325B,0xD709BF17,0xE3F27E18,0xA0870791,0x146D6F9,0x7C6140FF,0x10B69406,0x94DDE0F6,0x40B2BB6C]
res = [  0x44854502
,0x946CE85E
,0x88B54F65
,0xE9DF35C2
,0x312F8682
,0x313579B6
,0x7AD0C668
,0xED9183B5
,0x1881F30A
]
flag = []
for i in range(len(key)):
    flag.append(hex(key[i]^res[i]))

print((flag))

# 处理十六进制字符串列表
hex_strings = flag
decoded_flag = ""
tmp = ""
for hex_string in hex_strings:
    # 移除'0x'前缀
    hex_string = hex_string[2:]
    
    # 每两个字符一组转换为一个字节
    tmp = ""
    for i in range(0, len(hex_string), 2):
        
        if i+1 < len(hex_string):  # 确保有完整的字节
            byte = int(hex_string[i:i+2], 16)
            tmp += chr(byte)
    decoded_flag += tmp[::-1]

print("Decoded flag:", decoded_flag)


# 1234567890abcdefghijklmnopqrstuvwxyz
flag = decoded_flag
change_1 = "1234567890abcdefghijklmnopqrstuvwxyz"
change_2 = "vfw8xgy4zh9i2j0k5lam1nbo6pcq3rds7teu"

res = ""
for i in range(len(change_1)):
    tmp = change_2.index(change_1[i])
    res +=flag[tmp]
print(res)
