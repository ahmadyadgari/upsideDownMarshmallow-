// Ensure the button click triggers the analyze function
document.getElementById("analyzeButton").addEventListener("click", async () => {
  const userInput = document.getElementById("userInput").value;

  if (userInput.trim() === "") {
    alert("Please enter some text before analyzing.");
    return;
  }

  // Save the user input first
  await saveToTextFile(userInput);

  // Now analyze the input
  await analyzeInput();
});

// Save input to data.txt
async function saveToTextFile(input) {
  try {
    const response = await fetch("http://localhost:5003/save", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ input }),
    });

    if (!response.ok) {
      throw new Error("Failed to save input to data.txt");
    }
    console.log("Input saved to data.txt");
  } catch (error) {
    console.error("Error: ", error);
    alert("An error occurred while saving input");
  }
}

// Analyze input by sending a POST request to /analyze
async function analyzeInput() {
  try {
    const response = await fetch("http://localhost:5003/analyze", {
      method: "POST",
    });

    if (response.ok) {
      const { output } = await response.json();
      document.getElementById("aiOutput").value = output;
    } else {
      const { error } = await response.json();
      alert(`Analysis failed: ${error}`);
    }
  } catch (error) {
    console.error("Error: ", error);
    alert("An error occurred while analyzing input");
  }
}
