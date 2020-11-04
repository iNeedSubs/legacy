<template>
  <transition name="fall">
    <Load v-if="loading"/>
  </transition>
  <transition name="bounceIn">
    <div class="searchResults" v-if="showResults && !err">
      <h3>Results ({{results.length}})</h3>
      <p v-if="err.length > 1">Error: {{err}}</p>
      <p v-if="results.length === 0">Nothing has been found with that name.</p>
      <div class="results">
        <div
          class="result"
          :ref="e => {resultItems[i] = e}"
          :key="i"
          v-for="(result, i) in results"
        >
          <router-link :to="{ name: mediaType, params: { id: result.imdb_id }}">
            <Media :data="result"/>
          </router-link>
        </div>
      </div>
    </div>
  </transition>
  <transition name="bounceIn">
    <ErrBubble v-if="err" :msg="err"/>
  </transition>
</template>

<script lang="ts">
import { defineComponent, ref, watch, nextTick, onBeforeUpdate } from 'vue'
import { MediaData } from '@/ts/media'
import Load from './Load.vue'
import Media from './Media.vue'
import ErrBubble from '@/components/ErrBubble.vue'
import { Error } from '@/ts/err'

export default defineComponent({
  name: 'SearchResults',
  components: {
    Load,
    Media,
    ErrBubble
  },
  props: {
    query: String,
    mediaType: String
  },
  setup(props) {
    const results = ref<MediaData[]>([])
    const showResults = ref(false)
    const loading = ref(false)
    const loaded = ref(false)
    const err = ref('')
    const resultItems = ref<Array<HTMLAnchorElement>>([])

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
        const cacheItemName = `mediaType-${mediaType}-query-${query}`
        const cache = sessionStorage.getItem(cacheItemName)

        if (!cache) {
          const req = await fetch(`/api/v1/search?type=${mediaType}&query=${query}`)

          if (req.status === 500) {
            err.value = 'Something went wrong with the server'
            return
          }

          if (req.status !== 200) {
            const payload = await req.json() as Error
            err.value = payload.detail

            return
          }

          const payload = await req.json() as MediaData[]

          sessionStorage.setItem(cacheItemName, JSON.stringify(payload))
          results.value = payload
        } else {
          results.value = JSON.parse(cache) as MediaData[]
        }

        showResults.value = true

        await nextTick()

        // scrolls to first element in results
        resultItems.value[0]?.scrollIntoView({
          block: 'center'
        })
      } catch (e) {
        err.value = e
      } finally {
        loading.value = false
        loaded.value = true
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

.errBubble {
  margin-top: 2em;
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
}

@media only screen and (min-width: 350px) {
  .results {
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  }
}
</style>