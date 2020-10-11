<template>
  <div ref="container" class="lang">
    <Button
      :name="name"
      :showOptions="showOptions"
      @update-menu-visibility="toggleOptions"
    />
    <transition name="bounceIn">
      <Options
        :showOptions="showOptions"
        @update-lang="updateLang"
        @update-menu-visibility="toggleOptions"
      />
    </transition>
  </div>
</template>

<script lang="ts">
import { defineComponent, onMounted, onUnmounted, ref } from 'vue'
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
    const container = ref<HTMLDivElement>()

    // close language options if clicked outside menu
    const handleClick = (e: MouseEvent) => {
      const targetNode = e.target as Node

      if (targetNode.nodeName === "BUTTON" || !showOptions.value) return

      if (!container.value?.contains(targetNode)) {
        showOptions.value = false
      }
    }

    onMounted(() => {
      window.addEventListener('click', handleClick)
    })

    onUnmounted(() => {
      window.removeEventListener('click', handleClick)
    })

    const toggleOptions = (newState: boolean) => showOptions.value = newState

    const updateLang = (newCode: LangCode) => {
      const newName = newCode.toUpperCase() as keyof typeof LangName
      name.value = LangName[newName]
    }

    return {
      container,
      name,
      languages: LangName,
      showOptions,
      toggleOptions,
      updateLang,
    }
  }
})
</script>
