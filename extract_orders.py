import ast
with open('backend/routers/dashboard.py', 'r', encoding='utf-8') as f:
    code = f.read()
class FuncExtract(ast.NodeVisitor):
    def visit_FunctionDef(self, node):
        if node.name in ['recent_orders', 'today_orders']:
            print(f"--- {node.name} ---")
            print(ast.unparse(node))
FuncExtract().visit(ast.parse(code))
