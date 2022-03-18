import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [{
    path: '/',
    name: 'index',
    redirect: '/index',
    component: () => import('../pages/index.vue'),
    children: [{
      path: '/index',
      name: 'home',
      component: () => import('../components/index.vue')
    }, {
      path: '/project',
      name: 'project',
      redirect: '/project/list',
      component: () => import('../components/project/index.vue'),
      children: [{
        path: 'list',
        name: 'projectlist',
        component: () => import('../components/project/list.vue'),
      }, {
        path: "id=:id",
        name: "project_children",
        component: () => import('../components/project/children.vue')
      }]
    }]
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../pages/Login.vue')
  },
  {
    //错误页面
    path: '*',
    component: () => import('../pages/error.vue')
  },
]

const router = new VueRouter({
    //mode: 'history',
  /*删除 # 号 */
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