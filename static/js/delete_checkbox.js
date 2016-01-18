$(function(){
    var tours_for_delete = $('input[type=checkbox]');
    $('.select_all').change(function(){
        for (var i = 0; i < tours_for_delete.length-1; i++){
            tours_for_delete[i].checked = $(this).prop('checked');
        }
    });

    $('.delete').click(function(event){
        event.preventDefault();
        var data = {};
        for (var i = 0; i < tours_for_delete.length-1; i++){
            if (tours_for_delete[i].checked){
                data[$(tours_for_delete[i]).data('tour')] = $(tours_for_delete[i]).data('id');
            }
            var csrf = $('input[name=csrfmiddlewaretoken]').val();
            data['csrfmiddlewaretoken'] = csrf;
            $.ajax({
                url: $(this).data('url'),
                method: 'post',
                data: data,
                success: function(data){
                    window.location.href = data.url;
                }
            });
        }
    });

    $('.delete-tour').click(function(event){
        event.preventDefault();
        $('#deleteModal').modal('toggle');
        $('.confirm').attr('action', $(this).attr('href'));
    });

});