#!/bin/bash

INPUT=$(cat)
FILE=$(echo "$INPUT" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('tool_input',{}).get('path',''))" 2>/dev/null)

# Format TypeScript/JS/JSON/CSS/MD files
if [[ "$FILE" =~ \.(ts|tsx|js|jsx|css|json|md)$ ]]; then
    if [ -f "$FILE" ]; then
        npx prettier --write "$FILE" --log-level silent 2>/dev/null
    fi
fi

# Format Python files
if [[ "$FILE" =~ \.py$ ]]; then
    if [ -f "$FILE" ]; then
        python3 -m black "$FILE" --quiet 2>/dev/null || true
    fi
fi

exit 0
