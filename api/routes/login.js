var cors = require('cors');
var express = require('express');
var router = express.Router();

router.use(cors());

router.post('/', function(req, res) {
  res.send(req.body);
  console.log("req data is: " + req.body.Email);
  let info = req.body;
  router.get('/', function(req, res) {
    res.send(info);
  })
})

module.exports = router;
