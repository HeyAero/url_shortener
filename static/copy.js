let copyButton = document.getElementById('copy-button')

function handleCopy() {
  let copyLink = document.getElementById('url-link')
  copyLink.value = window.location.href + copyLink.value;
  copyLink.select()
  copyLink.setSelectionRange(0, 99999); /* For mobile devices */

  document.execCommand("copy");

  alert("Copied the link: " + copyLink.value);
}

copyButton.addEventListener('click', handleCopy)