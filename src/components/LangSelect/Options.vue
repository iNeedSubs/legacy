<template>
  <div class="options" v-if="showOptions">
    <div class="languages">
      <p
        v-for="(langName, langCode, i) in languages"
        :ref="e => {options[i] = e}"
        :key="langName"
        :class="{active: code.toUpperCase() === langCode.toUpperCase()}"
        @click="setLang(langCode)"
        @keydown="e => { if (e.keyCode === 13) { setLang(langCode)} }"
        tabindex="0"
      >
        {{langName}}
      </p>
    </div>
  </div>
</template>

<script lang="ts">
import { computed, defineComponent, onBeforeUpdate, onMounted, onUnmounted, ref, watch } from 'vue'
import { LangName, LangCode } from '@/ts/languages'

export default defineComponent({
  name: 'LangSelectOptions',
  emits: [
    'update-lang',
    'update-menu-visibility'
  ],
  props: {
    showOptions: Boolean,
    availableLangs: Array
  },
  setup(props, { emit }) {
    const preferredLangCode = localStorage.preferredLangCode as LangCode
    const code = ref(preferredLangCode || LangCode.ENGLISH)
    const searchLang = ref('')
    const options = ref<Array<HTMLParagraphElement>>([])

    const setLang = (newCode: LangCode) => {
      code.value = newCode
      emit('update-lang', newCode)
      emit('update-menu-visibility', false)
    }

    const handleKbrd = (e: KeyboardEvent) => {
      // close on escape
      if (e.keyCode === 27) {
        emit('update-menu-visibility', false)
        return
      }

      if (!props.showOptions || e.key.length > 1) return

      const onlyLetters = /[a-zA-Z]/g
      if (!onlyLetters.test(e.key)) return

      searchLang.value += e.key
    }

    // reset the resultItems before each update
    onBeforeUpdate(() => {
      options.value = []
    })

    onMounted(() => {
      window.addEventListener('keydown', handleKbrd)
    })

    onUnmounted(() => {
      window.removeEventListener('keydown', handleKbrd)
    })

    watch(() => searchLang.value, (value) => {
      const filteredLanguages = options.value.filter(e => {
        const langText = e.childNodes[0].textContent?.toLowerCase()
        const enteredValue = value.toLowerCase()

        return langText?.includes(enteredValue)
      })

      filteredLanguages[0]?.scrollIntoView({
        behavior: 'smooth'
      })

      filteredLanguages[0]?.focus()
    })

    watch(() => props.showOptions, () => {
      searchLang.value = ''
    })

    // TODO: written with intent to work, needs to be polished and re-written
    const availableLangs = computed(() => {
      if (!props.availableLangs) return;

      const langs: {[x: string]: LangName} = {}

      for (const lang of props.availableLangs) {
        const code = (lang as LangCode).toUpperCase()

        langs[code] = LangName[code as keyof typeof LangName]
      }

      return langs
    })

    return {
      code,
      setLang,
      languages: availableLangs.value || LangName,
      options
    }
  }
})
</script>

<style lang="scss" scoped>
.options {
  background: #51555c;
  overflow: hidden;
  margin: 0 auto;
  top: calc(100% + 15px);
  height: 150px;
  right: 0;
  left: 0;
  position: absolute;
  border-radius: 15px;
  z-index: 2;

  .languages {
    white-space: nowrap;
    overflow-y: auto;
    height: inherit;
    width: inherit;
    scrollbar-color: #de7b5a #333942;
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

    &:hover, &:focus {
      background: #6d707622;
    }

    &.active {
      background: #6d7076;
    }
  }
}
</style>