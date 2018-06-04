$(function () {
    var inspectot_info = location.search.split('=')[1];

    search_and_refresh(inspectot_info);
    
    $('#page6_jButton1').click(function () {
        var search_info = $('#page6_jEdit1').val();
        $('tr[class=info-cont]').remove();
        search_and_refresh(search_info);
    })
});

function search_and_refresh(inspector_info) {
    var table_height = 0;
    $.ajax({
        url: '/user/inspector/',
        type: 'POST',
        data: {'search_info': inspector_info},
        dataType: 'json',
        success: function (result) {
            if (result.code === 200){
                var inspector_list = result.inspector_list;
                $('tr[class=info-cont]').remove();
                // console.log('befor' + table_height);
                for (var i=0; i<inspector_list.length; i++){
                    var inspector = inspector_list[i];
                    var tr_tag = $('<tr>').attr('class', 'info-cont').css('height', '0px');
                    $(tr_tag).append($('<td>').text(inspector.id).attr('inspector_id', inspector.id));
                    $(tr_tag).append($('<td>').text(inspector.name));
                    $(tr_tag).append($('<td>').text(inspector.username));
                    $(tr_tag).append($('<td>').text(inspector.password));
                    $(tr_tag).append($('<td>').append($('<a>')
                        .attr('href', '/user/inspectormodify/?id=' + inspector.id).text('修改')));
                    $(tr_tag).append($('<td>').append($('<a>').text('删除').css('color', 'red')
                        .attr({'href': "javascript:;", 'inspector_id': inspector.id}).click(del_inspector)));
                    $('#inspector_table').append($(tr_tag));
                    // console.log($(tr_tag).height());
                    table_height += $(tr_tag).height();
                }
                console.log(table_height);
                $('#inspector_table').css('height', 45+table_height+'px');
                $('#page6_jPanel4').css('height', 100+45+table_height+'px');

            }
        },
        error: function (result) {
            alert('网络出错！');
        }
    })
}

function del_inspector() {
    var inspector_id = $(this).attr('inspector_id');
    // console.log($(this));
    console.log('inspector_id' + inspector_id);
    $.post('/user/delinspector/', {'inspector_id': inspector_id}, function (result) {
        if (result.code === 200){
            alert('删除成功!');
            search_and_refresh('');
        }else {
            alert(result.msg);
        }
    })
}