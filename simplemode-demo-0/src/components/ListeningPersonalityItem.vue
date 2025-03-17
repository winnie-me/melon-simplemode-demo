<template>
  <!--  <v-container>-->
  <v-card class="mb-1 pa-1" style="width: 350px;">
    <!--      <v-card-title>전체</v-card-title>-->
    <v-card-subtitle class="mb-1">{{ title }}</v-card-subtitle>
    <v-divider></v-divider>
    <apexchart
      type="bar"
      width="350"
      :options="chartOptions"
      :series="chartSeries"
    />
  </v-card>

  <!-- 차트 외부 정보 표시 -->
  <v-card class="pa-1" style="width: 350px;" elevation="0">
    <v-card-title class="text-body-1">청취 성향 간략 분석</v-card-title>
    <!--      <v-card-subtitle>{{ hoverData.value }}%</v-card-subtitle>-->
    <!--      <v-divider></v-divider>-->
    <v-list>
      <!--        <v-list-item
                class=" ma-0"
                v-for="(desc, index) in hoverData.descriptions"
                :key="index"
                style="min-height: 30px;"
              >
                <v-list-item-title>{{ desc }}</v-list-item-title>
              </v-list-item>-->
      <v-list-item
        class=" ma-0"
        style="min-height: 30px;"
      >
        <v-list-item-title>분석 내용 샤바샤바 1</v-list-item-title>
      </v-list-item>
      <v-list-item
        class=" ma-0"
        style="min-height: 30px;"
      >
        <v-list-item-title>분석 내용 샤바샤바 2</v-list-item-title>
      </v-list-item>
      <v-list-item
        class=" ma-0"
        style="min-height: 30px;"
      >
        <v-list-item-title>분석 내용 샤바샤바 3</v-list-item-title>
      </v-list-item>
      <v-list-item
        class=" ma-0"
        style="min-height: 30px;"
      >
        <v-list-item-title>분석 내용 샤바샤바 4</v-list-item-title>
      </v-list-item>
      <v-list-item
        class=" ma-0"
        style="min-height: 30px;"
      >
        <v-list-item-title>분석 내용 샤바샤바 5</v-list-item-title>
      </v-list-item>
    </v-list>
  </v-card>
  <!--  </v-container>-->
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

    const hoverData = ref(null);

    const descriptions = {
      "E (외향)": ["사람들과 함께하는 것을 좋아함", "새로운 환경에 빨리 적응함"],
      "I (내향)": ["혼자 있는 시간을 즐김", "깊은 관계를 중요하게 생각함"],
      "S (현실형)": ["현재 사실에 집중함", "경험과 데이터를 중요하게 여김"],
      "N (직관형)": ["아이디어와 가능성에 관심 많음", "창의적인 해결책을 찾음"],
      "T (사고형)": ["논리적이고 객관적으로 판단함", "비판적 사고를 선호함"],
      "F (감정형)": ["타인의 감정을 중시함", "조화를 중요하게 생각함"],
      "J (판단형)": ["계획적이고 체계적인 삶을 선호함", "목표 설정을 중요하게 생각함"],
      "P (인식형)": ["즉흥적이고 융통성이 많음", "계획보다 상황에 맞게 대처함"],
    };

    const chartOptions = ref({
      chart: {
        stacked: true,
        toolbar: {show: false},
        stackType: "100%",


        events: {
          dataPointMouseEnter: function (event, chartContext, {seriesIndex, dataPointIndex}) {
            const item = chartContext.w.config.series[seriesIndex];
            const name = item.name;
            const value = item.data[dataPointIndex];

            hoverData.value = {
              name,
              value,
              descriptions: descriptions[name] || ["설명 없음"],
            };
          },
          dataPointMouseLeave: function () {
            // hoverData.value = null; // 마우스가 벗어나면 초기화
          },
        },
      },
      legend: {
        show: false,
        // position: 'top',
        // horizontalAlign: 'left',
        // offsetX: 40
      },
      plotOptions: {
        bar: {horizontal: true},
      },
      // dataLabels: {enabled: true},
      xaxis: {categories: ["E/I", "S/N", "T/F", "J/P"]},
      colors: ["#FF5733", "#3498DB", "#2ECC71", "#B2A5FF", "#FB9EC6", "#F9CB43", "#FBA518", "#1ABC9C"],
      tooltip: {
        enabled: true,
        y: {
          formatter: function (value) {
            return value + "%"; // ✅ X축 카테고리 없이 값만 표시
          },
        }
      }, // 기본 툴팁 비활성화
    });

    return {chartSeries, chartOptions, hoverData};
  },
  props: {
    title: {
      type: String,
      required: false,
      default: "전체"
    },
  },
};
</script>

<style scoped>
.v-container {
  max-width: 600px;
  margin: auto;
}
</style>


