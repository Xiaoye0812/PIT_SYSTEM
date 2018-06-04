$(function () {
    $('#page8_jButton1').click(function (evt) {
        var inspector_id = $('#page8_jEdit1').val();  // 质检员编号
        var inspector_username = $('#page8_jEdit3').val();  // 质检员用户名
        var inspector_password = $('#page8_jEdit4').val();  // 质检员密码
        var inspector_name = $('#page8_jEdit2').val();  // 质检员姓名
        $.ajax({
            url: '/user/changeinspector/',
            type: 'POST',
            data: {
                'username': inspector_username,
                'name': inspector_name,
                'password': inspector_password,
                'inspector_id': inspector_id
            },
            dataType: 'json',
            success: function (result) {
                if (result.code === 200){
                    alert('修改成功!');
                    history.back();
                }
                else {
                    alert(result.msg);
                }
            },
            error: function () {
                alert('网络出错！');
            }
        })
    })
});