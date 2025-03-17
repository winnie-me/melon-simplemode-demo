<template>
  <v-container>
    <apexchart type="bar" height="300" :options="chartOptions" :series="chartSeries"/>
  </v-container>
</template>

<script>
import {ref} from "vue";
import VueApexCharts from "vue3-apexcharts";

export default {
  components: {apexchart: VueApexCharts},
  setup() {
    const chartSeries = ref([
      {name: "E (외향)", data: [60, 0, 0, 0]},
      {name: "I (내향)", data: [40, 0, 0, 0]},
      {name: "S (현실형)", data: [0, 55, 0, 0]},
      {name: "N (직관형)", data: [0, 45, 0, 0]},
      {name: "T (사고형)", data: [0, 0, 50, 0]},
      {name: "F (감정형)", data: [0, 0, 50, 0]},
      {name: "J (판단형)", data: [0, 0, 0, 65]},
      {name: "P (인식형)", data: [0, 0, 0, 35]},
    ]);

    const chartOptions = ref({
      chart: {stacked: true, toolbar: {show: false}, stackType: '100%'},
      plotOptions: {
        bar: {horizontal: true},
      },
      /*stroke: {
        width: 1,
        colors: ['#fff']
      },*/
      dataLabels: {
        enabled: true,
        style: {
          // fontWeight: "bold"
        }
      },
      xaxis: {
        categories: ["E/I", "S/N", "T/F", "J/P"]

      },
      yaxis: {
        // show: false,
        // title: {text: "비율 (%)"}
        // axisBorder: {
        //   show: false, // ✅ X축 라인 숨김
        // },
        // axisTicks: {
        //   show: false, // ✅ X축 눈금 숨김
        // },
      },
      colors: [
        "#FF5733", // E (연한 주황)
        "#3498DB", // I (연한 파랑)
        "#2ECC71", // S (연한 초록)
        "#B2A5FF", // N (연한 보라)

        "#FB9EC6", // J (회색빛 블루)
        "#F9CB43", // F (연한 핑크)
        "#FBA518", // T (골드)
        "#1ABC9C", // P (연한 청록)
      ],
      states: {
        hover: {
          filter: {
            // type: "none", // ✅ Hover 시 색상 변경 효과 제거
            type: "lighten", // ✅ Hover 시 색상이 더 밝아짐
            // value: 0.1, // ✅ 밝기 변화 정도 (기본값: 0.15)
          },
          // size: 5,
        },
        active: {
          allowMultipleDataPointsSelection: false,
          filter: {
            type: "none", // ✅ 클릭 시 색상 변화 제거
          },
        },
      },
      legend: {
        show: false,
        // position: 'top',
        // horizontalAlign: 'left',
        // offsetX: 40
      },
      // tooltip: {
      //   enabled: true,
      //   custom: function ({series, seriesIndex, dataPointIndex}) {
      //     return `<div class="custom-tooltip">
      //         <strong>${series[seriesIndex][dataPointIndex]}%</strong>
      //       </div>`;
      //   },
      // }
      tooltip: {
        /* marker: {show:false},
         x: {
           formatter: function (value) {
             return "";
           },
         },
         y: {
           formatter: function (value) {
             return value + "%"; // ✅ X축 카테고리 없이 값만 표시
           },
         },*/
        custom: function ({series, seriesIndex, dataPointIndex, w}) {
          const item = w.config.series[seriesIndex]; // 현재 데이터 아이템
          const name = item.name; // MBTI 성향 이름
          const value = item.data[dataPointIndex]; // 값

          // ✅ 설명 추가 (성향에 따른 예제 문장)
          const descriptions = {
            "E (외향)": ["사람들과 함께하는 것을 좋아함", "새로운 환경에 빨리 적응함", "말이 많고 표현력이 뛰어남"],
            "I (내향)": ["혼자 있는 시간을 즐김", "깊은 관계를 중요하게 생각함", "말보다 글로 표현하는 걸 선호함"],
            "S (현실형)": ["현재 사실에 집중함", "경험과 데이터를 중요하게 여김", "세부사항을 신경 씀"],
            "N (직관형)": ["아이디어와 가능성에 관심 많음", "창의적인 해결책을 찾음", "큰 그림을 보는 것을 선호함"],
            "T (사고형)": ["논리적이고 객관적으로 판단함", "감정보다 사실을 중시함", "비판적 사고를 선호함"],
            "F (감정형)": ["타인의 감정을 중시함", "조화를 중요하게 생각함", "결정할 때 감정을 고려함"],
            "J (판단형)": ["계획적이고 체계적인 삶을 선호함", "목표 설정을 중요하게 생각함", "일정을 지키려 함"],
            "P (인식형)": ["즉흥적이고 융통성이 많음", "계획보다 상황에 맞게 대처함", "변화를 쉽게 받아들임"],
          };

          const descriptionList = descriptions[name] || ["설명 없음"];

          // ✅ Vuetify 스타일을 적용한 툴팁 HTML 생성
          return `
      <div class="tooltip-container">
        <v-card class="pa-2" elevation="4">
          <v-card-title class="text-h6">${name}</v-card-title>
          <v-card-subtitle class="text-blue">${value}%</v-card-subtitle>
          <v-divider></v-divider>
          <v-list dense>
            ${descriptionList
            .map((desc) => `<v-list-item><v-list-item-title>${desc}</v-list-item-title></v-list-item>`)
            .join("")}
          </v-list>
        </v-card>
      </div>
    `;
        },
      },
    });

    return {chartSeries, chartOptions};
  },
};
</script>

<style scoped>
.v-container {
  max-width: 600px;
  margin: auto;
}
</style>
