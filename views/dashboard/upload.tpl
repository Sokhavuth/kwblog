<!--views/dashboard/upload.tpl-->
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>{{data['blogTitle']}}</title>
    <link href="/static/styles/upload.css" rel="stylesheet"></link>
    <link href="/static/images/site_logo.png" rel="icon" ></link>
    <link href="/static/fonts/setup.css" rel="stylesheet"></link>
  </head>
  <body>
    <form id='upload' action="/upload" method="POST" enctype="multipart/form-data">
      <a>ជ្រើសរើស​ឯកសារៈ</a><input type="file" name="fupload" />
      <a></a><input type='submit' value="ចំលងទុក​ក្នុង​គេហទំព័រ" />
    </form>
  </body>
</html>