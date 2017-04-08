+function ($) {
	'use strict';
	
	var Article = function (element, options) {
  	}

  // CAROUSEL PLUGIN DEFINITION
  // ==========================

 	function Plugin(option) {

  		var $this   = $(this)
    	var url 	= window.location.pathname;
    	var count 	= 1
    	var data    = $this.data('bs.post')

		if (!data) {
			$this.data('bs.post', (data = new Article(this, options)))

			if (url.length==1){
    			var path = '../static/json/post.json';

			}else{
    			var reg = new RegExp("/article/",'g');
    			var url = url.replace(reg,'');
    			var path = '../static/json/'+url+'.json';
			}
		}

		$.getdata(path,count);
    	count = count+1;
    }


	$(document).ready(function() {
		$('[data-ride="post"]').each(function () {
      		Plugin.call(this)
    	})
  	})


}(jQuery);