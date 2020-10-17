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
</style>

<div  id='main' class='main region'>

  %include('./dashboard/partials/sidebar.tpl')

  <section id='content' class='content'>
    
    <form action="/posting" method="post">
      <input id="post-title" name="post-title" type="text" placeholder="ចំណង​ជើង" />
      <textarea name="content" id="editor"></textarea>
      <div id="bottombar">
        <input type="submit" value="Submit">
      </div>
    </form>
    <script>
      ClassicEditor
        .create( document.querySelector( '#editor' ), {
          toolbar: ['fontfamily', 'fontsize', 'fontcolor', 'bold', 'italic', 
          'bulletedList', 'indent', 'outdent', 'numberedList', 'link', 'blockQuote', 
          'code', 'codeblock', 'imageinsert', 'mediaembed', 'undo', 'redo' ],
          fontFamily: {
            options: [
              'ឧត្តមាន​ជ័យ, OdorMeanChey', 'អក្សរដៃ, HandWriting',
              'គូលេន, Koulen', 'ក្រូច​ឆ្នារ, Limonf3',
              'បាយ័ន, Bayon', 'ក្រសាំង, Rooster',
              'មូល, Moul',
    				  'Arial, Helvetica, sans-serif',
 				      'Courier New, Courier, monospace',
 				      'Georgia, serif',
 				      'Lucida Sans Unicode, Lucida Grande, sans-serif',
 				      'Tahoma, Geneva, sans-serif',
 				      'Times New Roman, Times, serif',
 				      'Trebuchet MS, Helvetica, sans-serif',
				      'Verdana, Geneva, sans-serif',
            ],
            supportAllValues: true
          },
          
          fontSize: {
            options: [
                9,
                11,
                13,
                'default',
                17,
                19,
                21
            ],
            supportAllValues: true
          },
        })
        .catch( error => {
          console.error( error );
        });
    </script>

  </section><!--content-->
</div><!--main-->

%include('./dashboard/partials/footer.tpl')