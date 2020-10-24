<template>
  <div class="sadFace">
    <Glasses/>
    <SadMouth/>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import Glasses from './Glasses.vue'
import SadMouth from './SadMouth.vue'

export default defineComponent({
  name: 'SadFace',
  components: {
    Glasses,
    SadMouth
  }
})
</script>

<style lang="scss" scoped>
.sadFace {
  text-align: center;
}

.sadMouth {
  margin-top: 2em;
}
</style>
