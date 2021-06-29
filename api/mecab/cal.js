// // var app = require('express')();
// // var http = require('http').Server(app);
// // var url = require('url');
// const {PythonShell} = require('python-shell');
// // var colors = require('colors');
// // var mecab = 'mecab.py';
// // const axios = require('axios').default;
// const bodyParser = require('body-parser');

// // app.use(bodyParser.json());
// // app.use(bodyParser.urlencoded({
// //   extended: true
// // }));

// // app.get('/', function(req, res){
// //   res.send('입력 예시: 주소/data/?k=(입력하고자하는 일정을 등록하세요)');  
// // });

app.get('/data', function(req, res){
    // res.set('Content-Type', 'text/plain');
    // var url_parts = url.parse(req.url, true);
    // var query = url_parts.query;

  if(query['k'] != undefined) {
    var options = {
      mode: 'text',
      pythonPath: 'python',
      args: [query['k']]
    };
    PythonShell.run('mecab.py', options, function (err, results) {
      if(err) throw err;
      res.json(results);
      console.log(results)
    });
  }
});

// // http.listen(8000, function(){
// //   console.log('konlpy server is ready!!'.rainbow);
// // });

