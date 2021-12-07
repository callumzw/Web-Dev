function countdown(){
	var endDate = new Date("Dec 25, 2021 00:00:00").getTime();
	var x = setInterval(function() {
		var now = new Date().getTime();
		var distance = endDate - now;

		var days = Math.floor(distance / (1000 * 60 * 60 * 24));
		var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
		var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
		var seconds = Math.floor((distance % (1000 * 60)) / 1000);
		document.getElementById("clock").innerHTML = days + "d " + hours + "h " + minutes = "m " + seconds + "s";
		
		var d = new Date(); 
		if (d.getMonth() == 11 && d.getDate() == 24){
			clearInterval(x)
			document.getElementByID("clock").innerHTML = "Christmas Eve"
		}
		else if ( d.getMonth() == 11 && d.getDate == 25) {
			clearInterval(x);
			document.getElementByID("clock").innerHTML = "Christmas Day"
		}
		else if (distance < 0){
			clearInterval(x)
			document.getElementByID("clock").innerHTML = "See you next year!"
		}
	}
}

}
