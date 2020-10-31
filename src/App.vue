<template>
  <Header/>
  <router-view v-slot="{Component}">
    <keep-alive include="Home">
      <component :is="Component"/>
    </keep-alive>
  </router-view>
</template>

<script lang="ts">
import Header from './components/Header.vue'

export default {
  components: {
    Header
  }
}
</script>

<style lang="scss">
@font-face {
  font-family: 'Open Sans Bold';
  font-display: swap;
  src: url("assets/fonts/open_sans_bold_subset.woff2");
}

@font-face {
  font-family: 'Open Sans Regular';
  font-display: swap;
  src: url("assets/fonts/open_sans_regular_subset.woff2");
}

::-webkit-scrollbar {
  width: 1em;

  &-track {
    background: #333942;
  }

  &-thumb {
    background: #BC5938;
  }
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  outline: none;
}

html {
  scroll-behavior: smooth;
}

html, body {
  height: 100%;
  width: 100%;
}

body {
  font-family: 'Open Sans Regular', sans-serif;
  background: #222831;
  color: #fff;
}

main {
  margin: 0 auto;
  position: relative;
  padding: 30px;
  max-width: 1600px;
}

a {
  text-decoration: none;
  color: #fff;
}

.icon {
  display: inline-block;
  font-size: inherit;
  height: 1em;
  overflow: visible;
  vertical-align: -.125em;
  width: 1em;
  fill: #ffffff;
}

.bounceIn {
  &-enter-active,
  &-leave-active {
    transition: .4s cubic-bezier(0.2, 0.8, 0.3, 1.3);
    transition-property: opacity, transform;
  }

  &-enter-to,
  &-leave-from {
    transform: scale(1);
  }

  &-enter-from,
  &-leave-to {
    transform: scale(.9);
    opacity: 0;
  }
}

.fall {
  &-enter-active,
  &-leave-active {
    transition: .4s cubic-bezier(0.2, 0.8, 0.3, 1.3);
    transition-property: opacity, transform;
  }

  &-enter-to,
  &-leave-from {
    transform: scale(1) translateY(0);
  }

  &-enter-from,
  &-leave-to {
    transform: scale(.9) translateY(-100%);
    opacity: 0;
  }
}
</style>
