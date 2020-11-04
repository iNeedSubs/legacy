<template>
  <main>
    <section>
      <h3>🎯 Our purpose</h3>
      <p>A lot of subtitle downloader websites out there are littered with advertisement and outdated user interfaces leading to a very poor user experience.</p>
      <p>We created <span class="highlight">Subtitles</span> to solve all those issues and provide a clean interface for you that you can enjoy both on desktop and mobile to download your subtitles without any distractions.</p>
    </section>
    <section>
      <h3>👍 Attributions</h3>
      <p>We would like to say thank you to <a href="https://www.opensubtitles.org/" target="_blank" rel="noopener">OpenSubtitles</a> for their awesome API, which we are using to get all the media data and subtitles uploaded by their community and that this project would've taken much longer to complete without them 😃.</p>
      <img src="@/assets/icons/OpenSubtitlesLogo.webp"/>
    </section>
  </main>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'About'
})
</script>

<style lang="scss" scoped>
main {
  display: grid;
  gap: 2em;
  justify-content: center;
  padding: 0 30px 30px 30px;
}

section {
  display: grid;
  gap: 1em;
}

h3 {
  font-family: 'Open Sans Bold', sans-serif;
}

p {
  max-width: 55ch;
  line-height: 1.5em;
}

img {
  background: #fff;
  border-radius: 15px;
  padding: 1em;
}

.highlight, a {
  padding: 0 5px;
  border-radius: 15px;
}

.highlight {
  background: #BC5938;
}

a {
  background: #dcf2b8;
  color: #222831;
}

@media only screen and (min-width: 800px) {
  main {
    padding: 30px;
  }
}
</style>
