import {defineStore} from "pinia";
import {ref} from "vue";

export const useSelectedSongStore = defineStore("selectedSong", {
  state: () => ({
    selectedSong: null, // 선택된 곡 정보 저장
  }),
});
