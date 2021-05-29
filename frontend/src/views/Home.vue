<template>
  <div class="home"><HomeHero /> <LatestProducts /></div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import HomeHero from "../components/Home/HomeHero.vue";
import LatestProducts from "../components/Home/LatestProducts.vue";

export default defineComponent({
  name: "Home",
  components: { HomeHero, LatestProducts },
});
</script>
