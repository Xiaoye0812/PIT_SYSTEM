$(function () {
    var product_id = location.search.split('=')[1];
    console.log(product_id);
    if (product_id === '' || product_id === null){
        alert('商品编号有误!');
        location.href = '/';
    }else {
        $.ajax({
            url: '/product/productinfo/',
            type: 'POST',
            data: {'product_id': product_id},
            dataType: 'json',
            success: function (result) {
                if (result.code === 200){

                    var user_type = result.user_info.type;
                    if (user_type === 0 || user_type === 1){
                        $('a[href="/user/login/"]').parent().parent().css('display', 'none');
                        $('#logout-div').css('display', 'block');
                        $('#logout-div span').text(result.user_info.name);
                    }

                    var product = result.product;
                    $('#page1_jImages1 img')
                        .attr('src', product.image)
                        .css({'width': '250px', 'height': '250px', 'margin-top': '0px'});  // 商品图片
                    $('#page1_jLabel2').text(product.name);  // 商品名称
                    $('#page1_jLabel3').text(product.desc);  // 商品描述
                    $('#page1_jLabel6').text('商品批次：' + product.batch);  // 商品批次
                    $('#page1_jLabel8').text(product.inspector + ' 质检员');  // 质检员姓名
                    $('#page1_jLabel11').text(product.detection_time);  // 质检时间or添加时间
                    // 质检状态
                    if (product.status === 0){
                        $('#page1_jLabel12').text('未检测');
                    }else if (product.status === 1){
                        $('#page1_jLabel12').text('质检合格，允许出厂！');
                    }else {
                        $('#page1_jLabel12').text('质检不合格，不允许出厂！');
                    }
                }else {
                    alert('获取商品信息失败！');
                }
            },
            error: function () {
                alert('网络出错!');
            }
        })
    }
});