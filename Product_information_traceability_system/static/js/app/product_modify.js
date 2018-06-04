$(function () {
    $.post('/user/inspector/', {}, function (result) {
        var select = $('#page13_jComboBox1_select');
        if (result.code === 200){
            var inspector_list = result.inspector_list;

            for (var i=0; i<inspector_list.length; i++){
                var inspertor = inspector_list[i];
                $(select).append($('<option>').attr('value', inspertor.id).text(inspertor.name));
            }
        }else {
            $(select).append($('<option>').attr('value', '0').text('获取质检员姓名失败'))
        }
    });
    $('#page13_jButton1').click(function () {
        var formData = new FormData();
        var product_id = $('#page13_jEdit1').val();
        var name = $('#page13_jEdit7').val();
        var batch_id = $('#page13_jEdit6').val();
        var desc = $('#page13_jEdit8').val();
        var inspector_id = $('#page13_jComboBox1_select').val();
        var product_image = $('#upload').get(0).files[0];
        if (inspector_id === '0'){
            alert('未选择正确的质检员，无法修改产品信息');
            return
        }
        formData.append('product_id', product_id);
        formData.append('name', name);
        formData.append('batch_id', batch_id);
        formData.append('desc', desc);
        formData.append('inspector_id', inspector_id);
        formData.append('product_image', product_image);
        $.ajax({
            url: '/product/changeproduct/',
            type: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            success: function (result) {
                if (result.code === 200){
                    alert('修改成功');
                }else {
                    alert(result.msg);
                }
            },
            error: function () {
                alert('网络出错！');
            }
        })
    })
});
