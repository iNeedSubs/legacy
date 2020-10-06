<template>
  <header>
    <div>
      <Logo/>
      <h1>Subtitles</h1>
    </div>
    <Nav/>
  </header>
</template>

<script lang="ts">
import Nav from './Nav.vue'
import Logo from '@/assets/Logo.vue'

export default {
  components: {
    Nav,
    Logo
  }
}
</script>

<style lang="scss" scoped>
header {
  background: #d65a31;
  padding: 30px;
  text-align: center;
}

div {
  display: flex;
  gap: 1em;
  align-items: center;

  svg {
    width: 5em;
  }
}

h1 {
  font-size: 3em;
  margin-bottom: .5em;
  font-family: 'Open Sans Bold';
}

@media only screen and (min-width: 800px) {
  header {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  h1 {
    margin-bottom: 0;
  }
}
</style>
