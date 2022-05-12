function logout() {
    $.removeCookie('myToken');
    window.location.href = '/';
}
function api_add() {
    const mountain = {
        "title": $("#title").val(),
        "image": $("#image").val(),
        "name": $("#name").val(),
        "address": $("#address").val(),
        "level": $("#level option:selected").val(),
        "content": $("#content").val()
    }

    $.ajax({
        type: "POST",
        url: "/mountain/add",
        data: mountain,
        success: function (response) {
            if (response['result'] == 'success') {
                alert("등록 완료!")
                window.location.href = '/mountain/list';
            } else {
                alert("등록 실패!")
            }
        }
    });

}