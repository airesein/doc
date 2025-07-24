string1 = "_EUUmpVxbw#b7uE~&ff7xq%nfSd7sxusk"

# 将字符串转换为字节
byte_data = string1.encode('utf-8')


# 异或 0x16 解密
decrypted = bytes([b ^ 0x16 for b in byte_data])

# 输出解密结果
print(decrypted.decode('utf-8', errors='ignore'))
