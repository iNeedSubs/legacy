<template>
  <svg xmlns="http://www.w3.org/2000/svg" width="240.002" viewBox="0 0 240.002 60.002">
    <g transform="translate(-19.999 -60)">
      <path fill="#dddddd" d="M-8390-1569h-90a5.006,5.006,0,0,1-5-5v-50a5.006,5.006,0,0,1,5-5h90a5.006,5.006,0,0,1,5,5v50A5.006,5.006,0,0,1-8390-1569Zm-80-55a5.006,5.006,0,0,0-5,5v40a5.006,5.006,0,0,0,5,5h70a5.006,5.006,0,0,0,5-5v-40a5.006,5.006,0,0,0-5-5Z" transform="translate(8505 1689.001)"/>
      <path fill="#dddddd" d="M-8390-1569h-90a5.006,5.006,0,0,1-5-5v-50a5.006,5.006,0,0,1,5-5h90a5.006,5.006,0,0,1,5,5v50A5.006,5.006,0,0,1-8390-1569Zm-80-55a5.006,5.006,0,0,0-5,5v40a5.006,5.006,0,0,0,5,5h70a5.006,5.006,0,0,0,5-5v-40a5.006,5.006,0,0,0-5-5Z" transform="translate(8645 1689.001)"/>
      <rect fill="#dddddd" width="50" height="10" transform="translate(115 85)"/>
      <rect id="glowLeft" fill="#1780e8" opacity=".4" width="80" height="50" rx="5" transform="translate(30 65)"/>
      <rect id="glowRight" fill="#eb5857" opacity=".4" width="80" height="50" rx="5" transform="translate(170 65)"/>
    </g>

    <animate
      xlink:href="#glowLeft"
      attributeType="CSS"
      attributeName="opacity"
      values=".4;.5;.6;.7;.8;.7;.6;.5;.4"
      dur="4s"
      begin="0s"
      calcMode="paced"
      repeatCount="indefinite"
    />

    <animate
      xlink:href="#glowRight"
      attributeType="CSS"
      attributeName="opacity"
      values=".4;.5;.6;.7;.8;.7;.6;.5;.4"
      dur="4s"
      begin="1s"
      calcMode="paced"
      repeatCount="indefinite"
    />
  </svg>
</template>

<script>
export default {
  name: 'Glasses'
}
</script>