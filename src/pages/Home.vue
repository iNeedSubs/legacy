<template>
  <div>
    <Header/>
    <main>
      <p class="desc">Download subtitles for Movies, TV Shows and Anime in your preferred language.</p>
      <Search/>
    </main>
  </div>
</template>

<style scoped>
main {
  margin-top: 1em;
  padding: 30px;
}

.desc {
  margin-bottom: 2em;
  font-size: 18px;
  text-align: center;
}
</style>

<script>
import Header from '../components/Header'
import Search from '../components/Search'

export default {
  components: {
    Header,
    Search
  }
}
</script>
