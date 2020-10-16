<!--views/login.tpl-->
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>{{data['blogTitle']}}</title>
    <link href="/static/styles/login.css" rel="stylesheet"></link>
    <link href="/static/images/site_logo.png" rel="icon" ></link>
    <link href="/static/fonts/setup.css" rel="stylesheet"></link>
  </head>
  <body>
    <form id='login' action="/login" method="POST">
      <a>ឈ្មោះ​អ្នក​​ប្រើប្រាស់ៈ</a> <input type="text" name='fusername' value="admin" />
      <a>ពាក្យ​សំងាត់ៈ</a><input type="password" name="fpassword" value="password" />
      <a></a><input type='submit' />
    </form>
  </body>
</html>