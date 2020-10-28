<!--views/post.tpl-->
%include('./partials/header.tpl')
<style>
  #content{
    min-height: 350px;
    background: lavender;
    box-sizing: border-box;
  }
  #content article{
    background: rgb(247, 247, 248);
    min-height: 350px;
    padding: 20px;
  }
  #content .post-header{
    display: grid;
    grid-template-columns: auto auto;
  }
  #content .post-title{
    font: 20px/1.5 Oswald, Limonf3;
  }
  #content .post-author{
    font: bold 14px/1.5 "Lucida Sans";
    margin: 10px 0;
  }
  #content .post-date{
    float: right;
    text-align: right;
    width: 100% !important;
    font: bold 18px/1.5 'Lucida Sans';
  }
  #content .post-body{
    line-height: 1.75;
  }
  #content .post-body .image{
    padding: 0;
    margin: 0;
  }
  #content .post-body img{
    width: 100%;
  }
  #content .post-author{
    display: grid;
    grid-template-columns: auto auto;
    margin-bottom: 20px;
    align-items: center;
  }
  #content .post-author .icon-outer{
    text-align: right;
  }
  #content .edit-icon img,
  #content .delete-icon img{
    width: 35px;
  }
  #content .delete-icon img{
    width: 28px;
    margin-left: 5px;
    position: relative;
    top: -3.5px
  }
</style>

<div id='main' class='main region'>

  %include('./partials/sidebar.tpl')

  <section id='content' class='content'>
    <article class="post">
      %if 'post' in data:
      <div class='post-header'>
        <div class="post-title">{{data['post'][0][1]}}</div>
        <div class="post-date">{{data['post'][0][3].strftime("%d-%m-%Y")}}</div>
      </div>
      <div class="post-author">
        <a href="/author/{{data['post'][0][2]}}">{{data['post'][0][2]}}</a>
        %if 'showEdit' in data:
        <div class="icon-outer">
          <a class="edit-icon" href="/category/edit/{{data['post'][0][0]}}"><img src="/static/images/edit.png"/></a>
          <a class="delete-icon" href="/category/delete/{{data['post'][0][0]}}"><img src="/static/images/delete.png"/></a>
        </div>
        %del data['showEdit']
        %end
      </div>

      <div class="post-body">{{!data['post'][0][-1]}}</div>
      %end

      <div id="disqus_thread"></div>
      <script>
      (function() { // DON'T EDIT BELOW THIS LINE
        var d = document, s = d.createElement('script');
        s.src = 'https://khmerweb.disqus.com/embed.js';
        s.setAttribute('data-timestamp', +new Date());
        (d.head || d.body).appendChild(s);
      })();
      </script>
      <noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
                            
    </article>
  </section><!--content-->
</div><!--main-->

%include('./partials/category-footer.tpl')