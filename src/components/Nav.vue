<template>
    <nav>
        <router-link to="/">Home</router-link>
        <router-link to="/about">About</router-link>
        <router-link to="/contact">Contact</router-link>
    </nav>
</template>

<style scoped>
nav {
    font-family: Source Sans Pro SemiBold;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 1.5em;
}

nav a {
    color: #fff;
    text-decoration: none;
    border-radius: 5px;
    padding: 5px 10px;
    transition: background .1s ease-in-out;
}

nav a:hover {
    background: #de7b5a55;
}

nav a.router-link-exact-active {
    background: #de7b5a;
}
</style>
