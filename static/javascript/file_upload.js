$(document).on('click', '#close-preview', function(){
    $('.image-preview').popover('hide');
    // Hover befor close the preview
});

//$(document).on('submit', '#invoice_upload', function(e){
//    e.preventDefault();
//    alert('ok');
//    $.ajax({
//        type : 'POST',
//        url : 'submit_invoice/',
//        headers: {'X-CSRFToken': '{{ csrf_token }}'},
//        data : {
//            file : $('#invoice_xls').val(),
//            name : 'sumit',
//        },
//        success : function(data){
//            alert(JSON.stringify(data));
//        },
//        error : function(data){
//            alert(JSON.stringify(data));
//        }
//    });
//
//    alert('ok');
//});

$(function() {
    // Create the close button
    var closebtn = $('<button/>', {
        type:"button",
        text: 'x',
        id: 'close-preview',
        style: 'font-size: initial;',
    });
    closebtn.attr("class","close pull-right");

    // Clear event
    $('.image-preview-clear').click(function(){
        $('.image-preview').attr("data-content","").popover('hide');
        $('.image-preview-filename').val("");
        $('.image-preview-clear').hide();
        $('.image-preview-input input:file').val("");
        $(".image-preview-input-title").text("Browse");
    });
    // Create the preview image
    $(".image-preview-input input:file").change(function (){
        var img = $('<img/>', {
            id: 'dynamic',
            width:250,
            height:200
        });
        var file = this.files[0];
        var reader = new FileReader();
        // Set preview image into the popover data-content
        reader.onload = function (e) {
            $(".image-preview-input-title").text("Change");
            $(".image-preview-clear").show();
            $(".image-preview-filename").val(file.name);
        }
        reader.readAsDataURL(file);
    });
});