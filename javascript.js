
// USE THIS TO POST THE INFORMATION FROM THE FORM! MAKE SURE YOUR FORM IS ID'D CORRECTLY AND THE INPUT ELEMENTS HAVE THE CORRECT NAME
// NAME SHOULD BE data[column_name]
var form = document.getElementById("sheetdb-form");
form.addEventListener("submit", (e) => {
    fetch(form.action, {
    method: "POST",
    body: new FormData(document.getElementById("sheetdb-form"))
})
    .then((response) => response.json())
    .then((html) => {
      // you can put any JS code here
    });
});

url = ""
async function get_data () {

    const response = await fetch(url);
    const data = await response.json();
    
    document.getElementById("show_name").innerHTML = data[0].name;
    document.getElementById("show_msg").innerHTML = data[0].message;
    
}
    
get_data();