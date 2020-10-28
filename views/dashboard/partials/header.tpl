<!--views/dashboard/header.tpl-->
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
          <a href="/login"><img src="/static/images/site_logo.png"/></a>
          <span id="blog-title"><a href="/login">{{data['blogTitle']}}</a></span>
          <a>
            <form class="search" action="/search/backend" method="post">
              <input type="text"  placeholder="Search.." name="fquery" required>
              <button type="submit">ស្វែង​រក</button>
            </form>
          </a>
          <span id="log-in"><a href="/">ចេញ​ក្រៅ</a></span>
        </div><!--region-->
      </header>
      <div id="header-border"></div>
