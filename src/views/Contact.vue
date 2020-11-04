<template>
  <main>
    <section>
      <h3>👨‍💻 Maintainer</h3>
      <p>If you have:</p>
      <ul>
        <li>A question about something</li>
        <li>Found a bug somewhere</li>
        <li>Something else on your mind</li>
      </ul>
      <p>You can email me at the address down here:</p>
      <a class="email" href="mailto:eray_chumak@protonmail.com">eray_chumak@protonmail.com</a>
    </section>
    <section>
      <h3>⌨️ Our repository</h3>
      <p>
        We are open source btw! You can visit our repo on <a class="github" href="https://github.com/Spimy/Subtitles">GitHub</a> if
        you want to look around or even contribute 😃.
      </p>
    </section>
  </main>
</template>

<style lang="scss" scoped>
main {
  display: grid;
  gap: 2em;
  justify-content: center;
  padding: 0 30px 30px 30px;
}

h3 {
  margin-bottom: 1em;
  font-family: 'Open Sans Bold', sans-serif;
}

ul {
  margin: 1em 0;
  list-style-type:square;

  li {
    margin: .5em 0;
  }
}

p {
  max-width: 55ch;
  line-height: 1.5em;
}

a {
  border-radius: 15px;
  background: #BC5938;
  padding: 0 5px;
}

.email {
  margin-top: 1em;
  display: inline-block;
  padding: 5px 10px;
}

.github {
  background: #24292e;
  border: 1px solid white;
}


@media only screen and (min-width: 800px) {
  main {
    padding: 30px;
  }
}
</style>
