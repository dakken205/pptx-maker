import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import { Loading, Quasar } from 'quasar'
import quasarUserOptions from './quasar-user-options'
import axios from 'axios'
import { getFirestore } from 'firebase/firestore'
import { getAuth } from 'firebase/auth'
import { initializeApp } from 'firebase/app'

const firebase = initializeApp({
    apiKey: process.env.VUE_APP_FIREBASE_API_KEY,
    authDomain: process.env.VUE_APP_FIREBASE_AUTH_DOMAIN,
    projectId: process.env.VUE_APP_FIREBASE_PROJECT_ID,
    storageBucket: process.env.VUE_APP_FIREBASE_STORAGE_BUCKET,
    messagingSenderId: process.env.VUE_APP_FIREBASE_MESSAGE_SENDER_ID,
    appId: process.env.VUE_APP_FIREBASE_APP_ID,
})
const firestore = getFirestore()
const auth = getAuth()
const vueObj = createApp(App)

vueObj.config.globalProperties.$axios = axios.create({
    baseURL: process.env.VUE_APP_API_URL,
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
