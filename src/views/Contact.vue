<template>
  <main>
    <section>
      <h3>👨‍💻 Maintainers</h3>
      <p>If you have:</p>
      <ul>
        <li>A question about something</li>
        <li>Found a bug somewhere</li>
        <li>Something else on your mind</li>
      </ul>
      <p>You can email us at one of the addresses down here:</p>
      <div class="emails">
        <a href="mailto:eray_chumak@protonmail.com">
          <p>eray_chumak@protonmail.com</p>
        </a>
        <a href="mailto:williamlaw.3001@gmail.com">
          <p>williamlaw.3001@gmail.com</p>
        </a>
      </div>
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
  padding: 0 5px;
  transition: background .2s ease-in-out;
}

.emails {
  margin-top: 1em;
  display: grid;
  justify-content: start;
  gap: 1em;

  a {
    background: #BC5938;
    padding: 5px 10px;

    &:hover, &:focus {
      background: #d65a31;
    }
  }
}


.github {
  background: #24292e;
  border: 1px solid white;

  &:hover, &:focus {
    background: #353a3f;
  }
}


@media only screen and (min-width: 800px) {
  main {
    padding: 30px;
  }
}
</style>
