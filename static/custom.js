$.getdata = function(path,count){
    $.ajax({
        url: path, //json文件位置
        type: "GET", //请求方式为get
        dataType: "json", //返回数据格式为json
        success: function(data) {
            //请求成功完成后要执行的方法 
            //each循环 使用$.each方法遍历返回的数据date
            $.each(data, function(i, item) {
                //if(count<0 || (i<=3*count-1 && i>=3*count-3)){
                if(item.pageid<=3*count && item.pageid>=3*count-2){
                var h = $(document).height();
                $(".container").css("height",h+190); 
                $(".m_left").append(function(n) {
                    return "<div class='media'>\
              <div class='media-left'>\
              <a href='../article/"+ item.tag +"?pageid=" +item.pageid+ "'>\
               <img class='media-object' src='../static/pic/"+item.tag+"_"+item.pageid+"_1.jpg' alt='...'>\
              </a>\
                    </div>\
                    <div class='media-body'>\
                        <h4 class='media-heading'>" + item.title + "</h4>\
                        <p>" + item.content + "</p>\
                        <p><a class='btn btn-primary btn-lg' href='../article/"+ item.tag +"?pageid=" +item.pageid+ "' role='button'>Read more</a></p>\
                    </div>\
                </div>"

                });
            }

            })
        }
    })
}


var url = window.location.pathname;

if (url.length==1){
    var path = '../static/json/post.json';

}else{
    var reg = new RegExp("/article/",'g');
    var url = url.replace(reg,'');
    var path = '../static/json/'+url+'.json';
}


var count=1

$(document).ready(function() {
    $.getdata(path,count);
    count = count+1;
});



$(window).scroll(function(){
//滚动条所在位置的高度
totalheight = parseFloat($(window).height()) + parseFloat($(window).scrollTop());
//当前文档高度   小于或等于   滚动条所在位置高度  则是页面底部
if(($(document).height()) <= totalheight+10) {
    $.getdata(path,count);
    count = count+1;
 
}
});


