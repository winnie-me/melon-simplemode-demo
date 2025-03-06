<template>
  <!--  <v-app>-->
  <v-container>
    <h2 class="mb-4">재생목록</h2>

    <!-- 📌 바깥쪽 Expansion Panels -->
    <v-expansion-panels variant="accordion">
      <v-expansion-panel v-for="(item, itemIndex) in result" :key="itemIndex" elevation="0">
        <template v-slot:title>
          <v-list-item @click="playSong(item.song_info.song_id);clearSongs()">
            <template v-slot:prepend>
              <v-avatar rounded="lg" size="48">
                <img
                  :src="`https://cdnimg.melon.co.kr/${item.song_info.img}/melon/resize/282/quality/80/optimize`"
                  class="avatar-img"/>
              </v-avatar>
            </template>
            <v-list-item-title>{{ item.song_info.title }}</v-list-item-title>
            <v-list-item-subtitle>{{
                item.song_info.artist_names.join(',')
              }}
            </v-list-item-subtitle>
          </v-list-item>
        </template>

        <template v-slot:text>
          <!-- 📌 스와이프 가능한 버튼 그룹 -->
          <v-slide-group show-arrows class="pa-2">
            <v-slide-group-item v-for="(tagInfo, tagIndex) in item.tagList" :key="tagIndex">
              <v-btn class="mx-1" density="compact" variant="tonal" color="green-darken-1"
                     @click="loadSubSongList(itemIndex, tagIndex)">
                {{ tagInfo.tagName }}
              </v-btn>
            </v-slide-group-item>
          </v-slide-group>

          <!-- 📌 버튼 클릭 시 변경되는 곡 리스트 -->
          <v-list
            v-if="targetSubSongList.length === 0">
            곡 없음
          </v-list>
          <v-list
            v-if="targetSubSongList.length > 0">
            <v-divider></v-divider>
            <v-list-item
              v-for="(song, idx) in targetSubSongList"
              :key="idx"
              @click="playSong(song.song_id)">
              <template v-slot:prepend>
                <v-avatar rounded="lg" size="48">
                  <img
                    :src="`https://cdnimg.melon.co.kr/${song.img}/melon/resize/282/quality/80/optimize`"
                    class="avatar-img" alt=""/>
                </v-avatar>
              </template>

              <v-list-item-title>{{ song.title }}</v-list-item-title>
              <v-list-item-subtitle>{{ song.artist_names.join(',') }}</v-list-item-subtitle>
            </v-list-item>
          </v-list>

        </template>


      </v-expansion-panel>
    </v-expansion-panels>
  </v-container>
  <!--  </v-app>-->
</template>

<script>
import {nextTick} from "vue";

