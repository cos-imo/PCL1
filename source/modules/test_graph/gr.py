import graphviz

g = graphviz.Digraph('G', filename='hello.gv')

g.edge('fichier', 'decl', 'with Ada.Text_IO; use Ada.Text_IO \n procedure <pro> is is <decl> \n begin <instr>end <ident> $')

g.view()
