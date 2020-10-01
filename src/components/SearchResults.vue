<template>
  <transition name="fall">
    <Load v-if="loading"/>
  </transition>
  <transition name="bounceIn">
    <div class="searchResults" v-if="showResults">
      <h3>Results ({{results.length}})</h3>
      <p v-if="err.length > 1">Error: {{err}}</p>
      <p v-if="results.length === 0">Nothing has been found with that name.</p>
      <div class="results">
        <div v-for="(result, i) in results" :key="i" class="result">
          <img v-if="result.key_visual" :src="result.key_visual"/>
          <div class="noImage" v-else/>
          <p>{{result.title}}</p>
        </div>
      </div>
    </div>
  </transition>
</template>

<script lang="ts">
import { defineComponent, ref, watch } from 'vue'
import { Movie } from '@/ts/movies'
import Load from './Load.vue'

export default defineComponent({
  name: 'SearchResults',
  components: {
    Load
  },
  props: {
    query: String
  },
  setup(props) {
    const results = ref<Movie[]>([])
    const showResults = ref(false)
    const loading = ref(false)
    const loaded = ref(false)
    const err = ref('')

    const fetchQuery = async (query: string) => {
      results.value = []
      showResults.value = false
      loading.value = true
      loaded.value = false

      try {
        const req = await fetch(`/api/v1/search/movie/?query=${query}`)

        if (req.status !== 200) {
          return console.error('err', req)
        }

        const payload = await req.json() as Movie[]

        results.value = payload
        showResults.value = true
        loading.value = false
        loaded.value = true
      } catch (e) {
        err.value = e
      }
    }

    watch(() => props.query, (query) => {
      if (!query) {
        results.value = []
        showResults.value = false

        return
      }

      fetchQuery(query)
    })

    return {
      results,
      showResults,
      loading,
      loaded,
      err
    }
  }
})
</script>

<style lang="scss" scoped>
.load {
  right: 0;
  left: calc(50% - 40px);
  position: absolute;
  text-align: center;
  margin-top: 1em;
  z-index: -1;
}

.searchResults {
  margin-top: 2em;
}

h3 {
  margin-bottom: 1em;
}

.results {
  display: grid;
  gap: 1em;

  .result {
    background: #2C343F;
    border-radius: 5px;
    text-align: center;
    cursor: pointer;

    &:hover img {
      filter: brightness(1);
    }
  }
}

img {
  border-radius: 5px;
  width: 100%;
  filter: brightness(.8);
  transition: filter .2s ease-in-out;
}

.noImage {
  border-radius: 5px 0 0 5px;
  width: 101px;
  height: 150px;
  background: #2C343F;
  border-right: solid 1px #1b232e;
}

@media only screen and (min-width: 350px) {
  .results {
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  }

  .result {
    display: grid;
    grid-template-columns: auto 1fr;
    align-items: center;
    gap: 15px;
    text-align: left !important;
    padding-right: 1em;
  }
  img {
    width: auto;
    height: 150px;
  }
}
</style>