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
  padding: 30px;
  text-align: center;
}

div {
  display: flex;
  flex-direction: column;
  align-items: center;

  svg {
    margin-bottom: 1em;
    height: 3em;
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

  div {
    flex-direction: row;
    gap: 1em;

    svg {
      margin-bottom: 0;
      width: 5em;
    }
  }

  h1 {
    margin-bottom: 0;
  }
}
</style>
