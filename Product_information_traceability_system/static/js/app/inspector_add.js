$(function () {
    $('#page7_jButton1').click(function (evt) {
        var inspector_id = $('#page7_jEdit1').val();  // 质检员编号
        var inspector_username = $('#page7_jEdit3').val();  // 质检员用户名
        var inspector_password = $('#page7_jEdit4').val();  // 质检员密码
        var inspector_name = $('#page7_jEdit2').val();  // 质检员姓名
        $.ajax({
            url: '/user/addinspector/',
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
                    alert('添加成功!');
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