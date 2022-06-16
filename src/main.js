// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import Vant from 'vant';
import 'vant/lib/index.css';
// import 'vant/lib/index.less';
import 'amfe-flexible'
import 'lib-flexible/flexible'

// 复制功能
import VueClipboard from 'vue-clipboard2'
Vue.use(VueClipboard)

Vue.use(Vant)
Vue.config.productionTip = false

import axios from 'axios';

Vue.prototype.$axios = axios

// axios.defaults.baseURL = process.env.NODE_ENV === "production" ? "http://8.134.18.18:8069" : "/api"
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
