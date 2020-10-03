<template>
  <button @click="toggleOptions" class="lang">
    {{name}}
    <fa
      class="downIcon"
      :class="{active: showOptions}"
      icon="angle-down"
    />
  </button>
  <transition name="bounceIn">
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
  </transition>
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

.downIcon {
  transition: transform .4s cubic-bezier(0.2, 0.8, 0.3, 1.3);

  &.active {
    transform: rotate(-180deg);
  }
}

@media only screen and (min-width: 500px) {
  button {
    box-shadow: none;
    border-radius: 0 0 5px 0;
  }
}
</style>