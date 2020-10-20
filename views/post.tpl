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
  #content .post-title{
    font: 20px/1.5 Limonf3, Oswald;
  }
  #content .post-author{
    font: bold 14px/1.5 "Lucida Sans";
    margin: 10px 0;
  }
  #content .post-date{
    float: right;
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
</style>

<div id='main' class='main region'>

  %include('./partials/sidebar.tpl')

  <section id='content' class='content'>
    <article class="post">
      %if data['post']:
      <div class='post-header'>
        <span class="post-title">{{data['post'][0][1]}}</span>
        <span class="post-date">{{data['post'][0][3].strftime("%d-%m-%Y")}}</span>
      </div>
      <div class="post-author">{{data['post'][0][2]}}</div>

      <div class="post-body">{{!data['post'][0][6]}}</div>
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

%include('./partials/footer.tpl')