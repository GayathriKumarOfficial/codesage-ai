import ast

def explain_code(code):
    try:
        tree = ast.parse(code)
        explanation = []

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                explanation.append(f"Defines function `{node.name}` with {len(node.args.args)} parameter(s).")
            elif isinstance(node, ast.For):
                explanation.append("Contains a for loop.")
            elif isinstance(node, ast.If):
                explanation.append("Contains an if statement.")
            elif isinstance(node, ast.While):
                explanation.append("Contains a while loop.")
            elif isinstance(node, ast.Assign):
                explanation.append("Has a variable assignment.")
            elif isinstance(node, ast.Call):
                explanation.append("Makes a function call.")
        
        return "\n".join(explanation) or "No significant structure found to explain."
    except Exception as e:
        return f"Error while parsing: {e}"
