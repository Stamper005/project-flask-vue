<script setup lang="js">
    import {ref,onMounted} from 'vue'
    import request from '../axios/request.js'
    import * as echarts from 'echarts'
    let lineChart = ref()
    let myEchart = ref(null)
    let option = ref({
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
            type: 'line',
            }
        ]
    })
    const createLineChart=()=>{
        try{
            if(!lineChart.value){
                console.warn('容器未找到')
                return;
            }
            myEchart.value = echarts.init(lineChart.value,'light',{
                height:300,
                width:500
            })
            myEchart.value.setOption(option.value,true)
            window.addEventListener('resize',()=>{
                myEchart.value.resize()
            })
        }catch(err){
            console.log('err',err)
        }
    }
    const getData=()=>{
        return request({
            url:'http://127.0.0.1:5000/tel/get_day_count',
            method:'get'
        }).then(res=>{
            if(res.data.code==200){
                console.log('success')
                option.value.xAxis.data = res.data.data.days
                option.value.series[0].data = res.data.data.counts
            }else{
                console.log('err')
            }
        }).catch(err=>{
            console.log('err',err)
        })
    }
    onMounted(async()=>{
        await getData()
        createLineChart()
    })

</script>
<template>
    <div class="line-chart" ref="lineChart"></div>
</template>
<style lang="css" scoped>
    .line-chart{
        margin:0 auto;
    }
</style>