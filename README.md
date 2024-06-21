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
        direction LR
        subgraph Class: DotParser
                direction LR
                node_22df8e62["62: _parse_legend_colors()"]:::leaf
                node_5f8b35b1["44: _parse_subgraphs()"]:::filled
                node_5497ea49["150: add_to_markdown()"]:::trunk
                node_02ca0a3f["129: create_node_style()"]:::leaf
                node_51d03dd9["118: edges_to_mermaid()"]:::filled
                node_16523e49["77: get_edges()"]:::leaf
                node_5c227bbb["74: get_subgraphs()"]:::filled
                node_d13d141b["91: subgraphs_to_mermaid()"]:::filled
                node_2dadf109["136: to_mermaid()"]:::trunk
        end
        node_22df8e62["62: _parse_legend_colors()"]:::leaf
        node_5f8b35b1["44: _parse_subgraphs()"]:::filled
        node_5497ea49["150: add_to_markdown()"]:::trunk
        node_02ca0a3f["129: create_node_style()"]:::leaf
        node_51d03dd9["118: edges_to_mermaid()"]:::filled
        node_16523e49["77: get_edges()"]:::leaf
        node_5c227bbb["74: get_subgraphs()"]:::filled
        node_d13d141b["91: subgraphs_to_mermaid()"]:::filled
        node_2dadf109["136: to_mermaid()"]:::trunk
        node_961733e1["20: get_dot()"]:::trunk
        node_067f6587["9: read()"]:::leaf
        node_873f0360["15: save()"]:::leaf
    end

    %% Edges
    node_5f8b35b1 --> node_22df8e62
    node_5f8b35b1 --> node_5f8b35b1
    node_5497ea49 --> node_067f6587
    node_5497ea49 --> node_873f0360
    node_51d03dd9 --> node_16523e49
    node_5c227bbb --> node_5f8b35b1
    node_d13d141b --> node_5c227bbb
    node_2dadf109 --> node_02ca0a3f
    node_2dadf109 --> node_51d03dd9
    node_2dadf109 --> node_d13d141b
    node_961733e1 --> node_067f6587

    %% Edge styles
    linkStyle 0 stroke:#E69F00
    linkStyle 1 stroke:#E69F00
    linkStyle 2 stroke:#E69F00
    linkStyle 3 stroke:#E69F00
    linkStyle 4 stroke:#E69F00
    linkStyle 5 stroke:#009E73
    linkStyle 6 stroke:#009E73
    linkStyle 7 stroke:#E69F00
    linkStyle 8 stroke:#E69F00
    linkStyle 9 stroke:#E69F00
    linkStyle 10 stroke:#E69F00

    %% Node styles
    classDef filled fill:#555555,stroke:#000000,stroke-width:2px;
    classDef leaf fill:#5555FF,stroke:#000000,stroke-width:2px;
    classDef trunk fill:#AA5555,stroke:#000000,stroke-width:2px;
```

Compare it with code2flow png file:

![package.png](./package.png)