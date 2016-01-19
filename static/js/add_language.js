$(function(){
    $('.add_language').click(function(event){
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
    });

});