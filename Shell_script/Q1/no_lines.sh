#Shell script that counts the number of lines in file(s) that contain a specific word

#!/bin/bash

#Check if minimum arguments are provided
if [ $# -lt 2 ]; then
    echo "Usage: $0 search_word file1 [file2 ...]"
    exit 1
fi

search_word="$1"
shift

# Initialize total line count
total_count=0

# show the each file
for file in "$@"; do
    if [ ! -f "$file" ]; then
        echo "Error: File '$file' does not exist"
        continue
    fi

    # Count lines containing word
    count=$(grep -c "$search_word" "$file")
    echo "Lines containing '$search_word' in $file: $count"
    total_count=$((total_count + count))
done

# Print total count
if [ $# -gt 1 ]; then
    echo "Total lines containing '$search_word' in all files: $total_count"
fi