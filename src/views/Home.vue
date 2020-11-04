<template>
  <main>
    <p class="desc">Download subtitles for movies and shows in your preferred language</p>
    <Search
      @update-query="updateQuery"
      @update-type="updateType"
    />
    <SearchResults :query="query" :mediaType="mediaType"/>
  </main>
</template>

<script lang="ts">
import { ref } from 'vue'
import Search from '@/components/Search.vue'
import SearchResults from '@/components/SearchResults.vue'
import { MediaType } from '@/ts/media'

export default {
  name: 'Home',
  components: {
    Search,
    SearchResults
  },
  setup() {
    const query = ref('')
    const mediaType = ref(MediaType.MOVIE)

    const updateQuery = (value: string) => {
      query.value = value
    }

    const updateType = (newType: MediaType) => {
      mediaType.value = newType
    }

    return {
      updateQuery,
      updateType,
      query,
      mediaType
    }
  }
}
</script>

<style scoped>
main {
  padding: 0 30px 30px 30px;
}

.desc {
  margin: 0 auto 2em auto;
  line-height: 1.5em;
  font-size: clamp(1.1em, 4vw, 1.4em);
  max-width: 37ch;
  text-align: center;
  font-family: 'Open Sans Bold', sans-serif;
  color: #ddd;
}

@media only screen and (min-width: 800px) {
  main {
    padding: 30px;
  }
}
</style>