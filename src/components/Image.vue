<template>
  <img :class="name" v-if="src" :src="src" loading="lazy"/>
  <div class="noImage" v-else>
    <Logo/>
  </div>
</template>

<script lang="ts">
import Logo from "@/assets/Logo.vue"

export default {
  name: 'Image',
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
.noImage {
  display: flex;
  justify-content: center;
  align-items: center;

  svg {
    width: 3em;
  }
}
</style>