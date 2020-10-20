<!--views/daishboard/home.tpl-->
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>{{data['blogTitle']}}</title>
    <script src="/static/scripts/jQuery.js"></script>
    <script src="/static/scripts/main.js"></script>
    <script src="/static/scripts/ckeditor/ckeditor.js"></script>
    <link href="/static/styles/main.css" rel="stylesheet"></link>
    <link href="/static/images/site_logo.png" rel="icon" ></link>
    <link href="/static/fonts/setup.css" rel="stylesheet"></link>
  </head>
  <body>
    <div id="site">
      <header id="blog-header">
        <div class="region">
          <a><img src="/static/images/site_logo.png"/></a>
          <a id="blog-title">{{data['blogTitle']}}</a>
          <style>
            #top-menu li{
              list-style-type: none;
              display: inline-block;
              font: 16px/1.5 Bayon;
              margin: 0 10px;
            }
          </style>
          <ul id="top-menu">
            <li><a href="#">ការផ្សាយ</a></li>
            <li><a href="#">​ជំពូក</a></li>
            <li><a href="#">ទំព័រ</a></li>
            <li><a href="#">​ឯកសារ</a></li>
            <li><a href="#">​សមាជិក</a></li>
          </ul>
          <a id="log-in" href="/">ចេញ​ក្រៅ</a>
        </div><!--region-->
      </header>
      <div id="header-border"></div>
