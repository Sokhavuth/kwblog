<!--views/home.tpl-->
%include('./partials/header.tpl')

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

  #content #post-title{
    width: 100%;
    box-sizing: border-box;
    padding: 5px 10px;
    font: 16px/1.5 Koulen;
  }

  #content ::placeholder{
    opacity: .4;
  }

  #content #bottombar{
    background: #ebebeb;
    padding: 5px;
    border: 1px solid #bebbbb;
  }

  #content #bottombar .bottom-widget{
    font: 14px/1.5 OdorMeanChey;
    height: 30px;
  }

  #content #bottombar input:hover{
    cursor: pointer;
  }

  #content #bottombar #category{
    min-width: 80px;
    font:bold 14px/1.5 'Lucida Sans', OdorMeanChey !important;
  }

  #content #bottombar #category option{
    font:bold 14px/1.5 'Lucida Sans', OdorMeanChey !important;
  }

  #content .post-time{
    height: 24px !important;
    font:bold 14px/1.5 'Lucida Sans' !important;
    width: 100px;
  }

</style>

<div  id='main' class='main region'>

  %include('./partials/sidebar.tpl')

  <section id='content' class='content'>

    %include('./partials/search-footer.tpl')

  </section><!--content-->
</div><!--main-->

