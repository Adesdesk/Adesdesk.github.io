const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const path = require('path');

const app = express();
const PORT = 3000;

app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, '../public/')));

// define the answers array with mock data:
let answers = [
    { id: 1, task: 'Texas' },
    { id: 2, task: 'Manchester' }
  ];

// define routes needed on the front end
app.get('/api/answers', (req, res) => {
    try {
      res.status(200).json(answers);
    } catch (error) {
      console.error('Failed to get answers', error);
    }
  });
  
  app.post('/api/answers', (req, res) => {
    try {
      const newTodo = { id: answers.length + 1, task: req.body.task };
      answers.push(newTodo);
  
      res.status(201).json(newTodo);
    } catch (error) {
      console.error('Failed to submit answer', error);
    }
  });
  
  app.put('/api/answers/:id', (req, res) => {
    try {
      const id = parseInt(req.params.id);
      const answer = answers.find(t => t.id === id);
  
      if (!answer) {
        res.status(404).send('Todo not found');
  
        return;
      }
  
      answer.task = req.body.task;
  
      res.status(200).json(answer);
    } catch (error) {
      console.error('failed to edit answer', error);
    }
  });
  
  app.delete('/api/answers/:id', (req, res) => {
    try {
      const id = parseInt(req.params.id);
      answers = answers.filter(t => t.id !== id);
  
      res.status(204).send();
    } catch (error) {
      console.error('failed to delete answer', error);
    }
  });