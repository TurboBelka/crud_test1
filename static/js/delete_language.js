var get_id_for_delete = function(){}


var replace = function(){
    var index = 0;
    $.each($('.my_form .language'), function(i, value){
        var $this = $(this).find('input, select');
        $($this).attr('id',  $($this).attr('id').replace($($this).attr('id').match('[0-9]+')[0], (index)));
        $($this).attr('name', $($this).attr('name').replace($($this).attr('name').match('[0-9]+')[0], (index)));
        index += 1;
    })
}

$(function(){
    $('.languages_forms').on('click', 'a.add_language', function(event){
        event.preventDefault();
        var language_block = $('.my_form').last().clone();

        var cur_count_form = parseInt($('#id_tourleadslanguages_set-TOTAL_FORMS').val());
        $('#id_tourleadslanguages_set-TOTAL_FORMS').val(cur_count_form+1);

        $.each(language_block.find('.select_language'), function(index, value){
            var id_number = $(this).attr('id');
            id_number = parseInt(id_number.match('[0-9]+')[0]);
            $(this).attr('id',  $(this).attr('id').replace($(this).attr('id').match('[0-9]+')[0], (id_number+1)));
            $(this).attr('name', $(this).attr('name').replace($(this).attr('name').match('[0-9]+')[0], (id_number+1)));
        });

        $('.languages_forms').append(language_block);

        $.each($('.select_language'), function(index, value){
            if ($(this).val()){
                $(this).parent().find('span a').html('<i class="fa fa-remove fa-fw"></i>Remove');
                $(this).parent().find('span a').addClass('for_delete');
                $(this).parent().find('span a').removeClass('add_language');
            }else{
                $(this).parent().find('span a').html('<i class="fa fa-save fa-fw "></i>Add');
                $(this).parent().find('span a').addClass('add_language');
                $(this).parent().find('span a').removeClass('for_delete');
            }
        });

        replace();
    });

    $('.languages_forms').on('click', 'a.for_delete', function(event){
        event.preventDefault();

        var block_for_delete = $(this).parents('.my_form');

        var cur_count_form = parseInt($('#id_tourleadslanguages_set-TOTAL_FORMS').val());
        $('#id_tourleadslanguages_set-TOTAL_FORMS').val(cur_count_form-1);

        block_for_delete.remove();
        get_id_for_delete();
        replace();
    });
});

