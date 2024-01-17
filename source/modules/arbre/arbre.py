import graphviz

graph = graphviz.Digraph()

graph.node('A', 'fichier')  # doctest: +NO_EXE
graph.node('B', 'decl')

graph.edge('A','B', 'with Ada.Text_IO; use Ada.Text_IO \n procedure <pro> is is <decl> \n begin <instr>end <ident> $')

graph.render('L\'arbre syntaxique', view=True)