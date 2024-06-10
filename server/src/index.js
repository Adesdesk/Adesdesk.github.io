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
