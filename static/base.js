var toTop = document.getElementById('top-button');

window.onscroll = function (ev) {
    // 1.当拖动滚动条的是时候， 当内容滚动出去10px的时候，改变top的高度，并且显示回到顶部按钮
    // 如何获得滚动距离
    // document.body.scrollTop
    // document.documentElement.scrollTop
    var scrollTop = document.body.scrollTop || document.documentElement.scrollTop;
    if(scrollTop > 10) {
        // 显示回到顶部
        toTop.style.display = 'block';
    } else {
        toTop.style.display = 'none';
    }
};
// 2. 当点击回到顶部按钮的时候，以动画的方式，回到到最上面，让滚动距离为0
var timeId = null;
toTop.onclick = function (ev) {
    if(timeId) {
        clearInterval(timeId);
        timeId = null;
    }

    timeId = setInterval(function () {
        // 步进
        var step = 10;
        // 目标位置
        var target = 0;

        // 获取当前位置
        var current = document.body.scrollTop || document.documentElement.scrollTop;
        var currentRocket = toTop.offsetTop;
        if(current > target) {
            step = -Math.abs(step);
        }
        // 判断现在是否已经到达目标位置
        if(Math.abs(current - target) <= Math.abs(step)) {
            clearInterval(timeId);
            document.body.scrollTop = target;
            document.documentElement.scrollTop = target;
            toTop.style.top = '50%';
            return;
        }
        current += step;
        document.body.scrollTop = current;
        document.documentElement.scrollTop = current;

        currentRocket += step;
        toTop.style.top = currentRocket + 'px';

    }, 5)
};