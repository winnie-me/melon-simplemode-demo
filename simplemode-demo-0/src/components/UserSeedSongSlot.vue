<template>
  <v-slide-group>

    <v-slide-group-item v-if="songLists.length > 0 && songLists[0].length > 0">
      <v-list class="song-item">
        <SongListItem
          v-for="item in songLists[0]"
          :key="item.song_id"
          :song="item"
        />
      </v-list>
    </v-slide-group-item>

    <v-slide-group-item v-if="songLists.length > 1 && songLists[1].length > 0">
      <v-list class="song-item">
        <SongListItem
          v-for="item in songLists[1]"
          :key="item.song_id"
          :song="item"
        />
      </v-list>
    </v-slide-group-item>
    <v-slide-group-item v-if="songLists.length > 2 && songLists[2].length > 0">
      <v-list class="song-item">
        <SongListItem
          v-for="item in songLists[2]"
          :key="item.song_id"
          :song="item"
        />
      </v-list>
    </v-slide-group-item>
    <v-slide-group-item v-if="songLists.length > 3 && songLists[3].length > 0">
      <v-list class="song-item">
        <SongListItem
          v-for="item in songLists[3]"
          :key="item.song_id"
          :song="item"
        />
      </v-list>
    </v-slide-group-item>
    <v-slide-group-item v-if="songLists.length > 4 && songLists[4].length > 0">
      <v-list class="song-item">
        <SongListItem
          v-for="item in songLists[4]"
          :key="item.song_id"
          :song="item"
        />
      </v-list>
    </v-slide-group-item>
    <v-slide-group-item v-if="songLists.length > 5 && songLists[5].length > 0">
      <v-list class="song-item">
        <SongListItem
          v-for="item in songLists[5]"
          :key="item.song_id"
          :song="item"
        />
      </v-list>
    </v-slide-group-item>
    <v-slide-group-item v-if="songLists.length > 6 && songLists[6].length > 0">
      <v-list class="song-item">
        <SongListItem
          v-for="item in songLists[6]"
          :key="item.song_id"
          :song="item"
        />
      </v-list>
    </v-slide-group-item>
    <v-slide-group-item v-if="songLists.length > 7 && songLists[7].length > 0">
      <v-list class="song-item">
        <SongListItem
          v-for="item in songLists[7]"
          :key="item.song_id"
          :song="item"
        />
      </v-list>
    </v-slide-group-item>
    <v-slide-group-item v-if="songLists.length > 8 && songLists[8].length > 0">
      <v-list class="song-item">
        <SongListItem
          v-for="item in songLists[8]"
          :key="item.song_id"
          :song="item"
        />
      </v-list>
    </v-slide-group-item>
    <v-slide-group-item v-if="songLists.length > 9 && songLists[9].length > 0">
      <v-list class="song-item">
        <SongListItem
          v-for="item in songLists[9]"
          :key="item.song_id"
          :song="item"
        />
      </v-list>
    </v-slide-group-item>
    <v-slide-group-item v-if="songLists.length > 10 && songLists[10].length > 0">
      <v-list class="song-item">
        <SongListItem
          v-for="item in songLists[10]"
          :key="item.song_id"
          :song="item"
        />
      </v-list>
    </v-slide-group-item>
  </v-slide-group>
</template>
<script>
import SongListItem from "@/components/SongListItem.vue";
import {useUserStore} from "@/stores/userStore.js";

export default {
  components: {
    SongListItem
  },
  props: {},
  setup() {
    const store = useUserStore();
    return {
      store,
    };
  },
  data() {
    return {
      songs: [],
      songLists: [], // ✅ 2차원 배열 저장
    };
  },
  mounted() {
    this.fetchInitialData();
  },
  methods: {
    async fetchInitialData() {
      try {
        const response = await fetch(`https://winnie-bigquery-api-77vot6b6va-du.a.run.app/collections/user-profile-songs?user_id=${this.store.selectedUserId}`);
        const data = await response.json();

        this.splitSongs(data.data[0].songs)
        // this.songs = data.data[0].songs;
        console.log('this.songs', data.data[0].songs)

      } catch (error) {
        console.error('Error fetching data:', error);
        this.songLists = [];
      }
    },
    splitSongs(allSongs) { // 화면에 맞게 카드당 4곡씩 넣기
      const chunkSize = 4; // ✅ 4개씩 분할
      this.songLists = [];

      for (let i = 0; i < allSongs.length; i += chunkSize) {
        this.songLists.push(allSongs.slice(i, i + chunkSize));
      }
    },
  },
};
</script>
<style>
.song-item {
  width: 300px;
}
</style>
