$(function () {
    $.ajax({
        url: '/product/index/',
        Type: 'GET',
        success: function (result) {
            if (result.code === 200){
                for (var i=0; i<4; i++){
                    var product = result.product_list[i];
                    var a_tag = $('<a>').attr('class', 'a-tag').attr('href', '/product/productinfo/?id=' + product.id)
                        .append($('<div>').attr({'class': 'product-div'})
                            .append($('<div>').attr({'class': 'image-div'})
                                .append($('<img>').attr({
                                    'src': product.image,
                                    'onerror': "this.src='/static/images/logo.png';this.onerror=null"
                                })
                                )
                            )
                            .append($('<div>').attr('class', 'title-div').text(product.name))
                            .append($('<div>').attr('class', 'sub-div').text(product.desc))
                        );
                    $('#show-product').append($(a_tag));
                }
            }else {
                $('#show-product').attr('display', 'None');
                $('#no-product').attr('display', 'inline');
            }
        },
        error: function (result) {
            $('#show-product').attr('display', 'None');
            $('#no-product').attr('display', 'inline');
        }
    });

    $('#page2_jButton1').on('click', function (evt) {
        var search_str = $('#page2_jEdit1').val();
        console.log('123');
        location.href = '/product/productsearch/?search=' + search_str;
    });
    $.ajax({
        url: '/user/userinfo/',
        type: 'GET',
        success: function (result) {
            console.log('userinfo get');
            if (result.user_info.type === 0 || result.user_info.type === 1){
                $('a[href="/user/login/"]').parent().parent().css('display', 'none');
                $('#logout-div').css('display', 'block');
                $('#logout-div span').text(result.user_info.name);
            }else {
                $('a[href="/user/login/"]').parent().parent().css('display', 'block');
                $('#logout-div').css('display', 'none');
            }
        },
        error: function () {

        }
    })
});



// <a href="" class="a-tag">
//     <div class="product-div">
//         <div class="image-div">
//             <img src="" alt="" onerror="this.src='/static/images/logo.png';this.onerror=null"/>
//         </div>
//         <div class="title-div">123</div>
//         <div class="sub-div">测试数据</div>
//     </div>
// </a>