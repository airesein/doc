s=[35]#放adex数组里的值
with open("decrypted.dex", "wb")as f:

    f.write(bytes(s))
with open("enreal", "rb") as f:
    data = list(f.read())
for i in range(len(data)):
    data[i] = (data[i] << 2)|(data[i]>> 6)
    data[i] &= 0xff
    data[i] ^=0x55 #改为你自己的字节
    data[i] = (data[i] >> 3)|(data[i]<< 5)
    data[i] &= 0xff
with open("decode_enreal", "wb")as f:

    f.write(bytes(data))