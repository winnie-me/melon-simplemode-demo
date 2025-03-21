import {defineStore} from "pinia";
import {ref} from "vue";
import axios from "axios";

export const useUserStore = defineStore("user", () => {
  const selectedUserId = ref();
  const userList = ref([]);

  // API에서 데이터 가져오기
  async function fetchUserData() {
    try {
      const response = await axios.get(`https://winnie-bigquery-api-77vot6b6va-du.a.run.app/user/list`); // API 호출
      const data = response.data.data;
      console.log('response', data[0]['all_users'])

      userList.value = data[0]['all_users']
      selectedUserId.value = 46536104

    } catch (error) {
      console.error("API 호출 실패:", error);
    }
  }

  function setUserId(newUserId) {
    if (!userList.value.includes(newUserId)) {
      console.log('not includes')
      // alert("선택한 유저 ID가 존재하지 않습니다. 기본 유저로 변경됩니다.");
      // userId.value = defaultUserId.value;
      return
    }
    selectedUserId.value = newUserId;
  }

  return {selectedUserId, fetchUserData, userList, setUserId};
});

