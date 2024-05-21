def fetch_value(line: str, tag: str) -> str:
    """
    >>> fetch_value('trallalallala <b>sallalallalala</b> tumturumm' , 'b')
    'sallalallalala'
    >>> fetch_value('<ele>201.1999969482421875</ele>', 'ele')
    '201.1999969482421875'
    >>> fetch_value('<ns3:hr>57</ns3:hr>', 'ns3:hr')
    '57'
    >>> fetch_value('<foo>bar</foo>', 'foo')
    'bar'
    >>> fetch_value('bar bar bar <bar>foo</bar> bar <foo>bar</foo> bar', 'foo')
    'bar'
    """
    return line.split(f"<{tag}>")[1].split(f"</{tag}>")[0].strip()


def fetch_tag_values(file: str, tag: str, type: type = int) -> list[str]:
    values = []
    with open(file) as f:
        for line in f:
            if f"<{tag}>" in line:
                values.append(type(fetch_value(line, tag)))
    return values


def fetch_arg_values(opentag: str) -> dict[str, str]:
    """
    >>> fetch_arg_values('<trkpt lat="47.6332789845764636993408203125" lon="16.60075460560619831085205078125">')
    {'lat': '47.6332789845764636993408203125', 'lon': '16.60075460560619831085205078125'}
    >>> fetch_arg_values('<a href="https://www.google.com" target="_blank">')
    {'href': 'https://www.google.com', 'target': '_blank'}
    >>> fetch_arg_values('<foo bar="baz" qux="quux">')
    {'bar': 'baz', 'qux': 'quux'}
    >>> fetch_arg_values('<html lang="en">')
    {'lang': 'en'}
    """
    args = {}
    opentag = opentag.replace("<", " ").replace(">", " ")
    for token in opentag.split(" "):
        if "=" in token:
            name, value = token.split("=")
            args[name.strip()] = value.strip().strip('"')
    return args


if __name__ == "__main__":
    import doctest
    doctest.testmod(exclude_empty=True)