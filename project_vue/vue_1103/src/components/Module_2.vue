<script setup lang="js">
    import {reactive,onMounted} from 'vue'
    import request from '../axios/request.js'
    const config = reactive({
        data:[],
        colors: ['#e062ae', '#fb7293', '#e690d1', '#32c5e9', '#96bfff'],
    })
    const getData=()=>{
        request({
            url:'http://127.0.0.1:5000/tel/get_procedure_status',
            method:'get'
        }).then(res=>{
            if(res.data.code==200){
                console.log('success')
                config.data = res.data.data
            }else{
                console.log('error',res.data.data)
            }
        }).catch(err=>{
            console.log('error',err)
        })
    }
    onMounted(()=>{
        getData()
    })
</script>
<template>
     <dv-capsule-chart :config="config" style="width:350px;height:250px" />
</template>
<style>
    .dv-capsule-chart{
        position:relative;
        top:50px;
        transform: translateX(80px);        
    }
</style>