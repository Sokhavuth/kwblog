<!--views/partials/footer.tpl-->
<style>
.footer{
  min-height: 150px;
  background:  lavender;
  padding: 0px;
  box-sizing: border-box;
  margin: 15px auto;
}
.post-panel{
  padding: 15px;
  font: 16px/1.5 Oswald, Limonf3;
  display: grid;
  grid-template-columns: calc(12.5% - 13.125px) calc(12.5% - 13.125px) calc(12.5% - 13.125px) calc(12.5% - 13.125px) 
  calc(12.5% - 13.125px) calc(12.5% - 13.125px) calc(12.5% - 13.125px) calc(12.5% - 13.125px) ;
  grid-gap: 15px;
  margin-bottom: 15px;
}
.post-panel:last-child{
  margin-bottom: 0;
}
.post-panel .post-thumb{
  display: block;
  overflow: hidden;
}
.post-panel .post-thumb img{
  width: 100%;
  min-height: 100%;
  float: left;
  margin-bottom: 5px;
}
.post-panel .post-title{
  text-align: left;
  display: block;
  text-align: center;
}
.post-panel .post-author{
  text-align: right;
}
.post-panel .post-date{
  font: bold 14px/1.5 'Lucida Sans';
}
@media only screen and (max-width: 600px){
  .post-panel{
    grid-template-columns: 100%;
  }
}
#pagination{
  text-align: center;
  padding: 0 0 5px;
}
#pagination img:hover{
  opacity: .5;
  cursor: pointer;
}
</style>
      <footer class="footer region">
        <div class="post-panel">
        %if 'posts' in data:
          %for v in range(len(data['posts'])):
            <div class="post-outer">
              <a class="post-thumb" href="/user/{{data['posts'][v][0]}}"><img src="{{data['thumbs'][v]}}" /></a>
              <a class="post-title" href="/user/{{data['posts'][v][0]}}">{{data['posts'][v][1]}}</a>
              <div class="post-date"></div>
            </div>
          %end
        %end
        </div>
        <div id="pagination">
          <img onclick="paginate()" src="/static/images/load-more.png" />
        </div>
        <script>
          function paginate(){
            $('#pagination img').attr('src', '/static/images/loading.gif');
            $.get("/user/paginate/frontEnd", function(data, status){
              if((status=='success') && data.json){
                var posts = data.json;
                var thumbs = data.thumbs;
                var html = '';

                for(var index in posts){
                  html += '<div class="post-outer">';
                  html += `<a class="post-thumb" href="/user/${posts[index][0]}"><img src="${thumbs[index]}" /></a>`;
                  html += `<a class="post-title" href="/user/${posts[index][0]}">${posts[index][1]}</a>`;
                  html += `<div class="post-date"></div>`;
                  html += '</div>';
                }

                $('.post-panel').append(html);

                var width = $('footer .post-thumb img').css('width');
                var height = parseInt(width);
                $('footer .post-thumb').css({'height':height});
              }

              $('#pagination img').attr('src', '/static/images/load-more.png');

            });
          }

          var width = $('footer .post-thumb img').css('width');
          var height = parseInt(width);
          $('footer .post-thumb').css({'height':height});

          $(window).resize(function(){
            var width = $('footer .post-thumb img').css('width');
            var height = parseInt(width);
            $('footer .post-thumb').css({'height':height});
          });
        </script>
      </footer>
    </div><!--site-->
  </body>
</html>