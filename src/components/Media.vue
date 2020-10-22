<template>
  <div class="media">
    <Poster name="poster" :src="data.poster"/>
    <div class="name">
      <img
        class="banner"
        v-if="data.banner"
        :src="data.banner"
        loading="lazy"
      />
      <p>{{data.title}}</p>
    </div>
  </div>
</template>

<script lang="ts">
import Poster from './Poster.vue'

export default {
  name: 'Media',
  components: {
    Poster
  },
  props: {
    data: Object
  }
}
</script>

<style lang="scss" scoped>
.media {
  padding: .5em;
  background: #2C343F;
  border-radius: 15px;
  text-align: center;
  cursor: pointer;
  display: grid;
  min-height: 150px;
  grid-template-rows: 1fr auto;

  &:hover, &:focus {
    img, .noImage {
      filter: brightness(1);
    }
  }
}

.name {
  height: 100%;
  position: relative;
}

.banner {
  position: absolute;
  height: 100%;
  top: 0;
  left: 0;
  right: 0;
  width: 100%;
  border-radius: 15px;
  object-fit: cover;
  object-position: 0 80%;
  opacity: .1;
}

p {
  padding: 1em;
  z-index: 1;
}

@media only screen and (min-width: 350px) {
  .media {
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

    .banner {
      border-radius: 0 15px 15px 0;
    }
  }
}

</style>