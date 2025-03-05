<template>
  <v-container fluid class="list-container">
    <v-row justify="center" style="width: 800px; margin: auto;">
      <v-col cols="12" sm="12" md="12" lg="12">
        <v-list>
          <v-list-item
            v-for="(item, index) in items"
            :key="index"
            :title="item.title"
            :subtitle="item.artist_names.join(',')"
            class="clickable-item"
            @click="playSong(item.song_id)"
          >
            <template v-slot:prepend>
              <v-avatar rounded="lg" size="48">
                <img
                  :src="`https://cdnimg.melon.co.kr/${item.img}/melon/resize/282/quality/80/optimize`"
                  alt="Thumbnail" class="avatar-img"/>
              </v-avatar>
            </template>
          </v-list-item>
        </v-list>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      items: []
    };
  },
  mounted() {
    this.fetchInitialData();
  },
  methods: {
    async fetchInitialData() {
      try {
        const response = await fetch('https://winnie-bigquery-api-77vot6b6va-du.a.run.app/data'); // 실제 API URL로 변경
        const data = await response.json();
        this.items = data.data; // 데이터를 상태에 저장
      } catch (error) {
        console.error('Error fetching data:', error);
        this.items = [];
      }
    },
    playSong(song_id) {
      const url = `melonplayer://play?ref=XXX&cid=${song_id}&ctype=song&menuid=1234`;
      window.location.href = url; // URL 실행
    }
  }
};
</script>

<style scoped>
.clickable-item {
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.avatar-img {
  width: 100%; /* 부모(v-avatar)의 너비를 100%로 설정 */
  height: 100%; /* 부모(v-avatar)의 높이를 100%로 설정 */
  object-fit: cover; /* 이미지가 꽉 차면서 비율을 유지하도록 설정 */
}

.list-container {
  max-width: 1200px; /* 너무 넓어지는 것을 방지 */
  margin: 0 auto; /* 중앙 정렬 */
}
</style>
