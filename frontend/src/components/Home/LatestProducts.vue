<template>
  <div class="columns is-multiline">
    <div class="column is-12">
      <h2 class="is-size-2 has-text-centered">Latest Products</h2>
    </div>
    <div
      class="column is-3"
      v-for="product in latestProducts"
      v-bind:key="product.id"
    >
      <div class="box">
        <figure class="image mb-4">
          <img :src="product.get_thumbnail" alt="product.name" />
        </figure>

        <h3 class="is-size-4">{{ product.name }}</h3>
        <p class="is-size-6 has-text-grey">${{ product.price }}</p>

        <router-link v-bind:to="product.get_absolute_url" class="button is-dark mt-4"> View details</router-link>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import axios from "./../../utils/axios";
import { defineComponent } from "@vue/runtime-core";

export default defineComponent({
  name: "LatestProducts",
  components: {},
  data() {
    return {
      latestProducts: [],
    };
  },
  // Vue lifecycle hook
  mounted() {
    this.getLatestProducts();
  },
  methods: {
    async getLatestProducts() {
      try {
        const response = await axios.get("/latest");

        this.latestProducts = response.data;
      } catch (error) {
        console.error("Error has occurred!", error.message);
      }
    },
  },
});
</script>

<style lang="scss" scoped>
.image {
  height: 100%;
  width: 150px;
  margin: 0 auto;
}
</style>