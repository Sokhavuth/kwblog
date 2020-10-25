<!--views/dashboard/footer.tpl-->
<style>
  .footer{
    min-height: 150px;
    background: lavender;
    padding: 20px;
    box-sizing: border-box;
    margin: 15px auto;
  }
  .post-panel{
    padding: 10px;
    background: rgb(247, 247, 248);
    font: 16px/1.5 Oswald, Limonf3;
    display: grid;
    grid-template-columns: 150px auto 15%;
    grid-gap: 10px;
    margin-bottom: 15px;
  }
  .post-panel:last-child{
    margin-bottom: 0;
  }
  .post-panel .post-thumb{
    overflow: hidden;
    display: block;
  }
  .post-panel .post-thumb img{
    width: 100%;
    min-height: 100%;
    float: left;
  }
  .post-panel .post-title{
    text-align: left;
    display: block;
  }
  .post-panel .post-author{
    text-align: right;
    font: bold 16px/1.5 'Lucida Sans';
    display: block;
  }
  .post-panel .author-outer img{
    width: 35px;
    float: right;
    visibility: hidden;
  }
  .post-panel:hover > .author-outer img {
    visibility: visible;
  }
  .post-panel .author-outer .delete{
    width: 28px;
    margin-top: 4.5px;
    margin-left: 10px;
  }
  .post-panel .post-date{
    font: bold 14px/1.5 'Lucida Sans';
  }
  #pagination{
    text-align: center;
  }
  #pagination img:hover{
    opacity: .5;
    cursor: pointer;
  }
</style>
      <footer class="footer region">
        <div class="panel">
        %if 'posts' in data:
          %for v in range(len(data['posts'])):
            <div class="post-panel">
              <a class="post-thumb" target="_blank" href="/category/{{data['posts'][v][0]}}"><img src="{{data['thumbs'][v]}}" /></a>
              <div class="title-wrapper">
                <a class="post-title" target="_blank" href="/category/{{data['posts'][v][0]}}">{{data['posts'][v][1]}}</a>
                %postdate = data['posts'][v][3].strftime("%d-%m-%Y")
                <div class="post-date">{{postdate}}</div>
              </div>
              <div class="author-outer">
                <a class="post-author" href="/author/{{data['posts'][v][2]}}">{{data['posts'][v][2]}}</a>
                <a href="/category/delete/{{data['posts'][v][0]}}"><img title="Delete" class="delete" src="/static/images/delete.png" /></a>
                <a href="/category/edit/{{data['posts'][v][0]}}"><img title="Edit" src="/static/images/edit.png" /></a>
              </div>
            </div>
          %end
        %end
        </div>
        <div id="pagination" style="margin-top: 20px;">
          <img onclick="paginate()" src="/static/images/load-more.png" />
        </div>
        <script>
          function paginate(){
            $('#pagination img').attr('src', '/static/images/loading.gif');
            $.get("/category/paginate/backend", function(data, status){
              if((status=='success') && data.json){
                var posts = data.json;
                var thumbs = data.thumbs;
                var html = '';

                for(var index in posts){
                  html += '<div class="post-panel">';
                  html += `<a class="post-thumb" target="_blank" href="/category/${posts[index][0]}"><img src="${thumbs[index]}" /></a>`;
                  html += '<div class="title-wrapper">'
                  html += `<a class="post-title" target="_blank" href="/category/${posts[index][0]}">${posts[index][1]}</a>`;
                  html += `<div class="post-date">${posts[index][3]}</div>`;
                  html += '</div>';
                  html += `<div class="author-outer">`;
                  html += `<a class="post-author" href="/author/${posts[index][2]}">${posts[index][2]}</a>`;  
                  html += `<a href="/category/delete/${posts[index][0]}"><img title="Delete" class="delete" src="/static/images/delete.png" /></a>`;
                  html += `<a href="/category/edit/${posts[index][0]}"><img title="Edit" src="/static/images/edit.png" /></a>`;
                  html += '</div>';
                  html += '</div>';
                }

                $('footer .panel').append(html);

                var width = $('footer .post-thumb img').css('width');
                var height = parseInt(width) / 16 * 9;
                $('footer .post-thumb').css({'height':height});
              }

              $('#pagination img').attr('src', '/static/images/load-more.png');

            });
          }
        </script>
        <script>
          var width = $('.post-thumb').css('width');
          var height = parseInt(width) / 16 * 9;
          $('.post-thumb').css('height', height);
        </script>
      </footer>
    </div><!--site-->
  </body>
</html>