console.log(document.cookie);

let cookie = document.cookie + ";";
let correctCookie = cookie.match(/(session=.*;|; session=.*;$|; session=.*; )/);

if (correctCookie === null) {
 

    let a = document.createElement("a");
    a.setAttribute("class", "a6");
    let text = document.createTextNode("Login");
    a.appendChild(text);
    a.href = "https://lwu1822.github.io/fourWsFrontend/login";

    let div = document.createElement("div");
    div.setAttribute("class", "tooltip");
    div.appendChild(a);

    document.getElementById("loginStatus").appendChild(div);


    /*
    // show "Create Account" in navbar
    a = document.createElement("a");
    text = document.createTextNode("Create Account");
    a.appendChild(text);
    a.href = window.location.origin + "/createaccount";

    li = document.createElement("li");
    li.appendChild(a);

    document.getElementById("createAccount").appendChild(li);
    */

    // hide "profile" in navbar
    document.getElementById("profile").innerHTML = "";
    
} else {
    // show "Log Out" in navbar

    let a = document.createElement("a");
    a.setAttribute("class", "a6");
    let text = document.createTextNode("Log Out");
    a.appendChild(text);
    //a.href = window.location.origin + "/logout";
    a.href = "https://lwu1822.github.io/fourWsFrontend/logout";

    let div = document.createElement("div");
    div.setAttribute("class", "tooltip");
    div.appendChild(a);

    document.getElementById("loginStatus").appendChild(div);


    
    // show "Profile" in navbar
    a = document.createElement("a");
    a.setAttribute("class", "a5");
    text = document.createTextNode("Profile");
    a.appendChild(text);
    // a.href = window.location.origin + "/profile";
    a.href = "https://lwu1822.github.io/fourWsFrontend/profile";


    div = document.createElement("div");
    div.setAttribute("class", "bottom");
    text = document.createTextNode("Get a list of recommendations based on your data");
    div.appendChild(text);


    document.getElementById("profile").appendChild(a);
    document.getElementById("profile").appendChild(div);

    /*
    // hide "Create Account" in navbar
    document.getElementById("createAccount").innerHTML = "";
    */
}

