$(function () {
    var product_id = location.search.split('=')[1];
    if (product_id === '' || product_id === null){
        alert('商品编号有误!');
        location.href = '/';
    }else {
        $.ajax({
            url: '/product/product/',
            type: 'POST',
            data: {'product_info': product_id},
            dataType: 'json',
            success: function (result) {
                if (result.code === 200 && result.product_list.length >= 1){

                    var product = result.product_list[0];
                    $('#page4_jImages1 img')
                        .attr('src', product.image)
                        .css({'width': '180px', 'height': '180px', 'margin-top': '0px'});  // 商品图片
                    $('#page4_jLabel1').text('商品ID：' + product.id);
                    $('#page4_jLabel3').text(product.name);  // 商品名称
                    $('#page4_jMutiText1').text(product.desc);  // 商品描述
                    $('#page4_jLabel2').text('商品批次：' + product.batch);  // 商品批次
                }else {
                    alert('获取商品信息失败！');
                }
            },
            error: function () {
                alert('网络出错!');
            }
        });
        $('#page4_jButton1').click(function () {
            var status = $('#page4_jComboBox1_select').val();
            if (status === '0'){
                alert('请选择质检结果！');
                return
            }
            $.ajax({
                url: '/product/submit/',
                type: 'POST',
                data: {'product_id': product_id, 'status': status},
                dataType: 'json',
                success: function (result) {
                    if (result.code === 200){
                        alert('质检结果提交成功!');
                        history.back();
                    }else {
                        alert(result.msg);
                    }
                },
                error: function () {
                    alert('网络出错！');
                }
            })
        });
    }
});