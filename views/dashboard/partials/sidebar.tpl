<style>
  #sidebar{
    min-height: 350px;
    background: lavender;
    padding: 10px 0;
    box-sizing: border-box;
  }
  #sidebar-menu li{
    list-style-type: none;
    font: 16px/1.75 Koulen;
    margin-bottom: 20px;
    display: grid;
    grid-template-columns: 15% calc(85% - 10px);
    grid-gap: 10px;
    align-items: center;
  }
  #sidebar-menu li img{
    width: 100%;
  }
  #sidebar-menu li a{
    display: inline-block;
  }
</style>

<section id='sidebar' class="sidebar">
  <nav>
    <ul id="sidebar-menu">
      <li><img src="/static/images/posting.png" /><a href="/login">ចុះ​ផ្សាយ</a></li>
      <li><img src="/static/images/categorizing.png" /><a href="/category">បង្កើត​ជំពូក</a></li>
      <li><img src="/static/images/paging.png" /><a href="/page">បង្កើត​ទំព័រ</a></li>
      <li><img src="/static/images/multimedia.png" /><a target="_blank" href="/upload">ចំលង​ឯកសារ</a></li>
      <li><img src="/static/images/user.png" /><a href="/signup">ចុះ​ឈ្មោះ​​សមាជិក</a></li>
      <li><img src="/static/images/setting.png" /><a href="/setting">កំណត់ទំរង់​ដើម</a></li>
    </ul>
  </nav>
</section><!--sidebar-->