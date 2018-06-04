$(function () {
    var search_info = location.search.split('=')[1];

    search_and_refresh(search_info);

    $('#page11_jButton1').click(function () {
        var search_info = $('#page11_jEdit1').val();
        $('tr[class=info-cont]').remove();
        search_and_refresh(search_info);
    })
});

function search_and_refresh(product_info) {
    // var table_height = 0;
    $.ajax({
        url: '/product/product/',
        type: 'POST',
        data: {'product_info': product_info},
        dataType: 'json',
        success: function (result) {
            if (result.code === 200){
                var product_list = result.product_list;
                $('tr[class=info-cont]').remove();
                // console.log('befor' + table_height);
                for (var i=0; i<product_list.length; i++){
                    var product = product_list[i];
                    var tr_tag = $('<tr>').attr('class', 'info-cont').css('height', '50px');
                    $(tr_tag).append($('<td>').append($('<a>')
                        .attr('href', '/product/productinfo/?id=' + product.id)
                        .append($('<img>').attr('src', product.image))));
                    $(tr_tag).append($('<td>').text(product.id).attr('product_id', product.id));
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
                    $(tr_tag).append($('<td>').append($('<a>')
                        .attr('href', '/product/productmodify/?id=' + product.id).text('修改')));
                    $(tr_tag).append($('<td>').append($('<a>').text('删除').css('color', 'red')
                        .attr({'href': "javascript:;", 'product_id': product.id}).click(del_product)));
                    $('#product_table').append($(tr_tag));
                    // console.log($(tr_tag).height());
                    // table_height += $(tr_tag).height();
                }
                // console.log(table_height);
                // $('#product_table').css('height', 45+table_height+'px');
                // $('#page11_jPanel4').css('height', 100+45+table_height+'px');

            }
        },
        error: function (result) {
            alert('网络出错！');
        }
    })
}

function del_product() {
    var product_id = $(this).attr('product_id');
    // console.log($(this));
    console.log('product_id' + product_id);
    $.post('/product/delproduct/', {'product_id': product_id}, function (result) {
        if (result.code === 200){
            alert('删除成功!');
            search_and_refresh('');
        }else {
            alert(result.msg);
        }
    })
}