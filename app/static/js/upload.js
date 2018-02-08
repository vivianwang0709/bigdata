+ function($) {
    'use strict';


    function getObjectURL(file) {
        var url = null;
        if (window.createObjectURL != undefined) { // basic
            url = window.createObjectURL(file);
        } else if (window.URL != undefined) { // mozilla(firefox)
            url = window.URL.createObjectURL(file);
        } else if (window.webkitURL != undefined) { // webkit or chrome
            url = window.webkitURL.createObjectURL(file);
        }
        return url;
    }


    $(document).on('change.bs.button.data-api', '[id=uploadinput]', function(e) {
        var objUrl = getObjectURL(this.files[0]);
        var objName = this.files[0].name

        $("#uploadimg").parent().remove();

        $(".mkupload").append("<div>\
          <img src='"+objUrl+"' id='uploadimg' data-upload=0>\
          <span class='uimg' style='display:none'></span></div>");


        $("#uploadimg").click(function() {
            $("#uploadimg").parent().remove();
        });


        $("#uploadimg").hover(function() {
            $('.uimg').css("display", "block").text(objName);
        }, function() {
            $('.uimg').css("display", "none");
        });


    })


}(jQuery);
