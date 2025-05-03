#Shell script that checks if a given file is a symbolic link and displays the target of the link.
#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <filename>"
    exit 1
fi

file="$1"

if [ -L "$file" ]; then
    echo "'$file' is a symbolic link"
    target=$(readlink -f "$file")
    if [ -e "$target" ]; then
        echo "Target: $target"
    else
        echo "Warning: symbolic link is broken (target '$target' does not exist)"
    fi
elif [ -e "$file" ]; then
    echo "'$file' is not a symbolic link"
else
    echo "Error: '$file' does not exist"
fi
