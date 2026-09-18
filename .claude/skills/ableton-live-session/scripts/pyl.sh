#!/bin/zsh
f="$1"
code=$(python3 -c "
import sys
src=open(sys.argv[1],encoding='utf-8').read()
print('_g={\"song\":song,\"app\":app}\nexec(%s,_g)\nresult=_g.get(\"result\")' % repr(src))
" "$f")
cd "/Volumes/NO NAME/caude/lom-bridge" && python3 lom.py --timeout 180 py "$code"
