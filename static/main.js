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