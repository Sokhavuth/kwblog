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

  %include('./dashboard/partials/sidebar.tpl')

  <section id='content' class='content'>
    
    <form action="/posting" method="post">
      %if 'edit' in data:
      <input id="post-title" name="fpost-title" value="{{data['post'][0][1]}}" type="text" placeholder="ចំណង​ជើង​អត្ថបទ" required />
      <textarea name="fcontent" id="editor">{{data['post'][0][6]}}</textarea>
      <div id="bottombar">
        <input id="submit" class="bottom-widget" type="submit" value="ចុះ​ផ្សាយ">
        <select class="bottom-widget" id="category" name="fcategory">
          %if data['categories']:
            %for category in data['categories']:
              <option>{{category[1]}}</option>
            %end
          %end
        </select>
        <script>$("#category").val("{{data['post'][0][5]}}").change();</script>
        <input id="post-date" value="{{data['post'][0][3].strftime('%d-%m-%Y')}}" class="bottom-widget post-time" type="text" name="fpost-date" />
        <input id="post-time" value="{{data['post'][0][4].strftime('%H:%M:%S')}}" class="bottom-widget post-time" type="text" name="fpost-time" />
        <input disabled style="background:white;text-align:center;" type='text' value="{{data['post'][0][2]}}" id="post-author" class="bottom-widget post-time" />
      </div>
      %del data['edit']
      %else:
      <input id="post-title" name="fpost-title" type="text" placeholder="ចំណង​ជើងអត្ថបទ" required />
      <textarea name="fcontent" id="editor"></textarea>
      <div id="bottombar">
        <input id="submit" class="bottom-widget" type="submit" value="ចុះ​ផ្សាយ">
        <select class="bottom-widget" id="category" name="fcategory">
          %if data['categories']:
            %for category in data['categories']:
              <option>{{category[1]}}</option>
            %end
          %end
        </select>
        <input id="post-date" value="{{data['datetime'][0]}}" class="bottom-widget post-time" type="text" name="fpost-date" />
        <input id="post-time" value="{{data['datetime'][1]}}" class="bottom-widget post-time" type="text" name="fpost-time" />
        <input disabled style="background:white;text-align:center;" type='text' value="{{data['author']}}" id="post-author" class="bottom-widget post-time" />
      </div>
      %end
    </form>
    <div style="text-align: center;">{{data["message"]}}</div>
    %data['message'] = ""
    
    <script src="/static/scripts/ckeditor/config.js"></script>

  </section><!--content-->
</div><!--main-->

%include('./dashboard/partials/footer.tpl')