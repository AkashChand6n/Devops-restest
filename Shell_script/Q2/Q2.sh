#Shell script that checks if a given file is a symbolic link and displays the target of the link.
#!/bin/bash


if [ $# -ne 1 ]; then
    echo "Usage: $0 <filename>"
    exit 1
fi


file="$1"

# Check if file exists
if [ ! -e "$file" ]; then
    echo "Error: '$file' does not exist"
    exit 1
fi

# Check if it's a symbolic link
if [ -L "$file" ]; then
    target=$(readlink -f "$file")
    echo "'$file' is a symbolic link"
    echo "Target: $target"
else
    echo "'$file' is not a symbolic link"
fi