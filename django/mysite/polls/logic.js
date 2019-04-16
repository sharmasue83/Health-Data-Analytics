console.log("Test")

var xhr = new XMLHttpRequest();
var url = "url";
xhr.open("POST", url, true);
xhr.setRequestHeader("Content-type","application/json");
xhr.onreadystatechange = function () {
     if (xhr.readyState == 4 && xhr.status == 200) {
         // do something with response
         console.log(xhr.responseText);
     }
};
var dd = document.getElementById('country')
var data = JSON.stringify({'country': dd.option[dd.selectedIndex].text})
xhr.send(data);