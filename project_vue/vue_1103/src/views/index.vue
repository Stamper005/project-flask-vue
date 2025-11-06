<script setup lang="js">
    import { ref,onMounted,onUnmounted } from 'vue';
    import module_1 from '../components/Module_1.vue'
    import module_2 from '../components/Module_2.vue'
    import module_3 from '../components/Module_3.vue'
    import module_4 from '../components/Module_4.vue'
    import module_5 from '../components/Module_5.vue'
    import module_6 from '../components/Module_6.vue'
    const currentTime = ref('')
    function updateTime(){
        const now = new Date();
        currentTime.value = now.toLocaleDateString('zh-CN',{
            year:'numeric',
            month:'2-digit',
            day:'2-digit',
            hour:'2-digit',
            minute:'2-digit',
            second:'2-digit'
        })
    };
    function modules_add(){
        const modules = Array.from(document.querySelectorAll('.screen-module'));
        modules.forEach(module=>{
            module.addEventListener('mouseenter',()=>{
                module.style.boxShadow = '0 0 20px rgba(24,144,255)'
                module.style.transform = 'scale(1.05)'
                module.style.transition = 'all 1s ease'
            });
            module.addEventListener('mouseleave',()=>{
                module.style.boxShadow = '0 0 20px rgba(24,144,255,0.5)'
                module.style.transform = 'scale(1)'
            })
        });
    };
    let timer = null;
    onMounted(()=>{
        updateTime()
        timer = setInterval(updateTime,1000)
        modules_add()
    })
    onUnmounted(()=>{
        if(timer){
            clearInterval(timer)
        }
    })
</script>
<template>
    <div class="body">
        <div class="screen-container">
            <!--标题-->
            <header class="screen-header">
                <h1><i class="fa fa-signal" style="margin-right:5px"></i>电信通信网络监控大屏</h1>
                <div class="screen-time">{{ currentTime }}</div>
            </header>
            <!--可视化模块-->
            <div class="screen-grid">
                <div class="screen-module">
                    <div class="module-header">
                        <h2><i class="fa fa-sitemap" style="margin-right:5px"></i>服务类型的分布</h2>
                        <span class="module-status normal">运行正常</span>
                    </div>
                    <module_1></module_1>
                </div>
                <div class="screen-module">
                    <div class="module-header">
                        <h2><i class="fa fa-calculator" style="margin-right:5px"></i>网络接入类型</h2>
                        <span class="module-status warning">运行正常</span>
                    </div>
                    <module_2></module_2>
                </div>
                <div class="screen-module">
                    <div class="module-header">
                        <h2><i class="fa fa-feed" style="margin-right:5px"></i>网络性能评估</h2>
                        <span class="module-status error">运行正常</span>
                    </div>
                    <module_3></module_3>
                </div>
                <div class="screen-module">
                    <div class="module-header">
                        <h2><i class="fa fa-jpy" style="margin-right:5px"></i>核心网络拓扑</h2>
                        <span class="module-status normal">运行正常</span>
                    </div>
                    <module_4></module_4>
                </div>
                <div class="screen-module">
                    <div class="module-header">
                        <h2><i class="fa fa-diamond" style="margin-right:5px"></i>通话量统计</h2>
                        <span class="module-status warning">运行正常</span>
                    </div>
                    <module_5></module_5>
                </div>
                <div class="screen-module">
                    <div class="module-header">
                        <h2><i class="fa fa-desktop" style="margin-right:5px"></i>网络接入类型</h2>
                        <span class="module-status error">运行正常</span>
                    </div>
                    <module_6></module_6>
                </div>
            </div>
        </div>
    </div>
</template>
<style lang="css" scoped>
    *{
        margin:0;
        padding:0;
        box-sizing:border-box;
        font-family:'Microsoft YaHei',Arial,sans-serif
    }
    .body{
        background-color:#0f172a;
        background-image:url(../assets/imgs/bg.jpg),
        linear-gradient(rgba(12,23,42,0.9),rgba(15,23,42,0.95));
        background-blend-mode:overlay;
        background-size:cover;
        background-position:center;
        min-height:100vh;
        padding:20px;
        color:#e2e8f0
    }
    .screen-container{
        max-width:100vw;
        margin:0 auto;
        border:1px solid rgba(24,144,255,0.3);
        border-radius:8px;
        overflow:hidden;
        box-shadow:0 0 30px rgba(24,144,255,0.1)
    }
    .screen-header{
        background-color:rgba(15,23,42,0.8);
        padding:15px 30px;
        display:flex;
        justify-content:space-between;
        align-items:center
    }
    .screen-header h1{
        font-size:24px;
        color:#1890ff;
        font-weight:600
    }
    .screen-grid{
        display:grid;
        grid-template-columns:repeat(3,1fr);
        grid-template-rows:repeat(2,1fr);
        gap:20px;
        padding:20px;
        height:calc(100vh - 120px)
    }
    .screen-module{
        background-color:rgba(15,23,42,0.7);
        border:1px solid rgba(24,144,255,0.2);
        border-radius:8px;
        overflow:hidden;
        transition:all 0.3s ease;
        display:flex;
        flex-direction:column
    }
    .module-header{
        padding:12px 20px;
        background-color:rgba(24,144,255,0.1);
        display:flex;
        justify-content:space-between;
        align-items:center;
        border-bottom:1px solid rgba(24,144,255,0.3)
    }
    .module-header h2{
        font-size:18px;
        color:#93c5fd;
        font-weight:500
    }
    .module-status{
        font-size:14px;
        padding:3px 10px;
        border-radius:12px
    }
    .module-status.normal{
        background-color:rgba(82,196,26,0.2);
        color:#52c41a
    }
    .module-status.warning{
        background-color:rgba(250,173,20,0.2);
        color:#facc15
    }
    .module-status.error{
        background-color:rgba(245,108,108,0.2);
        color:#f87272
    }
</style>