+ function($) {
    'use strict';

  $(document).on('click.bs.button.data-api', '[data-click="more"]', function (e) {
      var $add = $("#more")
      var num = $add.data('num')
      var type = $add.data('type')
      var $img = $("#moreimg")
      var $btn = $("#morebtn")

      var max = $('.post').data('num')
      
      if (num-1>=max/5){
          $btn.css("display","none")
          $('.morediv').append('<p>親，感謝你的支持，已經加載到底部摟～</p>')
          return
      } 

      $btn.css("display","none")
      $img.css("display","block")

      if (type)
        var url = "http://bigdatainsight.herokuapp.com/get/"+num+"?type="+type
      else
        var url = "http://bigdatainsight.herokuapp.com/get/"+num
      
      $.get(url, function(data){
                $("#more").append(data);
                $img.css("display","none")
                $btn.css("display","block")
        });
      $add.data("num", num+1);


    })


}(jQuery);
