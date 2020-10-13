<template>
  <main>
    <p class="desc">Download subtitles for movies and shows in your preferred language.</p>
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
import { Media } from '@/ts/media'

export default {
  components: {
    Search,
    SearchResults
  },
  setup() {
    const query = ref('')
    const mediaType = ref(Media.MOVIE)

    const updateQuery = (value: string) => {
      query.value = value
    }

    const updateType = (newType: Media) => {
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
  padding: 30px;
}

.desc {
  margin: 0 auto 2em auto;
  line-height: 1.5em;
  font-size: 1.3em;
  max-width: 30ch;
  text-align: center;
  color: #ddd;
}
</style>