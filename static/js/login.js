function verifyPassword() {
    const password = $("#password").val();
    if (!password) { // 패스워드가 비어있다면
        $("#password-error-message").removeClass("is-hidden");
        $("#password").addClass("is-danger");
        $("#password-exclamation").removeClass("is-hidden");
        $("#password").focus();
        return false; // False
    } else { // 패스워드가 비어있지 않다면
        $("#password-error-message").addClass("is-hidden");
        $("#password").removeClass("is-danger");
        $("#password-exclamation").addClass("is-hidden");
    }

    return true;
}

function verifyEmail() {
    const exp = /^[0-9a-zA-Z]([-_\.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_\.]?[0-9a-zA-Z])*\.[a-zA-Z]{2, 3}$/i;
    const email = $("#email").val();

    // 이메일을 입력하지 않았을 경우
    if (!email) {
        $("#email_error_message_1").removeClass("is-hidden");
        $("#email_error_message_2").addClass("is-hidden");
        $("#email").addClass("is-danger");
        $("#email-exclamation").removeClass("is-hidden");
        $("#email").focus();
        return false;
    } else {
        $("#email_error_message_1").addClass("is-hidden");
        $("#email").removeClass("is-danger");
        $("#email-exclamation").addClass("is-hidden");
        // 이메일 형식이 아닐 경우
        if (!exp.test(email)) {
            $("#email_error_message_2").removeClass("is-hidden");
            $("#email").addClass("is-danger");
            $("#email-exclamation").removeClass("is-hidden");
            $("#email").focus();
            return false;
        } else {
            $("#email_error_message_2").addClass("is-hidden");
            $("#email").removeClass("is-danger");
            $("#email-exclamation").addClass("is-hidden");
        }
    }
    return true;
}

function login() {
    if (!verifyEmail() || !verifyPassword()) return;
    $.ajax({
        type: "POST",
        url: "/mountain/login",
        data: { email_give: $("#email").val(), password_give: $("#password").val() },
        success: function (response) {
            if (response['result'] == 'success') {
                alert('로그인 성공');
                $.cookie('myToken', response['token']);
                window.location.href = '/mountain/list';
            } else {
                alert(response['message']);
                $("#email").focus();
            }
        }
    });
}