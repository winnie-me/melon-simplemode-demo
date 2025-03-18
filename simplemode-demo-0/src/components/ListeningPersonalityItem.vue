<template>
  <div class="d-flex flex-column ma-1">
    <v-card class="mb-1 pa-1" style="width: 350px;">
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
      <v-list>
        <v-list-item
          class="ma-0"
          v-for="(desc, index) in computedAnaltics"
          :key="index"
          style="min-height: 30px;"
        >
          <v-list-item-title>{{ desc }}</v-list-item-title>
        </v-list-item>
<!--        <v-list-item class="ma-0" style="min-height: 30px;">
          <v-list-item-title>분석 내용 샤바샤바 1</v-list-item-title>
        </v-list-item>
        <v-list-item class="ma-0" style="min-height: 30px;">
          <v-list-item-title>분석 내용 샤바샤바 2</v-list-item-title>
        </v-list-item>
        <v-list-item class="ma-0" style="min-height: 30px;">
          <v-list-item-title>분석 내용 샤바샤바 3</v-list-item-title>
        </v-list-item>
        <v-list-item class="ma-0" style="min-height: 30px;">
          <v-list-item-title>분석 내용 샤바샤바 4</v-list-item-title>
        </v-list-item>
        <v-list-item class="ma-0" style="min-height: 30px;">
          <v-list-item-title>분석 내용 샤바샤바 5</v-list-item-title>
        </v-list-item>-->
      </v-list>
    </v-card>
  </div>
</template>

<script>
import VueApexCharts from "vue3-apexcharts";

export default {
  components: {apexchart: VueApexCharts},

  props: {
    title: {
      type: String,
      required: false,
      default: "전체"
    },
    content: {
      type: Object,
      required: true
    }
  },

  data() {
    return {
      chartSeries: [],
      hoverData: null,
      chartOptions: this.getChartOptions(),
/*      descriptions: {
        "E (외향)": ["사람들과 함께하는 것을 좋아함", "새로운 환경에 빨리 적응함"],
        "I (내향)": ["혼자 있는 시간을 즐김", "깊은 관계를 중요하게 생각함"],
        "S (현실형)": ["현재 사실에 집중함", "경험과 데이터를 중요하게 여김"],
        "N (직관형)": ["아이디어와 가능성에 관심 많음", "창의적인 해결책을 찾음"],
        "T (사고형)": ["논리적이고 객관적으로 판단함", "비판적 사고를 선호함"],
        "F (감정형)": ["타인의 감정을 중시함", "조화를 중요하게 생각함"],
        "J (판단형)": ["계획적이고 체계적인 삶을 선호함", "목표 설정을 중요하게 생각함"],
        "P (인식형)": ["즉흥적이고 융통성이 많음", "계획보다 상황에 맞게 대처함"]
      }*/
    };
  },

  computed: {
    computedChartSeries() {
      if (!this.content || !this.content._type) return [];

      return [ // todo 줄리안 노출 로직 확인드리기
        {name: "T (Timelessness)", data: [1 - this.content.tn_score, 0, 0, 0]},
        {name: "N (Newness)", data: [this.content.tn_score, 0, 0, 0]},

        {name: "C (Commonality)", data: [0, this.content.cu_score, 0, 0]},
        {name: "U (Uniqueness)", data: [0, 1 - this.content.cu_score, 0, 0]},

        {name: "L (Loyalty)", data: [0, 0, 1 - this.content.lv_score, 0]},
        {name: "V (Variety)", data: [0, 0, this.content.lv_score, 0]},

        {name: "F (Familiarity)", data: [0, 0, 0, this.content.fe_score]},
        {name: "E (Exploration)", data: [0, 0, 0, 1 - this.content.fe_score]}
      ];
    },

    computedAnaltics() { // todo 차차 로직 확인드리기
      let desc = []
      if (this.content.tn_score > 0.65)
        desc.push('최근 발매 음악을 선호함')
      if (this.content.fe_score > 0.65)
        desc.push('듣던 것과 다른 새로운 스타일의 음악을 선호함')
      if (this.content.lv_score가 > 0.65)
        desc.push('rising-artist 음악을 선호함')
      if (this.content.fe_score < 0.45)
        desc.push('팬덤 성향 유저일지도..')
      return desc
    }
  },

  methods: {
    getChartOptions() {
      return {
        chart: {
          stacked: true,
          toolbar: {show: false},
          stackType: "100%",
          events: {
            dataPointMouseEnter: (event, chartContext, {seriesIndex, dataPointIndex}) => {
/*              const item = chartContext.w.config.series[seriesIndex];
              const name = item.name;
              const value = item.data[dataPointIndex];

              this.hoverData = {
                name,
                value,
                descriptions: this.descriptions[name] || ["설명 없음"]
              };*/
            },
            dataPointMouseLeave: () => {
              // this.hoverData = null; // 마우스가 벗어나면 초기화
            }
          }
        },
        legend: {
          show: false
        },
        plotOptions: {
          bar: {horizontal: true}
        },
        xaxis: {categories: ["T/N", "C/U", "L/V", "F/E"]},
        colors: ["#FF5733", "#3498DB", "#2ECC71", "#B2A5FF", "#FB9EC6", "#F9CB43", "#FBA518", "#1ABC9C"],
        tooltip: {
          enabled: true,
          y: {
            formatter: value => `${value * 100}%`
          },
          x: {
            formatter: value => {
              const mapping = {
                "T/N": "Timelessness vs Newness",
                "C/U": "Commonality vs Uniqueness",
                "L/V": "Loyalty vs Variety",
                "F/E": "Familiarity vs Exploration"
              };
              return mapping[value] || value;
            }
          }
        }
      };
    }
  },

  watch: {
    content: {
      handler(newContent) {
        if (newContent && newContent._type) {
          this.chartSeries = this.computedChartSeries;
        }
      },
      immediate: true,
      deep: true
    }
  }
};
</script>

<style scoped>
.v-container {
  max-width: 600px;
  margin: auto;
}
</style>
