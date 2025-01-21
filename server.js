import express from 'express'
import fs from 'fs'
import bodyParser from 'body-parser'
import cors from 'cors'

const app = express()
const PORT = 5003;

// Enable CORS for all origins
app.use(cors());

// Middleware to parse JSON
app.use(bodyParser.json());

app.post('/save', (req, res) => {
  const userInput = req.body.input;
  fs.appendFile('data.txt', userInput + '\n', (err) => {
    if (err) {
      console.error('Error writing to file:', err);
      return res.status(500).json({ message: 'Failed to save input.' });
    }
    res.status(200).json({ message: 'Input saved successfully!' });
  })
})

app.listen(PORT, () => {
  console.log(`Server is running on locahost: ${PORT}`)
})