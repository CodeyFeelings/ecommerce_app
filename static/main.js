// SECTION: FLASH MESSAGE
window.addEventListener("load", function () {
  const flashMessage = document.getElementById("flash-message");
  if (flashMessage) {
    setTimeout(function () {
      flashMessage.style.display = "none";
    }, 4000);
  }
});

// SECTION: SHOW OVERLAY
function displayOverlay(overlayId, itemId = null) {
  if (itemId) {
    const overlay = document.getElementById(overlayId + itemId);
    overlay.style.display = "flex";
  } else {
    const overlay = document.getElementById(overlayId);
    overlay.style.display = "flex";
  }
}
// SECTION: HIDE OVERLAY
function hideOverlay(overlayId, itemId = null) {
  if (itemId) {
    const overlay = document.getElementById(overlayId + itemId);
    overlay.style.display = "none";
  } else {
    const overlay = document.getElementById(overlayId);
    overlay.style.display = "none";
  }
}

function closeOverlay(event){
    if (event.target.classList.contains('overlay')){
        event.target.style.display = 'none';
    }
}

// SECTION: REGISTER
document.querySelectorAll(".input-form").forEach(form =>{
  form.addEventListener("submit", function (event){
    event.preventDefault();
    const formData = new FormData(event.target)
    const actionUrl = form.getAttribute("action")
    fetch(actionUrl,{
      method: "POST",
      body: formData,
    }).then(response=> response.json())
    .then(data =>{
      console.log("Response data:", data); 
      if (data.success){
        window.location.href = data.redirect_url;
      }else{
        displayFlashMessage(data.message, "error");
      }
    })
    .catch(error=> console.error("Error:",error));
})
})

function displayFlashMessage(message,category){
  const flashMessage = document.getElementById("flash-message");
  flashMessage.className = "flash-message";
  flashMessage.innerText = message;
  flashMessage.classList.add(category)
  flashMessage.style.display = "block";
  
  setTimeout(()=>{
    flashMessage.style.display = "none"
  },4000);

}
