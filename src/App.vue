<script>
export default {
  name: 'App'
}
</script>

<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<style>
@font-face {
  font-family: Rubik;
  src: url("assets/fonts/rubik_bold.ttf");
}

@font-face {
  font-family: Source Sans Pro SemiBold;
  src: url("assets/fonts/source_sans_pro_semi_bold.ttf");
}

@font-face {
  font-family: Source Sans Pro Regular;
  src: url("assets/fonts/source_sans_pro_regular.ttf");
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
  font-family: Source Sans Pro Regular;
  background: #222831;
  color: #fff;
}
</style>
