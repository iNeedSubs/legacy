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
        <div
          class="result"
          :ref="e => {resultItems[i] = e}"
            v-for="(result, i) in results"
          :key="i"
        >
          <router-link :to="{ name: mediaType, params: { id: result.imdb_id }}">
            <img class="poster" v-if="result.poster" :src="result.poster" loading="lazy"/>
            <div class="noImage" v-else/>
            <div class="name">
              <img class="banner" v-if="result.banner" :src="result.banner" loading="lazy"/>
              <p>{{result.title}}</p>
            </div>
          </router-link>
        </div>
      </div>
    </div>
  </transition>
</template>

<script lang="ts">
import { defineComponent, ref, watch, nextTick, onBeforeUpdate } from 'vue'
import { Movie } from '@/ts/media'
import Load from './Load.vue'

export default defineComponent({
  name: 'SearchResults',
  components: {
    Load
  },
  props: {
    query: String,
    mediaType: String
  },
  setup(props) {
    const results = ref<Movie[]>([])
    const showResults = ref(false)
    const loading = ref(false)
    const loaded = ref(false)
    const err = ref('')
    const resultItems = ref<Array<HTMLDivElement>>([])

    // reset the resultItems before each update
    onBeforeUpdate(() => {
      resultItems.value = []
    })

    const fetchQuery = async (query: string, mediaType: string) => {
      results.value = []
      showResults.value = false
      loading.value = true
      loaded.value = false

      try {
        const req = await fetch(`/api/v1/search/${mediaType}?query=${query}`)

        if (req.status !== 200) {
          return console.error('err', req)
        }

        const payload = await req.json() as Movie[]

        results.value = payload
        showResults.value = true
        loading.value = false
        loaded.value = true

        await nextTick()

        // scrolls to first element in results
        resultItems.value[0].scrollIntoView({
          block: 'center'
        })
      } catch (e) {
        err.value = e
      }
    }

    watch(() => [props.query, props.mediaType], ([query, mediaType]) => {
      if (!query || !mediaType) {
        results.value = []
        showResults.value = false

        return
      }

      fetchQuery(query, mediaType)
    })

    return {
      results,
      showResults,
      loading,
      loaded,
      err,
      resultItems
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

  .result a {
    background: #2C343F;
    border-radius: 5px;
    text-align: center;
    cursor: pointer;
    display: grid;
    grid-template-rows: 1fr auto;

    &:hover img {
      filter: brightness(1);
    }

    .name {
      height: 100%;
      position: relative;

      .banner {
        position: absolute;
        height: 100%;
        top: 0;
        left: 0;
        right: 0;
        width: 100%;
        border-radius: 5px;
        object-fit: cover;
        opacity: .1;
      }

      p {
        padding: 1em;
        z-index: 1;
      }
    }

  }
}

.poster {
  border-radius: 5px;
  width: 100px;
  object-fit: cover;
  filter: brightness(.8);
  transition: filter .2s ease-in-out;
}

.noImage {
  border-radius: 5px;
  background: #3D454F;
  width: 100%;
  height: 411px;
}

@media only screen and (min-width: 350px) {
  .results {
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  }

  .result a {
    display: grid;
    grid-template-columns: auto 1fr;
    grid-template-rows: 1fr !important;
    align-items: center;
    text-align: left !important;

    .name {
      display: flex;
      align-items: center;

      p {
        padding: 0 1em;
      }
    }
  }

  img {
    width: auto;
    height: 150px;
  }

  .noImage {
    border-radius: 5px 0 0 5px;
    height: 150px;
    width: 100px;
  }
}
</style>