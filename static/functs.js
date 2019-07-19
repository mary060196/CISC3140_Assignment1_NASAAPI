function focusOnTheTextbox() 
{
 document.getElementById("API_KEY").focus();
}

function displayYear()
{
     document.getElementById("year").innerHTML = (new Date()).getFullYear();
}