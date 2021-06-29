const express = require('express');
const bodyParser = require("body-parser");
var cors = require('cors');
var axios = require('axios');
var router = express.Router();
const {PythonShell} = require('python-shell');

router.use(bodyParser.json());
router.use(cors());

let events = [];

router.post("/", function (req, res) {
  if(req.body.name !== undefined) {
    var options = {
      mode: 'text',
      pythonOptions: ['-u'],
      scriptPath: './mecab',
      args: [req.body.name]
    };
    PythonShell.run('mecab.py', options, function (err,  results) {
      if(err) throw err;
      var result = results.toString()
      
      res.send(JSON.parse(result.toString()));
      console.log("result: " + JSON.parse(result.toString()));
      
    });
  }
  console.log('body: ' + req.body.name);
});

router.get("/", function (req, res) {
    res.send("Get request was called");
});


  

module.exports = router;