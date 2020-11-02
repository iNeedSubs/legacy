<template>
  <div class="errBubble">
    <div class="msg">
      <TimesCircleIcon/>
      <p>{{msg}}</p>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import TimesCircleIcon from '@/assets/icons/TimesCircle.vue'

export default defineComponent({
  name: 'ErrBubble',
  components: {
    TimesCircleIcon
  },
  props: {
    msg: String
  }
})
</script>

<style lang="scss" scoped>
.errBubble {
  text-align: center;
}

.msg {
  display: inline-flex;
  align-items: center;
  background: #D63131;
  padding: .5em 1em;
  border-radius: 15px;
  text-align: left;

  svg {
    margin-right: 10px;
  }
}
</style>
