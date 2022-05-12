function account() {

    if (!varifyEmail() || !varifyPassword() || !varifyNick()) {
        return;
    }

    // 회원 생성 데이터
    $.ajax({
        type: "POST",
        url: "/mountain/account",
        data: {
            email_give: $('#userid').val(),
            password_give: $('#userpw').val(),
            nickname_give: $('#usernick').val()
        },
        success: function (response) {
            console.log("response", response)
            if (response['result'] == 'success') {
                alert('회원가입이 완료되었습니다.')
                // window.location.href = '/mountain/login'
            } else {
                alert(response['msg'])
                $("#userEmail").focus()
            }
        }
    })
}



// 이메일, 비밀번호, 닉네임 정규식

function is_email(asValue) {
    const regExp = /^[0-9a-zA-Z]([-_\.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_\.]?[0-9a-zA-Z])*\.[a-zA-Z]{2,3}$/i;
    return regExp.test(asValue);
}

function is_nickname(asValue) {
    const regExp2 = /^[a-zA-Z0-9-_/,.][a-zA-Z0-9-_/,. ]{1,10}$/;
    return regExp2.test(asValue);
}

function is_password(asValue) {
    var regExp = /^(?=.*\d)(?=.*[a-zA-Z])[0-9a-zA-Z!@#$%^&*]{8,20}$/;
    return regExp.test(asValue);
}


// 이메일 유효성 검사
function varifyEmail() {
    let userEmail = $("#userid").val()
    if (userEmail == "") {
        $("#help-email").text("이메일을 입력해주세요.").addClass('is-danger')
        $('.check-email').addClass('is-hidden')
        $('.email-icon').addClass('danger')
        $('.warn').removeClass('is-hidden').addClass('danger')
        $("#userid").addClass('is-danger')
        $("#userid").focus()
        return false;
    } else if (!is_email(userEmail)) {
        $("#help-email").text("이메일의 형식을 확인해주세요. 영문과 숫자, 특수문자(@) 사용 가능. 2-10자 길이").addClass("is-danger")
        $('.check-email').addClass('is-hidden')
        $('.email-icon').addClass('danger')
        $('.warn').removeClass('is-hidden').addClass('danger')
        $("#userid").addClass('is-danger')
        $("#userid").focus()
        return false;
    } else {
        $("#help-email").text("사용할 수 있는 이메일입니다.").removeClass('is-danger').addClass('is-success')
        $('.check-email').removeClass('is-hidden')
        $('.warn').addClass('is-hidden')
        $('.email-icon').removeClass('danger')
        $("#userid").removeClass('is-danger')
    }
    return true

}

// 이메일 중복 검사
function doubleCheckEmail() {
    let userEmail = $("#userid").val()
    if (userEmail == "") {
        $("#help-email").text("이메일을 입력해주세요.").addClass('is-danger')
        $('.check-email').addClass('is-hidden')
        $('.email-icon').addClass('danger')
        $('.warn').removeClass('is-hidden').addClass('danger')
        $("#userid").addClass('is-danger')
        $("#userid").focus()
        return;
    } else if (!is_email(userEmail)) {
        $("#help-email").text("이메일의 형식을 확인해주세요. 영문과 숫자, 특수문자(@) 사용 가능. 2-10자 길이").addClass("is-danger")
        $('.check-email').addClass('is-hidden')
        $('.email-icon').addClass('danger')
        $('.warn').removeClass('is-hidden').addClass('danger')
        $("#userid").addClass('is-danger')
        $("#userid").focus()
        return;
    }
    $.ajax({
        type: "POST",
        url: "/mountain/account/user",
        data: {
            email_give: $('#userid').val(),
            nickname_give: $('#usernick').val()
        },
        success: function (response) {
            console.log(response)
            if (response["exists"]) {
                $("#help-email").text("이미 존재하는 이메일입니다.").addClass("is-danger")
                $("#userid").addClass('is-danger')
                $('.check-email').addClass('is-hidden')
                $('.email-icon').addClass('danger')
                $('.warn').removeClass('is-hidden').addClass('danger')
                $("#userid").focus()
            } else {
                $("#help-email").text("사용 가능한 이메일입니다.").removeClass("is-danger").addClass("is-success")
                $('.warn').addClass('is-hidden')
                $('.check-email').removeClass('is-hidden')
                $('.email-icon').removeClass('danger')
                $("#userid").removeClass('is-danger')
            }
        }
    })
}

// 비밀번호 유효성 검사
function varifyPassword() {
    let userPw = $("#userpw").val()
    let userPw2 = $("#userpw2").val()

    if (userPw == '') {
        $("#help-password").text("비밀번호를 입력해주세요.").addClass('is-danger')
        $('.check-pw').addClass('is-hidden')
        $('.lock-icon').addClass('danger')
        $('.pw-warn').removeClass('is-hidden').addClass('danger')
        $("#userpw").addClass('is-danger')
        $("#userpw").focus()
        return false;
    } else if (!is_password(userPw)) {
        $("#help-password").text("비밀번호의 형식을 확인해주세요. 영문과 숫자 필수 포함, 특수문자(!@#$%^&*) 사용가능 8-20자").addClass('is-danger')
        $('.check-pw').addClass('is-hidden')
        $('.lock-icon').addClass('danger')
        $('.pw-warn').removeClass('is-hidden').addClass('danger')
        $("#userpw").addClass('is-danger')
        $("#userpw").focus()
        return false;
    } else {
        $("#help-password").text("사용할 수 있는 비밀번호입니다.").removeClass('is-danger').addClass('is-success')
        $('.pw-warn').addClass('is-hidden')
        $('.check-pw').removeClass('is-hidden')
        $('.lock-icon').removeClass('danger')
        $("#userpw").removeClass('is-danger')
    }
    if (userPw2 == '') {
        $("#help-password2").text("비밀번호를 입력해주세요.").addClass('is-danger')
        $('.check-pw2').addClass('is-hidden')
        $('.lock2-icon').addClass('danger')
        $('.pw2-warn').removeClass('is-hidden').addClass('danger')
        $("#userpw2").addClass('is-danger')
        $("#userpw2").focus()
        return false;
    } else if (userPw2 != userPw) {
        $("#help-password2").text("비밀번호가 일치하지 않습니다.").addClass('is-danger')
        $('.check-pw2').addClass('is-hidden')
        $('.lock2-icon').addClass('danger')
        $('.pw2-warn').removeClass('is-hidden').addClass('danger')
        $("#userpw2").addClass('is-danger')
        $("#userpw2").focus()
        return false;
    } else {
        $("#help-password2").text("비밀번호가 일치합니다.").removeClass('is-danger').addClass("is-success")
        $('.check-pw2').removeClass('is-hidden')
        $('.pw2-warn').addClass('is-hidden')
        $("#userpw2").removeClass('is-danger')
        $('.lock2-icon').removeClass('danger')
    }
    return true
}

// 닉네임 유효성 검사
function varifyNick() {
    let userNick = $("#usernick").val()
    if (userNick == "") {
        $("#help-nick").text("닉네임을 입력해주세요.").addClass('is-danger')
        $('.fa-check').addClass('is-hidden')
        $('.user-icon').addClass('danger')
        $('.nick-warn').removeClass('is-hidden').addClass('danger')
        $("#usernick").css({ 'border-color': 'red' })
        $("#usernick").addClass('is-danger')
        $("#usernick").focus()
        return false;
    } else if (!is_nickname(userNick)) {
        $("#help-nick").text('닉네임은 2-10자의 영문과 숫자와 일부 특수문자(._-)만 입력 가능합니다.').addClass('is-danger')
        $('.fa-check').addClass('is-hidden')
        $('.user-icon').addClass('danger')
        $('.nick-warn').removeClass('is-hidden').addClass('danger')
        $("#usernick").css({ 'border-color': 'red' })
        $("#usernick").addClass('is-danger')
        $("#usernick").focus()
        return false;
    } else {
        $("#help-nick").text("사용할 수 있는 닉네임입니다.").removeClass('is-danger').addClass('is-success')
        $('.check-nick').removeClass('is-hidden')
        $('.nick-warn').addClass('is-hidden')
        $('.user-icon').removeClass('danger')
        $("#usernick").removeClass('is-danger')
    }
    return true;
}

// 닉네임 중복 검사
function doubleCheckNick() {
    let userNick = $("#usernick").val()
    if (userNick == "") {
        $("#help-nick").text("닉네임을 입력해주세요.").addClass('is-danger')
        $('.fa-check').addClass('is-hidden')
        $('.user-icon').addClass('danger')
        $('.nick-warn').removeClass('is-hidden').addClass('danger')
        $("#usernick").css({ 'border-color': 'red' })
        $("#usernick").addClass('is-danger')
        $("#usernick").focus()
        return;
    } else if (!is_nickname(userNick)) {
        $("#help-nick").text('닉네임은 2-10자의 영문과 숫자와 일부 특수문자(._-)만 입력 가능합니다.').addClass('is-danger')
        $('.fa-check').addClass('is-hidden')
        $('.user-icon').addClass('danger')
        $('.nick-warn').removeClass('is-hidden').addClass('danger')
        $("#usernick").css({ 'border-color': 'red' })
        $("#usernick").addClass('is-danger')
        $("#usernick").focus()
        return;
    }
    $.ajax({
        type: "POST",
        url: "/mountain/account/user",
        data: {
            email_give: $('#userid').val(),
            nickname_give: $('#usernick').val()
        },
        success: function (response) {
            console.log(response)
            if (response["exists2"]) {
                $("#help-nick").text("이미 존재하는 닉네임입니다.").addClass("is-danger")
                $('.check-nick').addClass('is-hidden')
                $('.user-icon').addClass('danger')
                $('.nick-warn').removeClass('is-hidden').addClass('danger')
                $("#usernick").addClass('is-danger')
                $("#usernick").focus()
            } else {
                $("#help-nick").text("사용 가능한 닉네임입니다.").removeClass("is-danger").addClass("is-success")
                $('.nick-warn').addClass('is-hidden')
                $('.check-nick').removeClass('is-hidden')
                $('.user-icon').removeClass('danger')
                $("#usernick").removeClass('is-danger')
            }
        }
    });
}
