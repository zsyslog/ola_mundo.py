var xmlhttp = new XMLHttpRequest();

xmlhttp.onreadystatechange=function() {
  if (xmlhttp.readyState==4 && xmlhttp.status==200) {
  	console.log(xmlhttp)
  	var response = JSON.parse(xmlhttp.response)
  	console.log(response)
    document.getElementById("text").innerHTML=response.results.saludo;
  }
}

var update = function() {
	xmlhttp.open("GET","/salutation",true);
	xmlhttp.send();
}

document.getElementById('update_btn').addEventListener('click', update);

update();