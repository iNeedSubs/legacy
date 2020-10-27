<template>
  <Glasses/>
  <div class="search">
    <div class="inputContainer">
      <input placeholder="Search" v-model="query" v-on:keyup.enter="search"/>
      <button aria-label="Search" @click="search">
        <SearchIcon/>
      </button>
    </div>
    <div class="filters">
      <div class="types">
        <button
          :aria-label="`${MediaType.MOVIE} Filter`"
          class="movie"
          v-bind:class="{active: filter === MediaType.MOVIE}"
          @click="setFilter(MediaType.MOVIE)"
        >Movie</button>
        <button
          :aria-label="`${MediaType.SHOW} Filter`"
          class="show"
          v-bind:class="{active: filter === MediaType.SHOW}"
          @click="setFilter(MediaType.SHOW)"
        >TV Show</button>
      </div>
      <LangSelect/>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import Glasses from '@/assets/Glasses.vue'
import LangSelect from './LangSelect/Index.vue'
import { MediaType } from '@/ts/media'
import SearchIcon from '@/assets/icons/Search.vue'

export default defineComponent({
  components: {
    Glasses,
    LangSelect,
    SearchIcon
  },
  emits: [
    'update-query',
    'update-type'
  ],
  setup(props, { emit }) {
    const query = ref('')
    const filter = ref(MediaType.MOVIE)

    const search = () => emit('update-query', query.value)

    const setFilter = (type: MediaType) => {
      window.scroll(0, 0)
      filter.value = type
      emit('update-type', type)
    }

    return {
      search,
      query,
      filter,
      setFilter,
      LangSelect,
      MediaType
    }
  }
})
</script>

<style lang="scss" scoped>
.glasses {
  display: flex;
  justify-content: center;
  width: clamp(100px, 50vw, 240px);
  margin: 0 auto;
  animation: showUp .4s cubic-bezier(0.2, 0.8, 0.3, 1.3);
}

.search {
  position: relative;
  border-radius: 15px;
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
    background: #de7b5a;
    border-radius: 15px;
    color: #fff;
    transition: background .2s ease-in-out;

    &:hover, &:focus {
      background: #d65a31;
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
  border-radius: 15px 15px 0 0;
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
  border-radius: 0 0 15px 15px;

  button {
    background: #494d54;
    padding: .5em 1em;
    color: #fff;
    font-family: 'Open Sans Bold';
    font-size: 18px;
    transition: .2s ease-in-out;
    transition-property: background, color;

    &:hover, &:focus {
      background: #6d707622;
    }

    &.active {
      background: #de7b5a;
    }

    &:not(.active) {
      color: #ddd;
    }
  }
}

input::placeholder {
  color: #ddd;
}

.types {
  display: grid;
  grid-template-areas:
    "movie"
    "show";
  grid-area: types;
}

@keyframes showUp {
  from {
    transform: translateY(100%)
  }
  to {
    transform: translateY(0)
  }
}

@media only screen and (min-width: 300px) {
  .filters {
    grid-template-areas:
      "types"
      "lang";
  }
  .types {
    grid-template-areas: "movie show";
  }
}

@media only screen and (min-width: 500px) {
  .filters {
    justify-content: space-between;
    grid-template-areas: "types lang";
  }

  .types .movie {
    border-radius: 0 0 0 15px;
  }
}
</style>
