var guess = function () {
    $('#guess').submit(function () {
	$("#result").load("/guess", {
	    content: $("#paste-content").val()
	});
	return false;
    });
}();
