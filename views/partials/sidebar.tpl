<style>
  #sidebar{
    min-height: 350px;
    background: lavender;
    padding: 10px 0;
    box-sizing: border-box;
  }
  #sidebar-menu li{
    list-style-type: none;
    font: 16px/1.75 Koulen, Oswald;
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
      <li><img src="/static/images/node.png" /><a href="#">Node.js</a></li>
      <li><img src="/static/images/php.png" /><a href="#">PHP</a></li>
      <li><img src="/static/images/python.png" /><a href="#">Python</a></li>
      <li><img src="/static/images/webdesign.png" /><a href="#">Web Design</a></li>
      <li><img src="/static/images/contact.png" /><a href="#">Contact</a></li>
    </ul>
  </nav>
</section><!--sidebar-->