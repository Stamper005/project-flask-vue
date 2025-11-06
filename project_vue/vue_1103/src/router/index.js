import { createRouter,createWebHashHistory } from "vue-router";
import Index from '../views/index.vue'
const router = createRouter({
    history:createWebHashHistory(),
    routes:[
        {
            path:'/',
            redirect:'/index'
        },
        {
            path:'/index',
            component:Index
        }

    ]
})
export default router