<template>
  <div class="subtitles" v-if="subtitles.length > 0">
    <div class="subtitle" v-for="(subtitle, i) in subtitles" :key="i">
      <p>{{subtitle.file_name}}</p>
      <a class="download" :href="subtitle.download_url" download>
        <DownloadIcon/>
      </a>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import DownloadIcon from '@/assets/icons/Download.vue'

export default defineComponent({
  name: 'Subtitles',
  components: {
    DownloadIcon
  },
  props: {
    subtitles: Array
  }
})
</script>

<style lang="scss" scoped>
.subtitles {
  display: grid;
  gap: 1em;
}

.subtitle {
  padding: 1em;
  border-radius: 15px;
  background: #2C343F;
  display: grid;
  grid-template-columns: 1fr auto;
  align-items: center;
  gap: 1em;

  .download {
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 15px;
    background: #BC5938;
    height: 40px;
    width: 40px;
    text-align: center;
    transition: .2s ease-in-out;
    transition-property: opacity, background, transform;

    &:active {
      transform: scale(.9);
    }

    &:hover, &:focus {
      background: #D44206;
    }
  }

  p {
    word-break: break-all;
  }
}

@media only screen and (min-width: 500px) {
  .subtitles {
    grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
  }
}
</style>