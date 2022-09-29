import json
from typing import Tuple, List, Any


def main() -> Tuple[List[Any], List[Any], List[Any], List[Any]]:
    with open('data.txt', 'r') as file:
        data = json.loads(file.read())
    parse_command = list()
    copy_command = list()
    run_command = list()
    bad_command = list()
    for obj in data:
        if 'function' in obj and 'value' in obj and obj['value'] is not None:
            if obj['function'] == 'parse':
                parse_command.append(obj)
            elif obj['function'] == 'copy':
                copy_command.append(obj)
            elif obj['function'] == 'run':
                run_command.append(obj)
        if 'function' not in obj or 'value' not in obj:
            bad_command.append(obj)
    return parse_command, copy_command, run_command, bad_command


if __name__ == '__main__':
    parse_command, copy_command, run_command, bad_command = main()

    assert parse_command == [{'function': 'parse', 'help': 'file help', 'value': 'file'}]
    assert copy_command == [{'function': 'copy', 'help': 'copy help', 'value': 'file'}]
    assert run_command == [
        {'function': 'run', 'help': 'command help', 'value': 'command'},
        {'function': 'run', 'help': 'execute help', 'value': 'execute'},
        {'function': 'run', 'value': 'list'}]
    assert len(bad_command) == 2
