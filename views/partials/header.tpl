<!--views/home.tpl-->
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>{{data['blogTitle']}}</title>
    <script src="/static/scripts/jQuery.js"></script>
    <script src="/static/scripts/main.js"></script>
    <link href="/static/styles/main.css" rel="stylesheet"></link>
    <link href="/static/images/site_logo.png" rel="icon" ></link>
    <link href="/static/fonts/setup.css" rel="stylesheet"></link>
  </head>
  <body>
    <div id="site">
      <header id="blog-header">
        <div class="region">
          <a href="/"><img src="/static/images/site_logo.png"/></a>
          <a id="blog-title" href="/">{{data['blogTitle']}}</a>
          <a>
            <form class="search" action="/search" method="post">
              <input type="text"  placeholder="Search.." name="query" required>
              <button type="submit">ស្វែង​រក</button>
            </form>
          </a>
          <a id="log-in" href="#">ចូលក្នុងប្រព័ន្ធ</a>
        </div><!--region-->
      </header>
      <div id="header-border"></div>
