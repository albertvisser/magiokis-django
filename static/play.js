
function play_or_pause(item) {
    audio_id = 'play_' + item;
    button_id = 'pb_' + item;
    text = document.getElementById(button_id).value;
    if (text === 'Play') {
        document.getElementById(button_id).value = 'Pause';
        document.getElementById(audio_id).play();
    } else {
        document.getElementById(button_id).value = 'Play';
        document.getElementById(audio_id).pause();
    }
}
