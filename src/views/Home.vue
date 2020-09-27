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
  margin: 0 auto 2em auto;
  line-height: 1.5em;
  font-size: 1.3em;
  max-width: 40ch;
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
