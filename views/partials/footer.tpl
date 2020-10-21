<!--views/dashboard/footer.tpl-->
<style>
  .footer{
    min-height: 150px;
    background:  rgb(247, 247, 248);
    padding: 0px;
    box-sizing: border-box;
    margin: 15px auto;
  }
  .post-panel{
    padding: 15px;
    background: rgb(247, 247, 248);
    font: 16px/1.5 Limonf3, Oswald;
    display: grid;
    grid-template-columns: calc(25% - 11.25px) calc(25% - 11.25px) calc(25% - 11.25px) calc(25% - 11.25px);
    grid-gap: 15px;
    margin-bottom: 15px;
  }
  .post-panel:last-child{
    margin-bottom: 0;
  }
  .post-panel .post-thumb img{
    width: 100%;
    float: left;
    margin-bottom: 10px;
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
  @media only screen and (max-width: 600px){
    .post-panel{
      grid-template-columns: 100%;
    }
  }
</style>
      <footer class="footer region">
        <div class="post-panel">
        %if data['posts']:
          %for v in range(len(data['posts'])):
            <div class="post-outer">
              <a class="post-thumb" href="/post/{{data['posts'][v][0]}}"><img src="{{data['thumbs'][v]}}" /></a>
              <div class="title-wrapper">
                <a class="post-title" href="/post/{{data['posts'][v][0]}}">{{data['posts'][v][1]}}</a>
                %postdate = data['posts'][v][3].strftime("%d-%m-%Y")
                <div class="post-date">{{postdate}}</div>
              </div>
            </div>
          %end
        %end
        </div>
      </footer>
    </div><!--site-->
  </body>
</html>