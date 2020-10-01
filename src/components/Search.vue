<template>
  <div class="glasses">
    <Glasses/>
  </div>
  <div class="search">
    <div class="inputContainer">
      <input placeholder="Search" v-model="query" v-on:keyup.enter="search"/>
      <button @click="search">
        <fa icon="search"/>
      </button>
    </div>
    <div class="filters">
      <div class="types">
        <button
          class="movie"
          v-bind:class="{active: filter === Media.MOVIE}"
          @click="setFilter(Media.MOVIE)"
        >Movie</button>
        <button
          class="show"
          v-bind:class="{active: filter === Media.SHOW}"
          @click="setFilter(Media.SHOW)"
        >TV Show</button>
      </div>
      <div class="lang">
        <LangSelect @update-lang="updateLang"/>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import Glasses from '@/assets/Glasses.vue'
import LangSelect from './LangSelect.vue'
import { LangCode } from '@/ts/languages'
import { Media } from '@/ts/media'

enum Types {
  MOVIE = 'movie',
  TV_SHOW = 'tvShow'
}

export default defineComponent({
  components: {
    Glasses,
    LangSelect
  },
  emits: [
    'update-lang',
    'update-query'
  ],
  setup(props, { emit }) {
    const query = ref('')
    const filter = ref(Media.MOVIE)

    const search = () => emit('update-query', query.value)
    const setFilter = (type: Types) => filter.value = type

    const updateLang = (payload: LangCode) => {
      emit('update-lang', payload)
    }

    return {
      search,
      query,
      filter,
      setFilter,
      LangSelect,
      updateLang,
      Media
    }
  }
})
</script>

<style lang="scss" scoped>
.glasses {
  display: flex;
  justify-content: center;
  width: 60%;
  margin: 0 auto;
}

.search {
  position: relative;
  border-radius: 5px;
  margin: 0 auto;
  background: #51555c;
  max-width: 600px;
}

.inputContainer {
  display: flex;
  box-shadow: 0 5px 5px #22283111;
  position: relative;

   button {
    margin: 10px;
    padding: 0 1em;
    background: #d65a31;
    border-radius: 5px;
    color: #fff;
    transition: background .2s ease-in-out;

    &:hover {
      background: #de7b5a;
    }
  }
}

input {
  background: #51555c;
  padding: 1em 0 1em 1em;
  width: 100%;
  min-width: 0;
  border: none;
  font-family: 'Open Sans Regular';
  font-size: 18px;
  color: #fff;
  outline: none;
  border-radius: 5px 5px 0 0;
}

button {
  border: none;
  cursor: pointer;
  outline: none;
}

.filters {
  background: #494d54;
  display: grid;
  grid-template-areas:
    "types"
    "lang";
  border-radius: 0 0 5px 5px;

  button {
    background: #494d54;
    padding: .5em 1em;
    color: #fff;
    font-family: 'Open Sans Bold';
    font-size: 18px;
    transition: .2s ease-in-out;
    transition-property: background, color;

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
}

.types {
  display: grid;
  grid-template-areas:
    "movie"
    "tvShow";
  grid-area: types;

  .movie {
    border-radius: 0 0 0 5px;
  }
}

@media only screen and (min-width: 300px) {
  .filters {
    grid-template-areas:
      "types"
      "lang";
  }
  .types {
    grid-template-areas: "movie tvShow";
  }
}

@media only screen and (min-width: 500px) {
  .filters {
    justify-content: space-between;
    grid-template-areas: "types lang";
  }
}
</style>
