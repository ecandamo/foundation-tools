#!/bin/bash

INPUT=$(cat)
FILE=$(echo "$INPUT" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('tool_input',{}).get('path',''))" 2>/dev/null)

# Format Python files — the only stack this template formats automatically
if [[ "$FILE" =~ \.py$ ]]; then
    if [ -f "$FILE" ]; then
        python3 -m black "$FILE" --quiet 2>/dev/null || true
    fi
fi

exit 0
