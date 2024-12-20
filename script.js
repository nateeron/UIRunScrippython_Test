console.log('Running Script');


document.getElementById('execute-btn').addEventListener('click', async () => {
      const script = document.getElementById('script-editor').value;
    
      if (!script.trim()) {
        alert("Please write a script before running.");
        return;
      }
    
      try {
        // Send the script to the backend
        const response = await fetch('http://127.0.0.1:5000/execute-script', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ script: script }),
        });
    
        const result = await response.json();
    
        // Display output or error
        const outputElement = document.getElementById('output');
        if (result.success) {
          outputElement.textContent = result.output;
        } else {
          outputElement.textContent = `Error: ${result.error}`;
        }
      } catch (error) {
        console.error("Error executing script:", error);
      }
    });
    