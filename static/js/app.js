'use strict';

var main = function() {

    let togglePassword = function() {

        let passwordInput = document.getElementById('password');

        if (passwordInput.type == 'password') {
            passwordInput.type = 'text';
        } else {
            passwordInput.type = 'password';
        }

    };

    $('.toggle-password').click(togglePassword);
}

$(document).ready(main);