<template>
  <v-container fluid>
    <v-row no-gutters>
      <!-- 왼쪽 영역 (화면 1 그룹) -->
      <v-col cols="6">
        <v-row>
          <v-col cols="12"><h3>화면 1</h3></v-col>
        </v-row>
        <v-row>
          <v-col cols="12">
            <v-container class="content-container">
              <v-card class="pa-4">
                <v-card-title class="white--text text-h6">유저별 시드곡</v-card-title>
                <!--            <v-btn class="ma-2" color="grey darken-2" small>모두 재생</v-btn>-->

                <v-slide-group :show-arrows="false" class="custom-slide-group">

                  <v-slide-group-item>
                    <v-list>

                      <SongListItem
                        v-for="item in song_list_1"
                        :key="item.song_id"
                        :song="item"
                        @playSong="playSong"
                      /> <!-- @clearSongs="clearSongs" -->
                      
                    </v-list>
                  </v-slide-group-item>

                  <v-slide-group-item>
                    <v-list dark>
                      <v-list-item v-for="(song, index) in songs" :key="index">
                        <template v-slot:prepend>
                          <v-avatar rounded="lg" size="48">
                            <v-img :src="song.image"></v-img>
                          </v-avatar>
                        </template>
                        <v-list-item-title>{{ song.title }}</v-list-item-title>
                        <v-list-item-subtitle>{{ song.artist }} • {{ song.views }} 재생
                        </v-list-item-subtitle>

                      </v-list-item>
                    </v-list>
                  </v-slide-group-item>
                  <v-slide-group-item>
                    <v-list dark>
                      <v-list-item v-for="(song, index) in songs" :key="index">
                        <template v-slot:prepend>
                          <v-avatar rounded="lg" size="48">
                            <v-img :src="song.image"></v-img>
                          </v-avatar>
                        </template>
                        <v-list-item-title>{{ song.title }}</v-list-item-title>
                        <v-list-item-subtitle>{{ song.artist }} • {{ song.views }} 재생
                        </v-list-item-subtitle>
                      </v-list-item>
                    </v-list>
                  </v-slide-group-item>
                </v-slide-group>
              </v-card>
            </v-container>
          </v-col>
        </v-row>

        <v-row><!-- 원래 여기에 있으면 안됨. 슬롯으로 빼고, 곡 컴포넌트로 빼고 -->
          <v-col cols="12"><h3>역주행곡</h3></v-col>
        </v-row>
        <v-row>
          <v-col cols="12">
            <ExampleCardView2/>
          </v-col>
        </v-row>
      </v-col>

      <!-- 오른쪽 최상단 영역 (화면 2, 전체 높이 차지) -->
      <v-col cols="6">
        <v-row>
          <v-col cols="12"><h3>화면 2</h3></v-col>
        </v-row>
        <v-sheet height="100vh" class="d-flex align-center justify-center">
          <AccordionListView/>
        </v-sheet>
      </v-col>
    </v-row>

  </v-container>
</template>


<script>
import {useUserStore} from "@/stores/userStore";
import AccordionListView from "@/views/AccordionListView.vue";
import ExampleCardView2 from "@/views/ExampleCardView2.vue";
import SongListItem from "@/components/SongListItem.vue";

export default {
  components: {AccordionListView, ExampleCardView2, SongListItem},
  setup() {
    const store = useUserStore();

    return {
      store,
    };
  },
  data() {
    return {
      // shouldShowArrows: false,
      // store: useUserStore(),
      selectedUserId: null,
      songs: [],
      song_list_1: [],
      song_list_2: [],
      song_list_3: [],
      song_list_4: [],
    };
  },
  mounted() {
    // this.fetchInitialData();
    if (this.computedSelectedUserId) {
      this.selectedUserId = this.computedSelectedUserId;
      this.fetchInitialData();
    }
  },
  computed: {
    computedSelectedUserId() {
      return this.store.selectedUserId; // store의 selectedUserId를 computed로 반환
    }
  },
  watch: {
    computedSelectedUserId(newVal) {
      if (newVal) {
        this.selectedUserId = newVal; // 반응형 변수에 저장
        this.fetchInitialData();
      }
    }
  },

  methods: {
    async fetchInitialData() {
      try {
        const response = await fetch(`https://winnie-bigquery-api-77vot6b6va-du.a.run.app/collections/user-profile-songs?user_id=${this.selectedUserId}`);
        const data = await response.json();
        this.songs = data.data[0].songs;
        console.log('this.songs', data.data[0].songs)

        this.song_list_1 = data.data[0].songs.slice(0, 4)
        this.song_list_2 = data.data[0].songs.slice(4, 8)
        this.song_list_3 = data.data[0].songs.slice(8, 12)
        this.song_list_4 = data.data[0].songs.slice(12, 16)
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
.avatar-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.content-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  padding: 0px;
}

.content-container > * {
  flex-grow: 1; /* 내부 요소가 남은 공간을 전부 채움 */
  width: 100%;
  height: 100%;
}

/*.custom-slide-group {
  display: flex;
  gap: 12px; !* 요소 간 간격 *!
}*/

::v-deep(.v-slide-group__prev),
::v-deep(.v-slide-group__next) {
  display: none !important;
}
</style>
