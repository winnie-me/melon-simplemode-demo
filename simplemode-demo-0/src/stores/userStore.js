import { defineStore } from "pinia";
import { ref } from "vue";

export const useUserStore = defineStore("user", () => {
  const selectedUserId = ref('46536104');
  return { selectedUserId };
});
