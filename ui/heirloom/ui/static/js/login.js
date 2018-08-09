Pts.quickStart("#pts-container", "#123");

(function () {

    var pts = [];
    var star_density = 0.001; // 1 = every pixel is a star, 0 = no stars

    space.add({
        // init with 500 random points 
        start: (bound) => {
            var area = space.innerBound.size[0] * space.innerBound.size[1];
            var numStars = star_density * area
            pts = Create.distributeRandom(space.innerBound, numStars);
        },

        animate: (time, ftime) => {
            pts.forEach(point => {
                form.fillOnly("#fff").point(point, 0.5);
            });
        },

        resize: (size, event) => {
            var area = space.innerBound.size[0] * space.innerBound.size[1];
            var numStars = star_density * area
            pts = Create.distributeRandom(space.innerBound, numStars);
        }
    });
    space.bindMouse().bindTouch().play();
})();