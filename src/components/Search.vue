<template>
    <div class="search">
        <div class="inputContainer">
            <input placeholder="Search for a movie name"/>
            <button>
                <font-awesome-icon icon="search"/>
            </button>
        </div>
        <div class="filters">
            <button class="movie active">Movie</button>
            <button class="tvShow">Tv Show</button>
            <button class="anime">Anime</button>
            <button class="lang">English (US)</button>
        </div>
    </div>
</template>

<style scoped>
.search {
    background: #51555c;
    border-radius: 5px;
}

.inputContainer {
    display: flex;
    border-radius: 5px;
}

input {
    background: #51555c;
    padding: 1em;
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
    border-radius: 5px;
    cursor: pointer;
    outline: none;
}

.inputContainer button {
    margin: 10px;
    padding: 0 1em;
    background: #d65a31;
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
    grid-area: lang;
}
</style>
