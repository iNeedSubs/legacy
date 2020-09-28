<template>
  <nav>
    <router-link to="/">Home</router-link>
    <router-link to="/about">About</router-link>
    <router-link to="/contact">Contact</router-link>
  </nav>
</template>

<style lang="scss" scoped>
nav {
  font-family: 'Open Sans Bold';
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  font-size: 1.1em;

  a {
    color: #fff;
    text-decoration: none;
    border-radius: 5px;
    padding: 5px 10px;
    transition: background .1s ease-in-out;

    &:hover {
      background: #de7b5a55;
    }

    &.router-link-exact-active {
        background: #de7b5a;
    }
  }
}

@media only screen and (min-width: 800px) {
  nav {
    gap: 1em;
  }
}
</style>
