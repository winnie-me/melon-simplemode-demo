<template>
  <v-app>
    <v-container>
      <h2 class="mb-4">뮤직 리스트</h2>

      <!-- 📌 기본 리스트 -->
      <v-list>
        <v-list-item
          v-for="(item, index) in mainList"
          :key="index"
          @click="toggleExpand(index);playSong(item.song_id)"
        >
          <template v-slot:prepend>
            <v-avatar rounded="lg" size="48">
              <img :src="item.thumbnail" class="avatar-img" />
            </v-avatar>
          </template>

          <v-list-item-title>{{ item.title }}</v-list-item-title>
          <v-list-item-subtitle>{{ item.artist }}</v-list-item-subtitle>
        </v-list-item>

        <!-- 📌 클릭 시 확장되는 버튼 그룹 -->
        <v-expand-transition>
          <div v-if="expandedIndex === index">
            <v-slide-group show-arrows class="pa-2">
              <v-slide-group-item v-for="(btn, i) in buttonList" :key="i">
                <v-btn class="mx-2" color="primary" @click="loadSubList(btn.type)">
                  {{ btn.label }}
                </v-btn>
              </v-slide-group-item>
            </v-slide-group>
          </div>
        </v-expand-transition>
      </v-list>

      <!-- 📌 버튼 클릭 시 변경되는 서브 목록 -->
      <v-list v-if="subList.length > 0">
        <v-divider></v-divider>
        <v-list-item v-for="(sub, i) in subList" :key="i">
          <template v-slot:prepend>
            <v-avatar rounded="lg" size="48">
              <img :src="sub.thumbnail" class="avatar-img" />
            </v-avatar>
          </template>

          <v-list-item-title>{{ sub.title }}</v-list-item-title>
          <v-list-item-subtitle>{{ sub.artist }}</v-list-item-subtitle>
        </v-list-item>
      </v-list>
    </v-container>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      expandedIndex: null, // 클릭된 항목의 index 저장
      mainList: [
        { id: 1, title: 'Song A', artist: 'Artist 1', thumbnail: 'https://via.placeholder.com/50' },
        { id: 2, title: 'Song B', artist: 'Artist 2', thumbnail: 'https://via.placeholder.com/50' },
        { id: 3, title: 'Song C', artist: 'Artist 3', thumbnail: 'https://via.placeholder.com/50' },
        { id: 4, title: 'Song D', artist: 'Artist 4', thumbnail: 'https://via.placeholder.com/50' },
        { id: 5, title: 'Song E', artist: 'Artist 5', thumbnail: 'https://via.placeholder.com/50' },
      ],
      buttonList: [
        { label: '추천 곡', type: 'recommended' },
        { label: '인기 곡', type: 'popular' },
        { label: '최신 곡', type: 'latest' },
      ],
      subList: [], // 버튼 클릭 시 변경될 목록
    };
  },
  methods: {
    toggleExpand(index) {
      this.expandedIndex = this.expandedIndex === index ? null : index; // 클릭한 항목의 확장/닫기
    },
    loadSubList(type) {
      // 📌 타입별 더미 데이터 로드
      const data = {
        recommended: [
          { title: '추천 곡 1', artist: '추천 아티스트', thumbnail: 'https://via.placeholder.com/50' },
          { title: '추천 곡 2', artist: '추천 아티스트', thumbnail: 'https://via.placeholder.com/50' },
        ],
        popular: [
          { title: '인기 곡 1', artist: '인기 아티스트', thumbnail: 'https://via.placeholder.com/50' },
          { title: '인기 곡 2', artist: '인기 아티스트', thumbnail: 'https://via.placeholder.com/50' },
        ],
        latest: [
          { title: '최신 곡 1', artist: '최신 아티스트', thumbnail: 'https://via.placeholder.com/50' },
          { title: '최신 곡 2', artist: '최신 아티스트', thumbnail: 'https://via.placeholder.com/50' },
        ],
      };
      this.subList = data[type] || [];
    },
  },
};
</script>

<style>
.avatar-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>
