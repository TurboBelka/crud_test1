$(function(){
    var tours_for_delete = $('input[type=checkbox]');
    $('.select_all').change(function(){
        for (var i = 0; i < tours_for_delete.length-1; i++){
            tours_for_delete[i].checked = $(this).prop('checked');
        }
    });
    $('.delete').click(function(event){
        event.preventDefault();
        for (var i = 0; i < tours_for_delete.length-1; i++){
            if (tours_for_delete[i].checked){
                $.ajax({
                    url: $(tours_for_delete[i]).data('url'),
                    method: 'get',
                    success: function(data){
                        console.log(data);
                    }
                });
            }
        }
    });

});