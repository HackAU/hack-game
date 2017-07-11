'use strict';
 
var gulp = require('gulp');
var sass = require('gulp-sass');
 
gulp.task('sass', function () {
  return gulp.src('./gameapp/static/sass/main.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('./gameapp/static/css'));
});
 
gulp.task('sass:watch', function () {
  gulp.watch('./gameapp/static/sass/main.scss', ['sass']);
});