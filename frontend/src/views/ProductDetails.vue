<template>
  <Details v-bind:quantity="quantity" />
</template>

<script lang="ts">
import axios from "./../utils/axios";
import { defineComponent } from "@vue/runtime-core";

import Details from "./../components/ProductDetails/Details.vue";

export default defineComponent({
  name: "ProductDetails",
  components: {
    Details,
  },
  data() {
    return {
      product: {},
      quantity: 1,
    };
  },
  mounted() {
    this.getProduct();
  },
  methods: {
    async getProduct() {
      const category_slug = this.$route.params.category_slug;
      const product_slug = this.$route.params.product_slug;

      return;
    },
  },
});
</script>

<style lang="scss" scoped>
</style>