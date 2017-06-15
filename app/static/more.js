+ function($) {
    'use strict';

  $(document).on('click.bs.button.data-api', '[data-click="more"]', function (e) {
      var $add = $("#more")
      var num = $add.data('num')
      var type = $add.data('type')
      var $img = $("#moreimg")
      var $btn = $("#morebtn")
      $btn.css("display","none")
      $img.css("display","block")
      
      if (type)
        var url = "http://bigdatainsight.herokuapp.com/get/"+num+"?type="+type
      else
        var url = "http://bigdatainsight.herokuapp.com/get/"+num
      console.log(url)
      $.get(url, function(data){
                $("#more").append(data);
                $img.css("display","none")
                $btn.css("display","block")
        });
      $add.data("num", num+1);


    })


}(jQuery);
