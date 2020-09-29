<template>
  <div class="glasses">
    <Glasses/>
  </div>
  <div class="search">
    <div class="inputContainer">
      <input placeholder="Search"/>
        <button>
          <fa icon="search"/>
        </button>
    </div>
    <div class="filters">
      <div class="types">
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
      </div>
      <button class="lang">English (US) <fa icon="angle-down"/></button>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import Glasses from '../assets/Glasses.vue'

enum Types {
  MOVIE = 'movie',
  TV_SHOW = 'tvShow'
}

export default defineComponent({
  components: {
    Glasses
  },
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
.glasses {
  display: flex;
  justify-content: center;
  width: 60%;
  margin: 0 auto;
}

.search {
  border-radius: 5px;
  overflow: hidden;
  margin: 0 auto;
  background: #51555c;
  max-width: 600px;
}

.inputContainer {
  display: flex;

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
  background: #494d54;
  display: grid;
  grid-template-areas:
    "types"
    "lang";

  button {
    background: #494d54;
    padding: .5em 1em;
    color: #fff;
    font-family: 'Open Sans Bold';
    font-size: 18px;
    transition: .1s ease-in-out;
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
}

.lang {
  box-shadow: 0px -1px 15px #22283155;
  grid-area: lang;
  border-radius: 0 0 5px 5px;
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
  .inputContainer {
    box-shadow: 0 0 5px red;
  }

  .filters {
    justify-content: space-between;
    grid-template-areas: "types lang";

    .lang {
      box-shadow: none;
    }
  }
}
</style>
