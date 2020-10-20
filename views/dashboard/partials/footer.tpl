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
    font: 16px/1.5 Limonf3, Oswald;
    display: grid;
    grid-template-columns: 150px auto 15%;
    grid-gap: 10px;
    margin-bottom: 15px;
  }
  .post-panel:last-child{
    margin-bottom: 0;
  }
  .post-panel .post-thumb img{
    max-width: 100%;
    float: left;
  }
  .post-panel .post-title{
    text-align: left;
    display: block;
  }
  .post-panel .post-author{
    text-align: right;
  }
  .post-panel .post-date{
    font: bold 14px/1.5 'Lucida Sans';
  }
</style>
      <footer class="footer region">
        %if data['posts']:
          %for post in data['posts']:
            <div class="post-panel">
              <a class="post-thumb" href="/post/{{post[0]}}"><img src="/static/images/nopicture.jpg" /></a>
              <div class="title-wrapper">
                <a class="post-title" href="/post/{{post[0]}}">{{post[1]}}</a>
                %postdate = post[3].strftime("%d-%m-%Y")
                <div class="post-date">{{postdate}}</div>
                <a class="post-category">{{post[5]}}</a>
              </div>
              <a class="post-author" href="/author/{{post[2]}}">{{post[2]}}</a>
            </div>
          %end
        %end
        
        
      </footer>
    </div><!--site-->
  </body>
</html>