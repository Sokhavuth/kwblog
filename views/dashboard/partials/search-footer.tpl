<!--views/dashboard/footer.tpl-->
<style>
  .footer{
    min-height: 150px;
    background: lavender;
    padding: 20px;
    box-sizing: border-box;
    margin: 0 auto;
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
              <a class="post-thumb" target="_blank" href="/post/{{data['posts'][v][0]}}"><img src="{{data['thumbs'][v]}}" /></a>
              <div class="title-wrapper">
                <a class="post-title" target="_blank" href="/post/{{data['posts'][v][0]}}">{{data['posts'][v][1]}}</a>
                %postdate = data['posts'][v][3].strftime("%d-%m-%Y")
                <div class="post-date">{{postdate}}</div>
                <a class="post-category">{{data['posts'][v][5]}}</a>
              </div>
              <div class="author-outer">
                <a class="post-author" href="/author/{{data['posts'][v][2]}}">{{data['posts'][v][2]}}</a>
                <a href="/post/delete/{{data['posts'][v][0]}}"><img title="Delete" class="delete" src="/static/images/delete.png" /></a>
                <a href="/post/edit/{{data['posts'][v][0]}}"><img title="Edit" src="/static/images/edit.png" /></a>
              </div>
            </div>
          %end
        %end
        </div>
        <script>
          var width = $('.post-thumb').css('width');
          var height = parseInt(width) / 16 * 9;
          $('.post-thumb').css('height', height);
        </script>
      </footer>
    </div><!--site-->
  </body>
</html>