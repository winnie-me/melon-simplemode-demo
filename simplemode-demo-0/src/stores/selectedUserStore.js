import { defineStore } from 'pinia';
import { ref } from 'vue';
import axios from 'axios';

export const useUserStore = defineStore('user', () => {
  const userId = ref(null); // 현재 선택된 user_id
  const dt = ref(null); // 현재 선택된 dt
  const userDtMap = ref({}); // user_id → dt 목록 매핑
  const dtUserMap = ref({}); // dt → user_id 목록 매핑
  const defaultUserId = ref(null);
  const defaultDt = ref(null);

  // API에서 데이터 가져오기
  async function fetchUserData() {
    try {
      const response = await axios.get(`https://winnie-bigquery-api-77vot6b6va-du.a.run.app/user-history/list`); // API 호출
      const data = response.data.data;
      console.log('response', data)

      // 데이터 변환
      const tempUserDtMap = {};
      const tempDtUserMap = {};

      data.forEach(entry => {
        tempDtUserMap[entry.dt] = entry.user_ids;

        entry.user_ids.forEach(userId => {
          if (!tempUserDtMap[userId]) {
            tempUserDtMap[userId] = [];
          }
          tempUserDtMap[userId].push(entry.dt);
        });
      });

      userDtMap.value = tempUserDtMap;
      dtUserMap.value = tempDtUserMap;
      console.log('fetchUserData', tempUserDtMap, tempDtUserMap)

      // 기본값 설정
      defaultUserId.value = 46536104;
      defaultDt.value = '2025-03-01';
      userId.value = 46536104;
      dt.value = '2025-03-01';
    } catch (error) {
      console.error("API 호출 실패:", error);
    }
  }

  // user_id 변경 시 dt 리스트 필터링
  function setUserId(newUserId) {
    if (!userDtMap.value[newUserId]) {
      alert("선택한 유저 ID가 존재하지 않습니다. 기본 유저로 변경됩니다.");
      userId.value = defaultUserId.value;
    } else {
      userId.value = newUserId;
    }
    dt.value = userDtMap.value[userId.value][0] || defaultDt.value; // dt 변경
  }

  // dt 변경 시 user_id 리스트 필터링
  function setDt(newDt) {
    if (!dtUserMap.value[newDt]) {
      alert("선택한 날짜가 존재하지 않습니다. 기본 날짜로 변경됩니다.");
      dt.value = defaultDt.value;
    }
    userId.value = dtUserMap.value[dt.value][0] || defaultUserId.value; // user_id 변경
  }

  return {
    userId, dt, userDtMap, dtUserMap,
    fetchUserData, setUserId, setDt
  };
});
