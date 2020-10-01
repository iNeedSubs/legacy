<template>
  <div>
    <Header/>
    <main>
      <p class="desc">Download subtitles for Movies, TV Shows and Anime in your preferred&nbsp;language.</p>
      <Search @update-lang="updateLang" @update-query="updateQuery"/>
      <SearchResults :query="query"/>
    </main>
  </div>
</template>

<script lang="ts">
import { ref } from 'vue'
import Header from '@/components/Header.vue'
import Search from '@/components/Search.vue'
import SearchResults from '@/components/SearchResults.vue'
import { LangCode } from '@/ts/languages'

export default {
  components: {
    Header,
    Search,
    SearchResults
  },
  setup() {
    const query = ref('')
    const lang = ref(LangCode.ENGLISH)

    const updateQuery = (value: string) => {
      query.value = value
    }

    const updateLang = (newCode: LangCode) => {
      lang.value = newCode
    }

    return {
      updateQuery,
      updateLang,
      query
    }
  }
}
</script>

<style scoped>
main {
  padding: 30px;
}

.desc {
  margin: 0 auto 2em auto;
  line-height: 1.5em;
  font-size: 1.3em;
  max-width: 35ch;
  text-align: center;
  color: #ddd;
}
</style>