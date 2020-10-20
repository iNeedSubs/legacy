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
          <LangSelect @update-lang="updateLang"/>
        </div>
      </div>
    </transition>
    <transition name="bounceIn">
      <p class="err" v-if="subtitlesLoaded && subtitlesErr">Error: {{err}}</p>
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
import { MediaData } from '@/ts/media';
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

    const mediaLoaded = ref(false)
    const mediaLoading = ref(false)
    const mediaErr = ref('')

    const subtitlesLoaded = ref(false)
    const subtitlesLoading = ref(false)
    const subtitlesErr = ref('')

    const mediaData = ref<MediaData>()
    const subtitles = ref<MediaData>()

    const fetchMediaData = async () => {
      mediaLoaded.value = false
      mediaLoading.value = true
      mediaErr.value = ''

      try {
        const req = await fetch(`/api/v1/media?imdb_id=${route.params.id}`)
        const payload = await req.json()

        if (req.status !== 200) {
          mediaLoaded.value = true
          mediaLoading.value = false
          mediaErr.value = payload.detail || 'There has been an error'
          return
        }

        mediaLoaded.value = true
        mediaLoading.value = false
        mediaData.value = payload
      } catch (e) {
        mediaErr.value = e
        mediaLoaded.value = true
        mediaLoading.value = false
      }
    }

    const preferredLangName = ref(localStorage.preferredLangName as LangName || LangName.ENG)
    const preferredLangLangCode = ref(localStorage.preferredLangCode as LangCode || LangCode.ENGLISH)

    const fetchSubtitles = async () => {
      subtitlesLoaded.value = false
      subtitlesLoading.value = true
      subtitlesErr.value = ''

      const imdbID = `imdb_id=${route.params.id}`
      const langParam = preferredLangLangCode.value ? `&lang=${preferredLangLangCode.value.toLowerCase()}` : ''

      try {
        const req = await fetch(`/api/v1/subtitles?${imdbID}${langParam}`)
        const payload = await req.json()

        if (req.status !== 200) {
          subtitlesLoaded.value = true
          subtitlesLoading.value = false
          subtitlesErr.value = payload.detail || 'There has been an error'
          return
        }

        subtitles.value = payload.subtitles
        subtitlesLoaded.value = true
        subtitlesLoading.value = false
      } catch (e) {
        subtitlesErr.value = e
        subtitlesLoaded.value = true
        subtitlesLoading.value = false
      }
    }

    fetchMediaData()
    fetchSubtitles()

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
