<template>
  <img
    class="poster"
    v-if="src"
    :src="src"
    loading="lazy"
    alt="Media Poster"
  />
  <div class="noImage" v-else>
    <Logo/>
  </div>
</template>

<script lang="ts">
import Logo from "@/assets/Logo.vue"

export default {
  name: 'Poster',
  components: {
    Logo
  },
  props: {
    name: String,
    src: String
  }
}
</script>

<style lang="scss" scoped>
img.poster, .noImage {
  margin: 1em auto;
  border-radius: 15px;
  width: 100px;
  height: 150px;
  transition: filter .2s ease-in-out;
}

img.poster {
  object-fit: cover;
  filter: brightness(.8);
}

.noImage {
  display: flex;
  justify-content: center;
  align-items: center;

  svg {
    width: 3em;
  }
}

.noImage {
  background: #3D454F;
  filter: brightness(.9);
}

@media only screen and (min-width: 350px) {
  img.poster, .noImage {
    margin: unset;
    border-radius: 15px 0 0 15px;
  }
}

</style>