import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import { Quasar } from 'quasar'
import quasarUserOptions from './quasar-user-options'
import axios from 'axios'

const vueObj = createApp(App)

vueObj.config.globalProperties.$axios = axios.create({
    baseURL: 'http://127.0.0.1:5000/'
})

vueObj.use(Quasar, quasarUserOptions)
vueObj.use(store)
vueObj.use(router)
vueObj.mount('#app')
