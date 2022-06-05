$(document).ready(function(){
    // $('.basket_list input[type=number]').click(function(){
    $('.basket_list').on(types: 'click', selector: 'input[type=number]', data: function(){
        let pk = event.target.name;
        let quantity = event.target.value;
        $.ajax(url:{
            url: '/basket/edit/' + pk + '/' + quantity + '/',
            success: function(data){
                $('.basket_list').html(data.result);
            }
        });
    });

//    $('.basket_list').on(types: 'click', selector: '.add-quantity', data: function(){
//    let pk = $(this).attr(name:'data-pk');
//        let quantity = parseInt($(this).attr(name: 'data-quantity')) + 1;
//        $.ajax(url:{
//            url: '/basket/edit/' + pk + '/' + quantity + '/',
//            success: function(data){
//                $('.basket_list').html(data.result);
//            }
//        });
//    });
});