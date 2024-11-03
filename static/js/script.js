$(document).ready(function () {
    // 身長　音声入力ボタンがクリックされた時の処理
    $('#record-button-height').click(function () {
        $.ajax({
            url: '/api/transcribe',
            type: 'POST',
            success: function (data) {
                $('#input-height-text').val(data.text);
            },
            error: function () {
                alert('音声認識に失敗しました');
            }
        });
    });
    // 体重　音声入力ボタンがクリックされた時の処理
    $('#record-button-weight').click(function () {
        $.ajax({
            url: '/api/transcribe',
            type: 'POST',
            success: function (data) {
                $('#input-weight-text').val(data.text);
            },
            error: function () {
                    alert('音声認識に失敗しました');
            }
        });
    });
    // 音声入力ボタンの上にマウスが来た時の処理
    $(".input-text").on("mouseover", function () {
        $(".input-text").css({
            color: "#ff0000",
            backgroundColor: "#ffc042"
        })
    });
    // 音声入力ボタンからマウスが離れた時の処理
    $(".input-text").on("mouseout", function () {
        $(".input-text").css({
            color: "",
            backgroundColor: ""
        })
    });
});