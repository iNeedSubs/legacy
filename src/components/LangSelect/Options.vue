<template>
  <div class="options" v-if="showOptions">
    <p
      v-for="(langName, langCode) in languages"
      :key="langName"
      :class="{active: code.toUpperCase() === langCode.toUpperCase()}"
      @click="setLang(langCode)"
    >
      {{langName}}
    </p>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import { LangName, LangCode } from '@/ts/languages'

export default defineComponent({
  name: 'LangSelectOptions',
  emits: ['update-lang'],
  props: {
    showOptions: Boolean
  },
  setup(props, { emit }) {
    const code = ref(LangCode.ENGLISH)

    const setLang = (newCode: LangCode) => {
      code.value = newCode
      emit('update-lang', newCode)
    };

    return {
      code,
      setLang,
      languages: LangName
    }
  }
})
</script>

<style lang="scss" scoped>
.options {
  margin: 0 auto;
  height: 150px;
  overflow-y: auto;
  white-space: nowrap;
  top: calc(100% + 15px);
  right: 0;
  left: 0;
  position: absolute;
  background: #51555c;
  border-radius: 5px;
  scrollbar-color: #d65a31 #333942;
  z-index: 2;

  &::-webkit-scrollbar {
    &-track {
      border-radius: 0 5px 5px 0;
      background: #333942;
    }

    &-thumb {
      border-radius: 0 5px 5px 0;
      background: #d65a31;
    }
  }

  p {
    cursor: pointer;
    padding: 0 1em;
    white-space: nowrap;
    display: flex;
    align-items: center;
    width: 100%;
    height: 30px;
    transition: background .2s ease-in-out;

    &:hover {
      background: #6d707622;
    }

    &.active {
      background: #6d7076;
    }
  }
}
</style>