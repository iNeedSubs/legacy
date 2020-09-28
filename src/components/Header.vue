<template>
  <header>
    <h1>Subtitles</h1>
    <Nav/>
  </header>
</template>

<script>
import Nav from './Nav'

export default {
  components: {
    Nav
  }
}
</script>

<style lang="scss" scoped>
header {
  background: #d65a31;
  padding: 30px;
  text-align: center;
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
