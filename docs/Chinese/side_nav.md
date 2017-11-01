```html
<script>$(document).ready(function(){
    $(".button-collapse").sideNav();
        });
</script>
<ul id="slide-out" class="side-nav fixed">
<li>
    <div class="userView">
        <div class="background teal">
        </div>
        <a href="#!user"><img class="circle" src="static/images/face.jpeg"></a>
        <a href="#!name"><span class="black-text name">姓名</span></a>
        <a href="#!email">
            <span class="black-text ">学号</span></a>
    </div>
</li>
<li>
    <ul class='collapsible' data-collapsible="accordion">
    <li>
        <a class="collapsible-header waves-effect waves-teal">
            个人中心
        </a>
        <div class="collapsible-body">
        </div>
    </li>
    </ul>
</li>
<li>
    <ul class='collapsible' data-collapsible="accordion">
    <li>
        <a class="collapsible-header waves-effect waves-teal">
            事务管理 
            <span class="new badge">4</span>
        </a>
        <div class="collapsible-body">
            <ul>
            <li>
                <a href="#!" class="black-text">
                     今日课程
                    <span class="badge">2</span>
                </a>
            </li>
            <li>
                <a href="#!" class="black-text">
                    会议讲座
                    <span class="badge">1</span>
                </a>
            </li>
            <li>
                <a href="#!" class="black-text">
                    组织活动
                    <span class="badge">1</span>
                </a>
            </li>
            </ul>
        </div>
    </li>
    </ul>
</li>
<li>
    <ul class='collapsible' data-collapsible="accordion">
    <li>
        <a class="collapsible-header waves-effect waves-teal">
            我的课程
        </a>
        <div class="collapsible-body">
            <ul>
            <li>
                <a href="#!" class="black-text">学期概况</a>
            </li>
            <li>
                <a href="#!" class="black-text">成绩概况</a>
            </li>
            </ul>
        </div>
    </li>
    </ul>
</li>
<li>
    <ul class='collapsible' data-collapsible="accordion">
    <li>
        <a class="collapsible-header waves-effect waves-teal">
            热点
        </a>
        <div class="collapsible-body">
        </div>
    </li>
    </ul>
</li>
</ul>
<a href="#" data-activates="slide-out" class="button-collapse"><i class="material-icons">menu</i></a>
```