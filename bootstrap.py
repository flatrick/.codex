#!/usr/bin/env python3
"""Build config.toml from baseline + profile + optional local override."""

from pathlib import Path
from datetime import date, datetime, time
import os
import re
import sys
import tomllib


KEY_SEGMENT_RE = re.compile(r'^[A-Za-z0-9_-]+$')


def format_key_segment(segment: str) -> str:
    if KEY_SEGMENT_RE.match(segment):
        return segment
    escaped = segment.replace('\\', '\\\\').replace('"', '\\"')
    return f'"{escaped}"'


def format_toml_value(value: object) -> str:
    if isinstance(value, str):
        escaped = value.replace('\\', '\\\\').replace('"', '\\"')
        return f'"{escaped}"'
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, list):
        return '[' + ', '.join(format_toml_value(item) for item in value) + ']'
    if isinstance(value, (date, datetime, time)):
        return value.isoformat()
    raise TypeError(f'unsupported value type: {type(value).__name__}')


def parse_toml(path: Path) -> dict[str, object]:
    return tomllib.loads(path.read_text(encoding='utf-8'))


def deep_merge(base: dict[str, object], updates: dict[str, object]) -> None:
    for key, value in updates.items():
        current = base.get(key)
        if isinstance(current, dict) and isinstance(value, dict):
            deep_merge(current, value)
        else:
            base[key] = value


def emit_table_lines(data: dict[str, object], prefix: tuple[str, ...] = ()) -> list[str]:
    lines: list[str] = []
    scalar_items = sorted((k, v) for k, v in data.items() if not isinstance(v, dict))
    table_items = sorted((k, v) for k, v in data.items() if isinstance(v, dict))

    if prefix:
        table_name = '.'.join(format_key_segment(segment) for segment in prefix)
        lines.append(f'[{table_name}]')

    for key, value in scalar_items:
        lines.append(f'{format_key_segment(key)} = {format_toml_value(value)}')

    for index, (key, value) in enumerate(table_items):
        if lines:
            lines.append('')
        lines.extend(emit_table_lines(value, prefix + (key,)))
        if index != len(table_items) - 1:
            lines.append('')

    return lines


def main() -> int:
    root = Path('.')
    profile_name = os.environ.get('CODEX_PROFILE', 'safe')
    profile = root / 'profiles' / f'{profile_name}.toml'
    files = [root / 'config.template.toml', profile, root / 'config.local.toml']

    if not profile.exists():
        print(f'Profile not found: {profile}', file=sys.stderr)
        return 1

    merged: dict[str, object] = {}
    try:
        for path in files:
            if path.exists():
                deep_merge(merged, parse_toml(path))
    except (TypeError, tomllib.TOMLDecodeError) as exc:
        print(f'Config parse error: {exc}', file=sys.stderr)
        return 1

    lines = emit_table_lines(merged)
    while lines and not lines[-1]:
        lines.pop()
    (root / 'config.toml').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'Wrote config.toml using profile: {profile.name}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
