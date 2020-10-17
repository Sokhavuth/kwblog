<!--views/dashboard/home.tpl-->
%include('./dashboard/partials/header.tpl')

<style>
  #content{
    min-height: 350px;
    background: lavender;
    padding: 0;
    box-sizing: border-box;
  }

  #content .ck-editor__editable {
    min-height: 350px !important;
}
</style>

<div  id='main' class='main region'>

  %include('./dashboard/partials/sidebar.tpl')

  <section id='content' class='content'>
    <div id="editor"></div>
    <script>
      ClassicEditor
        .create( document.querySelector( '#editor' ))
        .catch( error => {
          console.error( error );
        });
    </script>
  </section><!--content-->
</div><!--main-->

%include('./dashboard/partials/footer.tpl')