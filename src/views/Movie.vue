<template>
  <main>
    <transition name="fall">
      <Load v-if="mediaLoading"/>
    </transition>
    <transition name="bounceIn">
      <Media v-if="mediaLoaded && !mediaErr" :data="mediaData"/>
    </transition>
    <transition name="bounceIn">
      <div v-if="subtitlesLoaded && !subtitlesErr" class="actions">
        <h3>Subtitles ({{subtitles.length}})</h3>
        <div class="buttonContainer">
          <LangSelect @update-lang="updateLang" :langs="availableLangs"/>
        </div>
      </div>
    </transition>
    <transition name="bounceIn">
      <ErrMessage :msg="subtitlesErr"/>
    </transition>
    <transition name="bounceIn">
      <p class="notice" v-if="subtitlesLoaded && !subtitlesErr && subtitles.length === 0">
        No {{preferredLangName}} subtitles have been found for this media.
      </p>
    </transition>
    <transition name="bounceIn">
      <Subtitles v-if="!subtitlesErr && subtitlesLoaded" :subtitles="subtitles"/>
    </transition>
  </main>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import { useRoute } from 'vue-router';
import { LangName, LangCode } from '@/ts/languages';
import { Error } from '@/ts/err';
import { MediaData, MediaSubtitles, Subtitle } from '@/ts/media';
import LangSelect from '@/components/LangSelect/Index.vue'
import Load from '@/components/Load.vue'
import Media from '@/components/Media.vue'
import Subtitles from '@/components/Subtitles.vue'
import ErrMessage from '@/components/ErrMessage.vue'

export default defineComponent({
  name: 'Movie',
  components: {
    LangSelect,
    Load,
    Media,
    Subtitles,
    ErrMessage
  },
  setup() {
    const route = useRoute()

    const mediaLoaded = ref(false)
    const mediaLoading = ref(false)
    const mediaErr = ref('')

    const availableLangs = ref<LangCode[]>()
    const subtitlesLoaded = ref(false)
    const subtitlesLoading = ref(false)
    const subtitlesErr = ref('')

    const mediaData = ref<MediaData>()
    const subtitles = ref<Subtitle[]>()

    const preferredLangName = ref(localStorage.preferredLangName as LangName || LangName.ENG)
    const preferredLangLangCode = ref(localStorage.preferredLangCode as LangCode || LangCode.ENGLISH)

    const fetchSubtitles = async () => {
      subtitlesLoaded.value = false
      subtitlesLoading.value = true
      subtitlesErr.value = ''

      const imdbID = `imdb_id=${route.params.id}`
      const langParam = preferredLangLangCode.value ? `&lang=${preferredLangLangCode.value.toLowerCase()}` : ''

      try {
        const cacheItemName = `imdb_id-${route.params.id}-lang-${preferredLangLangCode.value}`
        const cache = sessionStorage.getItem(cacheItemName)

        if (!cache) {
          const req = await fetch(`/api/v1/subtitles?${imdbID}${langParam}`)

          if (req.status !== 200) {
            const payload = await req.json() as Error

            subtitlesLoaded.value = true
            subtitlesLoading.value = false
            subtitlesErr.value = payload.detail
            return
          }

          const payload = await req.json() as MediaSubtitles

          subtitles.value = payload.subtitles
          availableLangs.value = payload.available_langs

          sessionStorage.setItem(cacheItemName, JSON.stringify(payload))
        } else {
          const payload = JSON.parse(cache) as MediaSubtitles

          subtitles.value = payload.subtitles
          availableLangs.value = payload.available_langs
        }
      } catch (e) {
        subtitlesErr.value = e
      } finally {
        subtitlesLoaded.value = true
        subtitlesLoading.value = false
      }
    }

    const fetchMediaData = async () => {
      mediaLoaded.value = false
      mediaLoading.value = true
      mediaErr.value = ''

      try {
        const cacheItemName = `imdb_id-${route.params.id}`
        const cache = sessionStorage.getItem(cacheItemName)

        if (!cache) {
          const req = await fetch(`/api/v1/media?imdb_id=${route.params.id}`)
          const payload = await req.json()

          if (req.status !== 200) {
            mediaLoaded.value = true
            mediaLoading.value = false
            mediaErr.value = payload.detail || 'There has been an error'
            return
          }

          mediaData.value = payload
        } else {
          mediaData.value = JSON.parse(cache)
        }

        fetchSubtitles()
      } catch (e) {
        mediaErr.value = e
      } finally {
        mediaLoaded.value = true
        mediaLoading.value = false
      }
    }

    fetchMediaData()

    const updateLang = async () => {
      preferredLangName.value = localStorage.preferredLangName as LangName || LangName.ENG
      preferredLangLangCode.value = localStorage.preferredLangCode as LangCode || LangCode.ENGLISH

      await fetchSubtitles()
    }

    return {
      subtitles,
      mediaData,
      mediaLoaded,
      mediaLoading,
      mediaErr,
      availableLangs,
      subtitlesLoaded,
      subtitlesLoading,
      subtitlesErr,
      preferredLangName,
      updateLang
    }
  }
})
</script>

<style lang="scss" scoped>
main {
  padding: 0 30px;
}

::v-deep(.media) {
  margin: 0 auto;
  max-width: 500px;
  margin-bottom: 2em;
  cursor: default;

  .poster, .noImage {
    filter: brightness(1);
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

.errMessage {
  margin-top: 4em;
}

.actions {
  position: relative;
  margin-bottom: 1em;
  width: 100%;

  h3 {
    margin-bottom: 1em;
  }

  .buttonContainer {
    border-radius: 15px;
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

  ::v-deep(.lang .options) {
    width: 300px;
    left: unset;
  }
}

@media only screen and (min-width: 800px) {
  main {
    padding: 30px;
  }
}
</style>
