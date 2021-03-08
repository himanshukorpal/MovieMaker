const mobileBtn = document.getElementById("mobile-cta");
nav = document.querySelector("nav");
mobileBtnExit = document.getElementById("mobile-exit");

mobileBtn.addEventListener("click", () => {
  nav.classList.add("menu-btn");
});

mobileBtnExit.addEventListener("click", () => {
  nav.classList.remove("menu-btn");
});

function loading() {
  $(".loader").show();
  let frm = document.getElementById("#form");
  frm.submit();
  frm.reset();

  return false;
  // document.getElementById("form").reset();
  // $("#content").prop("disabled", false);
}

function toggle() {
  document.querySelector(".trailer").remove();
  // window.location.href = "http://127.0.0.1:5000/";
  // let video = document.querySelector("video");
  // trailer.classList.toggle("active");
  // video.pause();
  // video.currentTime = 0;
}
