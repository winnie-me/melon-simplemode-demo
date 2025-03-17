<template>
  <keep-alive>
    <v-slide-group>
      <v-slide-group-item v-for="(content, index) in contents" :key="index" :disabled="true">
        <SongListCard :content="content"
                      :disable-tooltip="true"
                      :card-width="'400px'"
                      :navigate-obj="{path: '/custom-collection-detail', query: {id: content.id}}"
        />
      </v-slide-group-item>

    </v-slide-group>
  </keep-alive>
</template>
<script>
import SongListCard from "@/components/SongListCard.vue";
import {useUserStore} from "@/stores/userStore.js";

export default {
  components: {SongListCard},
  setup() {
    const store = useUserStore();
    return {
      store,
    };
  },
  data() {
    return {
      contents: [],
    };
  },
  mounted() {
    this.fetchInitialData();
  },
  computed: {
    /*    disableTooltip() {
          const os = this.$getOS();
          return os === "Android" || os === "iOS";
        },*/
  },
  methods: {
    async fetchInitialData() {
      try {
        const response = await fetch(`https://winnie-bigquery-api-77vot6b6va-du.a.run.app/custom-collections/list?user_id=${this.store.selectedUserId}`);
        const data = await response.json();
        this.contents = data.data[0].customs;
        console.log('this.contents', data.data[0].customs)
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


.slot-card /*::v-deep()*/
{
  padding: 0 !important; /* 기본 padding을 강제로 덮어쓰기 */
}

.disable-click {
  pointer-events: none; /* 스와이프 중에는 클릭 비활성화 */
}
</style>
