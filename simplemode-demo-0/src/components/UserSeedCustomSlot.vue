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
  },
  methods: {
    async fetchInitialData() {
      try {
        const response = await fetch(`https://winnie-bigquery-api-77vot6b6va-du.a.run.app/custom-collections/list?user_id=${this.store.selectedUserId}`);
        const data = await response.json();
        this.contents = data.data[0].customs;
        // console.log('this.contents', data.data[0].customs)
      } catch (error) {
        console.error('Error fetching data:', error);
        this.contents = [];
      }
    },
  }
};
</script>

