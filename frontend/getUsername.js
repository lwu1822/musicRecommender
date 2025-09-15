async function fetchUsername() {
    // retrieve cookie's value
    console.log(document.cookie);

    let cookie2 = document.cookie + ";";
    let correctCookie2 = cookie2.match(/(session=.*;|; session=.*;$|; session=.*; )/);
    correctCookie2 = correctCookie2[0].replace(/;/g, '');
    correctCookie2 = correctCookie2.replace('session=', '');
    correctCookie2 = correctCookie2.replace(/ /g, '');
    console.log(correctCookie2);

    // send fetch to backend's endpoint for user info
    var baseurl = "https://fourws.duckdns.org/api/users/info";
    
    const body = {
        token: correctCookie2,
    };

    // Set Headers to support cross origin
    //IMPORTANT!!!!!!! TO SUCCESSFULLY POST, YOU NEED TO REMOVE
    // credentials:'include'
    const requestOptions = {
        method: 'POST',
        mode: 'cors', // no-cors, *cors, same-origin
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        //credentials: 'include', // include, *same-origin, omit
        body: JSON.stringify(body),
        headers: {
            "content-type": "application/json"
        },
    };

    let response = await fetch(baseurl, requestOptions)

    if (!response["ok"]) {
        window.location.href = window.location.origin + "/logout";
    }

    let data = await response.json();
    return data; 

}



async function fetchUsernameOnly() {
    let data = await fetchUsername();
    return data["sub"];
}

async function showUsername() {
    let data = await fetchUsername();

    // debugging
    console.log(data);


    let p = document.createElement("p");
    p.setAttribute("class", "inline");
    let text = document.createTextNode(data["sub"]);
    p.appendChild(text);
    document.getElementById("username").appendChild(p);
}



