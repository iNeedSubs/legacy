<template>
  <div class="search">
    <div class="inputContainer">
      <input placeholder="Search"/>
        <button>
          <fa icon="search"/>
        </button>
    </div>
    <div class="filters">
      <button
        class="movie"
        v-bind:class="{active: filter === Types.MOVIE}"
        @click="setFilter('movie')"
      >Movie</button>
      <button
        class="tvShow"
        v-bind:class="{active: filter === Types.TV_SHOW}"
        @click="setFilter('tvShow')"
      >TV Show</button>
      <button class="lang">English (US)</button>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'

enum Types {
  MOVIE = 'movie',
  TV_SHOW = 'tvShow'
}

export default defineComponent({
  setup() {
    const filter = ref('movie')

    const setFilter = (type: Types) => filter.value = type;

    return {
      filter,
      setFilter,
      Types
    }
  }
})
</script>

<style lang="scss" scoped>
.search {
  margin: 0 auto;
  background: #51555c;
  border-radius: 5px;
  max-width: 600px;
}

.inputContainer {
  display: flex;
  border-radius: 5px;
  z-index: 1;

   button {
    margin: 10px;
    padding: 0 1em;
    background: #d65a31;
    border-radius: 5px;
    color: #fff;
    transition: background .1s ease-in-out;

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
  border-radius: 5px;
  font-family: 'Open Sans Regular';
  font-size: 18px;
  color: #fff;
  outline: none;
}

button {
  border: none;
  cursor: pointer;
  outline: none;
}

.filters {
  border-radius: 5px;
  background: #494d54;
  display: grid;
  grid-template-areas:
    "movie tvShow"
    "lang lang";

  button {
    background: #494d54;
    padding: .5em 1em;
    color: #fff;
    font-family: 'Open Sans Bold';
    font-size: 18px;
    transition: background .1s ease-in-out;

    &:hover {
      background: #6d707622;
    }

    &.active {
      background: #d65a31;
    }
  }
}

.movie {
  grid-area: movie;
}

.tvShow {
  grid-area: tvShow;
}

.lang {
  box-shadow: 0px -1px 15px #22283155;
  grid-area: lang;
  border-radius: 0 0 5px 5px;
}
</style>
