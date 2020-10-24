<template>
  <div class="load">
    <div/><div/><div/>
  </div>
</template>

<style lang="scss" scoped>
.load {
  position: relative;
  width: 80px;
  height: 80px;

  div {
    display: inline-block;
    position: absolute;
    border-radius: 15px;
    left: 8px;
    width: 16px;
    background: #ddd;
    animation: loading 1.2s cubic-bezier(0, 0.5, 0.5, 1) infinite;

    &:nth-child(1) {
      left: 8px;
      animation-delay: -.24s;
    }

    &:nth-child(2) {
      left: 32px;
      animation-delay: -.12s;
    }

    &:nth-child(3) {
      left: 56px;
      animation-delay: 0;
    }
  }
}
@keyframes loading {
  0% {
    top: 8px;
    height: 64px;
  }
  50%, 100% {
    top: 24px;
    height: 32px;
  }
}
</style>