<template>
  <keep-alive>
    <v-slide-group center-active>

      <v-slide-group-item v-for="(content, index) in contents" :key="index">
        <SongListCard :content="content"
                      :disable-tooltip="disableTooltip"
                      :navigate-obj="{path: '/seasonality', query: {title: content.title}}"
        />
      </v-slide-group-item>

    </v-slide-group>
  </keep-alive>
</template>

<script>
import SongListCard from "@/components/SongListCard.vue";

export default {
  components: {SongListCard},
  data() {
    return {
      contents: [],
      selected: null,

      lastScrollTop: 0,
      isScrollReset: false,
    };
  },
  mounted() {
    this.fetchInitialData();
  },

  computed: {
    disableTooltip() {
      const os = this.$getOS();
      return os === "Android" || os === "iOS";
    },
  },
  methods: {
    async fetchInitialData() {
      try {
        const response = await fetch(`https://winnie-bigquery-api-77vot6b6va-du.a.run.app/seasonality/list`); //
        const data = await response.json();
        this.contents = data.data[0].contents;
        // console.log('this.contents', data.data[0].contents)
      } catch (error) {
        console.error('Error fetching data:', error);
        this.contents = [];
      }
    },
  }
};
</script>

