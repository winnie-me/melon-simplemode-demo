import {defineStore} from "pinia";
import {ref} from "vue";

export const useSelectedArtistStore = defineStore("selectedArtist", {
  state: () => ({
    selectedArtist: null, // 선택된 아티스트 정보 저장
  }),
});
