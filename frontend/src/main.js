import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import { Quasar } from 'quasar'
import quasarUserOptions from './quasar-user-options'
import axios from 'axios'
import { firebaseConfig } from './firebaseConfig'
import { getFirestore } from 'firebase/firestore'
import { initializeApp } from 'firebase/app'

const firebase = initializeApp(firebaseConfig)
const firestore = getFirestore()
const vueObj = createApp(App)

vueObj.config.globalProperties.$axios = axios.create({
    baseURL: 'http://127.0.0.1:5000/'
})
vueObj.config.globalProperties.$firebase = firebase
vueObj.config.globalProperties.$firestore = firestore

vueObj.use(Quasar, quasarUserOptions)
vueObj.use(store)
vueObj.use(router)
vueObj.mount('#app')
