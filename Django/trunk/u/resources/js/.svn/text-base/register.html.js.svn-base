$(document).ready(init);
$(window).resize(resize);
function resize() {
	var w=$(window).width()
	var h=$(window).height()
	// $('div#register_panel').width(0.4*w+"px")
// 	$('div#register_panel').height(0.8*h+"px")
// 	$('div#register_panel').css("top",0.1*h+"px")
}
function init() {
	resize()
	$("div#step_two").hide()
	function repeat_pwd() {
		if ($("input#rpwd").val()!=$("input#pwd").val()) {
			$("input#rpwd").parent().parent().addClass("error")
		} else {
			$("input#rpwd").parent().parent().removeClass("error")
		}
	}
	$("input#rpwd").keyup(repeat_pwd)
	$("input#pwd").keyup(repeat_pwd)
	
}