function logout() {
    $.removeCookie('myToken');
    window.location.href = '/';
}

function api_delete(no_give) {
    $.ajax({
        type: "POST",
        url: "/mountain/delete",
        data: { "no_give": no_give },
        success: function (response) {
            if (response['result'] == "success") {
                alert("삭제 완료!");
                window.location.href = '/mountain/list';
            } else {
                alert("삭제 실패!");
            }
        }
    });
}