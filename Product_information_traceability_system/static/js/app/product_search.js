$(function () {
    var product_info = location.search.split('=')[1];
    search_and_show(product_info);

    $('#page6_jButton1').click(function () {
        var search_info = $('#page6_jEdit1').val();
        $('tr[class=info-cont]').remove();
        search_and_show(search_info);
    })
});

function search_and_show(product_info) {
    $.ajax({
        url: '/product/product/',
        type: 'POST',
        data: {'product_info': product_info},
        dataType: 'json',
        success: function (result) {
            $('#search_info').text(product_info);
            $('tr[class=info-content]').remove();
            if (result.code === 200){
                var product_list = result.product_list;
                var user_type = result.user_info.type;
                if (user_type === 0 || user_type === 1){
                    $('a[href="/user/login/"]').parent().parent().css('display', 'none');
                    $('#logout-div').css('display', 'block');
                    $('#logout-div span').text(result.user_info.name);
                }
                for (var i=0; i<product_list.length; i++){
                    var product = product_list[i];
                    var tr_tag = $('<tr>').attr('class', 'info-content');
                    $(tr_tag).append($('<td>').append($('<a>')
                        .attr('href', '/product/productinfo/?id=' + product.id)
                        .append($('<img>').attr('src', product.image))));
                    $(tr_tag).append($('<td>').text(product.id));
                    $(tr_tag).append($('<td>').text(product.name));
                    $(tr_tag).append($('<td>').text(product.batch));
                    $(tr_tag).append($('<td>').text(product.desc));
                    $(tr_tag).append($('<td>').text(product.inspector));
                    if (product.status === 0){
                        $(tr_tag).append($('<td>').text('未检测'));
                    }else if (product.status === 1) {
                        $(tr_tag).append($('<td>').text('通过质检'));
                    }else {
                        $(tr_tag).append($('<td>').text('未通过质检'));
                    }
                    if (user_type === 1 && product.status ===0){
                        $(tr_tag).append($('<td>').append($('<a>')
                            .attr('href', '/product/submit/?id=' + product.id).text('质检')));
                    }else {
                        $(tr_tag).append($('<td>'));
                    }
                    $('#info-list').append($(tr_tag));
                }

                $('#page16_jPanel4').css('height', 100+45+51*product_list.length+'px');
            }
        },
        error: function (result) {
            alert('网络出错！');
        }

    })
}