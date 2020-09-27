<template>
  <div class="search">
    <div class="inputContainer">
      <input placeholder="Search"/>
        <button>
          <font-awesome-icon icon="search"/>
        </button>
    </div>
    <div class="filters">
      <button :class="movie" @click="setFilter('movie')">Movie</button>
      <button :class="tvShow" @click="setFilter('tvShow')">TV Show</button>
      <button :class="anime" @click="setFilter('anime')">Anime</button>
      <button class="lang">English (US)</button>
    </div>
  </div>
</template>

<script>
export default {
  data: () => ({
    filter: 'movie',
    setFilter (filter) {
      this.filter = filter
    }
  }),
  computed: {
    movie () {
      return this.filter === 'movie' ? 'movie active' : 'movie'
    },
    tvShow () {
      return this.filter === 'tvShow' ? 'tvShow active' : 'tvShow'
    },
    anime () {
      return this.filter === 'anime' ? 'anime active' : 'anime'
    }
  }
}
</script>

<style scoped>
.search {
  margin: 0 auto;
  background: #51555c;
  border-radius: 5px;
  max-width: 600px;
}

.inputContainer {
  display: flex;
  border-radius: 5px;
}

input {
  background: #51555c;
  padding: 1em 0 1em 1em;
  width: 100%;
  min-width: 0;
  border: none;
  border-radius: 5px;
  font-family: Source Sans Pro Regular;
  font-size: 18px;
  color: #fff;
  outline: none;
}

input::placeholder {
  color: #fff;
}

button {
  border: none;
  cursor: pointer;
  outline: none;
}

.inputContainer button {
  margin: 10px;
  padding: 0 1em;
  background: #d65a31;
  border-radius: 5px;
  color: #fff;
  transition: background .1s ease-in-out;
}

.inputContainer button:hover {
  background: #de7b5a;
}

.filters {
  border-radius: 5px;
  background: #494d54;
  display: grid;
  grid-template-areas:
    "movie tvShow anime"
    "lang lang lang";
}

.filters button {
  background: #494d54;
  padding: .5em 1em;
  color: #fff;
  font-family: Source Sans Pro SemiBold;
  font-size: 18px;
  transition: background .1s ease-in-out;
}

.filters button:hover {
  background: #6d707622;
}

.filters button.active {
  background: #d65a31;
}

.movie {
  grid-area: movie;
}

.tvShow {
  grid-area: tvShow;
}

.anime {
  grid-area: anime;
}

.lang {
  box-shadow: 0px -1px 15px #22283155;
  grid-area: lang;
  border-radius: 0 0 5px 5px;
}
</style>
