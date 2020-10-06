<template>
  <main>
    <div class="actions">
      <transition name="bounceIn">
        <h3 v-if="loaded">Results ({{subtitles.length}})</h3>
      </transition>
      <transition name="bounceIn">
        <p class="err" v-if="loaded && err">Error: {{err}}</p>
      </transition>
      <transition name="bounceIn">
        <p class="notice" v-if="!err && loaded && subtitles.length === 0">
          No subtitles have been found for this media.
        </p>
      </transition>
      <transition name="bounceIn">
        <div v-if="!err && loaded && subtitles.length > 0" class="buttonContainer">
          <LangSelect/>
        </div>
      </transition>
      <transition name="fall">
        <Load v-if="loading"/>
      </transition>
    </div>
    <transition name="bounceIn">
      <div class="subtitles" v-if="subtitles.length > 0">
        <div class="subtitle" v-for="(subtitle, i) in subtitles" :key="i">
          <p>{{subtitle.name}}</p>
          <a class="download" :href="subtitle.download_url" download>
            <fa icon="download"/>
          </a>
        </div>
      </div>
    </transition>
  </main>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import { useRoute } from 'vue-router';
import { MovieSubtitle } from '@/ts/media';
import LangSelect from '@/components/LangSelect/Index.vue'
import Load from '@/components/Load.vue'

export default defineComponent({
  name: 'Movie',
  components: {
    LangSelect,
    Load
  },
  setup() {
    const route = useRoute()
    const loaded = ref(false)
    const loading = ref(true)
    const err = ref('')
    const subtitles = ref<Array<MovieSubtitle>>([])

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

        console.log(payload);

        subtitles.value = payload
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
      subtitles,
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
  margin-bottom: 2em;
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

.subtitles {
  display: grid;
  gap: 1em;
}

.subtitle {
  padding: 1em;
  border-radius: 5px;
  background: #2C343F;
  display: grid;
  grid-template-columns: 1fr auto;
  align-items: center;
  gap: 1em;

  .download {
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 5px;
    background: #D65A31;
    height: 40px;
    width: 40px;
    text-align: center;
    transition: .2s ease-in-out;
    transition-property: opacity, background, transform;

    &:active {
      transform: scale(.9);
    }

    &:hover {
      background: #de7b5a;
    }
  }

  p {
    word-break: break-all;
  }
}

@media only screen and (min-width: 500px) {
  .actions {
    width: 200px;
  }
}

</style>
