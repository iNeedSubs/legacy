<template>
  <div class="glasses">
    <svg xmlns="http://www.w3.org/2000/svg" width="240" viewBox="0 0 240 60">
      <defs>
        <filter id="a" x="88" y="20" width="64" height="27" filterUnits="userSpaceOnUse">
          <feGaussianBlur stdDeviation="3" result="blur"/>
          <feFlood flood-color="#222831" flood-opacity=".502"/>
          <feComposite operator="in" in2="blur"/>
          <feComposite in="SourceGraphic"/>
        </filter>
      </defs>
      <g transform="translate(-1117 -321)">
        <rect id="glowLeft" width="80" height="50" rx="10" transform="translate(1127.001 326)" fill="#1780e8" opacity=".5"/>
        <g transform="translate(1127.001 326)" fill="none" stroke="#1780e8" stroke-width="5">
          <rect width="80" height="50" rx="10" stroke="none"/>
          <rect x="2.5" y="2.5" width="75" height="45" rx="7.5"/>
        </g>
        <path d="M1347 381h-80a10.011 10.011 0 01-10-10v-40a10.011 10.011 0 0110-10h80a10.011 10.011 0 0110 10v40a10.011 10.011 0 01-10 10zm-70-55a10.012 10.012 0 00-10 10v30a10.012 10.012 0 0010 10h60a10.011 10.011 0 0010-10v-30a10.011 10.011 0 00-10-10z" fill="#fff"/>
        <path d="M1207 381h-80a10.011 10.011 0 01-10-10v-40a10.011 10.011 0 0110-10h80a10.011 10.011 0 0110 10v40a10.011 10.011 0 01-10 10zm-70-55a10.012 10.012 0 00-10 10v30a10.012 10.012 0 0010 10h60a10.011 10.011 0 0010-10v-30a10.011 10.011 0 00-10-10z" fill="#fff"/>
        <g transform="translate(1117 321)" filter="url(#a)">
          <rect width="46" height="9" rx="4.5" transform="translate(97 26)" fill="#fff"/>
        </g>
        <rect id="glowRight" width="80" height="50" rx="10" transform="translate(1267.001 326)" fill="#eb5857" opacity=".5"/>
        <g transform="translate(1267.001 326)" fill="none" stroke="#eb5857" stroke-width="5">
          <rect width="80" height="50" rx="10" stroke="none"/>
          <rect x="2.5" y="2.5" width="75" height="45" rx="7.5"/>
        </g>
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
  </div>
</template>

<script>
export default {
  name: 'Glasses'
}
</script>