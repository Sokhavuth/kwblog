%include('./partials/header.tpl')

<style>
  #content{
    min-height: 350px;
    background: lavender;
    padding: 0px;
    box-sizing: border-box;
  }
</style>

<div id='main' class='main region'>

  %include('./partials/sidebar.tpl')

  <section id='content' class='content'>
    <div  style="position:relative;padding-top:56.25%;">
      <iframe src="https://www.youtube.com/embed/JJmcL1N2KQs" frameborder="0" allowfullscreen 
        style="position:absolute;top:0;left:0;width:100%;height:100%;">
      </iframe>
    </div>
  </section><!--content-->
</div><!--main-->

%include('./partials/footer.tpl')