export default {
  data() {
    return {
      currentItemIndex: -1,
      currentItemTagIndex: -1,
      targetSubSongList: [
        {
          "song_id": 33525187,
          "song_id_1": 33525187,
          "title": "십자가를 바라보며 (Live)",
          "album_id": 10616806,
          "album_name": "오버플로우 라이브",
          "artist_ids": [
            2894763
          ],
          "artist_names": [
            "OVERFLOW (오버플로우)"
          ],
          "class": "CC0001=기독교음악",
          "genre": [
            "GC0042=국내CCM"
          ],
          "style": [],
          "copyright": [
            "RC0054=881788|존추",
            "RC0055=881788|존추\f2940826|김영수",
            "RC0057=881788|존추"
          ],
          "disk_no": 1,
          "track_no": 4,
          "play_time": 316,
          "issue_date": "20210531",
          "svc_info": "00100000000500010000",
          "opened_at": "2021-05-31T12:00:00.000+0900",
          "registered_at": "2021-06-28T00:20:08.000+0900",
          "img": "/cm2/album/images/106/16/806/10616806_20210528161333.jpg"
        },
        {
          "song_id": 4193346,
          "song_id_1": 4193346,
          "title": "Heart Attack",
          "album_id": 2195303,
          "album_name": "The 1st Album &#39;XOXO&#39; Repackage",
          "artist_ids": [
            724619
          ],
          "artist_names": [
            "EXO"
          ],
          "class": "CC0006=한국대중음악",
          "genre": [
            "GC0011=Dance",
            "GC0089=댄스 10‘~",
            "GC0090=아이돌 남자",
            "GC0093=아이돌 댄스"
          ],
          "style": [
            "SC0381=10' Dance"
          ],
          "copyright": [
            "RC0054=697315|Goodwill\f179702|MGI",
            "RC0055=640031|Misfit",
            "RC0057=697315|Goodwill\f179702|MGI"
          ],
          "disk_no": 1,
          "track_no": 10,
          "play_time": 218,
          "issue_date": "20130805",
          "svc_info": "00000000000500000000",
          "opened_at": "2013-08-05T11:59:00.000+0900",
          "registered_at": "2025-01-28T14:40:52.000+0900",
          "img": "/cm/album/images/021/95/303/2195303.jpg"
        },],
      result:
        [ // item.tagList[currentItemTagIndex].subSongList
          {
            song_info: {
              song_id: 33525187,
              title: "십자가를 바라보며 (Live)",
              artist_names: [
                "OVERFLOW (오버플로우)"
              ],
              img: "/cm2/album/images/106/16/806/10616806_20210528161333.jpg"
            },
            tagList: [
              {
                tagName: "용기를 주는",
                subSongList: []
              },
              {
                tagName: "영적인",
                subSongList: []
              },
              {
                tagName: "드럼",
                subSongList: []
              },
              {
                tagName: "감정적인",
                subSongList: []
              },
            ],
          },
          {
            song_info: {
              song_id: 4193346,
              title: "Heart Attack",
              artist_names: [
                "EXO"
              ],
              img: "/cm/album/images/021/95/303/2195303.jpg"
            },
            tagList: [
              {
                tagName: "강렬한",
                subSongList: []
              },
              {
                tagName: "감상적인",
                subSongList: []
              },
              {
                tagName: "카리스마 있는",
                subSongList: []
              },
              {
                tagName: "타악기",
                subSongList: []
              },
            ],
          },
          {
            song_info: {
              song_id: 37687954,
              title: "Rockstar",
              artist_names: [
                "리사 (LISA)"
              ],
              img: "/cm2/album/images/115/24/489/11524489_20240627143934.jpg"
            },
            tagList: [
              {
                tagName: "놀기좋은",
                subSongList: []
              },
              {
                tagName: "래퍼 같은",
                subSongList: []
              },
              {
                tagName: "반항적인",
                subSongList: []
              },
              {
                tagName: "전자 기타",
                subSongList: []
              },
            ],
          },
        ]
    }
      ;
  },

  methods: {
    async loadSubSongList(itemIndex, tagIndex) {
      try {
        const response = await fetch('https://winnie-bigquery-api-77vot6b6va-du.a.run.app/data'); // ✅ 실제 API 주소 입력
        const jsonResponse = await response.json();

        // ✅ API 응답에서 `data` 하위의 4개만 가져오기
        const songs = jsonResponse.data?.slice(0, 4) || [];

        console.info('결과:', songs);

        // ✅ Vue 3에서는 직접 할당해도 반응형 감지가 가능
        // this.result[itemIndex].tagList[tagIndex].subSongList = [...songs];
        this.result[itemIndex].tagList[tagIndex].subSongList.splice(0, this.result[itemIndex].tagList[tagIndex].subSongList.length, ...songs);
        this.currentItemIndex = itemIndex
        this.currentItemTagIndex = tagIndex
        console.info('currentItemTagIndex:', this.currentItemIndex, this.currentItemTagIndex);
        console.info('this.result[itemIndex].tagList[tagIndex]:', this.result[itemIndex].tagList[tagIndex]);
        // console.info('this.result[itemIndex].tagList[tagIndex]:', this.result[this.currentItemIndex].tagList[this.currentItemTagIndex]);

        // ✅ targetSubSongList 업데이트
        this.targetSubSongList = [...songs];

        console.info('target:', this.result[this.currentItemIndex].tagList[this.currentItemTagIndex].subSongList);
        await nextTick();
      } catch (error) {
        console.error('API 요청 실패:', error);
        // 오류 발생 시 빈 배열 설정
        this.result[itemIndex].tagList[tagIndex].subSongList = [];
        this.targetSubSongList = [];
        this.currentItemIndex = -1
        this.currentItemTagIndex = -1
        // await nextTick();
      }
      // this.targetSubSongList = this.result[itemIndex].tagList[tagIndex].subSongList
      // console.info('target:', this.targetSubSongList);
      // ✅ UI 강제 업데이트
      // await nextTick();
    },
    playSong(song_id) {
      const url = `melonplayer://play?ref=XXX&cid=${song_id}&ctype=song&menuid=1234`;
      window.location.href = url; // URL 실행
    },
    clearSongs() {
      this.targetSubSongList = []
    }
  },
};
</script>

<style scoped>
.avatar-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/*
::v-deep(.v-container) {
  width: 100%;
  padding: 0px;
  margin-right: auto;
  margin-left: auto;
}*/

::v-deep(.v-expansion-panel-title) {
  align-items: center;
  text-align: start;
  border-radius: inherit;
  display: flex;
  font-size: 0.9375rem;
  line-height: 1;
  min-height: 48px;
  outline: none;
  padding: 4px 1px;
  position: relative;
  transition: 0.3s min-height cubic-bezier(0.4, 0, 0.2, 1);
  width: 100%;
  justify-content: space-between;
}

::v-deep(.v-expansion-panel-text__wrapper) {
  padding: 0px;
  flex: 1 1 auto;
  max-width: 100%;
}

</style>
