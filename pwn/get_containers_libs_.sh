#!/bin/bash

# 引数チェック
if [ $# -lt 3 ]; then
    echo "usage: $0 my_container /srv/lib/x86_64-linux-gnu" ./out_dir
    exit 1
fi

CONTAINER_NAME="$1"
SRC_DIR="$2"
DEST_DIR="$3"

FILES=(
    "ld-linux-x86-64.so.2"
    "libc.so.6"
)

mkdir -p "$DEST_DIR"

for FILE in "${FILES[@]}"; do
    SRC_PATH="${SRC_DIR}/${FILE}"
    docker cp "$CONTAINER_NAME:$SRC_PATH" "$DEST_DIR/"
    echo "Copied $CONTAINER_NAME:$SRC_PATH to $DEST_DIR/"
done

echo "All files copied successfully!"
