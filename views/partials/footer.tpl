<!--views/dashboard/footer.tpl-->
<style>
  
</style>
      <footer class="footer region">
        <div class="post-panel">
        %if 'posts' in data:
          %for v in range(len(data['posts'])):
            <div class="post-outer">
              <a class="post-thumb" href="/post/{{data['posts'][v][0]}}"><img src="{{data['thumbs'][v]}}" /></a>
                <a class="post-title" href="/post/{{data['posts'][v][0]}}">{{data['posts'][v][1]}}</a>
                %postdate = data['posts'][v][3].strftime("%d-%m-%Y")
                <div class="post-date">{{postdate}}</div>
            </div>
          %end
        %end
        </div>
        <div id="pagination">
          <img onclick="paginate()" src="/static/images/load-more.png" />
        </div>
        <script>
          function paginate(){
            $.get("/paginate", function(data, status){
              if(status && data.json){
                var posts = data.json;
                var thumbs = data.thumbs;
                var html = '';

                $('#pagination img').attr('src', '/static/images/loading.gif');

                for(var index in posts){
                  html += '<div class="post-outer">';
                  html += `<a class="post-thumb" href="/post/${posts[index][0]}"><img src="${thumbs[index]}" /></a>`;
                  html += `<a class="post-title" href="/post/${posts[index][0]}">${posts[index][1]}</a>`;
                  html += `<div class="post-date">${posts[index][3]}</div>`;
                  html += '</div>';
                }

                $('.post-panel').append(html);
                $('#pagination img').attr('src', '/static/images/load-more.png');

                var width = $('footer .post-thumb img').css('width');
                var height = parseInt(width) / 16 * 9;
                $('footer .post-thumb').css({'height':height});
              }
            });
          }

          var width = $('footer .post-thumb img').css('width');
          var height = parseInt(width) / 16 * 9;
          $('footer .post-thumb').css({'height':height});

          $(window).resize(function(){
            var width = $('footer .post-thumb img').css('width');
            var height = parseInt(width) / 16 * 9;
            $('footer .post-thumb').css({'height':height});
          });
        </script>
      </footer>
    </div><!--site-->
  </body>
</html>