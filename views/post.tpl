<!--views/post.tpl-->
%include('./partials/header.tpl')

<style>
  #content{
    min-height: 350px;
    background: lavender;
    padding: 10px;
    box-sizing: border-box;
  }
</style>

<div id='main' class='main region'>

  %include('./partials/sidebar.tpl')

  <section id='content' class='content'>
    post
  </section><!--content-->
</div><!--main-->

%include('./partials/footer.tpl')