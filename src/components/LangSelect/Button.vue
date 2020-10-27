<template>
  <button aria-label="Download Subtitle File" @click="toggleOptions" class="lang">
    {{name}}
    <ChevronDownIcon
      class="downIcon"
      :class="{active: showOptions}"
    />
  </button>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import ChevronDownIcon from '@/assets/icons/ChevronDown.vue'

export default defineComponent({
  name: 'LangSelectButton',
  emits: ['update-menu-visibility'],
  components: {
    ChevronDownIcon
  },
  props: {
      name: String,
      showOptions: Boolean
  },
  setup(props, { emit }) {
    const toggleOptions = () => {
      emit('update-menu-visibility', !props.showOptions)
    }

    return {
      toggleOptions,
    }
  }
})
</script>

<style lang="scss" scoped>
button {
  border: none;
  cursor: pointer;
  outline: none;
  background: #494d54;
  padding: .5em 1em;
  color: #fff;
  font-family: 'Open Sans Bold';
  font-size: 18px;
  transition: .1s ease-in-out;
  transition-property: background, color;
  width: 100%;
  box-shadow: 0px -1px 15px #22283155;
  border-radius: 0 0 15px 15px;

  &:hover, &:focus {
    background: #6d707622;
  }

  &:not(.active) {
    color: #ddd;
  }
}

.downIcon {
  transition: transform .4s cubic-bezier(0.2, 0.8, 0.3, 1.3);

  &.active {
    transform: rotate(-180deg);
  }
}

@media only screen and (min-width: 500px) {
  button {
    box-shadow: none;
    border-radius: 0 0 15px 0;
  }
}
</style>