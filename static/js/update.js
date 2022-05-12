function logout() {
    $.removeCookie('myToken');
    window.location.href = '/';
}

function api_update(no_give) {
    const mountain = {
        "no": no_give,
        "title": $("#title").val(),
        "image": $("#image").val(),
        "name": $("#name").val(),
        "address": $("#address").val(),
        "level": $("#level option:selected").val(),
        "content": $("#content").val()
    }

    $.ajax({
        type: "POST",
        url: "/mountain/update",
        data: mountain,
        success: function (response) {
            if (response['result'] == 'success') {
                alert("수정 완료!")
                window.location.href = '/mountain/list';
            } else {
                alert("수정 실패!")
            }
        }
    });

}