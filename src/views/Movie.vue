<template>
  <main>
    <transition name="fall">
      <Load v-if="loading"/>
    </transition>
    <transition name="bounceIn">
      <Media v-if="loaded && !err" :data="movie"/>
    </transition>
    <transition name="bounceIn">
      <div v-if="loaded && !err" class="actions">
        <h3>Subtitles ({{movie.subtitles.length}})</h3>
        <div v-if="movie.subtitles.length > 0" class="buttonContainer">
          <LangSelect/>
        </div>
      </div>
    </transition>
    <transition name="bounceIn">
      <p class="err" v-if="loaded && err">Error: {{err}}</p>
    </transition>
    <transition name="bounceIn">
      <p class="notice" v-if="loaded && !err && movie.subtitles.length === 0">
        No subtitles have been found for this media.
      </p>
    </transition>
    <transition name="bounceIn">
      <Subtitles v-if="!err && loaded" :subtitles="movie.subtitles"/>
    </transition>
  </main>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import { useRoute } from 'vue-router';
import { MovieSubtitle } from '@/ts/media';
import LangSelect from '@/components/LangSelect/Index.vue'
import Load from '@/components/Load.vue'
import Media from '@/components/Media.vue'
import Subtitles from '@/components/Subtitles.vue'

export default defineComponent({
  name: 'Movie',
  components: {
    LangSelect,
    Load,
    Media,
    Subtitles
  },
  setup() {
    const route = useRoute()
    const loaded = ref(false)
    const loading = ref(true)
    const err = ref('')
    const movie = ref<MovieSubtitle>()

    const fetchSubtitles = async () => {
      loaded.value = false
      loading.value = true

      try {
        const req = await fetch(`/api/v1/search/subtitles?imdb_id=${route.params.id}`)
        const payload = await req.json()

        if (req.status !== 200) {
          loaded.value = true
          loading.value = false
          err.value = payload.detail || 'There has been an error searching for subtitles'
          return
        }

        movie.value = payload
        loaded.value = true
        loading.value = false
      } catch (e) {
        err.value = e
        loaded.value = true
        loading.value = false
      }
    }

    fetchSubtitles()

    return {
      movie,
      err,
      loaded,
      loading
    }
  }
})
</script>

<style lang="scss" scoped>
main {
  padding: 30px;
}

::v-deep {
  .media {
    margin: 0 auto;
    max-width: 500px;
    margin-bottom: 2em;
    cursor: default;

    .poster, .noImage {
      filter: brightness(1);
    }
  }
}

.load {
  right: 0;
  left: calc(50% - 40px);
  position: absolute;
  text-align: center;
  margin-top: 1em;
  z-index: -1;
}

.load {
  right: 0;
  left: calc(50% - 40px);
  position: absolute;
  text-align: center;
  margin-top: 1em;
  z-index: -1;
}

.err {
  width: 50ch;
}

.actions {
  position: relative;
  margin-bottom: 1em;
  width: 100%;

  h3 {
    margin-bottom: 1em;
  }

  .buttonContainer {
    border-radius: 5px;
    overflow: hidden;
    background: #494d54;
  }
}

@media only screen and (min-width: 500px) {
  .actions {
    display: flex;
    justify-content: space-between;
    align-items: center;

    h3 {
      margin-bottom: unset;
    }
  }

  ::v-deep .lang .options {
    width: 300px;
    left: unset;
  }
}
</style>
