from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import traceback
from  Libary.fn import plot

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

@app.route('/execute-script', methods=['POST'])
def execute_script():
    try:
        # Get the script and input data from the user
        data = request.json
        user_script = data.get("script", "")
        inputs = data.get("inputs", {})

        # Write the script to a temporary file
        with open("user_script.py", "w") as script_file:
            script_file.write(user_script)

        # Execute the script securely
        result = subprocess.run(
            ['python', 'user_script.py'],
            capture_output=True,
            text=True
        )

        # Return the output
        if result.returncode == 0:
            return jsonify({"success": True, "output": result.stdout})
        else:
            return jsonify({"success": False, "error": result.stderr})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
