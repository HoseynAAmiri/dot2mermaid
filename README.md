# dot2mermaid

A library that convers .dot file to mermaid and markdown.

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
        subgraph Class: DotParser
            node_3fb2c4c4["61: _parse_legend_colors()"]:::leaf
            node_e0f78b1b["43: _parse_subgraphs()"]:::filled
            node_80f26d2d["143: add_to_markdown()"]:::trunk
            node_3b2214c5["76: get_edges()"]:::leaf
            node_36838d77["73: get_subgraphs()"]:::filled
            node_3e889beb["90: subgraphs_to_mermaid()"]:::filled
            node_e83bdddf["137: to_markdown()"]:::trunk
            node_528d619b["116: to_mermaid()"]:::filled
        end
        node_3fb2c4c4["61: _parse_legend_colors()"]:::leaf
        node_e0f78b1b["43: _parse_subgraphs()"]:::filled
        node_80f26d2d["143: add_to_markdown()"]:::trunk
        node_3b2214c5["76: get_edges()"]:::leaf
        node_36838d77["73: get_subgraphs()"]:::filled
        node_3e889beb["90: subgraphs_to_mermaid()"]:::filled
        node_e83bdddf["137: to_markdown()"]:::trunk
        node_528d619b["116: to_mermaid()"]:::filled
        node_0e6d2aa3["19: get_dot()"]:::trunk
        node_80dbcb82["8: read()"]:::leaf
        node_7467b54c["14: save()"]:::leaf
    end

    %% Edges
    node_e0f78b1b --> node_3fb2c4c4
    node_e0f78b1b --> node_e0f78b1b
    node_80f26d2d --> node_80dbcb82
    node_80f26d2d --> node_7467b54c
    node_36838d77 --> node_e0f78b1b
    node_3e889beb --> node_36838d77
    node_e83bdddf --> node_528d619b
    node_528d619b --> node_3b2214c5
    node_528d619b --> node_3e889beb
    node_0e6d2aa3 --> node_80dbcb82

    %% Edge styles
    linkStyle 0 stroke:#009E73
    linkStyle 1 stroke:#009E73
    linkStyle 2 stroke:#0072B2
    linkStyle 3 stroke:#0072B2
    linkStyle 4 stroke:#CC79A7
    linkStyle 5 stroke:#009E73
    linkStyle 6 stroke:#CC79A7
    linkStyle 7 stroke:#009E73
    linkStyle 8 stroke:#009E73
    linkStyle 9 stroke:#009E73

    %% Node styles         
    classDef filled fill:#555555,stroke:#000000,stroke-width:2px;         
    classDef leaf fill:#5555FF,stroke:#000000,stroke-width:2px;         
    classDef trunk fill:#AA5555,stroke:#000000,stroke-width:2px;         
```

Compare it with code2flow png file:

![package.png](./package.png)