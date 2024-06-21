# dot2mermaid

A library for converting dot file to mermaid and markdown.

Requirements:

    - graphviz
    - code2flow
    - pygraphviz

Windows users should install pygraphviz after graphviz by:
```bash
py -m pip install --use-pep517 --config-settings="--global-option=build_ext"  --config-settings="--global-option=-IC:\Program Files\Graphviz\include"  --config-settings="--global-option=-LC:\Program Files\Graphviz\lib" pygraphviz
```

After proper installation, try:

```python
from dot2mermaid import DotParser, get_dot

path = "./path/to/your/code/directory"
dot_file = get_dot(path)
parser = DotParser(dot_file)
colors = {
    'regular': '#555555',
    'trunk': '#AA5555',
    'leaf': '#5555FF'
}
markdown_content = parser.to_mermaid(colors=colors)
parser.add_to_markdown('./README.md', markdown_content)  # to replace mermaid
```

```mermaid
graph LR
    %% Subgraphs
    subgraph File: dot2mermaid
        direction LR
        subgraph Class: DotParser
            direction LR
            node_e87307ce["62: _parse_legend_colors()"]:::leaf
            node_4ae5ed1a["44: _parse_subgraphs()"]:::filled
            node_9e04e6af["151: add_to_markdown()"]:::trunk
            node_1435b8f8["130: create_node_style()"]:::leaf
            node_ba5c8ee4["119: edges_to_mermaid()"]:::filled
            node_6fed536c["77: get_edges()"]:::leaf
            node_c9b26d7f["74: get_subgraphs()"]:::filled
            node_4c63ab74["91: subgraphs_to_mermaid()"]:::filled
            node_c0357d7b["137: to_mermaid()"]:::trunk
        end
        node_e87307ce["62: _parse_legend_colors()"]:::leaf
        node_4ae5ed1a["44: _parse_subgraphs()"]:::filled
        node_9e04e6af["151: add_to_markdown()"]:::trunk
        node_1435b8f8["130: create_node_style()"]:::leaf
        node_ba5c8ee4["119: edges_to_mermaid()"]:::filled
        node_6fed536c["77: get_edges()"]:::leaf
        node_c9b26d7f["74: get_subgraphs()"]:::filled
        node_4c63ab74["91: subgraphs_to_mermaid()"]:::filled
        node_c0357d7b["137: to_mermaid()"]:::trunk
        node_3a20c0f3["20: get_dot()"]:::trunk
        node_98f88cb0["9: read()"]:::leaf
        node_ec40940c["15: save()"]:::leaf
    end

    %% Edges
    node_4ae5ed1a --> node_e87307ce
    node_4ae5ed1a --> node_4ae5ed1a
    node_9e04e6af --> node_98f88cb0
    node_9e04e6af --> node_ec40940c
    node_ba5c8ee4 --> node_6fed536c
    node_c9b26d7f --> node_4ae5ed1a
    node_4c63ab74 --> node_c9b26d7f
    node_c0357d7b --> node_1435b8f8
    node_c0357d7b --> node_ba5c8ee4
    node_c0357d7b --> node_4c63ab74
    node_3a20c0f3 --> node_98f88cb0

    %% Edge styles
    linkStyle 0 stroke:#56B4E9
    linkStyle 1 stroke:#56B4E9
    linkStyle 2 stroke:#CC79A7
    linkStyle 3 stroke:#CC79A7
    linkStyle 4 stroke:#F0E442
    linkStyle 5 stroke:#CC79A7
    linkStyle 6 stroke:#F0E442
    linkStyle 7 stroke:#009E73
    linkStyle 8 stroke:#009E73
    linkStyle 9 stroke:#009E73
    linkStyle 10 stroke:#009E73

    %% Node styles
    classDef filled fill:#555555,stroke:#000000,stroke-width:2px;
    classDef leaf fill:#5555FF,stroke:#000000,stroke-width:2px;
    classDef trunk fill:#AA5555,stroke:#000000,stroke-width:2px;
```

Compare it with code2flow png file:

![package.png](./package.png)