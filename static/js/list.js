function logout() {
    $.removeCookie('myToken');
    window.location.href = '/';
}