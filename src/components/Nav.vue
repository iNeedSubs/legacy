<template>
  <nav>
    <router-link to="/">Home</router-link>
    <router-link to="/about">About</router-link>
    <router-link to="/contact">Contact</router-link>
  </nav>
</template>

<style lang="scss" scoped>
nav {
  font-family: 'Open Sans Bold', sans-serif;
  display: flex;
  flex-direction: column;
  gap: 5px;
  justify-content: space-evenly;
  align-items: center;
  font-size: 1.1em;

  a {
    color: #fff;
    text-decoration: none;
    border-radius: 15px;
    padding: 10px 15px;
    transition: background .1s ease-in-out;

    &:hover, &:focus {
      background: #de7b5a44;
    }

    &.router-link-exact-active {
        background: #d65a31;
    }
  }
}

@media only screen and (min-width: 300px) {
  nav {
    flex-direction: row;
  }
}

@media only screen and (min-width: 800px) {
  nav {
    gap: 1em;
  }
}
</style>
