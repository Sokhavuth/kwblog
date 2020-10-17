%include('./dashboard/partials/header.tpl')

<style>
  #content{
    min-height: 350px;
    background: lavender;
    padding: 10px;
    box-sizing: border-box;
  }
</style>

<div id='main' class='main region'>

  %include('./dashboard/partials/sidebar.tpl')

  <section id='content' class='content'>
    content
  </section><!--content-->
</div><!--main-->

%include('./dashboard/partials/footer.tpl')