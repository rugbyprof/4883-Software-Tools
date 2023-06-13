## Graphviz - Simple Intro
#### Due: ∞


### Docs
- [Graphviz Website](https://graphviz.org/)

### Online Editors
- [Graphviz Online](https://dreampuf.github.io/GraphvizOnline/)
- [Edotor.net/](https://edotor.net/)
- [Magjac.com](http://magjac.com/graphviz-visual-editor/)
- [Devtoolsdaily.com](https://www.devtoolsdaily.com/graphviz/)

### Python Lib

https://github.com/xflr6/graphviz

### Attributes

[Color names](https://graphviz.org/doc/info/colors.html)

[Node Shapes](https://graphviz.org/doc/info/shapes.html)

[Edge Attributes](https://graphviz.org/docs/edges/)

[Arrow Shapes](https://graphviz.org/doc/info/arrows.html)

### Overview

Graphviz is an open-source software tool that is widely used for visualizing and analyzing graphs and networks. It provides a set of tools and libraries for creating and rendering graph representations in various formats.

`Graphviz` uses a declarative language called the **`DOT`** language to define the structure and layout of graphs. The **`DOT`** language allows you to specify nodes, edges, and their attributes, such as labels, colors, shapes, and styles. With this language, you can describe complex relationships and connections between different entities.

Once you have defined a graph using the **`DOT`** language, you can use the `Graphviz` software to generate visual representations of the graph. `Graphviz` offers different layout algorithms that determine how the nodes and edges are positioned in the final visualization. Some popular layout algorithms include **`DOT`**, `neato`, `circo`, and `twopi`, each suited for different types of graphs.

`Graphviz` supports various output formats for the generated visualizations, such as PNG, SVG, PDF, and PostScript. This flexibility allows you to integrate the visualizations into various documents, presentations, or web pages.

Besides its visual capabilities, `Graphviz` also provides a set of command-line tools and APIs for programmatically working with graphs. These tools enable you to manipulate and analyze graphs, compute various graph metrics, and even create dynamic graphs based on external data sources.

Overall, `Graphviz` is a powerful and versatile tool for creating, analyzing, and visualizing graphs, making it widely used in fields such as data analysis, network analysis, software engineering, and information visualization.



#### Basic
```java
digraph {
    A->B
    B->C
    C->D
    D->E
}
```

```java
digraph {
    rankdir=LR;
    A->B
    B->C
    C->D
    D->E
}
```

```java
digraph {
    rankdir=LR;
    node [shape=record]

    A->B
    B->C
    C->D
    D->E
}
```


```java
digraph linkedlist {
    rankdir=LR;
    node [shape=record]
    
    // Define the nodes
    A [label="<data> A"];
    B [label="<data> B"];
    C [label="<data> C"];
    D [label="<data> D"];
    E [label="<data> E"];
    
    // Define the edges
    A -> B;
    B -> C;
    C -> D;
    D -> E;
}
```


```java
digraph linkedlist {
    rankdir=LR;
    node [shape=record]
    
    // Define the nodes
    A [label="{<data> 1|<next>}"];
    B [label="<data> 2|<next>"];
    C [label="<data> 3|<next>"];
    D [label="<data> 4|<next>"];
    E [label="<data> 5|<next>"];
    
    // Define the edges
    A:next -> B:data;
    B:next -> C:data;
    C:next -> D:data;
    D:next -> E:data;
}
```

```java
digraph linkedlist {
        rankdir=LR;
        node [shape=record,color=purple];
        A [label="{ <data> 1 | <next>  }"]
        B [label="{ <data> 2 | <next>  }"];
        C [label="{ <data> 3 | <next>  }"];
        D [label="<data> 4|<next>"];
        E [label="<data> 5|<next>"];
        null [shape=circle,color=white];

        A:next:c -> B:data [arrowhead=vee, arrowtail=dot, color=orange, dir=both, tailclip=false];
        B:next -> C:data [arrowhead=vee, arrowtail=dot, color=orange, dir=both, tailclip=false];
        C:next -> null  [arrowhead=vee, arrowtail=dot, color=orange, dir=both, tailclip=false];
}
```