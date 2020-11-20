// '.tbl-content' consumed little space for vertical scrollbar, scrollbar width depend on browser/os/platfrom. Here calculate the scollbar width .
$(window).on("load resize ", function() {
    var scrollWidth = $('.tbl-content').width() - $('.tbl-content table').width();
    $('.tbl-header').css({'padding-right':scrollWidth});
  }).resize();



function load() {
  var accept = document.getElementsByClassName('accept')
  var decline = document.getElementsByClassName('decline')
  var decision = document.getElementsByClassName('decision')
  for (let i = 0;i<accept.length;i++) {
    accept[i].onclick = function() {
      decision[i].value = "accept";
    }
    
    decline[i].onclick = function() {
      decision[i].value = "decline";
    }
  }
}
