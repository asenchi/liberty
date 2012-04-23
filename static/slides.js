window.onload = function() {
	var slides = document.getElementById('slides');
	if(!slides) return;  // Not showing a song, nothing to do

	// Put together a list of slides
	var anchors = slides.getElementsByTagName('a'), slides = [];
	for(var i=0; i < anchors.length; i++) {
		var index = anchors[i].name;
		var slide = document.getElementById('slide' + index);
		slides.push(slide);
	}

	// Change slides as necessary
	var current = 0;
	function activate(index) {
		if(index < 0 || index >= slides.length) return;  // Out of bounds
		slides[current].style.display = 'none';
		slides[index].style.display = '';
		current = index;
	}

	// Respond to keyboard events
	document.onkeydown = function(event) {
		if(event.altKey || event.shiftKey) return;
		switch(event.keyCode) {
			case 13:  // Enter
			case 32:  // Space
			case 34:  // Page Down
			case 39:  // Right
			case 40:  // Down
				activate(current + 1);
				event.preventDefault();
				return false;
			case 8:   // Backspace
			case 33:  // Page Up
			case 37:  // Left
			case 38:  // Up
				activate(current - 1);
				event.preventDefault();
				return false;
			case 66:  // B
				var hidden = slides[current].style.display == 'none';
				slides[current].style.display = hidden ? '' : 'none';
				event.preventDefault();
				return false;
		}
	}
}
