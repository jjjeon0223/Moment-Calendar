var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
var cors = require('cors');

var app = express();

app.disable('etag');
// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');


app.use(express.json());
app.use(express.urlencoded({ extended: false }));


app.use(
  cors({
  origin: 'http://localhost:3000',
  credentials: true})
);
app.use(logger('dev'));


app.use(cookieParser());

app.use(express.static(path.join(__dirname, 'public')));


var indexRouter = require('./routes/index');
var serverRouter = require('./routes/server');
var loginRouter = require('./routes/login');
app.use('/', indexRouter);
app.use('/data', serverRouter);
app.use('/login', loginRouter);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  console.log(err)
  // console.log(req)
  // console.log(res)
  // console.log(next)
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;
