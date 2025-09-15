console.log(document.cookie);

let cookie2 = document.cookie + ";";
let correctCookie2 = cookie2.match(/(session=.*;|; session=.*;$|; session=.*; )/);