<!--views/dashboard/signup.tpl-->
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

  #content #bottombar #post-author{
    min-width: 200px;
  }

  #content #bottombar .category{
    min-width: 80px;
    font: 14px/1.75 'Lucida Sans', OdorMeanChey !important;
  }

  #content #bottombar .category option{
    font: 14px/1.5 'Lucida Sans', OdorMeanChey !important;
  }

  #content .post-time{
    height: 24px !important;
    font:bold 14px/1.75 'Lucida Sans' !important;
    width: 100px;
  }

</style>

<div  id='main' class='main region'>

  %include('./dashboard/partials/sidebar.tpl')

  <section id='content' class='content'>
    
    <form action="/signup" method="post" autocomplete="new-password">
      %if 'edit' in data:
      <input id="post-title" name="fusername" value="{{data['post'][0][1]}}" type="text" placeholder="ឈ្មោះ​អ្នក​ប្រើប្រាស់" required />
      <textarea name="fprofile" id="editor">{{data['post'][0][5]}}</textarea>
      <div id="bottombar">
        <input id="submit" class="bottom-widget" type="submit" value="ចុះ​បញ្ជីរ">
        <input id="post-date" value="{{data['post'][0][2]}}" class="bottom-widget post-time" type="password" name="fpassword" />
        <select class="bottom-widget category" id="rights" name="frights">
          <option>author</option>
          <option>Admin</option>
        </select>
        <script>$("#rights").val("{{data['post'][0][3]}}").change();</script>
        <input type="email"  pattern="^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$"
         name="femail" value="{{data['post'][0][4]}}" id="post-author" class="bottom-widget post-time" required />
        <select class="bottom-widget category" id="gender" name="fgender">
          <option>ប្រុស</option>
          <option>ស្រី</option>
        </select>
        <script>$("#gender").val("{{data['post'][0][6]}}").change();</script>
      </div>
      %del data['edit']
      %else:
      <input id="post-title" value="" name="fusername"  type="text" placeholder="ឈ្មោះ​អ្នក​ប្រើប្រាស់" required />
      <textarea name="fprofile" id="editor"></textarea>
      <div id="bottombar">
        <input id="submit" class="bottom-widget" type="submit" value="ចុះ​បញ្ជីរ">
        <input id="post-date" class="bottom-widget post-time" type="password" name="fpassword" />
        <select class="bottom-widget category" id="rights" name="frights">
          <option>author</option>
          <option>Admin</option>
        </select>
        <input type='text' name="femail" pattern="^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$"
         placeholder="Email" id="post-author" class="bottom-widget post-time" required />
        <select class="bottom-widget category" id="gender" name="fgender">
          <option>ប្រុស</option>
          <option>ស្រី</option>
        </select>
      </div>
      %end
    </form>
    <div style="text-align: center;">{{data["message"]}}</div>
    %data['message'] = ""
    
    <script src="/static/scripts/ckeditor/config.js"></script>

  </section><!--content-->
</div><!--main-->

%include('./dashboard/partials/signup-footer.tpl')