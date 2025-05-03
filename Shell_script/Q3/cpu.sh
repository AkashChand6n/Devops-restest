#!/bin/bash

# Email settings
EMAIL="akashchand6n@gmail.com"
SUBJECT="System Resource Alert on $(hostname)"

# Collect system info
echo "===== System Information ====="
echo "Date and Time: $(date)"
echo

echo "===== CPU Usage ====="
CPU_IDLE=$(top -bn1 | grep "Cpu(s)" | awk '{print $8}')
CPU_USAGE=$(echo "100 - $CPU_IDLE" | bc)
echo "CPU Usage: $CPU_USAGE%"
echo

echo "===== Memory Usage ====="
MEM_TOTAL=$(free | awk '/Mem:/ {print $2}')
MEM_USED=$(free | awk '/Mem:/ {print $3}')
MEM_USAGE=$(echo "$MEM_USED * 100 / $MEM_TOTAL" | bc)
echo "Memory Usage: $MEM_USAGE%"
echo

echo "===== Disk Space Usage ====="
df -h
echo

echo "===== Network Statistics ====="
if command -v ifstat &> /dev/null; then
    ifstat 1 1
else
    echo "ifstat not found. Showing fallback from /proc/net/dev:"
    cat /proc/net/dev | awk 'NR>2'
fi
echo

# Alert if thresholds exceeded
if (( $(echo "$CPU_USAGE > 80" | bc -l) )) || (( $(echo "$MEM_USAGE > 80" | bc -l) )); then
    MESSAGE="High resource usage detected on $(hostname):\nCPU: $CPU_USAGE%\nMemory: $MEM_USAGE%"
    echo -e "$MESSAGE" | mail -s "$SUBJECT" "$EMAIL"
    echo "Alert sent to $EMAIL"
else
    echo "System resource usage is normal."
fi