<!--views/dashboard/upload.tpl-->
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>{{data['blogTitle']}}</title>
    <script src="/static/scripts/jQuery.js"></script>
    <link href="/static/styles/upload.css" rel="stylesheet"></link>
    <link href="/static/images/site_logo.png" rel="icon" ></link>
    <link href="/static/fonts/setup.css" rel="stylesheet"></link>
  </head>
  <body>
    <div id="upload">
      <input id="copy" type="button" value="ចំលងតំណរភ្ជាប់" /><input class="url" type="text" value="{{data['uploadUrl']}}" />
      <script>
        $('#copy').click(function(){
          $(this).siblings('input.url').select();      
          document.execCommand("copy");
          window.close();
        });
      </script>
    </div>
  </body>
</html>