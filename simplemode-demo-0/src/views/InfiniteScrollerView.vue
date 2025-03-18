<template>
  <v-container>
    <v-infinite-scroll :items="items" :onLoad="loadMore">
      <v-list>
        <v-list-item
          v-for="(item, index) in items"
          :key="index"
          :title="item.title"
          :subtitle="item.artist"
        >
          <template v-slot:prepend>
            <v-avatar rounded="lg" size="48">
              <img :src="item.thumbnail" alt="Thumbnail" class="avatar-img"/>
            </v-avatar>
          </template>
        </v-list-item>
      </v-list>
    </v-infinite-scroll>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      items: [
        {
          title: '즐게 (Feat. Leellamarz)',
          artist: 'Kid Wine',
          thumbnail: 'https://cdn.vuetifyjs.com/images/john.png'
        },
        {title: 'Vancouver', artist: 'BIG Naughty', thumbnail: 'cover2.jpg'},
        {title: '담아 (Feat. 염따, pH-1)', artist: '스윙스, 키드밀리', thumbnail: 'cover3.jpg'},
        {title: 'OHAYO MY NIGHT', artist: 'D-Hack, PATEKO', thumbnail: 'cover4.jpg'},
        {title: 'Counting Stars (Feat. Beenzino)', artist: 'BE O', thumbnail: 'cover5.jpg'},
        {title: 'Good Night (Feat. BE O)', artist: 'Coogie', thumbnail: 'cover6.jpg'},
        {title: '이혼서류', artist: '기리보이', thumbnail: 'cover7.jpg'}
      ]
    };
  },
  methods: {
    async loadMore({done}) { // ✅ async 키워드 추가
      // 데이터를 동적으로 불러오는 로직 추가 가능

      await new Promise(resolve => setTimeout(resolve, 1000)); // 1초 딜레이 (로딩 느낌)

      const newItems = Array.from(
        {length: 10},
        (_, i) => `Item ${this.items.length + i + 1}`
      );

      this.items.push(...newItems);

      done(newItems.length > 0); // 데이터가 남아있다면 true, 없으면 false
    }
  }
};
</script>

<style>
.avatar-img {
  width: 100%;  /* 부모(v-avatar)의 너비를 100%로 설정 */
  height: 100%; /* 부모(v-avatar)의 높이를 100%로 설정 */
  object-fit: cover; /* 이미지가 꽉 차면서 비율을 유지하도록 설정 */
}
</style>
