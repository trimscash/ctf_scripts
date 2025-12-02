#!/bin/bash

TARGET_BINARY="$1"

LIBC_PATH="./libc.so.6"
LD_PATH="./ld-linux-x86-64.so.2"

if [[ ! -f "$TARGET_BINARY" ]]; then
    echo "error: $TARGET_BINARY not found"
    exit 1
fi

# echo "changing libc.so.6 to $LIBC_PATH ..."
# patchelf --replace-needed libc.so.6 "$LIBC_PATH" "$TARGET_BINARY"

echo "setting ld-linux-x86-64.so.2 to $LD_PATH ..."
patchelf --set-interpreter "$LD_PATH" "$TARGET_BINARY"

echo
patchelf --set-rpath './' "$TARGET_BINARY"

echo "changed binary....."
ldd "$TARGET_BINARY"

