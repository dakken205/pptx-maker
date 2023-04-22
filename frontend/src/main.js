import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import { Loading, Quasar } from 'quasar'
import quasarUserOptions from './quasar-user-options'
import axios from 'axios'
import { firebaseConfig } from './firebaseConfig'
import { getFirestore } from 'firebase/firestore'
import { getAuth } from 'firebase/auth'
import { initializeApp } from 'firebase/app'

const firebase = initializeApp(firebaseConfig)
const firestore = getFirestore()
const auth = getAuth()
const vueObj = createApp(App)

vueObj.config.globalProperties.$axios = axios.create({
    baseURL: 'http://127.0.0.1:5000/'
})
vueObj.config.globalProperties.$firebase = firebase
vueObj.config.globalProperties.$firestore = firestore
vueObj.config.globalProperties.$auth = auth

vueObj.use(Quasar, quasarUserOptions, {
    plugins: {
        Loading
    },
    config: {
        loading: {
            message: 'Processing your request...'
        }
    }
})
vueObj.use(store)
vueObj.use(router)
vueObj.mount('#app')
