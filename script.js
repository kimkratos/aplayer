document.addEventListener('DOMContentLoaded', () => {
    const ap = new APlayer({
        container: document.getElementById('player1'),
        fixed: true,
        autoplay: true,
        theme: '#FADFA3',
        loop: 'all',  // 循环播放
        order: 'list',  // 列表顺序播放
        preload: 'auto',
        volume: 0.7,
        mutex: true,
        listFolded: false,  // 展开播放列表
        listMaxHeight: 90,
        lrcType: 3,
        audio: [
            {
                name: 'Pink Palaka',
                artist: 'Andrew E',
                url: '/music/PinkPalaka.m4a',
                cover: '/music/pink.png',
                lrc: '/music/pink.lrc'
            },
            {
                name: 'Ferrari',
                artist: 'Bebe Rexha',
                url: '/music/ferrari.m4a',
                cover: '/music/ferrari.png',
                lrc: '/music/ferrari.lrc'
            },
            {
                name: '霜雪千年',
                artist: '洛天依/乐正绫',
                url: '/music/sxqn.m4a',
                cover: '/music/sxqn.png',
                lrc: '/music/sxqn.lrc'
            },
            {
                name: 'jar of love',
                artist: '曲婉婷',
                url: '/music/ajar_Of_Love.m4a',
                cover: '/music/jar.png',
                lrc: '/music/jaroflove.lrc'
            },
            {
                name: '差不多先生',
                artist: 'hot dog',
                url: '/music/almostnew.m4a',
                cover: '/music/almost.png',
                lrc: '/music/almost.lrc'
            },
            {
                name: '垃圾话',
                artist: 'GAI',
                url: '/music/trash_talk_GAI.m4a',
                cover: '/music/trash.png',
                lrc: '/music/trash.lrc'
            },
            {
                name: '威远故事',
                artist: 'GAI',
                url: '/music/official_GAI.m4a',
                cover: '/music/offical.png',
                lrc: '/music/offical.lrc'
            },
        ]
    });

    const animationContainer = document.getElementById('animation-container');

    function createRipple() {
        const ripple = document.createElement('div');
        ripple.classList.add('ripple');
        animationContainer.appendChild(ripple);

        setTimeout(() => {
            ripple.remove();
        }, 2000);
    }

    setInterval(createRipple, 1000);
});
