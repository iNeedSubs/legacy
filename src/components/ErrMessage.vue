<template>
  <div v-if="msg" class="errMessage">
    <SadFace/>
    <p class="err">{{msg}}</p>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import SadFace from '@/assets/SadFace.vue'

export default defineComponent({
  name: 'ErrMessage',
  components: {
    SadFace
  },
  props: {
    visible: Boolean,
    msg: String
  }
})
</script>

<style lang="scss" scoped>
.errMessage {
  display: block;
  border-radius: 15px;
}

.err {
  margin: 2em auto 0 auto;
  text-align: center;
  max-width: 40ch;
}

</style>