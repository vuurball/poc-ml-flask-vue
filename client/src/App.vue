<template>
  <div id="app">
    <router-view/>
  </div>
</template>
<style>
#app {
  margin-top:60px;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

.text-highlight {
    text-align: center;
    background-image: url('https://social-streams.com/wp-content/themes/Total/assets/images/highlight-left.png'),
    url('https://social-streams.com/wp-content/themes/Total/assets/images/highlight-center.png'),
    url('https://social-streams.com/wp-content/themes/Total/assets/images/highlight-right.png');
    background-repeat: repeat-x;
    background-repeat: no-repeat, repeat-x, no-repeat;
    background-position: center;
    background-position: left, center, right;
    background-clip: padding-box, content-box, padding-box;
    color: #a5651a;
    padding: 0 20px;
    margin: 0 -6px;
}

.pill {
    border: 1px solid #ddd;
    border-color: #9a5e9a;
    font-size: 16px;
    font-weight: 400;
    color: #9A5E9A;
    vertical-align: baseline;
    cursor: pointer;
    margin-right: 12px;
    margin-bottom: 12px;
    float: none;
    display: inline-block;
    margin: 0 5px 5px 0;
    padding: .2em 1em;
    font-family: "Montserrat";
    box-sizing: border-box;
    text-align: center;
    border-radius: 0;
}

.ff-header h1 {
    color: rgb(255, 255, 255);
    font-size: 50px;
    text-align: center;
    font-weight: normal;
    margin: 20px 20px 12px !important;
}

.ff-header h2 {
    color: rgb(255, 255, 255);
    font-size: 26px;
    text-align: center;
    font-weight: 300;
    margin: 12px 20px 20px !important;
    font-weight: 600;
}

.card{
  color: white;
  margin: 10px;
  background-color:rgb(92, 15, 78);
}

.card h5 {
  color:#9a5e9a;
}

.is-selected {
  background: #9a5e9a;
  color: #fff;
}

.img-thumbnail {
  max-width: 100px;
}
</style>
