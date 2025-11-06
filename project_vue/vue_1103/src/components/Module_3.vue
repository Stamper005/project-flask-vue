<script setup lang="js">
    import {ref,onMounted} from 'vue'
    import request from '../axios/request.js'
    import * as echarts from 'echarts'
    let myEchart = null
    let radarChart = ref()
    let option = {
        title: {
        text:'业务指标对比'
    },
        legend: {
        data: ['业务数据']
    },
        radar: {
            indicator: []
        },
        series: [
            {
            name: '业务指标对比',
            type: 'radar',
            data: []
            }
        ]
    }
    const getData=()=>{
        return request({
            url:'http://127.0.0.1:5000/tel/get_radar_chart',
            method:'get'
        }).then(res=>{
            if(res.data.code==200){
                option.radar.indicator = res.data.data.indicator
                option.series[0].data = res.data.data.seriesData
            }else{
                console.log('err')
            }
        }).catch(err=>{
            console.log(err,'err')
        })
    }
    const createRadarChart=()=>{
        myEchart = echarts.init(radarChart.value)
        myEchart.setOption(option)
    }

    onMounted(async()=>{
        await getData()
        createRadarChart()
    })

    
</script>
<template>
    <div class="radar-chart" ref="radarChart"></div>
</template>
<style lang="css" scoped>
    .radar-chart{
        width:600px;
        height:500px;
        margin:0 auto
    }
</style>