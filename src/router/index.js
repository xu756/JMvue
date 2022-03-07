import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [{
    path: '/',
    name: 'index',
    redirect:'/index',
    component: () => import('../pages/index.vue'),
    children:[{
      path: '/index',
      name: 'home',
      component: () => import('../components/index.vue')
    },{
      path: '/myproject',
      name: 'myproject',
      component: () => import('../components/project/myproject.vue')
    }]
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../pages/Login.vue')
  },
]

const router = new VueRouter({
  routes
})

router.beforeEach((to, from, next) => {
  if (to.path === '/login') return next();
  const tokenStr = window.sessionStorage.getItem('token')
  if (!tokenStr) return next('/login')
  next()
})
const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(err => err)
}
export default router