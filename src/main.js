import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './plugins/element'

import axios from 'axios'
// 配置请求的跟路径
axios.defaults.baseURL = 'api/'
Vue.prototype.$http = axios
Vue.config.productionTip = false
new Vue({
  router,
  render: h => h(App)
}).$mount('#app')