// save user input to a text file
async function saveToTextFile(input) {
  try {
    const response = await fetch('http://localhost:5003/save', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ input }),
    })

    if (response.ok) {
      console.log('Input saved to data.txt');
    } else {
      console.log('Failed to save input to data.txt');
    }

  } catch (error) {
    console.error('Error: ', error);
    alert('An error occurred');
  }
}

document.getElementById('analyzeButton').addEventListener('click', () => {
  const userInput = document.getElementById('userInput').value;

  if (!userInput.trim()) {
    alert('Please enter some input before proceeding!');
  }
  else {
    saveToTextFile(userInput);
  }
})


