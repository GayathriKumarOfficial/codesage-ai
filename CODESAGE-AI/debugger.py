import subprocess
import tempfile

def debug_code(code):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".py", mode="w") as tmp:
            tmp.write(code)
            tmp.flush()

            result = subprocess.run(['pyflakes', tmp.name], capture_output=True, text=True)
            if result.stdout:
                return result.stdout
            else:
                return "✅ No issues found."
    except Exception as e:
        return f"Error during debug: {e}"
