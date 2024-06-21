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
            node_eb797174["62: _parse_legend_colors()"]:::leaf
            node_1c8038fc["44: _parse_subgraphs()"]:::filled
            node_3f7b9c44["149: add_to_markdown()"]:::trunk
            node_f9f1c152["128: create_node_style()"]:::leaf
            node_3208e0e0["117: edges_to_mermaid()"]:::filled
            node_801bb883["77: get_edges()"]:::leaf
            node_f0610ee1["74: get_subgraphs()"]:::filled
            node_591e81b1["91: subgraphs_to_mermaid()"]:::filled
            node_97d1ba45["135: to_mermaid()"]:::trunk
        end
        node_eb797174["62: _parse_legend_colors()"]:::leaf
        node_1c8038fc["44: _parse_subgraphs()"]:::filled
        node_3f7b9c44["149: add_to_markdown()"]:::trunk
        node_f9f1c152["128: create_node_style()"]:::leaf
        node_3208e0e0["117: edges_to_mermaid()"]:::filled
        node_801bb883["77: get_edges()"]:::leaf
        node_f0610ee1["74: get_subgraphs()"]:::filled
        node_591e81b1["91: subgraphs_to_mermaid()"]:::filled
        node_97d1ba45["135: to_mermaid()"]:::trunk
        node_74fde869["20: get_dot()"]:::trunk
        node_a7893f35["9: read()"]:::leaf
        node_9f9b9383["15: save()"]:::leaf
    end

    %% Edges
    node_1c8038fc --> node_eb797174
    node_1c8038fc --> node_1c8038fc
    node_3f7b9c44 --> node_a7893f35
    node_3f7b9c44 --> node_9f9b9383
    node_3208e0e0 --> node_801bb883
    node_f0610ee1 --> node_1c8038fc
    node_591e81b1 --> node_f0610ee1
    node_97d1ba45 --> node_f9f1c152
    node_97d1ba45 --> node_3208e0e0
    node_97d1ba45 --> node_591e81b1
    node_74fde869 --> node_a7893f35

    %% Edge styles
    linkStyle 0 stroke:#F0E442
    linkStyle 1 stroke:#F0E442
    linkStyle 2 stroke:#F0E442
    linkStyle 3 stroke:#F0E442
    linkStyle 4 stroke:#000000
    linkStyle 5 stroke:#E69F00
    linkStyle 6 stroke:#E69F00
    linkStyle 7 stroke:#0072B2
    linkStyle 8 stroke:#0072B2
    linkStyle 9 stroke:#0072B2
    linkStyle 10 stroke:#E69F00

    %% Node styles
    classDef filled fill:#555555,stroke:#000000,stroke-width:2px;
    classDef leaf fill:#5555FF,stroke:#000000,stroke-width:2px;
    classDef trunk fill:#AA5555,stroke:#000000,stroke-width:2px;
```

Compare it with code2flow png file:

![package.png](./package.png)