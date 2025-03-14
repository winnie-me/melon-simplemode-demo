<template>
  <v-slide-group>
    <v-slide-group-item v-for="(content, index) in contents" :key="index">

      <v-card @click="navigateTo(content.title)" style="padding: 0">
        <v-card-title class="white--text text-h6">
          {{ content.title }}
        </v-card-title>
        <v-card-text>
          <v-list class="song-item">
            <SongListItem
              v-for="item in content.songs"
              :key="item.song_id"
              :song="item"
              :disableTooltip="disableTooltip"
            />
          </v-list>
        </v-card-text>
      </v-card>

    </v-slide-group-item>

  </v-slide-group>
</template>

<script>
import SongListItem from "@/components/SongListItem.vue";

export default {
  components: {SongListItem},
  data() {
    return {
      contents: [],
    };
  },
  // emits: ["clickCard"],
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
    handleClick(card) {
      this.$emit("clickCard", card.title);
    },
    navigateTo(title) {
      this.$router.push({path: '/trend-revival-list', query: {tag: title}});
    },

    async fetchInitialData() {
      try {
        const response = await fetch(`https://winnie-bigquery-api-77vot6b6va-du.a.run.app/trending-revival/list`);
        const data = await response.json();
        this.contents = data.data[0].contents;
        console.log('this.contents', data.data[0].contents)
      } catch (error) {
        console.error('Error fetching data:', error);
        this.contents = [];
      }
    },
  }
};
</script>

<style scoped>
.image-card {
  width: 150px;
  height: 100px;
  border-radius: 10px;
  overflow: hidden;
}

::v-deep(.v-slide-group__prev),
::v-deep(.v-slide-group__next) {
  display: none !important;
}

.slot-card /*::v-deep()*/
{
  padding: 0 !important; /* 기본 padding을 강제로 덮어쓰기 */
}

.song-item {
  width: 300px;
}
</style>
