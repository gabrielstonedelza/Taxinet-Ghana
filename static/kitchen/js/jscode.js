// var contact_button = document.getElementById("contact-address-button")
// var contact_details = document.getElementById("contact-details")

// contact_button.addEventListener("click", function () {
//     contact_details.style.display = "block"
//     console.log("hiiiiiiiiii")
// },false);

// contact_details.addEventListener("click", function () {
//     contact_details.style.display = "none"
// });
document.getElementById('contact-address-button').addEventListener('click', function() {
    var contactInfo = document.getElementById('contact-info');
    if (contactInfo.style.display === 'none') {
      contactInfo.style.display = 'block';
    } else {
      contactInfo.style.display = 'none';
    }
  });