import ast
with open('backend/routers/dashboard.py', 'r', encoding='utf-8') as f:
    code = f.read()
class FuncExtract(ast.NodeVisitor):
    def visit_FunctionDef(self, node):
        if node.name == 'get_kpis':
            print(ast.unparse(node))
FuncExtract().visit(ast.parse(code))
