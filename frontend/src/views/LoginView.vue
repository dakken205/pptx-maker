<template>
    <div class="flex flex-center column" style="margin-top: 100px;">
        <q-card class="q-pa-md q-pt-lg" style="width: 350px; height: 190px;">
            <div class="column q-gutter-y-md">
                <div class="col row">
                    <span class="col text-right q-pr-sm q-pt-sm">e-mail : </span><q-input v-model="email" class="col-9" dense filled />
                </div>
                <div class="col row">
                    <span class="col text-right q-pr-sm q-pt-sm">password : </span><q-input v-model="password" class="col-9" dense filled />
                </div>
                <div class="col q-mt-xs">
                    <q-btn @click="login" class=" float-right" color="primary" style="width: 100px;">Login</q-btn>
                </div>
            </div>
        </q-card>
        <template v-if="failed">
            <div class="q-mt-lg" style="color: red;">
                Sorry, e-mail or password is wrong.
            </div>
        </template>
    </div>
</template>

<script>
import {ref} from 'vue'
import { signInWithEmailAndPassword, getAuth, setPersistence, browserLocalPersistence } from 'firebase/auth'

export default {
    setup() {
        return {
            email: ref(''),
            password: ref(''),
            failed: ref(false),
        }
    },
    methods: {
        async login() {
            this.failed = false
            await setPersistence(getAuth(), browserLocalPersistence)
            signInWithEmailAndPassword(getAuth(), this.email, this.password)
                .then(() => {
                    this.$router.push('/')
                }).catch((err) => {
                    const errCode = err.code
                    const errMessage = err.message
                    console.log(errCode, errMessage)
                    this.failed = true
                    this.password = ''
                })
        }
    }
}

</script>
