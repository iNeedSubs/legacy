<template>
  <button @click="toggleOptions" class="lang">{{name}} <fa icon="angle-down"/></button>
  <div class="options" v-if="showOptions">
    <p
      v-for="(langName, langCode) in languages"
      :key="langName"
      :class="{active: code === langCode.toUpperCase()}"
      @click="setLang(langCode)"
    >
      {{langName}}
    </p>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import { LangName, LangCode } from '../ts/languages'

export default defineComponent({
  name: 'LangSelect',
  emits: ['update-lang'],
  setup(props, { emit }) {
    const code = ref(LangCode.ENGLISH)
    const name = ref(LangName.ENG)
    const showOptions = ref(false)

    const setLang = (newCode: LangCode) => {
      code.value = newCode

      const newName = newCode.toUpperCase() as keyof typeof LangName
      name.value = LangName[newName]

      emit('update-lang', newCode)
    };

    const toggleOptions = () => showOptions.value = !showOptions.value

    return {
      name,
      code,
      setLang,
      languages: LangName,
      showOptions,
      toggleOptions
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
  border-radius: 0 0 5px 5px;

  &:hover {
    background: #6d707622;
  }

  &.active {
    background: #d65a31;
  }

  &:not(.active) {
    color: #ddd;
  }
}

.options {
  height: 150px;
  overflow-y: auto;
  white-space: nowrap;
  top: calc(100% + 15px);
  right: 0;
  left: 0;
  position: absolute;
  background: #51555c;
  border-radius: 5px;
}

p {
  cursor: pointer;
  padding: 0 1em;
  white-space: nowrap;
  display: flex;
  align-items: center;
  width: 100%;
  height: 30px;
  transition: background .1s ease-in-out;

  &:hover {
    background: #6d707622;
  }

  &.active {
    background: #6d7076;
  }
}

@media only screen and (min-width: 500px) {
  button {
    box-shadow: none;
    border-radius: 0 0 5px 0;
  }
}
</style>