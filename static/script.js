function showOverlay() {
  overlay=document.getElementById('loginOverlay');
  overlay.style.display='block';
}

function showSignUpOverlay(){
  signUpOverlay=document.getElementById('signUpOverlay');
  signUpOverlay.style.display='block';
}

function hideOverlay() {
  loginOverlay=document.getElementById('loginOverlay');
  loginOverlay.style.display='none';

  signUpOverlay=document.getElementById('signUpOverlay');
  signUpOverlay.style.display = 'none';
}

function logout(){
  window.location.href = '/logout';
}