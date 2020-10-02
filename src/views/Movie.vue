<template>
  <Header/>
  <main>
    <p v-if="err">Error: {{err}}</p>
    <div class="actions">
      <h3>Results ({{subtitles.length}})</h3>
      <div class="buttonContainer">
        <LangSelect/>
      </div>
    </div>
    <div class="subtitles">
      <div class="subtitle" v-for="(subtitle, i) in subtitles" :key="i">
        <p>{{subtitle.name}}</p>
        <a class="download" :href="subtitle.download_url" download>
          <fa icon="download"/>
        </a>
      </div>
    </div>
  </main>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import Header from '@/components/Header.vue'
import { useRoute } from 'vue-router';
import { MovieSubtitle } from '@/ts/media';
import LangSelect from '@/components/LangSelect.vue'

export default defineComponent({
  name: 'Movie',
  components: {
    Header,
    LangSelect
  },
  props: {
    id: String
  },
  setup() {
    const route = useRoute()
    const err = ref('')
    const subtitles = ref<Array<MovieSubtitle>>([])

    const fetchSubtitles = async () => {
      try {
        console.log(route.params.id)
        const req = await fetch(`/api/v1/search/subtitles/?imdb_id=${route.params.id}`)

        if (req.status !== 200) {
          err.value = 'There has been an error searching for subtitles'
          return
        }

        const payload = await req.json()
        console.log(payload)
        subtitles.value = payload
      } catch (e) {
        err.value = e
      }
    }

    fetchSubtitles()

    return {
      subtitles,
      err
    }
  }
})
</script>

<style lang="scss" scoped>
main {
  padding: 30px;
}

.actions {
  position: relative;
  margin-bottom: 2em;

  h3 {
    margin-bottom: 1em;
  }

  .buttonContainer {
    border-radius: 5px;
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

  p {
    word-break: break-all;
  }
}

.download {
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 5px;
  background: #D65A31;
  padding: 0 1em;
  height: 50px;
  width: 50px;
  text-align: center;
}
</style>
