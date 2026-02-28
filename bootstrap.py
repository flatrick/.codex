#!/usr/bin/env python3
"""Build config.toml from baseline + profile + optional local override."""

from pathlib import Path
import os
import sys


def parse_simple_toml(path: Path) -> dict[str, str]:
    parsed: dict[str, str] = {}
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        key, value = line.split('=', 1)
        parsed[key.strip()] = value.strip()
    return parsed


def main() -> int:
    root = Path('.')
    profile_name = os.environ.get('CODEX_PROFILE', 'safe')
    profile = root / 'profiles' / f'{profile_name}.toml'
    files = [root / 'config.template.toml', profile, root / 'config.local.toml']

    if not profile.exists():
        print(f'Profile not found: {profile}', file=sys.stderr)
        return 1

    merged: dict[str, str] = {}
    for path in files:
        if path.exists():
            merged.update(parse_simple_toml(path))

    lines = [f"{k} = {merged[k]}" for k in sorted(merged)]
    (root / 'config.toml').write_text('\n'.join(lines) + '\n')
    print(f'Wrote config.toml using profile: {profile.name}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
