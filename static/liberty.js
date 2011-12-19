
var slides
var totalslides = 0
var slidenum = 0

function setupSongs(load_songs) {

    initSongs();

    // event handlers
    document.onkeydown = keyDown
    document.onkeyup   = keyUp
}

function initSongs() {
    slides = $('#slides .slide')
    totalslides = slides.size();

    // Show the first slide
    slides.first().addClass('current');
}

function keyDown(event) {
    var keyCode = event.keyCode // || event.which, arrow = {left: 37, up: 38, right: 39, down: 40 }

    debug('keydown: ' + keyCode);

    switch(keyCode) {
        case 37:
        break;
        case 38:
        break;
        case 39:
        break;
        case 40:
        break;
        case 84:
            window.location.href = '/songs/';
        break;
    }
}

function debug(data) {
    $('#debugInfo').text(data);
}
