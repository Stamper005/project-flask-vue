<script setup lang="js">
    import request from '../axios/request.js'
    import { reactive,onMounted } from 'vue';
    const config = reactive({
        data:[]
    })
    const getData=()=>{
        request({
            url:'http://127.0.0.1:5000/tel/test',
            method:'get'
        }).then(res=>{
            if(res.data.code==200){
                console.log('success')
                config.data = res.data.data
            }else{
                console.log('fail',res)
            }
        }).catch(err=>{
            console.log('fail',err)
        })
    }
    onMounted(()=>{
        getData()
    })
</script>
<template>
     <dv-active-ring-chart :config="config" style="width:450px;height:300px" />
</template>
<style lang="css" scoped>
    .dv-active-ring-chart{
        margin:0 auto;
        top:20px
    }
</style>