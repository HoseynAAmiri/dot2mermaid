from dot2mermaid import DotParser, get_dot

path = "./dot2mermaid"
dot_file = get_dot(path)
parser = DotParser(dot_file)
colors = {
    'regular': '#555555',
    'trunk': '#AA5555',
    'leaf': '#5555FF'
}

markdown_content = parser.to_mermaid(colors=colors)
parser.add_to_markdown('./README.md', markdown_content)
