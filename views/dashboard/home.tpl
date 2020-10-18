<!--views/dashboard/home.tpl-->
%include('./dashboard/partials/header.tpl')

<style>
  #content{
    min-height: 350px;
    background: white;
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
  }

  #content #post-date, #content #post-time{
    height: 24px !important;
    font:bold 14px/1.5 'Lucida Sans' !important;
    width: 100px;
  }

  #content #video{
    min-width: 70px;
  }
</style>

<div  id='main' class='main region'>

  %include('./dashboard/partials/sidebar.tpl')

  <section id='content' class='content'>
    
    <form action="/posting" method="post">
      <input id="post-title" name="post-title" type="text" placeholder="ចំណង​ជើង" />
      <textarea name="content" id="editor"></textarea>
      <div id="bottombar">
        <input class="bottom-widget" type="submit" value="ចុះ​ផ្សាយ">
        <select class="bottom-widget" id="category" name="category">
          <option>News</option>
          <option>Python</option>
          <option>Node.js</option>
          <option>PHP</option>
        </select>
        <input id="post-date" value="{{data['datetime'][0]}}" class="bottom-widget" type="text" name="post-date" />
        <input id="post-time" value="{{data['datetime'][1]}}" class="bottom-widget" type="text" name="post-time" />
        <input id="video" class="bottom-widget" type="button" value="VIDEO" />
      </div>
    </form>
    <script src="/static/scripts/ckeditor/config.js"></script>

  </section><!--content-->
</div><!--main-->

%include('./dashboard/partials/footer.tpl')