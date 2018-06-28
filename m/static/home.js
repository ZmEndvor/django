const ap = new APlayer({
	container: document.getElementById('aplayer'),
	mini: true,
	fixed: true,
	autoplay: true,
	theme: '#FADFA3',
	loop: 'all',
	preload: 'auto',
	volume: 0.7,
	mutex: true,
	listFolded: true,
	audio: [
		{
			name: 'Try',
	        artist: 'Asher Book',
	        url: 'static/music/g.mp3',
	        theme: '#505d6b',
            cover: 'static/img/try.jpg',
		}
	]
});
