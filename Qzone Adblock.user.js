// ==UserScript==
// @name        Qzone Adblock
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       Su
// @match        https://user.qzone.qq.com/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';


    // feed流广告
    var feeds = document.getElementsByClassName("f-single f-s-s");
    feeds = [...feeds];
    feeds.map(e=>e.getElementsByClassName("f-single-top").length?e.remove():e);

    // 右侧广告
    document.getElementById("QM_Container_100005").remove();
    document.getElementById("QM_Container_100002").remove();

    // 左侧广告
    document.getElementById("QM_Container_100006").remove();

})();