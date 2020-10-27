<!--views/dashboard/home.tpl-->
%include('./dashboard/partials/header.tpl')

<style>
  #content{
    min-height: 350px;
    background: lavender;
    padding: 20px;
    box-sizing: border-box;
  }
  #content #setting{
    display: grid;
    grid-template-columns: 17% 50%;
    grid-gap: 5px;
    align-items: center;
  }
  #content #setting span{
    text-align: right;
    font: 14px/1.5 Oswald, Bayon;
  }
  #content #setting input{
    padding: 5px 10px;
    font: 14px/1.5 Arial, OdorMeanChey;
  }
</style>

<div  id='main' class='main region'>

  %include('./dashboard/partials/sidebar.tpl')

  <section id='content' class='content'>
    
    <form id="setting" action="/setting" method="post">
      <span>Blog Title:</span><input type="text" name="fblog-title" value="{{data['post'][0]}}" required />
      <span>Secret Key:</span><input type="text" name="fsecret-key" value="{{data['post'][1]}}" required/>
      <span>Dashboard Post Limit:</span><input type="text" name="fdpost-limit" value="{{data['post'][2]}}" required />
      <span>Frontend Post Limit:</span><input type="text" name="ffpost-limit" value="{{data['post'][3]}}" required />
      <span>Home Post Limit:</span><input type="text" name="fhpost-limit" value="{{data['post'][4]}}" required />
      <span>Author Post Limit:</span><input type="text" name="fapost-limit" value="{{data['post'][5]}}" required />
      <span>Blog Description:</span><input type="text" name="fblog-description" value="{{data['post'][6]}}" required />
      <a></a><input type="submit" value="បញ្ចូល​ទិន្នន័យ" />
    </form>
    <div style="text-align: center;">{{data["message"]}}</div>
    %data['message'] = ""

  </section><!--content-->
</div><!--main-->

%include('./dashboard/partials/footer.tpl')