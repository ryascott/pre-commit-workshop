from pathlib import Path


def validate_uppercase_filename(filename: str) -> int:
    # extract the name so that `/my/repo/x.py` becomes `x`
    name = Path(filename).stem

    # check if uppercase
    if failure := name != name.upper():
        print(f'file {name} not UPPERCASE ')

    # convert to an exit code for later
    return int(failure)
