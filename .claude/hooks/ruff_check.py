#!/usr/bin/env python3
"""Hook PostToolUse: roda `ruff check` + `ruff format --check` no arquivo
.py que acabou de ser editado/criado (Write/Edit/MultiEdit). Se falhar,
bloqueia via JSON `{"decision": "block", "reason": ...}` — o harness devolve
isso como erro que precisa ser corrigido antes de seguir, não como aviso.
"""

import json
import os
import re
import subprocess
import sys

_ANSI_ESCAPE = re.compile(r"\x1b\[[0-9;]*m")


def _strip_ansi(text: str) -> str:
    return _ANSI_ESCAPE.sub("", text)


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0

    file_path = payload.get("tool_input", {}).get("file_path", "")
    if not file_path.endswith(".py"):
        return 0

    checks = [
        ("ruff check", ["ruff", "check", "--output-format=concise", file_path]),
        ("ruff format --check", ["ruff", "format", "--check", file_path]),
    ]
    env = {**os.environ, "NO_COLOR": "1"}

    failures = []
    for label, cmd in checks:
        result = subprocess.run(cmd, capture_output=True, text=True, env=env)
        if result.returncode != 0:
            output = _strip_ansi((result.stdout + result.stderr).strip())
            failures.append(f"[{label}]\n{output}")

    if not failures:
        return 0

    reason = (
        f"Ruff encontrou problema(s) em {file_path} — corrija antes de continuar.\n\n"
        + "\n\n".join(failures)
    )
    print(json.dumps({"decision": "block", "reason": reason}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
