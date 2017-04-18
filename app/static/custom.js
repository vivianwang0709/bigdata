+function ($) {
	'use strict';
	
	var Article = function () {
		this.count = 1
		this.path  = null
  	}

  	Article.prototype.getPath = function (url) {

		if (url.length==1){
    		this.path = '../static/json/post.json';

		}else{
    		var reg = new RegExp("/post/",'g');
    		var url = url.replace(reg,'');
    		this.path = '../static/json/'+url+'.json';
		}
      this.path = '../static/json/news1.json';
    	return this.path
  	}

  	Article.prototype.getData = function (path,count) {
  		$.ajax({
        	url: path, //json文件位置
        	type: "GET", //请求方式为get
        	dataType: "json", //返回数据格式为json
        	success: function(data) {
            //请求成功完成后要执行的方法 
            //each循环 使用$.each方法遍历返回的数据date
            for (var i = 3*count-3; i < 3*count; i++) { 
              //console.log(data[i].pid)
              //console.log(data[0].title)
              //console.log(data[1].title)

              $(".post").append(function(n){
                //return "<p>"+ data[i].article_type +"</p>"
                return "<div class='article'><div class='a_img'><a href='../post/"+ data[i].article_type +"?pageid=" +data[i].pid+ "'><img src='../static/pic/"+data[i].article_type+"/"+data[i].pid+"_1.jpg' alt=''></a></div><div class='a_right'><div class='a_title'><p>" + data[i].title + "</p></div><div class='a_editor'></div><div class='a_date'></div><div class='a_content'><p>"+ data[i].scontent + "</p></div><div class='a_tag'><p><a class='btn btn-primary pull-right' href='../post/"+ data[i].article_type +"?pageid=" +data[i].pid+ "'>Read more<span class=''></span></a></p></div></div></div>"
              });
            }

        	}	
    	})

  		this.count = count + 1
  		return this.count
  	}


 	function Plugin(target) {

  		var $this   = $(this)
    	var url 	= window.location.pathname;
    	var data    = $this.data('bs.post')
    	
		if (!data) {
			$this.data('bs.post', (data = new Article()))
			data.getPath(url)
		}
		
		data.getData(data.path,data.count);

		return this

    }

	$(window).scroll(function(){

		//滚动条所在位置的高度
		var totalheight = parseFloat($(window).height()) + parseFloat($(window).scrollTop());

		//当前文档高度   小于或等于   滚动条所在位置高度  则是页面底部
		if(($(document).height()) <= totalheight+10) {
  		var $target = $(".post")
			Plugin.call($target,$target.data())
		}
    })
    

	$(document).ready(function() {
		$('[data-ride="post"]').each(function () {
			  var $this = $(this);
      	Plugin.call($this,$this.data())
    	})
  	})
  	

}(jQuery);