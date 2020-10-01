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

::-webkit-scrollbar {
  width: 1em;

  &-track {
    border-radius: 5px;
    background: #333942;
  }

  &-thumb {
    border-radius: 5px;
    background: #d65a31;
  }
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
  }

  &-enter-from,
  &-leave-to {
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
  }

  &-enter-from,
  &-leave-to {
    opacity: 0;
  }
}
</style>
