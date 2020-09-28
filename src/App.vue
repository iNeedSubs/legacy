<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<style lang="scss">
@font-face {
  font-family: 'Open Sans Bold';
  src: url("assets/fonts/open_sans_bold.ttf");
}

@font-face {
  font-family: 'Open Sans Regular';
  src: url("assets/fonts/open_sans_regular.ttf");
}

@font-face {
  font-family: 'Open Sans Light';
  src: url("assets/fonts/open_sans_light.ttf");
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html, body, #app {
  height: 100%;
  width: 100%;
}

body {
  font-family: 'Open Sans Regular';
  background: #222831;
  color: #fff;
}

.icon {
  display: inline-block;
  font-size: inherit;
  height: 1em;
  overflow: visible;
  vertical-align: -.125em;
  width: 1em;
}
</style>
