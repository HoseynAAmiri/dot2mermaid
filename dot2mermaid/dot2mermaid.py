import pygraphviz as pgv
import re
import tempfile
import os
from code2flow import code2flow


def read(input_file):
    with open(input_file, 'r') as file:
        content = file.read()
    return content


def save(content, output_file):
    with open(output_file, "w") as f:
        f.write(content)


def get_dot(code_path: str) -> str:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".dot") as temp_file:
        temp_file_path = temp_file.name

    try:
        code2flow(code_path, temp_file_path, hide_legend=False)
        dot_content = read(temp_file_path)

    finally:
        os.remove(temp_file_path)

    return dot_content


class DotParser:
    def __init__(self, dot_file):
        self.graph = pgv.AGraph(dot_file)
        self.direction = None
        self.colors = {
            'regular': None,
            'trunk': None,
            'leaf': None
        }

    def _parse_subgraphs(self, subgraph: pgv.AGraph):
        subgraphs = {}
        for sub in subgraph.subgraphs():
            subgraph_name = sub.name
            if subgraph_name == 'legend':
                self.direction = sub.graph_attr.get('rankdir', None)
                legend = dict(sub.get_node('Legend').attr)
                label_html = legend['label']
                self._parse_legend_colors(label_html)
            else:
                subgraphs[subgraph_name] = {
                    'attributes': dict(sub.graph_attr),
                    'nodes': {node.get_name(): dict(node.attr) for node in sub.nodes()},
                    'subgraphs': self._parse_subgraphs(sub)
                }

        return subgraphs

    def _parse_legend_colors(self, label_html):
        color_pattern = re.compile(
            r"<tr><td>([^<]+)</td><td [^>]*bgcolor='([^']+)'")
        matches = color_pattern.findall(label_html)
        for name, color in matches:
            if 'Regular function' in name:
                self.colors['regular'] = color
            elif 'Trunk function' in name:
                self.colors['trunk'] = color
            elif 'Leaf function' in name:
                self.colors['leaf'] = color

    def get_subgraphs(self):
        return self._parse_subgraphs(self.graph)

    def get_edges(self):
        edges = {}
        for i, edge in enumerate(self.graph.edges()):
            edges[i] = (edge, dict(edge.attr))
        return edges

    def get_nodes(self):
        nodes = {}
        for node in self.graph.nodes():
            if node == 'Legend':
                continue
            nodes[node.get_name()] = dict(node.attr)
        return nodes

    def subgraphs_to_mermaid(self) -> str:
        subgraphs = self.get_subgraphs()

        def subgraph_to_mermaid(subgraph_data, indent=4):
            result = []
            for subgraph, data in subgraph_data.items():
                label = data['attributes'].get('label', subgraph)
                result.append(" " * indent + f"subgraph {label}")
                result.extend(subgraph_to_mermaid(
                    data['subgraphs'], indent + 4))
                for node, attrs in data['nodes'].items():
                    node_class = ""
                    fillcolor = attrs.get("fillcolor", "")
                    if fillcolor == self.colors['regular']:
                        node_class = ":::filled"
                    elif fillcolor == self.colors['leaf']:
                        node_class = ":::leaf"
                    elif fillcolor == self.colors['trunk']:
                        node_class = ":::trunk"
                    result.append(" " * (indent + 4) +
                                  f'{node}["{attrs["label"]}"]{node_class}')
                result.append(" " * indent + "end")
            return result

        return "\n".join(subgraph_to_mermaid(subgraphs))

    def to_mermaid(self, colors=None) -> str:
        colors = colors if colors else self.colors
        subgraphs = self.subgraphs_to_mermaid()
        edges = self.get_edges()
        edges_content = "    %% Edges"
        edge_style = "\n    %% Edge styles"
        for i, edge in enumerate(edges.values()):
            edges_content += f"\n    {edge[0][0]} --> {edge[0][1]}"
            color = edge[1]['color']
            edge_style += f"\n    linkStyle {i} stroke:{color}"

        mermaid_content = f"graph {self.direction}\n"
        mermaid_content += "    %% Subgraphs \n" + \
            subgraphs + 2 * "\n" + edges_content + "\n" + edge_style + "\n"
        mermaid_content += "\n    %% Node styles \
        \n    classDef filled fill:{},stroke:#000000,stroke-width:2px; \
        \n    classDef leaf fill:{},stroke:#000000,stroke-width:2px; \
        \n    classDef trunk fill:{},stroke:#000000,stroke-width:2px; \
        ".format(colors['regular'], colors['leaf'], colors['trunk'])
        return mermaid_content

    def to_markdown(self, colors=None) -> str:
        markdown_content = "```mermaid\n"
        markdown_content += self.to_mermaid(colors=colors)
        markdown_content += "\n```"
        return markdown_content

    def add_to_markdown(self, input_file, new_graph):
        content = read(input_file)
        pattern = re.compile(r'```mermaid\n.*?\n```', re.DOTALL)
        new_content = f"```mermaid\n{new_graph}\n```"
        updated_content = re.sub(pattern, new_content, content)

        save(updated_content, input_file)
