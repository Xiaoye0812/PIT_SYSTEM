$(function () {
    $('#page15_jButton3').on('click', function (evt) {
        console.log('login-btn-click');
        var username = $('#page15_jEdit5').val().trim();
        var password = $('#page15_jEdit4').val();
        if (username === '' || username === null){
            alert('用户名不能为空！');
            return
        }
        if (password === '' || password === null){
            alert('密码不能为空！');
            return
        }
        $.ajax({
            url: '/user/login/',
            type: 'POST',
            data: {'username': username, 'password': password},
            dataType: 'json',
            success: function (result) {
                if (result.code === 200){
                    var userinfo = result.user_info;
                    if (userinfo.type === 0){
                        location.href = '/user/manage/';
                    }else {
                        location.href = '/product/productsearch/'
                    }
                }else{
                    alert('用户名或密码错误！');
                }
            },
            error: function (result) {
                alert('网络出错！');
            }
        })
    });
});