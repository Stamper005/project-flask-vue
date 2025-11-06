<script setup lang="js">
    import { ref,onMounted } from 'vue';
    import request from '../axios/request.js'
    import * as echarts from 'echarts'
    let myEchart = null
    let dlineChart = ref()
    let option = {
            tooltip: {
            trigger: 'axis'
        },
            legend: {
                data: ['2G', '3G', '4G', '5G']
            },
            grid: {
                left: '3%',
                right: '4%',
                bottom: '3%',
                containLabel: true
            },
            toolbox: {
                feature: {
                saveAsImage: {}
                }
            },
            xAxis: {
                type: 'category',
                boundaryGap: false,
                data: []
            },
            yAxis: {
                type: 'value'
            },
            series: [
                {
                name: '2G',
                type: 'line',
                stack: 'Total',
                data: []
                },
                {
                name: '3G',
                type: 'line',
                stack: 'Total',
                data: []
                },
                {
                name: '4G',
                type: 'line',
                stack: 'Total',
                data: []
                },
                {
                name: '5G',
                type: 'line',
                stack: 'Total',
                data: []
                },
            ]
        }
    const createLineChart=()=>{
        myEchart = echarts.init(dlineChart.value)
        myEchart.setOption(option)
    }
        
    const getData=()=>{
        return request({
            url:'http://127.0.0.1:5000/tel/get_day_count_type',
            method:'get'
        }).then(res=>{
            if(res.data.code==200){
                console.log('success')
                option.xAxis.data = res.data.data.xAxisData
                option.series[0].data = res.data.data.dataG['2G']
                option.series[1].data = res.data.data.dataG['3G']
                option.series[2].data = res.data.data.dataG['4G']
                option.series[3].data = res.data.data.dataG['5G']
            }else{
                console.log('error',res.data.code)
            }
        }).catch(err=>{
            console.log('fail',err)
        })
    }
    onMounted(async()=>{
        await getData()
        createLineChart()
    })
    
</script>
<template>
    <div class="div-line" ref="dlineChart"></div>
</template>
<style lang="css" scoped>
    .div-line{
        width:450px;
        height:290px;
        margin:0 auto;
        top:1px
    }
</style>