import Vue from 'vue'
import Router from 'vue-router'
import MyVantForm from '@/components/MyVantForm'
import PuTiForm from '@/components/PuTiForm'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'MyVantForm',
      component: MyVantForm
    },
    {
      path: '/success',
      name: 'PuTiForm',
      component: PuTiForm
    }
  ]
})
