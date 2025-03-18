<template>

  <v-card class="mx-2 my-1 flex-grow-1"
          @click="navigateTo('/list-0',card)"
          :style="{ border: `3px solid ${randomColor}` }"
  >
    <v-card-title v-text="item.const_title"/>
  </v-card>

</template>

<script>
export default {
  props: {
    item: {
      type: Object,
      required: true,
    },
  },
  setup(props) {
  },
  computed: {},
  data() {
    return {
      domParser: new DOMParser(),
      imgList: [
        "https://cdn.vuetifyjs.com/images/cards/house.jpg",
        "https://cdn.vuetifyjs.com/images/cards/road.jpg",
        "https://cdn.vuetifyjs.com/images/cards/plane.jpg",
        "https://cdn.vuetifyjs.com/docs/images/cards/purple-flowers.jpg",
        "https://cdn.vuetifyjs.com/images/cards/sunshine.jpg",
        "https://cdn.vuetifyjs.com/images/cards/foster.jpg",
        "https://cdn.vuetifyjs.com/images/cards/docks.jpg",
        "https://cdn.vuetifyjs.com/images/cards/cooking.png",
      ],
      randomImage: null,
      randomColor: null,
      colorList: [
        '#FFC1B4',
        '#DDEB9D',
        '#FFB8E0',
        '#B7B1F2',
        '#FFB200',
        '#A1D6CB',
        '#81BFDA',
        '#FF4545',
        '#FADA7A',
      ],
    };
  },
  mounted() {
    this.randomImage = this.imgList[Math.floor(Math.random() * this.imgList.length)]
    this.randomColor = this.colorList[Math.floor(Math.random() * this.colorList.length)]
  },
  methods: {},
};
</script>

<style scoped>

.custom-tooltip ::v-deep(.v-overlay__content) {
  background-color: #dcedc8 !important; /* ✅ Light Green Lighten-5 색상 */
  color: black !important; /* ✅ 텍스트 색상 변경 */
  opacity: 0.9;
}

</style>
