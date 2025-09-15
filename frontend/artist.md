---
layout: custom
---

<style>
  @import url('https://fonts.googleapis.com/css2?family=Dosis&display=swap');
</style>
<html>
<head>
    <title>Artist Recommendor</title>
</head>
<link rel="stylesheet" href="./index.min.css" />
<body>
<h1>Artist Recommendor</h1>


  <div class="as">
        <div class="tooltip">
        <a href="songrecinput.html" class="a1">Song</a>
        <div class="bottom">Input Songs</div>
        </div>
        <div class="tooltip">
        <a href="artist.html" class="a2">Artist</a>
        <div class="bottom">Input Artists</div>
        </div>
        <div class="tooltip">
        <a href="toptracks.html" class="a4">Top Tracks</a>
        <div class="bottom">Get a list of Top Tracks daily</div>
        </div>
        <div class="tooltip">
          <a href="chatgptapi.html" class="a4">Chat GPT</a>
          <div class="bottom">Ask Chat GPT for song recommendations</div>
        </div>
        <div class="tooltip" id="profile">
        </div>
        <span id="loginStatus"></span>
    </div>

<p>Enter three artists you like:</p>
    <p>Artist 1:</p>
    <input type="text" id="song1">
    <p>Artist 2:</p>
    <input type="text" id="song2">
    <p>Artist 3:</p>
    <input type="text" id="song3">
    <br>
    <br>
    <button onclick="songrec()">Recommend Songs!</button>
    <br>
    <br>
    <p>Recommended Songs:</p>
    <p id="rec"></p>
<!-- Include the JavaScript file -->

<script type="text/javascript" src="{{ site.baseurl }}/cookieCheck.js"></script>
<script>


</script>
</body>
</html>