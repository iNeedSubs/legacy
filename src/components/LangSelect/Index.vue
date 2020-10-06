<template>
  <Button
    :name="name"
    :showOptions="showOptions"
    @update-menu-visibility="toggleOptions"
  />
  <transition name="bounceIn">
    <Options
      :showOptions="showOptions"
      @update-lang="updateLang"
    />
  </transition>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import { LangCode, LangName } from '@/ts/languages'
import Button from './Button.vue'
import Options from './Options.vue'

export default defineComponent({
  name: 'LangSelect',
  emits: ['update-lang'],
  components: {
    Button,
    Options
  },
  setup() {
    const name = ref(LangName.ENG)
    const showOptions = ref(false)

    const toggleOptions = () => showOptions.value = !showOptions.value

    const updateLang = (newCode: LangCode) => {
      const newName = newCode.toUpperCase() as keyof typeof LangName
      name.value = LangName[newName]
    }

    return {
      name,
      languages: LangName,
      showOptions,
      toggleOptions,
      updateLang
    }
  }
})
</script>
