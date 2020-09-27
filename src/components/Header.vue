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

<style scoped>
header {
  background: #d65a31;
  padding: 30px;
  text-align: center;
}

h1 {
  font-size: 3.5em;
  margin-bottom: .5em;
  font-family: Rubik;
}
</style>
