<script setup lang="js">
    import {ref,onMounted} from 'vue'
    import request from '../axios/request.js'
    import * as echarts from 'echarts'
    let myEchart = null
    let barChart = ref()
    let option = {
        xAxis: {
        type: 'category',
        data: []
        },
        yAxis: {
        type: 'value'
        },
        series: [
        {
            data: [],
            type: 'bar'
        }
        ]
    }
    const getData=()=>{
        return request({
            url:'http://127.0.0.1:5000/tel/get_bar_chart',
            method:'get'
        }).then(res=>{
            if(res.data.code==200){
                console.log('success')
                option.xAxis.data = res.data.data.types.map(item=>item.type)
                option.series[0].data = res.data.data.counts.map(item=>item.count)
            }else{
                console.log('error')
            }
        }).catch(err=>{
            console.log('error',err)
        })
    }
    const createBarChart=()=>{
        myEchart = echarts.init(barChart.value)
        myEchart.setOption(option)
    }
    onMounted(async()=>{
        await getData()
        createBarChart()
    })
</script>
<template>
    <div class="bar-chart" ref="barChart"></div>
</template>
<style>
    .bar-chart{
        height:400px;
        width:100%;
        margin:0 auto
    }
</style>