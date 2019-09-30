window.addEventListener("load", function() {
	var form = document.getElementById("file_uploader");
	form.addEventListener("submit", function(event) {
		event.preventDefault();
		addBook();
	});

	function addBook() {
		var xmlhttp = new XMLHttpRequest();
		var fd = new FormData(form);

		if (xmlhttp != null) {
			xmlhttp.open('POST', 'add_book', true);
			
			xmlhttp.onreadystatechange = function() {
				if (xmlhttp.readyState === 4) {
					if (this.status == 200) {
						alert("Book saved");
					} else {
						alert("Something went wrong!\nPlease try again!");
					}
				}
			}

			xmlhttp.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
			message = "";
			fd.forEach(function(value, key){
			   message += key + '=' +  value + '&';
			});
			xmlhttp.send(message);
		}
	}
});